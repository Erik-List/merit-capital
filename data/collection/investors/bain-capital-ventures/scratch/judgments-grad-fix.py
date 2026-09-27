"""PRO-162 graduation pass follow-ups (list A judge): EverTrue's entry was a Series A, not the band's Seed; DCG's graduation
rests on its one later priced event, open for Erik."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
TC = "https://techcrunch.com/2013/03/21/techstars-alum-evertrue-lands-5-25m-from-bain-david-cohen-bonobos-ceo-to-reinvent-fundraising-in-education/"
CNBC = "https://www.cnbc.com/2021/11/01/digital-currency-group-sees-10-billion-valuation-as-softbank-google-invest.html"
L = [
    jl.cls("evertrue", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=TC, entry_date="2013-03",
        flags=["stage_disputes_band"],
        note="Donor CRM for education (Boston); the firm lists it as Acquired. 'TechStars Alum EverTrue Lands $5.25M From Bain' "
             "(TechCrunch, 2013-03-21), a '$5.25 million series A funding round, led by Bain Capital Ventures': the Series A, not the "
             "Form D band's Seed."),
    jl.cls("digital-currency-group", grad="graduated", grad_src="web_verified", grad_cite=CNBC, grad_conf="medium",
        rounds=[jl.rnd("2021-11", "Secondary sale", 700000000, "SoftBank", None, CNBC, "press")],
        note="Crypto holding company (Stamford, CT; Grayscale's parent). BCV's listing: 2014, Seed (Matt Harris; the 2015 formation "
             "round that also brought in Mastercard and others). The $10B mark is the November 2021 sale of about $700M of shares led "
             "by SoftBank (CNBC); after Genesis's 2023 collapse no newer priced event is known, so it stands, stale. GRADUATION, OPEN "
             "for Erik: DCG raised no later primary round on record; the 2021 transaction priced the company at $10B but sold existing "
             "holders' shares. Read as graduated at medium confidence (verify rule 7 refuses a $1B+ row that did not graduate)."),
]
if __name__ == "__main__":
    jl.write("grad-fix", L)
