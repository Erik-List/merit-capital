// Extract the firm's blog/stories from the Nuxt /stories payload into compact rows.
const fs = require("fs");
const [,, inPath, outPath] = process.argv;
const src = fs.readFileSync(inPath, "utf8");
let captured = null;
new Function("__NUXT_JSONP__", src)((route, data) => { captured = { route, data }; });
const d = captured.data.data[0];
function rich(node) {
  if (!node) return "";
  if (Array.isArray(node)) return node.map(rich).join("");
  if (typeof node === "string") return node;
  if (node.nodeType === "text") return node.value || "";
  if (node.fields) return Object.values(node.fields).filter(v => typeof v === "string" || (v && typeof v === "object")).map(v => typeof v === "string" ? v + " " : "").join("");
  return (node.content || []).map(rich).join("");
}
const rows = [];
for (const a of d.articles || []) {
  const f = a.fields || {};
  const rel = (f.relatedCompanies || []).map(c => c && c.fields ? { title: c.fields.title, slug: c.fields.slug } : null).filter(Boolean);
  const author = f.author && f.author.fields ? f.author.fields.name : null;
  const body = (f.markdown || "") + (f.content ? " " + rich(f.content) : "");
  rows.push({ slug: f.slug, title: f.title, date: f.date, category: f.category, type: f.typeTalkAbout,
              author, related_companies: rel, excerpt: typeof f.excerpt === "string" ? f.excerpt : rich(f.excerpt),
              url: f.slug ? `https://creandum.com/stories/${f.slug}` : (f.url || null),
              text: body.replace(/\s+/g, " ").trim().slice(0, 6000) });
}
rows.sort((a, b) => (a.date || "").localeCompare(b.date || ""));
fs.writeFileSync(outPath, JSON.stringify({ _readme: "creandum.com/stories decoded from the site's own Nuxt static payload (/_nuxt/static/<build>/stories/payload.js) on 2026-09-04: every article the CMS publishes (the firm's blog since 2009, migrated into Contentful), with date, category, author, the CMS's related-company links and the body text (markdown or rich text, truncated at 6,000 chars). 'Companies' posts naming a round are class-1 entry-round citations (COLLECTION.md §6); the URL is the live story page.", articles: rows }, null, 1));
console.log("stories:", rows.length, "with related companies:", rows.filter(r => r.related_companies.length).length, "with text:", rows.filter(r => r.text.length > 50).length);
