import "dotenv/config";
import { createHash } from "node:crypto";
import { readFileSync, writeFileSync } from "node:fs";
import path from "node:path";
import { createClient } from "@supabase/supabase-js";
import sharp from "sharp";

// Fetch an investor's logo from a source URL, normalize it to the 256x256
// PNG master (contain; the source's own background is kept, padding is
// transparent), upload it to the "Icon Images" bucket under
// investors/<slug>-<contenthash>.png, and write the public URL into the
// investor's icon_url in data/collection/investors/<slug>/investor.json.
// The DB row updates through the normal ingest:
//   npm run ingest:investor -- --investors name=<slug> --columns icon_url
//
// Usage: tsx scripts/fetch-investor-icon.ts <slug> <source-url>

const BUCKET = "Icon Images";
const MASTER_SIZE = 256;
const investorFile = (slug: string) =>
  path.join(process.cwd(), "data/collection/investors", slug, "investor.json");

async function main() {
  const [slug, sourceUrl] = process.argv.slice(2);
  if (!slug || !sourceUrl) {
    throw new Error("Usage: tsx scripts/fetch-investor-icon.ts <slug> <source-url>");
  }

  const url = process.env.SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL;
  const serviceKey =
    process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!url || !serviceKey) {
    throw new Error(
      "Missing Supabase credentials. Set SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY."
    );
  }

  const filePath = investorFile(slug);
  const investor = JSON.parse(readFileSync(filePath, "utf8")) as Record<
    string,
    unknown
  >;
  if (investor.slug !== slug) {
    throw new Error(`${filePath} carries slug "${investor.slug}", not "${slug}"`);
  }

  console.log(`Fetching ${sourceUrl} ...`);
  const response = await fetch(sourceUrl, {
    headers: { "user-agent": "Mozilla/5.0 (compatible; MeritCapital icon fetch)" },
  });
  if (!response.ok) {
    throw new Error(`Source fetch failed: ${response.status} ${response.statusText}`);
  }
  const source = Buffer.from(await response.arrayBuffer());

  const master = await sharp(source)
    .resize(MASTER_SIZE, MASTER_SIZE, {
      fit: "contain",
      background: { r: 0, g: 0, b: 0, alpha: 0 },
    })
    .png()
    .toBuffer();

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
  console.log(
    `Next: npm run ingest:investor -- --investors name=${slug} --columns icon_url`
  );
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
