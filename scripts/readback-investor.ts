// Read-only readback of an investor's published people: public.investors.individuals
// for one or more slugs, compared with investor/investor.json in the working tree
// (names, positions and both social links). Run before a re-ingest it lists what the
// ingest would change; run after, it must print 0 differing people per slug.
// Usage: npx tsx scripts/readback-investor.ts <slug> [<slug> ...]
import "dotenv/config";
import { readFileSync } from "fs";
import { createClient } from "@supabase/supabase-js";

type Person = { name: string; position: string | null; socials?: { linkedin_url?: string | null; x_url?: string | null } };

function norm(p: Person) {
  return JSON.stringify({
    name: p.name, position: p.position ?? null,
    linkedin: p.socials?.linkedin_url ?? null, x: p.socials?.x_url ?? null,
  });
}

async function main() {
  const slugs = process.argv.slice(2);
  if (!slugs.length) throw new Error("usage: readback-investor.ts <slug> [<slug> ...]");
  const url = process.env.SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL!;
  const sb = createClient(url, process.env.SUPABASE_SERVICE_ROLE_KEY!);
  let total = 0;
  for (const slug of slugs) {
    const want: Person[] = JSON.parse(
      readFileSync(`data/collection/investors/${slug}/investor/investor.json`, "utf8")).individuals ?? [];
    const { data, error } = await sb.from("investors").select("individuals").eq("slug", slug).maybeSingle();
    if (error) throw new Error(error.message);
    if (!data) { console.log(`readback ${slug}: no investor row`); total++; continue; }
    const live: Person[] = (data.individuals as Person[] | null) ?? [];
    const liveBy = new Map(live.map((p) => [p.name, norm(p)]));
    const wantNames = new Set(want.map((p) => p.name));
    let diffs = 0;
    for (const p of want) {
      const got = liveBy.get(p.name);
      if (got === undefined) { diffs++; console.log(`  MISSING in DB  ${slug}: ${p.name}`); continue; }
      if (got !== norm(p)) { diffs++; console.log(`  DIFF ${slug}: ${p.name}\n    db   ${got}\n    file ${norm(p)}`); }
    }
    for (const p of live) if (!wantNames.has(p.name)) { diffs++; console.log(`  EXTRA in DB    ${slug}: ${p.name}`); }
    const linked = (ps: Person[]) => ps.filter((p) => p.socials?.linkedin_url || p.socials?.x_url).length;
    console.log(`readback ${slug}: file ${want.length} people (${linked(want)} linked), db ${live.length} ` +
                `(${linked(live)} linked), differing people ${diffs}`);
    total += diffs;
  }
  console.log(`readback total: ${total} differing people over ${slugs.length} investor(s)`);
}
main();
