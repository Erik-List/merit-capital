"""Lead judgments 7 (2026-10-06): adjudication of the blind 5% sample (COLLECTION.md s8 duty 7)."""
import judge_lib as jl
lines = [
    jl.cls("zany-brainy", status="acquired", rng="below_1b",
           note="Blind-sample adjudication 2026-10-06: acquired. Zany Brainy filed for Chapter 11 on 2001-05-15 and its "
                "assets were sold to The Right Start later that year (Wikipedia, 'Zany Brainy', "
                "https://en.wikipedia.org/wiki/Zany_Brainy); an asset sale out of insolvency reads acquired, with the "
                "successor named (COLLECTION.md s6). The successor liquidated the chain in December 2003."),
    jl.cls("datahub", city="Palo Alto", city_src="web_verified",
           note="Blind-sample adjudication 2026-10-06: the company's own about page says 'The company is headquartered in "
                "Palo Alto, California' (https://datahub.com/about/, read 2026-10-06); the city moves from San Francisco."),
    jl.cls("aivar", city="Coimbatore", clear=["city_unknown"],
           note="Blind-sample adjudication 2026-10-06: the blind re-judgment read Coimbatore as the headquarters on the "
                "company's own contact page; taken at that reading."),
]
jl.write("lead7", lines)
