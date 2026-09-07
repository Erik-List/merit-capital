// Icon normalization: the quality rules every investor icon master must meet.
//
// Kept separate from fetch-investor-icon.ts so the same rules can be applied
// to a new icon (fetch) and asserted against the ones already published
// (`--audit`). Nothing here talks to the network or to Supabase.
//
// The three defects these rules exist to kill, all measured on the first four
// investors (2026-09-03):
//
//   1. NO BACKGROUND. A source that is a bare glyph on transparency (the
//      Lightspeed favicon is one #303030 path with fill="none" on the svg
//      root) produced a master that is 83% transparent. The app renders
//      icons at `rounded-full object-cover` on the leaderboard and has a
//      dark mode (tailwind darkMode: ['class']), so a near-black glyph on
//      transparency is invisible against a dark page. An icon master must
//      carry its own opaque background.
//   2. NO SAFE AREA. Sequoia's tree reaches 94% of the circle radius, so the
//      `rounded-full` crop shaves its edges and it reads as cramped next to
//      a16z, whose circular mark sits at 68%. Artwork needs a keyline.
//   3. LOW CONTRAST. A plate is only a fix if the glyph is legible on it;
//      synthesizing white behind a white logo is worse than transparency.
//
// A source that already carries its own background is left alone (see
// `classifyPlate`): Accel's dark rounded square with transparent corners is
// a deliberate shape, not a defect, and insetting it would shrink a
// full-bleed plate into a small sticker.

import sharp from "sharp";

export const MASTER_SIZE = 256;

// Artwork keyline. SAFE_BOX bounds the glyph's bounding box; SAFE_RADIUS
// bounds its furthest pixel from centre, which is what the circular crop
// actually cuts. Material's adaptive-icon keyline is 66.7% and a16z (the
// best-looking of the four) measures 68% on both, so 0.74/0.80 is a
// deliberately mild rule: it shrinks what is clipped, not what is merely large.
export const SAFE_BOX = 0.74;
export const SAFE_RADIUS = 0.80;
// A glyph smaller than this is lost in its own padding and is scaled UP to
// SAFE_BOX, never past the source's own resolution.
export const MIN_BOX = 0.45;
// WCAG contrast ratio. 3:1 is the large-text/graphics threshold; below it a
// synthesized plate is rejected rather than published.
export const MIN_CONTRAST = 3;
// Resolution. The fourth defect, found on Thrive (2026-09-05): the source
// handed to the fetch was the site's 32x32 favicon, the contain-fit resize
// upscaled it 8x to the 256 canvas and the keyline then shrank it again, so
// the published master was a blurred 8x enlargement — and `describe(before)`
// reported "256x256" because it measured the canvas, not the source. Accel
// had hit the same trap in June (a 32px /icon.png "upscaled into a soft grey
// A") and was fixed by hand. Two rules now make it structural:
//   MAX_UPSCALE — raster artwork is never enlarged: the artwork's pixels in
//     the master may not exceed its pixels in the source (5% tolerance for
//     rounding). Vectors are exempt; they render at 2x density.
//   MAX_RAMP — the anti-aliasing ramp around the artwork, measured on the
//     master in pixels (partial-coverage pixels per perimeter pixel). A crisp
//     256px render sits at 0.5-1.1px on every published icon; the upscaled
//     Thrive master measured 6.1px and a 32->256 enlargement 8.8px. This
//     catches sources that arrive pre-blurred, which the scale rule cannot see,
//     and lets `--audit` find soft masters without their sources.
export const MAX_UPSCALE = 1.05;
export const MAX_RAMP = 2.0;

// How the source backs itself. Only `bare-glyph` needs a plate synthesized;
// a disc plate (Accel: a solid dark disc with a white mark, 100% opaque
// inside the inscribed circle) is a deliberate full-bleed design and is left
// alone — insetting it would shrink a full-bleed logo into a small sticker.
export type PlateKind = "opaque-plate" | "disc-plate" | "bare-glyph";

