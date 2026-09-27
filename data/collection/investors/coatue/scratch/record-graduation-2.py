#!/usr/bin/env python3
"""Graduation re-check (2026-09-27). The Form D name scan showed a September 2025 single-deal vehicle named after
Meticulous; a web search then found its July 2026 Series A, which the four standard surfaces had missed. Every
absence-test row was therefore re-checked by one web search each, and the Form D lines now say what each hit is."""
import json
from pathlib import Path
INV = Path(__file__).resolve().parents[1]
prev = {json.loads(l)["slug"]: json.loads(l) for l in open(INV / "scratch/queue/agent-a-2.out.jsonl")}
FD = "formd: issuer names beginning '%s' searched in the Form D bulk data 2008q1 to 2026q2 -> %s"
FORMD = {
 "butterflies-ai": FD % ("Butterflies", "one hit, Butterflies of Bill Baker LLC (2013), a different issuer; the company itself never filed"),
 "crypthulhu-studios": FD % ("Crypthulhu", "one filing, Crypthulhu Studios Inc. 2022q1 $2,125,000 sold, which is the seed round itself; no later filing"),
 "sundeck": FD % ("Sundeck", "one hit, Sundeck Investments LP (2026), a different issuer; the company itself never filed"),
 "meld": FD % ("Meld", "no filing"), "product-science": FD % ("Product Science", "no filing"), "lutra-ai": FD % ("Lutra", "no filing"),
 "httpie": FD % ("HTTPie", "no filing"), "fero": FD % ("Fero", "no filing (the company is Dutch and does not file in the US)"), "amo": FD % ("Amo", "not searched by name, the company is French and does not file in the US"),
}
WEB = {
 "butterflies-ai": "websearch: Butterflies AI Vu Tran funding 2025 OR 2026 shut down OR acquired OR raises -> the June 2024 seed announcement is the latest financing reported; no later round, sale or shutdown reported",
 "crypthulhu-studios": "websearch: Crypthulhu Studios Dimension X funding OR shut down OR acquired -> the July 2022 seed is the only financing reported; trademarks abandoned in 2024, no sale or later round",
 "sundeck": "websearch: Sundeck query engineering Series A OR acquired OR funding 2025 -> the May 2023 seed is the only financing reported",
 "meld": "websearch: Meld meld.io funding Series A raised -> one later round, $7M announced 2026-01-14 and led by Lightspeed Faction, which the company calls a strategic round (https://www.prnewswire.com/news-releases/meld-raises-7-million-strategic-round-to-accelerate-global-network-expansion-302661430.html); it carries no series name and is below twice the $8M seed, so it does not graduate the row",
 "product-science": "websearch: Product Science mobile performance funding Series A -> the January 2023 seed is the only financing reported",
 "lutra-ai": "websearch: Lutra AI funding Series A raised 2025 OR 2026 -> the December 2023 seed is the only financing reported",
 "httpie": "websearch: HTTPie funding Series A raised -> the seed is the only financing reported",
 "fero": "websearch: Fero funding Series A Coatue -> the November 2023 seed is the only financing reported (Fero Labs, which raised a Series A, is a different company)",
 "amo": "websearch: Amo app Antoine Martin funding Series A OR acquired OR shut down -> the 2023 round is the only financing reported; no sale or shutdown reported",
}
S = json.load(open(INV / "scratch/graduation-surfaces.json"))
def pubs(k):
    e = S.get(k, {}).get("surfaces", {}); L = []
    for s in ("googlenews", "googlenews_firm", "googlenews_local", "techcrunch", "crunchbase_news"):
        if s in e and e[s].get("status") == "ok": L.append(f"{s}: {e[s].get('query')} -> {e[s].get('n')} items read, none names a later priced round of this company")
    return L
out = []
for k in ("butterflies-ai", "crypthulhu-studios", "sundeck", "meld", "product-science", "lutra-ai", "httpie", "fero"):
    name = FORMD[k].split("'")[1]
    out.append({"slug": k, "seed_to_a_graduation": "not_graduated", "graduation_source": "absence_check", "graduation_asof": "2026-09-27", "flags": [],
                "graduation_surfaces": [f"firm: coatue.com/blog and coatue.com/c/takes searched for {name} -> no post names a later round", FORMD[k], WEB[k]] + pubs(k),
                "note": "Absence test re-checked by web search on 2026-09-27; the Form D line states what each name hit is."})
out.append({"slug": "amo", "entry_date": "2023-03", "seed_to_a_graduation": "not_graduated", "graduation_source": "absence_check", "graduation_asof": "2026-09-27", "flags": ["stage_uncited"],
            "graduation_surfaces": ["firm: coatue.com/blog and coatue.com/c/takes searched for Amo -> no post names a later round", FORMD["amo"], WEB["amo"]] + pubs("amo"),
            "note": "Amo, Paris, social apps by the Zenly founders. Coatue joined the $20M (EUR 18M) round of February or March 2023 led by New Wave (https://techcrunch.com/2023/11/19/with-amo-the-founder-of-zenly-wants-to-make-social-apps-social-again/). That page gives no round word; Sifted's article of 2023-11-27 calls it a seed round in its search snippet, but its body is paywalled and could not be opened, so the stage stays uncited. No later round found."})
