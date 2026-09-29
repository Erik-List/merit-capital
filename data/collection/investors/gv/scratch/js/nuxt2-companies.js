// Evaluate a captured gv.com page's window.__NUXT__ (Nuxt 2 over Contentful, 2022-09 to 2025) and print
// the Contentful entries of content type `company` as JSON lines: name, acquiredBy, sector, deal partners.
// The payload is a cyclic object graph (company -> investors -> teamMember -> investments -> company),
// so it is walked with a visited set rather than stringified. Usage: node nuxt2-companies.js <file>
const fs = require("fs");
const html = fs.readFileSync(process.argv[2], "utf8");
const m = html.match(/<script>(window\.__NUXT__=[\s\S]*?)<\/script>/);
if (!m) { process.stdout.write("[]"); process.exit(0); }
const window = {};
eval(m[1]);
const seen = new WeakSet(), out = new Map();
const ctype = (o) => o && o.sys && o.sys.contentType && o.sys.contentType.sys && o.sys.contentType.sys.id;
const nameOf = (o) => (o && o.fields && (o.fields.name || o.fields.fullName || o.fields.title)) || "";
(function walk(o) {
  if (!o || typeof o !== "object" || seen.has(o)) return;
  seen.add(o);
  if (ctype(o) === "company" && o.fields && o.fields.name) {
    const f = o.fields;
    const inv = (f.investors || []).map(nameOf).filter(Boolean);
    const sec = f.sector ? nameOf(f.sector) : "";
    out.set(o.sys.id, {name: f.name, acquiredBy: f.acquiredBy || "", website: f.website || "",
                       investors: inv, sector: sec, id: o.sys.id});
  }
  for (const k of Object.keys(o)) walk(o[k]);
})(window.__NUXT__);
process.stdout.write(JSON.stringify([...out.values()]));
