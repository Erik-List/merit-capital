import "dotenv/config";
import { createHash } from "node:crypto";
import { readFileSync, writeFileSync, readdirSync, existsSync } from "node:fs";
import { createClient } from "@supabase/supabase-js";
import sharp from "sharp";
import { INVESTORS_DIR, Paths } from "./utils/paths";
import {
  normalize, measure, describe, probeSource,
  MASTER_SIZE, MAX_UPSCALE, MAX_RAMP,
} from "./utils/icon-normalize";

// Fetch an investor's logo from a source URL, normalize it to the 256x256 PNG
// master, upload it to the "Icon Images" bucket under
// investors/<slug>-<contenthash>.png, write the public URL into the
// investor's icon_url in data/collection/investors/<slug>/investor.json and
// the source provenance (URL, intrinsic size, artwork pixels, scale, ramp)
// into investor/sources.json. The DB row updates through the normal ingest:
//   npm run ingest:investor -- --investors name=<slug> --columns icon_url
//
// Normalization is not just a resize: scripts/utils/icon-normalize.ts holds
// the published quality rules (own opaque background, keylined artwork,
// contrast-checked, never upscaled, crisp edges), with the reasoning for
// each. The resolution rules exist because a favicon URL looks like any
// other URL: Thrive's site handed us a 32x32 PNG and the master was an 8x
// enlargement (2026-09-05). `--discover` lists what a site actually offers,
// with sizes, so the largest source is chosen by measurement, not by the
// first <link rel="icon"> found. `--audit` replays every rule against the
// icons already published, so a rule added later finds the icons that
// predate it.
//
// Usage:
//   tsx scripts/fetch-investor-icon.ts --discover <site-url>
//   tsx scripts/fetch-investor-icon.ts <slug> <source-url> [options]
//     --plate auto|keep|<colour>   background policy (default auto)
//     --dry-run <out.png>          normalize to a local file, no upload
//     --allow-upscale              publish a soft icon knowingly (logged in provenance)
//     --allow-low-contrast         publish a brand plate under the 3:1 floor knowingly (logged in provenance)
//   tsx scripts/fetch-investor-icon.ts --audit [slug ...]

const BUCKET = "Icon Images";
const investorFile = (slug: string) => new Paths(slug).investor;
const sourcesFile = (slug: string) => new Paths(slug).investor_sources;

const UA = { "user-agent": "Mozilla/5.0 (compatible; MeritCapital icon fetch)" };

async function download(url: string) {
  const response = await fetch(url, { headers: UA });
  if (!response.ok) {
    throw new Error(`Source fetch failed: ${response.status} ${response.statusText}`);
  }
  return Buffer.from(await response.arrayBuffer());
}

type Provenance = {
  source_url: string; format: string; width: number; height: number; vector: boolean;
  artwork_source_px: number | null; artwork_master_px: number; upscale: number;
  ramp_px: number; master_size: number; fetched: string; allow_upscale: boolean;
  allow_low_contrast?: boolean;
};

/** Enumerate the icon-sized assets a site declares, with their intrinsic
 *  sizes, so the source is chosen by measurement. Read-only. */