def grad(k, cite, note, **kw):
    c = {"slug": k, "seed_to_a_graduation": "graduated", "graduation_source": "first_party", "graduation_citation": cite, "flags": [], "note": note}; c.update(kw); out.append(c)
grad("meticulous-ai", "https://www.meticulous.ai/blog/series-a", "Graduated: the company announced its $15M Series A on 2026-07-14 (its own post). The four standard surfaces had missed it; a September 2025 single-deal vehicle named after the company in the Form D data prompted the search.")
grad("stability", "https://stability.ai/news-updates/stability-ai-latest-funding-backed-by-entertainment-industry-biggest-names", "Graduated: the company announced a $76M Series B on 2026-08-25, with Coatue participating for a second consecutive round (its own post). An unnamed round of about $80M in June 2024 came between the seed and the Series B.")
grad("wisdom-ai", "https://www.wisdom.ai/blog/announcing-our-series-a-funding", "Graduated: the company announced its $50M Series A led by Kleiner Perkins on 2025-11-12 and names Coatue among the previous investors (its own post).")
out.append({"slug": "revops", "status": "acquired", "valuation_range": "below_1b", "seed_to_a_graduation": "not_graduated", "graduation_source": "first_party", "graduation_citation": "https://www.revops.io/blog/maxio-acquires-revops", "graduation_asof": "2026-09-27",
            "graduation_surfaces": ["firm: coatue.com/blog and coatue.com/c/takes searched for RevOps -> no post names a later round", FD % ("RevOps", "six hits, all RevOps Health, Inc. or RevOpsis Therapeutics, different issuers; the company itself never filed"),
                                    "company: revops.io/blog -> Maxio acquired the company, announced 2025-03-03; no round after the seed", "websearch: RevOps.io deal desk funding Series A OR acquired -> the October 2021 seed is the only financing reported"] + pubs("revops"),
            "flags": [], "note": "Maxio acquired RevOps, announced 2025-03-03 (the company's own post); the October 2021 seed was its last round."})
out.append({"slug": "fire-pit-collective-inc", "status": "acquired", "valuation_range": "below_1b", "entry_stage": "Seed", "entry_stage_source": "formd_band", "entry_stage_confidence": "low", "entry_date": "2022-12",
            "hq_country": "US", "hq_country_source": "formd_address", "hq_country_confidence": "high", "focus": "Media, Gaming & Advertising", "focus_source": "model",
            "seed_to_a_graduation": "not_graduated", "graduation_source": "web_verified", "graduation_citation": "https://www.kempersports.com/2025/07/kempersports-acquires-fire-pit-productions/", "graduation_asof": "2026-09-27",
            "graduation_surfaces": ["firm: coatue.com portfolio, blog and takes searched for Fire Pit -> not named anywhere", "formd: the company's own sequence (CIK 1862796) -> one filing, December 2022, a $5M equity offering with nothing sold at filing; no later filing",
                                    "company: kempersports.com -> KemperSports acquired Fire Pit Productions, announced 2025-07-16", "websearch: Fire Pit Collective golf Matt Ginella funding investors raised -> no financing reported after 2022; the founder describes downsizing before the sale"],
            "flags": ["boundary", "needs_review"], "note": "Fire Pit Collective, golf media, Oceanside CA. The only evidence of a position is Thomas Laffont as director on the December 2022 Form D ($5M offering, nothing sold at filing); the firm never names the company, so a personal holding is possible (open ruling). KemperSports acquired Fire Pit Productions in July 2025; its page names Productions, not Collective, so the match of the two entities is read from the founder's own account."})
FX = {"mech-mind": ("9615", 10.41e9, 1327130974.0, "HKD 10.41B @ ECB 2026-09-25 (HKD/EUR 8.9445, EUR/USD 1.1403) = $1.33B"), "kujiale": ("0068", 13.59e9, 1732536978.0, "HKD 13.59B @ ECB 2026-09-25 (HKD/EUR 8.9445, EUR/USD 1.1403) = $1.73B")}
for k, (t, hkd, usd, note) in FX.items():
    out.append({"slug": k, "status": "public", "valuation_usd": usd, "valuation_source": "web_verified", "valuation_citation": f"https://stockanalysis.com/quote/hkg/{t}/market-cap/", "valuation_asof": "2026-09-25",
                "valuation_range": "1b_plus", "valuation_range_source": "web_verified", "valuation_confidence": "high", "clear_flags": ["needs_web_value", "needs_review", "stale"], "flags": [],
                "note": f"Cap pass: listed in Hong Kong (HKG:{t}); the exchange's page quotes the cap in HKD; {note} as of 2026-09-25 (stockanalysis.com)."})
(INV / "scratch/queue/graduation-2.out.jsonl").write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in out))
print(len(out), "lines")