export type IconMetrics = {
  width: number; height: number;
  opaqueFraction: number; edgeCoverage: number; // edgeCoverage = inscribed-disc opacity
  plateKind: PlateKind; plate: [number, number, number, number] | null;
  inkBox: { x: number; y: number; w: number; h: number };
  boxFraction: number; radiusFraction: number;
  inkLuminance: number; contrast: number | null;
  rampWidth: number; // anti-aliasing ramp in px: partial-coverage pixels per perimeter pixel
};

export type SourceInfo = { format: string; width: number; height: number; vector: boolean };

/** The source as it is, before any canvas: the number that decides whether
 *  a master can be made from it at all. */
export async function probeSource(source: Buffer): Promise<SourceInfo> {
  const m = await sharp(source).metadata();
  return {
    format: m.format ?? "unknown",
    width: m.width ?? 0, height: m.height ?? 0,
    vector: m.format === "svg",
  };
}

const relLuminance = (r: number, g: number, b: number) => {
  const f = (v: number) => {
    const s = v / 255;
    return s <= 0.03928 ? s / 12.92 : Math.pow((s + 0.055) / 1.055, 2.4);
  };
  return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b);
};

export const contrastRatio = (a: [number, number, number], b: [number, number, number]) => {
  const la = relLuminance(...a), lb = relLuminance(...b);
  return (Math.max(la, lb) + 0.05) / (Math.min(la, lb) + 0.05);
};

/** Rasterize a source buffer to RGBA. SVGs are rendered at high density
 *  first: sharp defaults to 72dpi, so the 193px Lightspeed favicon was being
 *  rasterized at 193px and upscaled to 256 — soft edges from the start. */
export async function rasterize(source: Buffer, target = MASTER_SIZE) {
  const probe = await sharp(source).metadata();
  const isVector = probe.format === "svg";
  const intrinsic = Math.max(probe.width ?? target, probe.height ?? target);
  // render vectors at >=2x the master so the downsample is what softens edges,
  // not the rasterizer
  const density = isVector ? Math.ceil((72 * target * 2) / Math.max(intrinsic, 1)) : 72;
  return sharp(source, isVector ? { density } : {});
}

/** Measure a square RGBA master: does it carry a background, and where is
 *  the artwork inside it. */
