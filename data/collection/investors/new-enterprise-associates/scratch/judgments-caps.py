"""A/B pass A for public members (lead): the market cap of 2026-09-30 from stockanalysis.com, cited and dated,
replacing SEC-float values (COLLECTION.md s6: a public row's canonical value is its market cap; the float
corroborates). Non-US listings converted at the ECB rate of the date (fx-convert.py). Skips non-members and the
duplicate rows that merge away at the rebuild."""
import json
import judge_lib as jl
caps = json.load(open("caps.json"))
led = json.load(open("../companies/membership-ledger.json"))["new-enterprise-associates"]["verdicts"]
merges = json.load(open("../companies/identity-merges.json"))["new-enterprise-associates"]["merges"]
dups = {d for m in merges for d in m["duplicates"]}
def band(u):
    return "100b_plus" if u >= 1e11 else "10b_plus" if u >= 1e10 else "1b_plus" if u >= 1e9 else "below_1b"
L = []
for s, c in sorted(caps.items()):
    if c.get("status") != "ok" or led.get(s, {}).get("verdict") != "member" or s in dups:
        continue
    u = round(c["usd"])
    rng = band(u)
    edge = any(abs(u - e) / e < 0.05 for e in (1e9, 1e10, 1e11))
    fx = f" ({c['fx_note']})" if c.get("fx_note") and c.get("currency") != "USD" else ""
    note = (f"Market cap ${u/1e9:.2f}B on {c['asof']} (stockanalysis.com){fx}"
            + ("; within 5% of a band edge" if edge else "") + ".")
    L.append(jl.cls(s, status="public", rng=rng, usd=u, val_src="web_verified", val_cite=c["url"], asof=c["asof"],
                    val_conf="high", note=note, extra={"valuation_range_source": "web_verified"}))
print(len(L), "lines")
jl.write("caps", L)
