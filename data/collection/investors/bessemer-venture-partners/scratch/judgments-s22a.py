"""Second pass s22, file a: rows first seen 1969 to 2000 (queue/s2-2.json). Entry stages read off the firm's own
archived sentences (ARCH), statuses and cities settled. Only changed keys are emitted; notes append to the stored
note."""
import judge_lib as jl

cls, rnd, ARCH, W = jl.cls, jl.rnd, jl.ARCH, jl.W


def firm_round(slug, date, label):
    return [rnd(date, label, None, None, True, ARCH(slug), "firm")]


lines = [
    cls("icot", status="acquired", stage="Series A", stage_src="first_party", stage_cite=ARCH("icot"),
        stage_conf="medium", entry_date="1968", city="San Jose", flags=("pre_spinout",),
        rounds=firm_round("icot", "1968", "first round"),
        note="Second pass: the firm's archived description says BVP participated in the first round in 1968, read "
             "Series A as the first round since nothing suggests an earlier seed; the entry date follows that "
             "sentence. ICOT took the name Amati Communications in 1995 (from memory) and Texas Instruments acquired "
             "Amati in 1997 (Wikipedia, Texas Instruments), so acquired; city San Jose from memory."),
    cls("numerax", status="acquired", flags=("pre_spinout",), rounds=[],
        note="Second pass: acquired by McGraw-Hill in 1986 per the firm's later description, which says Bill Burgin "
             "invested in 1972. The firm's earlier text, which says first round in 1974, describes another company "
             "(Numerex, wireless products), so the round stays undetermined. City still not established."),
    cls("micro-peripherals", stage="Seed", stage_src="first_party", stage_cite=ARCH("micro-peripherals"),
        stage_conf="high", entry_date="1978", flags=("pre_spinout",),
        rounds=firm_round("micro-peripherals", "1978", "seed"),
        note="Second pass: the firm's archived description says that in 1978 BVP invested in the seed and most of the "
             "subsequent rounds. The same text dates the sale to CTS 1984, the firm's list 1983. Graduation left for "
             "the graduation pass."),
    cls("polaris-petroleum", stage="Seed", stage_src="first_party", stage_cite=ARCH("polaris-petroleum"),
        stage_conf="high", entry_date="1979", flags=("pre_spinout",),
        rounds=firm_round("polaris-petroleum", "1979", "seed round"),
        note="Second pass: the firm's archived description says Bill Burgin invested in the 1979 seed round; the "
             "company merged with Cabre Exploration in 1992 per the same text. Graduation left for the graduation "
             "pass."),
    cls("compumotor", city="Petaluma", flags=("pre_spinout",),
        note="Second pass: city Petaluma, California, from memory (Compumotor Corporation before Parker Hannifin "
             "bought it in 1986). The firm's text names no round."),
    cls("vitelic", stage="Series A", stage_src="first_party", stage_cite=ARCH("vitelic"), stage_conf="medium",
        entry_date="1984", rounds=firm_round("vitelic", "1984", "first of four rounds"),
        note="Second pass: the firm's archived description says BVP participated in all four of the company's rounds, "
             "starting in 1984, so it was in the first round; read Series A since nothing suggests an earlier seed."),
    cls("the-sports-authority", entry_date="1987-04",
        rounds=[rnd("1987", "founding venture round", None, "William Blair Venture Partners", True,
                    W("Sports Authority"), "press")],
        note="Second pass: entry date April 1987 from the firm's own success page. Wikipedia says the company was "
             "founded in 1987 by a venture syndicate led by William Blair that included Bessemer, and the firm says "
             "it took part in the 1987 and 1988 rounds; no source labels the founding round, so the stage stays "
             "undetermined."),
    cls("netframe-systems", stage="Growth", stage_src="first_party", stage_cite=ARCH("netframe-systems"),
        stage_conf="high", entry_date="1988", rounds=firm_round("netframe-systems", "1988", "later rounds"),
        note="Second pass: the firm's archived description says Neill Brownstein invested in the company's later "
             "rounds, read Growth."),
    cls("myco-pharmaceuticals", stage="Seed", stage_src="first_party", stage_cite=ARCH("myco-pharmaceuticals"),
        stage_conf="high", entry_date="1990", rounds=firm_round("myco-pharmaceuticals", "1990", "seed"),
        note="Second pass: the firm's archived description says Chris Gabrieli invested in the seed and all "
             "subsequent rounds. The firm's list dates the investment 1990 although the same text gives 1992 as the "
             "founding year; the list year is kept. Graduation left for the graduation pass."),
    cls("versant-object-technology", rng="below_1b", city="Redwood City", city_src="web_verified", rounds=[],
        note="Second pass: Wikipedia (Versant Corporation) places the last headquarters in Redwood City and confirms "
             "the sale to Actian in late 2012, so below $1B with no mark. The firm says it led an investment round in "
             "1990, which names no round."),
    cls("horizon-cellular-group", status="acquired", stage="Series A", stage_src="first_party",
        stage_cite=ARCH("horizon-cellular-group"), stage_conf="medium", entry_date="1992",
        rounds=firm_round("horizon-cellular-group", "1992", "first round"),
        note="Second pass: the firm's archived description says Bill Burgin participated in Horizon Cellular's first "
             "round in 1992, read Series A as the first round since nothing suggests an earlier seed. The same text "
             "says the company sold its assets to other operators in 1997, so acquired. City still not established."),
    cls("american-medical-communications", country="US", clear=("country_unknown",),
        note="Second pass: United States, inferred from the name and from its merger into New York's Medsite.com, "
             "the later name on the firm's list; city still not established."),
    cls("celcore", stage="Series A", stage_src="first_party", stage_cite=ARCH("celcore"), stage_conf="medium",
        entry_date="1994", city="Memphis", rounds=firm_round("celcore", "1994", "first round"),
        note="Second pass: the firm's archived description says BVP participated in the company's first round in "
             "1994, read Series A as the first round since nothing suggests an earlier seed. City Memphis, Tennessee, "
             "from memory."),
    cls("cellaccess", stage="Series A", stage_src="first_party", stage_cite=ARCH("cellaccess"), stage_conf="medium",
        entry_date="1995-09", rounds=firm_round("cellaccess", "1995-09", "only venture round"),
        note="Second pass: the firm's archived description says David Cowan led the only venture round in September "
             "1995, two months before Fore Systems bought the company; read Series A as the first and only venture "
             "round."),
    cls("powertel-pcs-partners", entry_date="1995-01", city="West Point", city_src="web_verified", rounds=[],
        note="Second pass: entry date January 1995 from the firm's own success page; Wikipedia (Powertel) places the "
             "company in West Point, Georgia. The firm says Bill Burgin led its 1995 investment, which names no "
             "round."),
    cls("airtech", city="Aylesbury", rounds=[],
        note="Second pass: city Aylesbury, Buckinghamshire, from memory. The firm says Felda Hardymon invested in the "
             "1997 spin-out of the business, which names no round; whether the investor group bought control "
             "(decisions.md R1) was not checked."),
    cls("omnia-communications", stage="Series A", stage_src="first_party", stage_cite=ARCH("omnia-communications"),
        stage_conf="medium", city="Marlborough", city_src="web_verified",
        rounds=firm_round("omnia-communications", "1996", "first of three rounds"),
        note="Second pass: the firm's archived description says BVP invested in all three rounds, so it was in the "
             "first; read Series A since nothing suggests an earlier seed. Wikipedia (Ciena) places Omnia in "
             "Marlborough, Massachusetts."),
    cls("altiga-networks", stage="Series A", stage_src="first_party", stage_cite=ARCH("altiga-networks"),
        stage_conf="medium", entry_date="1998", city="Franklin",
        rounds=firm_round("altiga-networks", "1998", "first of three rounds"),
        note="Second pass: the firm's archived description says BVP invested in all three rounds starting in 1998, so "
             "it was in the first; read Series A since nothing suggests an earlier seed. City corrected to Franklin, "
             "Massachusetts, where Cisco's 2000 purchase placed the company (from memory)."),
    cls("emed-technologies", country="US", clear=("country_unknown",),
        note="Second pass: United States from memory (a Massachusetts medical-imaging software company, bought by "
             "Cedara Software in 2004); the town is not established, so the city stays unknown."),
    cls("mobile-systems-international", city="London",
        note="Second pass: city corrected to London, where Mo Ibrahim's MSI was headquartered (from memory); "
             "Cambridge was a first-pass recall."),
    cls("telocity", stage="Series A", stage_src="first_party", stage_cite=ARCH("telocity"), stage_conf="high",
        entry_date="1998", rounds=firm_round("telocity", "1998", "first venture round"),
        note="Second pass: the firm's 2002 to 2007 site description says David Cowan co-led the first venture round "
             "in 1998, read Series A."),
    cls("endonetics", stage="Growth", stage_src="first_party", stage_cite=ARCH("endonetics"), stage_conf="high",
        entry_date="1999", country="US", city="San Diego", clear=("country_unknown",),
        rounds=firm_round("endonetics", "1999", "expansion round"),
        note="Second pass: the firm's archived description says Chris Gabrieli invested in the 1999 expansion round, "
             "read Growth; Medtronic bought the company in 2001 per the same text. San Diego, California, from "
             "memory."),
    cls("envoy-networks", country="US", clear=("country_unknown",),
        note="Second pass: United States from memory; the firm's text describes a developer of broadband wireless "
             "infrastructure bought by Texas Instruments in 2002 (the first-pass note calling it a DSL company is "
             "wrong). The town is not established, so the city stays unknown."),
    cls("pirus-networks", stage="Seed", stage_src="first_party", stage_cite=ARCH("pirus-networks"), stage_conf="high",
        rounds=firm_round("pirus-networks", "1999", "seed"),
        note="Second pass: the firm's 2002 to 2007 site description says BVP seeded the company in late 1999; the "
             "firm's own investment date of 2000-01-18 is kept as the entry date. Graduation left for the graduation "
             "pass."),
]

jl.write("s22a", lines)