export async function measure(img: sharp.Sharp): Promise<IconMetrics> {
  const { data, info } = await img.clone().ensureAlpha().raw()
    .toBuffer({ resolveWithObject: true });
  const { width: w, height: h, channels: c } = info;
  const at = (x: number, y: number): [number, number, number, number] => {
    const i = (y * w + x) * c;
    return [data[i], data[i + 1], data[i + 2], data[i + 3]];
  };

  let opaque = 0;
  for (let i = 0; i < w * h; i++) if (data[i * c + 3] > 250) opaque++;

  // Self-backing is about COVERAGE, not about painting the square's corners:
  // a disc plate leaves the corners empty and is still a background. The
  // inscribed circle is the region every crop in the app keeps, so opacity
  // there is what decides.
  const cx0 = (w - 1) / 2, cy0 = (h - 1) / 2, rIns = w / 2 - 2;
  let discOpaque = 0, discTotal = 0;
  for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) {
    if (Math.hypot(x - cx0, y - cy0) > rIns) continue;
    discTotal++; if (at(x, y)[3] > 250) discOpaque++;
  }
  const discCoverage = discOpaque / discTotal;

  const corners = [at(1, 1), at(w - 2, 1), at(1, h - 2), at(w - 2, h - 2)];
  const allCornersOpaque = corners.every((p) => p[3] > 250);
  const plateKind: PlateKind =
    discCoverage > 0.98 && allCornersOpaque ? "opaque-plate"
    : discCoverage > 0.98 ? "disc-plate"
    : "bare-glyph";

  // Plate colour is the modal opaque colour, not a corner sample: a disc
  // plate has no opaque corner, and a plate is by definition the colour most
  // of the icon is made of.
  let plate: [number, number, number, number] | null = null;
  if (plateKind !== "bare-glyph") {
    const hist = new Map<string, number>();
    for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) {
      const p = at(x, y);
      if (p[3] < 250) continue;
      // quantize so anti-aliased plate noise collapses onto the plate colour
      const k = `${p[0] >> 3},${p[1] >> 3},${p[2] >> 3}`;
      hist.set(k, (hist.get(k) ?? 0) + 1);
    }
    const [k, n] = Array.from(hist.entries()).sort((a, b) => b[1] - a[1])[0];
    if (n / Math.max(discOpaque, 1) > 0.4) {
      const [r, g, b] = k.split(",").map((v: string) => (Number(v) << 3) + 4);
      plate = [r, g, b, 255];
    }
  }
  const edgeCoverage = discCoverage;

  // Ink = artwork. Against a plate that means "differs from the plate
  // colour"; on transparency it means "not transparent".
  const isInk = (p: [number, number, number, number]) => {
    if (p[3] < 16) return false;
    if (!plate) return true;
    return Math.abs(p[0] - plate[0]) + Math.abs(p[1] - plate[1]) + Math.abs(p[2] - plate[2]) > 60;
  };

  let minX = w, minY = h, maxX = -1, maxY = -1, maxR = 0;
  let lr = 0, lg = 0, lb = 0, n = 0;
  const cx = (w - 1) / 2, cy = (h - 1) / 2;
  for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) {
    const p = at(x, y);
    if (!isInk(p)) continue;
    if (x < minX) minX = x; if (x > maxX) maxX = x;
    if (y < minY) minY = y; if (y > maxY) maxY = y;
    const r = Math.hypot(x - cx, y - cy); if (r > maxR) maxR = r;
    lr += p[0]; lg += p[1]; lb += p[2]; n++;
  }
  if (maxX < 0) throw new Error("icon has no visible artwork");
  const box = { x: minX, y: minY, w: maxX - minX + 1, h: maxY - minY + 1 };
  const mean: [number, number, number] = [lr / n, lg / n, lb / n];

  // Edge ramp. Luminance composited on the plate (white where transparent),
  // deviation from the plate normalized by the artwork's own full ink (99.5th
  // percentile, so a red or grey logo counts as fully inked at its own colour).
  // Ink = deviation > 85%, partial = 15-85%; perimeter = ink pixels with a
  // non-ink 4-neighbour. Ramp width = partial / perimeter.
  // sRGB-weighted luminance on the same scale as the per-pixel value below
  // (not the gamma-linearized relLuminance, which put a dark plate 50 levels
  // away from itself and read Accel's whole disc as a soft edge).
  const plateLum = plate ? 0.2126 * plate[0] + 0.7152 * plate[1] + 0.0722 * plate[2] : 255;
  const dev = new Float32Array(w * h);
  const histo = new Uint32Array(256);
  for (let i = 0; i < w * h; i++) {
    const a = data[i * c + 3] / 255;
    const lum = (0.2126 * data[i * c] + 0.7152 * data[i * c + 1] + 0.0722 * data[i * c + 2]) * a
      + plateLum * (1 - a);
    const d = Math.abs(lum - plateLum);
    dev[i] = d; histo[Math.min(255, Math.round(d))]++;
  }
  let acc = 0, p995 = 255;
  for (let v = 0; v < 256; v++) { acc += histo[v]; if (acc >= 0.995 * w * h) { p995 = v; break; } }
  const full = Math.max(1, p995);

  // A logo may carry more than one ink, and normalizing every pixel against a
  // single "full ink" reads the second colour as anti-aliasing. Lux's mark is
  // a black monogram beside a #FF1C24 cross: red sits at 0.70 of black's
  // deviation from white, inside the 15-85% partial band, so every red pixel
  // counted as a soft edge and a pixel-crisp vector measured a 5.45px ramp —
  // the same geometry filled black measured 0.87px.
  //
  // The distinction that matters is FLATNESS, not colour count: a two-ink logo
  // puts nearly all of its non-plate pixels at a couple of exact colours, while
  // a blurred or upscaled source smears them across a continuum. So quantize
  // the non-plate pixels, keep only bins holding >=10% of them, and use those
  // as ink colours ONLY when they account for most of the artwork
  // (FLAT_MASS_MIN). Measured on this run: the Lux mark puts 87% of its mass in
  // two bins, while the same mark blurred puts 20% in its largest and 33% in
  // every bin over 5%. Below the bar we fall through to the single-ink rule, so
  // the soft-source guard behaves exactly as before.
  const FLAT_BIN_MIN = 0.10;   // share of non-plate pixels for a bin to be an ink
  const FLAT_MASS_MIN = 0.60;  // ... and the inks together must cover this much
  const INK_DIST = 24;         // RGB euclidean; a flat fill lands within a bin's width
  const composite = (i: number): [number, number, number] => {
    const a = data[i * c + 3] / 255;
    return [data[i * c] * a + (plate ? plate[0] : 255) * (1 - a),
            data[i * c + 1] * a + (plate ? plate[1] : 255) * (1 - a),
            data[i * c + 2] * a + (plate ? plate[2] : 255) * (1 - a)];
  };
  let cand = 0;
  const bins = new Map<number, { n: number; r: number; g: number; b: number }>();
  for (let i = 0; i < w * h; i++) {
    if (dev[i] / full <= 0.15) continue;
    cand++;
    const [r, g, b] = composite(i);
    const key = ((r >> 4) << 8) | ((g >> 4) << 4) | (b >> 4);
    const e = bins.get(key) || { n: 0, r: 0, g: 0, b: 0 };
    e.n++; e.r += r; e.g += g; e.b += b; bins.set(key, e);
  }
  const inks: [number, number, number][] = [];
  let flatMass = 0;
  for (const e of [...bins.values()].sort((a, b) => b.n - a.n).slice(0, 4)) {
    if (e.n < FLAT_BIN_MIN * Math.max(1, cand)) break;
    inks.push([e.r / e.n, e.g / e.n, e.b / e.n]);
    flatMass += e.n;
  }
  const multiInk = inks.length > 1 && flatMass >= FLAT_MASS_MIN * Math.max(1, cand);
  const atFlatInk = (i: number) => {
    if (!multiInk) return false;
    const [r, g, b] = composite(i);
    for (const k of inks) if (Math.hypot(r - k[0], g - k[1], b - k[2]) <= INK_DIST) return true;
    return false;
  };
  const inkMask = new Uint8Array(w * h);
  let partial = 0;
  for (let i = 0; i < w * h; i++) {
    const d = dev[i] / full;
    if (d > 0.85 || (d > 0.15 && atFlatInk(i))) inkMask[i] = 1;
    else if (d > 0.15) partial++;
  }
  let perimeter = 0;
  for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) {
    const i = y * w + x;
    if (!inkMask[i]) continue;
    if (x === 0 || y === 0 || x === w - 1 || y === h - 1
        || !inkMask[i - 1] || !inkMask[i + 1] || !inkMask[i - w] || !inkMask[i + w]) perimeter++;
  }
  const rampWidth = partial / Math.max(1, perimeter);

  return {
    width: w, height: h,
    opaqueFraction: opaque / (w * h), edgeCoverage,
    plateKind, plate,
    inkBox: box,
    boxFraction: Math.max(box.w, box.h) / w,
    radiusFraction: maxR / (w / 2),
    inkLuminance: relLuminance(...mean),
    contrast: plate ? contrastRatio(mean, [plate[0], plate[1], plate[2]]) : null,
    rampWidth,
  };
}