async function discover(siteUrl: string) {
  const base = new URL(siteUrl);
  const html = (await download(base.href)).toString("utf8");
  const candidates = new Map<string, string>(); // url -> how it was found
  const add = (href: string | undefined, how: string) => {
    if (!href) return;
    try { const u = new URL(href.trim(), base).href; if (!candidates.has(u)) candidates.set(u, how); } catch { /* skip */ }
  };
  for (const m of Array.from(html.matchAll(/<link\b[^>]*>/gi))) {
    const tag = m[0];
    const rel = /rel=["']([^"']+)["']/i.exec(tag)?.[1]?.toLowerCase() ?? "";
    const href = /href=["']([^"']+)["']/i.exec(tag)?.[1];
    const sizes = /sizes=["']([^"']+)["']/i.exec(tag)?.[1];
    if (/icon/.test(rel)) add(href, `<link rel="${rel}"${sizes ? ` sizes="${sizes}"` : ""}>`);
    if (rel === "manifest" && href) {
      try {
        const manifest = JSON.parse((await download(new URL(href, base).href)).toString("utf8"));
        for (const icon of manifest.icons ?? []) add(icon.src, `manifest icon${icon.sizes ? ` sizes="${icon.sizes}"` : ""}`);
      } catch { /* no manifest */ }
    }
  }
  for (const m of Array.from(html.matchAll(/<meta\b[^>]*>/gi))) {
    const tag = m[0];
    const prop = (/(?:property|name)=["']([^"']+)["']/i.exec(tag)?.[1] ?? "").toLowerCase();
    if (/^(og:image|twitter:image)/.test(prop)) add(/content=["']([^"']+)["']/i.exec(tag)?.[1], `<meta ${prop}>`);
  }
  for (const m of Array.from(html.matchAll(/<img\b[^>]*>/gi))) {
    const tag = m[0];
    if (!/logo|brand|mark/i.test(tag)) continue;
    add(/src=["']([^"']+)["']/i.exec(tag)?.[1], `<img> with logo/brand in its attributes`);
  }
  const inlineSvgs = Array.from(html.matchAll(/<svg\b[^>]*(?:id|class)=["'][^"']*(?:logo|brand|mark)[^"']*["'][^>]*>/gi)).length;

  console.log(`${candidates.size} icon candidate(s) on ${base.href}` +
    (inlineSvgs ? `, plus ${inlineSvgs} inline <svg> logo element(s) (save one to a file and pass the path as the source)` : ""));
  const rows: { url: string; how: string; info: string; px: number }[] = [];
  for (const [url, how] of Array.from(candidates.entries())) {
    try {
      const buf = await download(url);
      if (/\.ico(\?|$)/i.test(url) || buf.subarray(0, 4).equals(Buffer.from([0, 0, 1, 0]))) {
        // ICO container: member sizes are in the directory (byte 6 onward, 16 bytes each)
        const n = buf.readUInt16LE(4);
        const sizes = Array.from({ length: n }, (_, i) => {
          const w = buf[6 + i * 16] || 256, h = buf[7 + i * 16] || 256; return `${w}x${h}`;
        });
        const px = Math.max(...sizes.map((s) => Number(s.split("x")[0])));
        rows.push({ url, how, info: `ico [${sizes.join(", ")}] — extract the largest member to a PNG`, px });
        continue;
      }
      const s = await probeSource(buf);
      rows.push({ url, how, info: s.vector ? `svg (vector, ${s.width}x${s.height} intrinsic)` : `${s.format} ${s.width}x${s.height}`,
        px: s.vector ? Number.MAX_SAFE_INTEGER : Math.max(s.width, s.height) });
    } catch (err) {
      rows.push({ url, how, info: `unreadable (${(err as Error).message.slice(0, 60)})`, px: -1 });
    }
  }
  rows.sort((a, b) => b.px - a.px);
  for (const r of rows) {
    const verdict = r.px === Number.MAX_SAFE_INTEGER ? "✓ vector"
      : r.px >= MASTER_SIZE ? "✓"
      : r.px >= Math.round(MASTER_SIZE * 0.74) ? "~ marginal (artwork may not reach the keyline)"
      : r.px < 0 ? "?" : "✗ too small (would be upscaled)";
    console.log(`  ${verdict.padEnd(46)} ${r.info.padEnd(44)} ${r.url}\n${" ".repeat(48)} found as ${r.how}`);
  }
  console.log(`\nRule: raster artwork is never enlarged (limit ${MAX_UPSCALE}x); pick the vector or the largest raster.`);
}

/** Replay the current rules against what is already published. Read-only. */
async function audit(slugs: string[]) {
  const targets = slugs.length ? slugs : readdirSync(INVESTORS_DIR).filter((d) => {
    try { return readFileSync(investorFile(d), "utf8").length > 0; } catch { return false; }
  });
  let failures = 0;
  for (const slug of targets) {
    let row: Record<string, unknown>;
    try { row = JSON.parse(readFileSync(investorFile(slug), "utf8")); } catch { continue; }
    const iconUrl = row.icon_url as string | null;
    if (!iconUrl) { console.log(`${slug.padEnd(18)} no icon_url`); continue; }
    try {
      const m = await measure(sharp(await download(iconUrl)));
      const problems: string[] = [];
      const warnings: string[] = [];
      if (m.plateKind === "bare-glyph") problems.push("NO BACKGROUND (invisible in dark mode)");
      if (m.radiusFraction > 0.86) problems.push(`artwork at ${(m.radiusFraction * 100).toFixed(0)}% of the circle radius (clipped by rounded-full)`);
      if (m.boxFraction > 0.80) problems.push(`artwork fills ${(m.boxFraction * 100).toFixed(0)}% of the canvas (no keyline)`);
      if (m.contrast !== null && m.contrast < 3) problems.push(`contrast ${m.contrast.toFixed(1)}:1 against its own background`);
      if (m.rampWidth > MAX_RAMP) problems.push(`SOFT EDGES: ${m.rampWidth.toFixed(2)}px ramp (limit ${MAX_RAMP}px) — an upscaled or pre-blurred raster source; re-fetch from a larger one`);
      // provenance: written by this script since the resolution rule; older icons carry none
      let prov: Provenance | undefined;
      try {
        const sources = JSON.parse(readFileSync(sourcesFile(slug), "utf8"));
        prov = sources?.fields?.icon_url?.provenance;
      } catch { /* no sidecar */ }
      if (!prov) warnings.push("no source provenance recorded (fetched before the resolution rule); the ramp check above is the only resolution evidence");
      else if (prov.upscale > MAX_UPSCALE) problems.push(`published from a ${prov.width}x${prov.height} source at ${prov.upscale.toFixed(2)}x enlargement${prov.allow_upscale ? " (--allow-upscale)" : ""}`);
      if (prov?.allow_low_contrast) {
        // the owner accepted the brand plate as-is; report, do not fail
        const ci = problems.findIndex((p) => p.startsWith("contrast "));
        if (ci >= 0) { warnings.push(`${problems[ci]} (published with --allow-low-contrast)`); problems.splice(ci, 1); }
      }
      console.log(`${slug.padEnd(18)} ${describe(m)}${prov ? `  ← ${prov.format} ${prov.width}x${prov.height}, ${prov.upscale.toFixed(2)}x` : ""}`);
      problems.forEach((p) => { console.log(`${" ".repeat(19)}✗ ${p}`); failures++; });
      warnings.forEach((p) => console.log(`${" ".repeat(19)}· ${p}`));
    } catch (err) {
      console.log(`${slug.padEnd(18)} unreadable: ${(err as Error).message}`);
      failures++;
    }
  }
  if (failures) {
    console.log(`\n${failures} problem(s). Re-run the fetch for those slugs (use --discover to find a larger source) to republish them under the current rules.`);
    process.exit(1);
  }
  console.log("\nAll published icons meet the current rules.");
}

async function main() {
  const argv = process.argv.slice(2);
  if (argv[0] === "--audit") return audit(argv.slice(1));
  if (argv[0] === "--discover") {
    if (!argv[1]) throw new Error("Usage: tsx scripts/fetch-investor-icon.ts --discover <site-url>");
    return discover(argv[1]);
  }

  const flag = (name: string) => {
    const i = argv.indexOf(name);
    return i >= 0 ? argv[i + 1] : undefined;
  };
  const BOOL_FLAGS = new Set(["--allow-upscale", "--allow-low-contrast"]);
  const positional = argv.filter((a, i) =>
    !a.startsWith("--") && !(i > 0 && argv[i - 1].startsWith("--") && !BOOL_FLAGS.has(argv[i - 1])));
  const [slug, sourceUrl] = positional;
  const plate = flag("--plate") ?? "auto";
  const dryRun = flag("--dry-run");
  const allowUpscale = argv.includes("--allow-upscale");
  const allowLowContrast = argv.includes("--allow-low-contrast");

  if (!slug || !sourceUrl) {
    throw new Error("Usage: tsx scripts/fetch-investor-icon.ts <slug> <source-url> [--plate auto|keep|<colour>] [--dry-run <out.png>] [--allow-upscale] [--allow-low-contrast]");
  }

  const filePath = investorFile(slug);
  const investor = JSON.parse(readFileSync(filePath, "utf8")) as Record<string, unknown>;
  if (investor.slug !== slug) {
    throw new Error(`${filePath} carries slug "${investor.slug}", not "${slug}"`);
  }

  console.log(`Fetching ${sourceUrl} ...`);
  const source = /^https?:/i.test(sourceUrl) ? await download(sourceUrl) : readFileSync(sourceUrl);

  const result = await normalize(source, { plate, allowUpscale, allowLowContrast });
  const { buffer: master, before, after, notes } = result;
  console.log(`  source  ${result.source.format} ${result.source.width}x${result.source.height}` +
    `${result.source.vector ? " (vector)" : ""}; on the ${MASTER_SIZE}px canvas: ${describe(before)}`);
  notes.forEach((n) => console.log(`  ${n}`));
  console.log(`  master  ${describe(after)}`);

  const provenance: Provenance = {
    source_url: sourceUrl, format: result.source.format, width: result.source.width, height: result.source.height,
    vector: result.source.vector,
    artwork_source_px: result.source.vector ? null : result.artworkSourcePx,
    artwork_master_px: result.artworkMasterPx, upscale: Number(result.upscale.toFixed(3)),
    ramp_px: Number(after.rampWidth.toFixed(2)), master_size: MASTER_SIZE,
    fetched: new Date().toISOString().slice(0, 10), allow_upscale: allowUpscale,
    allow_low_contrast: allowLowContrast,
  };

  if (dryRun) {
    writeFileSync(dryRun, master);
    console.log(`✓ dry run: wrote ${dryRun} (${master.length} bytes), nothing uploaded`);
    console.log(`  provenance ${JSON.stringify(provenance)}`);
    return;
  }

  const url = process.env.SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL;
  const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!url || !serviceKey) {
    throw new Error("Missing Supabase credentials. Set SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY.");
  }

  const hash = createHash("sha256").update(master).digest("hex").slice(0, 10);
  const objectPath = `investors/${slug}-${hash}.png`;

  const supabase = createClient(url, serviceKey);
  const { error: uploadError } = await supabase.storage
    .from(BUCKET)
    .upload(objectPath, master, {
      contentType: "image/png",
      cacheControl: "31536000",
      upsert: false,
    });
  // The content hash makes re-runs idempotent: the same master already
  // uploaded is not an error.
  if (uploadError && !/already exists/i.test(uploadError.message)) {
    throw new Error(`Upload failed: ${uploadError.message}`);
  }

  const { data: publicUrlData } = supabase.storage.from(BUCKET).getPublicUrl(objectPath);
  const iconUrl = publicUrlData.publicUrl;

  investor.icon_url = iconUrl;
  writeFileSync(filePath, `${JSON.stringify(investor, null, 2)}\n`);

  // Provenance into the sources sidecar, so --audit and the next reader know
  // what the master was made from.
  const sPath = sourcesFile(slug);
  if (existsSync(sPath)) {
    const sources = JSON.parse(readFileSync(sPath, "utf8"));
    sources.fields = sources.fields ?? {};
    const basis = `fetched ${provenance.fetched} by scripts/fetch-investor-icon.ts from ${sourceUrl}: ` +
      `${provenance.format} ${provenance.width}x${provenance.height}${provenance.vector ? " (vector, rendered at 2x)" : ""}, ` +
      (provenance.vector ? "" : `artwork ${provenance.artwork_source_px}px in the source → `) +
      `${provenance.artwork_master_px}px in the ${MASTER_SIZE}px master (${provenance.upscale.toFixed(2)}x); ` +
      `${notes.filter((n) => !n.startsWith("resolution:")).join("; ")}; master ${describe(after)}` +
      (allowUpscale ? "; published with --allow-upscale" : "") +
      (allowLowContrast ? "; published with --allow-low-contrast (brand plate accepted by Erik)" : "");
    sources.fields.icon_url = { value: iconUrl, source: sourceUrl, basis, provenance };
    writeFileSync(sPath, `${JSON.stringify(sources, null, 2)}\n`);
    console.log(`✓ provenance in investor/sources.json`);
  }

  console.log(`✓ Uploaded ${objectPath} (${master.length} bytes)`);
  console.log(`✓ icon_url in investor.json: ${iconUrl}`);
  console.log(`Next: npm run ingest:investor -- --investors name=${slug} --columns icon_url`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
