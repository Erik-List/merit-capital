"""Lead overrides 1 (2026-10-01): the Forge team's prior-firm companies that bvp.com/companies carried in its
January 2022 capture only (decisions.md R4). not_member, with the firm's own Forge page for the company as citation."""
import json
import judge_lib as jl
man = json.loads((jl.INV / "sources/wayback/cc-manifest.json").read_text())
def forge_page(slug):
    c = sorted((v["timestamp"], v["capture_url"]) for v in man.values() if v.get("status") == "ok"
               and v.get("path", "").rstrip("/") in (f"/forge/experience/{slug}", f"/forge/companies/{slug}", f"/forge/partner/{slug}"))
    if not c:
        raise SystemExit(f"no forge page capture for {slug}")
    return c[0][1]
ROWS = {"1010data": "1010data", "absensesoft": "absensesoft", "appriss": "appriss", "avetta": "avetta", "cority": "cority",
        "diligent": "diligent", "galvanize": "galvanize", "supplier-io": "supplier-io",
        "the-retail-equation": "the-retail-equation", "turnitin": "turnitin", "vector-solutions": "vector-solutions"}
lines = []
for slug, fslug in ROWS.items():
    lines.append(jl.verdict(slug, "not_member",
        "Listed on bvp.com/companies only in the January 2022 capture, when the site folded in the BVP Forge team's "
        "'Our Experience' companies: a company the Forge partners worked with at their previous firms or a BVP Forge "
        "buyout, not a position of the venture funds (partner-carried rule, Erik 2026-09-17; decisions.md D2, R4).",
        ec="site_listing", conf="high", cite=forge_page(fslug)))
jl.write("lead1", lines)