/** The scale that brings artwork inside the keyline. <1 shrinks a clipped
 *  glyph, >1 rescues one lost in whitespace, 1 leaves a good icon alone. */
export function safeAreaScale(m: IconMetrics) {
  const shrink = Math.min(SAFE_BOX / m.boxFraction, SAFE_RADIUS / m.radiusFraction);
  if (shrink < 1) return shrink;
  if (m.boxFraction < MIN_BOX) return Math.min(shrink, SAFE_BOX / m.boxFraction);
  return 1;
}

/** Produce the published master: opaque, keylined, contrast-checked. */
export type NormalizeResult = {
  buffer: Buffer; before: IconMetrics; after: IconMetrics; notes: string[];
  source: SourceInfo;
  /** longest side of the artwork's bounding box, in source pixels (raster) */
  artworkSourcePx: number;
  /** the same box in the master, after the keyline inset */
  artworkMasterPx: number;
  /** artworkMasterPx / artworkSourcePx; >1 means the raster was enlarged */
  upscale: number;
};

export async function normalize(
  source: Buffer,
  opts: { plate?: string; size?: number; allowUpscale?: boolean; allowLowContrast?: boolean } = {}
): Promise<NormalizeResult> {
  const size = opts.size ?? MASTER_SIZE;
  const notes: string[] = [];

  const src = await probeSource(source);
  const base = (await rasterize(source, size)).resize(size, size, {
    fit: "contain",
    background: { r: 0, g: 0, b: 0, alpha: 0 },
  });
  const squared = await base.png().toBuffer();
  const before = await measure(sharp(squared));

  // Resolution accounting, in the source's own pixels. contain-fit maps the
  // source's longest side onto the canvas, so the artwork's box in the canvas
  // divided by that fit is its size in the source.
  const fit = size / Math.max(1, Math.max(src.width, src.height));
  const boxPx = Math.max(before.inkBox.w, before.inkBox.h);
  const artworkSourcePx = src.vector ? Infinity : Math.round(boxPx / fit);

  // Choose the background. An icon that already backs itself keeps what it
  // has; only a bare glyph gets a synthesized plate, coloured for contrast.
  let plateColor: sharp.Color | null = null;
  if (opts.plate && opts.plate !== "auto" && opts.plate !== "keep") {
    plateColor = opts.plate;
  } else if (opts.plate === "keep") {
    notes.push("plate: kept as-is by request");
  } else if (before.plateKind === "bare-glyph") {
    plateColor = before.inkLuminance < 0.5 ? "#ffffff" : "#111111";
    notes.push(`plate: synthesized ${plateColor} behind a bare glyph (source was ` +
      `${Math.round((1 - before.opaqueFraction) * 100)}% transparent)`);
  } else {
    notes.push(`plate: source is self-backing (${before.plateKind}), kept`);
  }

  // Inset the artwork to the keyline.
  const scale = safeAreaScale(before);
  const artworkMasterPx = Math.round(boxPx * scale);
  const upscale = src.vector ? 1 : artworkMasterPx / Math.max(1, artworkSourcePx);
  notes.push(src.vector
    ? `resolution: vector source (${src.width}x${src.height} intrinsic), rendered at 2x density — exempt from the upscale rule`
    : `resolution: ${src.format} ${src.width}x${src.height}, artwork ${artworkSourcePx}px in the source → ${artworkMasterPx}px in the master (${upscale.toFixed(2)}x)`);
  if (!src.vector && upscale > MAX_UPSCALE) {
    const msg = `Refusing to publish: the ${src.width}x${src.height} ${src.format} source holds ${artworkSourcePx}px ` +
      `of artwork and the master needs ${artworkMasterPx}px (${upscale.toFixed(2)}x enlargement, limit ${MAX_UPSCALE}x). ` +
      `Find a larger source — an SVG, the apple-touch-icon, a manifest icon, og:image or a press-kit logo ` +
      `(\`--discover <site-url>\` lists them with sizes) — or pass --allow-upscale to publish a soft icon knowingly.`;
    if (!opts.allowUpscale) throw new Error(msg);
    notes.push(`WARNING: ${msg.replace("Refusing to publish: ", "")}`);
  }
  let work = sharp(squared);
  if (Math.abs(scale - 1) > 0.02) {
    const glyph = await sharp(squared)
      .extract({ left: before.inkBox.x, top: before.inkBox.y,
                 width: before.inkBox.w, height: before.inkBox.h })
      .toBuffer();
    const gw = Math.max(1, Math.round(before.inkBox.w * scale));
    const gh = Math.max(1, Math.round(before.inkBox.h * scale));
    const resized = await sharp(glyph).resize(gw, gh, { fit: "fill" }).toBuffer();
    // rebuild on the plate the source had (so a plate icon keeps its plate)
    const bg = plateColor
      ?? (before.plate
        ? { r: before.plate[0], g: before.plate[1], b: before.plate[2], alpha: 1 }
        : { r: 0, g: 0, b: 0, alpha: 0 });
    work = sharp({ create: { width: size, height: size, channels: 4, background: bg } })
      .composite([{ input: resized, left: Math.round((size - gw) / 2), top: Math.round((size - gh) / 2) }]);
    notes.push(`safe area: artwork scaled ${scale.toFixed(3)} ` +
      `(box ${(before.boxFraction * 100).toFixed(0)}%→${(before.boxFraction * scale * 100).toFixed(0)}%, ` +
      `radius ${(before.radiusFraction * 100).toFixed(0)}%→${(before.radiusFraction * scale * 100).toFixed(0)}%)`);
  } else {
    notes.push(`safe area: already within the keyline (box ${(before.boxFraction * 100).toFixed(0)}%, ` +
      `radius ${(before.radiusFraction * 100).toFixed(0)}%)`);
  }

  // Flatten last, so a synthesized plate also fills the padding the inset made.
  if (plateColor) work = work.flatten({ background: plateColor });

  const buffer = await work.png().toBuffer();
  const after = await measure(sharp(buffer));

  if (after.contrast !== null && after.contrast < MIN_CONTRAST) {
    const msg = `artwork contrast against its background is ` +
      `${after.contrast.toFixed(2)}:1, below the ${MIN_CONTRAST}:1 minimum.`;
    // A brand plate the owner accepts as-is (USV's white-on-green mark, Erik
    // 2026-09-06) publishes only with --allow-low-contrast, logged in provenance.
    if (!opts.allowLowContrast) {
      throw new Error(`Refusing to publish: ${msg} Pass --plate <colour> with a background the logo is legible on.`);
    }
    notes.push(`WARNING: ${msg} Published with --allow-low-contrast.`);
  }
  // A source that arrives already blurred (a CDN-resized favicon, a JPEG
  // screenshot of a logo) passes the scale rule and fails here.
  if (after.rampWidth > MAX_RAMP && !opts.allowUpscale) {
    throw new Error(
      `Refusing to publish: the master's edge ramp is ${after.rampWidth.toFixed(2)}px ` +
      `(limit ${MAX_RAMP}px) — the source is soft (pre-blurred or resized up by its host). ` +
      `Find a sharper source or pass --allow-upscale to publish it knowingly.`);
  }
  return { buffer, before, after, notes, source: src, artworkSourcePx, artworkMasterPx, upscale };
}

export function describe(m: IconMetrics) {
  return `${m.width}x${m.height} ${m.plateKind}` +
    `${m.plate ? ` rgb(${m.plate.slice(0, 3).join(",")})` : ""}` +
    ` opaque=${(m.opaqueFraction * 100).toFixed(0)}%` +
    ` box=${(m.boxFraction * 100).toFixed(0)}%` +
    ` radius=${(m.radiusFraction * 100).toFixed(0)}%` +
    `${m.contrast !== null ? ` contrast=${m.contrast.toFixed(1)}:1` : ""}` +
    ` ramp=${m.rampWidth.toFixed(2)}px`;
}
