"""Batch 6 (pass 1): the rest of the Form D name-match rows, judged cluster-first as in
batch 5. Merged legal entities carry no line: nomnomnow-inc (Nom Nom), rizio-inc
(Voicea); merchantry-inc is the canonical of the Ixtens/Merchantry pair."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, verdict, write, rnd  # noqa: E402

MAT_BIO = "https://headline.com/team/matt-brown/"
BROWN = ("Matthew / Matt Brown cluster: Headline's Matt Brown joined from The Chernin Group (earlier Wag and Stripes Group, "
         "his CMS bio); the name is common, the firm lists none of these companies, and no Headline round was found.")
IXTENS = "https://techcrunch.com/2010/09/27/ixtens-secures-4-6-million-series-a-from-greycroft-partners-and-bv-capital/"
MUNCH = "https://techcrunch.com/2012/11/08/meals-marketplace-munchery-raises-4-million-for-expansion-now-delivering-high-quality-meals-to-all-of-bay-area-l-a-in-2013/"
PESTO = "https://finance.yahoo.com/news/pesto-spices-digital-workplaces-remote-130004679.html"
GENTRACE = "https://siliconangle.com/2024/12/10/generative-ai-app-testing-platform-gentrace-raises-8m-make-llm-development-accessible/"
REELIO = "https://www.tubefilter.com/2015/08/26/reelio-5-million-series-a/"
ZUMPER = "https://www.zumper.com/blog/zumper-raises-60-million-series-d-led-by-e-ventures/"
VIAVIA = "https://www.sec.gov/Archives/edgar/data/1929563/000192956326000001/0001929563-26-000001-index.htm"
MEADOW = "https://www.alleywatch.com/2025/04/meadow-higher-education-payments-platform-student-financial-services-tuition-payment-university-alfredo-brillembourg/"
L = [
    verdict("lav-gear-parent-inc", "not_member", f"{BROWN} Here a 2016-2019 Woodland Hills holding-company director seat, before his Headline tenure.",
            ec="formd_adjudicated", conf="high", cite=MAT_BIO),
    verdict("livetiles-ltd", "not_member", f"{BROWN} Here an executive officer of LiveTiles, an ASX-listed Australian software company (2018).",
            ec="formd_adjudicated", conf="high", cite=MAT_BIO),
    verdict("mamamancini-s-inc", "not_member", f"{BROWN} Here a director and officer of MamaMancini's, a listed food company (2011-2022): an operator role.",
            ec="formd_adjudicated", conf="high", cite=MAT_BIO),
    verdict("meadow-technologies-inc", "not_member",
            f"{BROWN} Meadow (New York tuition payments) raised its $14M Series A in April 2025 led by Matrix with Susa Ventures, Giant Ventures, Treble Capital and GoGlobal (AlleyWatch); no account names Headline, so the director seat is uncorroborated.",
            ec="formd_adjudicated", conf="medium", cite=MEADOW),
    verdict("merchantry-inc", "member",
            "Merchantry, formerly Ixtens (EDGAR CIK 1502734, renamed): BV Capital co-led Ixtens' $4.6M Series A with Greycroft Partners (TechCrunch 2010-09-27); Gieselmann director on the 2010-2013 Form Ds.",
            ec="web", conf="high", cite=IXTENS),
    cls("merchantry-inc", status="unknown", city="New York", rng="below_1b", stage="Series A", stage_src="web_verified",
        stage_conf="high", stage_cite=IXTENS, entry_date="2010-09",
        note="Ixtens (marketplace software for retailers), renamed Merchantry; Series A $4.6M led by Greycroft and BV Capital with Marvin Traub Associates (2010-09-27); later Form Ds 2011 and 2013 ($7M). Current state not established.",
        rounds=[rnd("2010-09-27", "Series A", 4600000, "Greycroft Partners; BV Capital", True, IXTENS, "press")]),
    verdict("munchery-inc", "member",
            "Munchery: e.ventures led the $4M Series A (TechCrunch 2012-11-08; Wikipedia names E.ventures among its investors); Gieselmann director on the 2012-2015 Form Ds. Its co-founder Conrad Chu later joined Headline.",
            ec="web", conf="high", cite=MUNCH),
    cls("munchery-inc", status="defunct", city="San Francisco", rng="below_1b", stage="Series A", stage_src="web_verified",
        stage_conf="high", stage_cite=MUNCH, entry_date="2012-11", flags=["stage_disputes_band"],
        note="e.ventures led the $4M Series A (announced 2012-11-08); the Form D band had read the first filing as a Seed. Shut down January 2019 after about $125M raised (Wikipedia).",
        rounds=[rnd("2012-11-08", "Series A", 4000000, "e.ventures", True, MUNCH, "press")]),
    verdict("national-energy-improvement-fund-llc", "not_member", f"{BROWN} Here the director of an Allentown, Pennsylvania energy-efficiency lender (2018, 2024), not a venture company.",
            ec="formd_adjudicated", conf="high", cite=MAT_BIO),
    verdict("pattern89-inc", "not_member", f"{BROWN} Here an executive officer of Pattern89, Indianapolis (2018): an operator role.",
            ec="formd_adjudicated", conf="high", cite=MAT_BIO),
    verdict("pragli-inc", "member",
            "Pragli, Inc. is Pesto, now Gentrace (founders Doug Safreno and Vivek Nair). Headline led Pesto's $5M seed (TechCrunch, February 2022) and joined Gentrace's $8M Series A (December 2024); Jett Fein, then a Headline partner, is director on the 2023-2025 Form Ds.",
            ec="web", conf="high", cite=PESTO),
    cls("pragli-inc", status="private", city="San Francisco", rng="below_1b", stage="Seed", stage_src="web_verified",
        stage_conf="high", stage_cite=PESTO, entry_date="2022-02",
        grad="graduated", grad_src="web_verified", grad_cite=GENTRACE, flags=["stage_disputes_band"],
        note="Pragli (virtual office, 2020 pre-seed led by K9) became Pesto, then Gentrace (LLM testing). Headline led the $5M seed (2022-02-01); Gentrace's $8M Series A was led by Matrix with Headline and K9 (2024-12-10). The withheld Form D band read the 2023 filing as Pre-Seed.",
        rounds=[rnd("2020-04", "Pre-Seed", None, "K9 Ventures", False, "https://www.k9ventures.com/blog/2020/04/14/the-story-of-how-why-k9-invested-in-pragli/", "firm"),
                rnd("2022-02-01", "Seed", 5000000, "Headline", True, PESTO, "press"),
                rnd("2024-12-10", "Series A", 8000000, "Matrix", True, GENTRACE, "press")]),
    verdict("promo-works-holding-corp", "not_member",
            "Michael Kent homonym: director of a New York promotions company (2009-2010); Headline's Michael Kent is Azimo's London founder, at the firm from about 2022.",
            ec="formd_adjudicated", conf="high"),
    verdict("quantifi-inc", "not_member", f"{BROWN} Here an executive officer (2017).",
            ec="formd_adjudicated", conf="high", cite=MAT_BIO),
    verdict("reelio-inc", "member",
            "Reelio (New York influencer marketplace): Andreas Haug director on the 2014-2015 Form Ds, and e.ventures named in the syndicate of its $5M Series A (Tubefilter 2015-08-26).",
            ec="web", conf="high", cite=REELIO),
    cls("reelio-inc", status="unknown", city="New York", rng="below_1b",
        grad="graduated", grad_src="web_verified", grad_cite=REELIO, entry_date="2014-02-21",
        note="e.ventures' first filing is the 2014 seed ($1.29M, Haug director); the $5M Series A followed in August 2015 with e.ventures in the syndicate. Current state not established.",
        rounds=[rnd("2014-02-21", "Seed", 1295000, None, True, "https://www.sec.gov/Archives/edgar/data/1601883/000123191914000032/0001231919-14-000032-index.htm", "filing"),
                rnd("2015-08-26", "Series A", 5000000, None, True, REELIO, "press")]),
    verdict("research-imaging-company-llc", "not_member", f"{BROWN} Here the director of a Teaneck, New Jersey imaging-centre company ($57M, 2023), not a venture round.",
            ec="formd_adjudicated", conf="high", cite=MAT_BIO),
    verdict("simuwatt-inc", "not_member", f"{BROWN} Here an executive officer of simuwatt, Boulder (2024): an operator role.",
            ec="formd_adjudicated", conf="high", cite=MAT_BIO),
    verdict("sourcepass-holdings-llc", "not_member", f"{BROWN} Here the director of an East Northport, New York IT-services roll-up (2022).",
            ec="formd_adjudicated", conf="high", cite=MAT_BIO),
    verdict("that-s-us-technologies-inc", "not_member", f"{BROWN} Here an executive officer of a Tampa issuer (2012).",
            ec="formd_adjudicated", conf="high", cite=MAT_BIO),
    verdict("thoughtforge-inc", "not_member", f"{BROWN} Here an executive officer of a Berkeley issuer (2022).",
            ec="formd_adjudicated", conf="high", cite=MAT_BIO),
    verdict("viavia-corp", "member",
            "Director of record (COLLECTION.md s1): Clarey Zhu, a current Headline growth investor with an exact distinctive name, is director on ViaVia Corp's 2026 Form D ($30.1M), in tenure, and the issuer resolves to VIAVIA, the West Hollywood video-first fashion commerce company (seed $8M 2022 co-led by NEA and Basis Set). No announcement yet; medium, flagged for the A/B pass.",
            ec="formd_adjudicated", conf="medium", cite=VIAVIA),
    cls("viavia-corp", status="private", city="West Hollywood", rng="below_1b", flags=["formd_adjudicated", "unannounced_deal"],
        note="VIAVIA: seed $8M (2022, NEA and Basis Set), Series A 2025 (Form D $10M), then the 2026 $30.1M round with Clarey Zhu on the filing, from the growth fund."),
    verdict("wildcat-topco-inc", "not_member", f"{BROWN} Here a 2020-2022 Santa Monica holding-company director seat, during his Chernin Group years (T4).",
            ec="formd_adjudicated", conf="high", cite=MAT_BIO),
    verdict("zumper-inc", "member",
            "Zumper: 'Zumper Raises $60 Million Series D Led By E.ventures' (the company's own blog, March 2020); Jonathan Turner director on the 2020-2022 Form Ds. decisions.md D4 (the reverse): Accel's run reads this e.ventures-era seat the same way.",
            ec="web", conf="high", cite=ZUMPER),
    cls("zumper-inc", status="private", city="San Francisco", rng="below_1b", stage="Growth", stage_src="web_verified",
        stage_conf="high", stage_cite=ZUMPER, entry_date="2020-03", flags=["model_disputes_source"],
        note="e.ventures led the $60M Series D (March 2020), Greycroft joining. Zumper operates (a CEO transition in March 2026); the 'acquired' pre-fill is wrong. Aligned with the a16z row (private, below_1b).",
        rounds=[rnd("2020-03-10", "Series D", 60000000, "e.ventures", True, ZUMPER, "company")]),
]
if __name__ == "__main__":
    write("batch-006", L, record="--dry" not in sys.argv)
