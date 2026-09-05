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
};

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
    const [k, n] = [...hist.entries()].sort((a, b) => b[1] - a[1])[0];
    if (n / Math.max(discOpaque, 1) > 0.4) {
      const [r, g, b] = k.split(",").map((v) => (Number(v) << 3) + 4);
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

  return {
    width: w, height: h,
    opaqueFraction: opaque / (w * h), edgeCoverage,
    plateKind, plate,
    inkBox: box,
    boxFraction: Math.max(box.w, box.h) / w,
    radiusFraction: maxR / (w / 2),
    inkLuminance: relLuminance(...mean),
    contrast: plate ? contrastRatio(mean, [plate[0], plate[1], plate[2]]) : null,
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
export async function normalize(
  source: Buffer,
  opts: { plate?: string; size?: number } = {}
): Promise<{ buffer: Buffer; before: IconMetrics; after: IconMetrics; notes: string[] }> {
  const size = opts.size ?? MASTER_SIZE;
  const notes: string[] = [];

  const base = (await rasterize(source, size)).resize(size, size, {
    fit: "contain",
    background: { r: 0, g: 0, b: 0, alpha: 0 },
  });
  const squared = await base.png().toBuffer();
  const before = await measure(sharp(squared));

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
    throw new Error(
      `Refusing to publish: artwork contrast against its background is ` +
      `${after.contrast.toFixed(2)}:1, below the ${MIN_CONTRAST}:1 minimum. ` +
      `Pass --plate <colour> with a background the logo is legible on.`);
  }
  return { buffer, before, after, notes };
}

export function describe(m: IconMetrics) {
  return `${m.width}x${m.height} ${m.plateKind}` +
    `${m.plate ? ` rgb(${m.plate.slice(0, 3).join(",")})` : ""}` +
    ` opaque=${(m.opaqueFraction * 100).toFixed(0)}%` +
    ` box=${(m.boxFraction * 100).toFixed(0)}%` +
    ` radius=${(m.radiusFraction * 100).toFixed(0)}%` +
    `${m.contrast !== null ? ` contrast=${m.contrast.toFixed(1)}:1` : ""}`;
}
