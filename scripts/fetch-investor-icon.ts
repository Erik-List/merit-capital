import "dotenv/config";
import { createHash } from "node:crypto";
import { readFileSync, writeFileSync, readdirSync } from "node:fs";
import path from "node:path";
import { createClient } from "@supabase/supabase-js";
import sharp from "sharp";
import { normalize, measure, describe, MASTER_SIZE } from "./utils/icon-normalize";

// Fetch an investor's logo from a source URL, normalize it to the 256x256 PNG
// master, upload it to the "Icon Images" bucket under
// investors/<slug>-<contenthash>.png, and write the public URL into the
// investor's icon_url in data/collection/investors/<slug>/investor.json.
// The DB row updates through the normal ingest:
//   npm run ingest:investor -- --investors name=<slug> --columns icon_url
//
// Normalization is not just a resize: scripts/utils/icon-normalize.ts holds
// the published quality rules (own opaque background, keylined artwork,
// contrast-checked), with the reasoning for each. `--audit` replays those
// rules against icons already published, so a rule added later finds the
// icons that predate it.
//
// Usage:
//   tsx scripts/fetch-investor-icon.ts <slug> <source-url> [options]
//     --plate auto|keep|<colour>   background policy (default auto)
//     --dry-run <out.png>          normalize to a local file, no upload
//   tsx scripts/fetch-investor-icon.ts --audit [slug ...]

const BUCKET = "Icon Images";
const COLLECTION = path.join(process.cwd(), "data/collection/investors");
const investorFile = (slug: string) => path.join(COLLECTION, slug, "investor.json");

const UA = { "user-agent": "Mozilla/5.0 (compatible; MeritCapital icon fetch)" };

async function download(url: string) {
  const response = await fetch(url, { headers: UA });
  if (!response.ok) {
    throw new Error(`Source fetch failed: ${response.status} ${response.statusText}`);
  }
  return Buffer.from(await response.arrayBuffer());
}

/** Replay the current rules against what is already published. Read-only. */
async function audit(slugs: string[]) {
  const targets = slugs.length ? slugs : readdirSync(COLLECTION).filter((d) => {
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
      if (m.plateKind === "bare-glyph") problems.push("NO BACKGROUND (invisible in dark mode)");
      if (m.radiusFraction > 0.86) problems.push(`artwork at ${(m.radiusFraction * 100).toFixed(0)}% of the circle radius (clipped by rounded-full)`);
      if (m.boxFraction > 0.80) problems.push(`artwork fills ${(m.boxFraction * 100).toFixed(0)}% of the canvas (no keyline)`);
      if (m.contrast !== null && m.contrast < 3) problems.push(`contrast ${m.contrast.toFixed(1)}:1 against its own background`);
      console.log(`${slug.padEnd(18)} ${describe(m)}`);
      problems.forEach((p) => { console.log(`${" ".repeat(19)}✗ ${p}`); failures++; });
    } catch (err) {
      console.log(`${slug.padEnd(18)} unreadable: ${(err as Error).message}`);
      failures++;
    }
  }
  if (failures) {
    console.log(`\n${failures} problem(s). Re-run the fetch for those slugs to republish them under the current rules.`);
    process.exit(1);
  }
  console.log("\nAll published icons meet the current rules.");
}

async function main() {
  const argv = process.argv.slice(2);
  if (argv[0] === "--audit") return audit(argv.slice(1));

  const flag = (name: string) => {
    const i = argv.indexOf(name);
    return i >= 0 ? argv[i + 1] : undefined;
  };
  const positional = argv.filter((a, i) =>
    !a.startsWith("--") && !(i > 0 && argv[i - 1].startsWith("--")));
  const [slug, sourceUrl] = positional;
  const plate = flag("--plate") ?? "auto";
  const dryRun = flag("--dry-run");

  if (!slug || !sourceUrl) {
    throw new Error("Usage: tsx scripts/fetch-investor-icon.ts <slug> <source-url> [--plate auto|keep|<colour>] [--dry-run <out.png>]");
  }

  const filePath = investorFile(slug);
  const investor = JSON.parse(readFileSync(filePath, "utf8")) as Record<string, unknown>;
  if (investor.slug !== slug) {
    throw new Error(`${filePath} carries slug "${investor.slug}", not "${slug}"`);
  }

  console.log(`Fetching ${sourceUrl} ...`);
  const source = await download(sourceUrl);

  const { buffer: master, before, after, notes } = await normalize(source, { plate });
  console.log(`  source  ${describe(before)}`);
  notes.forEach((n) => console.log(`  ${n}`));
  console.log(`  master  ${describe(after)}`);

  if (dryRun) {
    writeFileSync(dryRun, master);
    console.log(`✓ dry run: wrote ${dryRun} (${master.length} bytes), nothing uploaded`);
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

  console.log(`✓ Uploaded ${objectPath} (${master.length} bytes)`);
  console.log(`✓ icon_url in investor.json: ${iconUrl}`);
  console.log(`Next: npm run ingest:investor -- --investors name=${slug} --columns icon_url`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
