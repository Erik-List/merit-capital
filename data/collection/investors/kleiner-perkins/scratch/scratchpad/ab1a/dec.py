import sys, json
sys.path.insert(0, '.')
import judge_lib as jl
want = [
 ("fin", "Salesforce Completes Acquisition of Fin - Salesforce"),
 ("cultureamp", "Culture Amp Raises $82M in Series E"),
 ("cultureamp", "Blackbird's new Canva"),
 ("cultureamp", "liquidity event on the backburner"),
 ("front", "Front Raises $59M From High-Profile"),
 ("front", "Raised $66 Million From Sequoia"),
 ("houzz", "raises $165M"),
 ("houzz", "Gets $35M Cash Injection"),
 ("inmobi", "True North picks up $50-60 mn stake in IPO-bound InMobi - Livemint"),
 ("inmobi", "True North Acquires Minority Stake in IPO-Bound InMobi"),
 ("dji", "nabs $75 million"),
 ("dji", "DJI to Raise $1 Billion in Innovative"),
 ("cognition", "Announcing our Series E"),
 ("cognition", "Cognition raises US$1B in latest funding round"),
 ("cognition", "How Windsurf went from OpenAI"),
 ("databricks", "Kleiner Perkins, Founders Fund, SoftBank"),
 ("flock-safety", "Valued At $8.4 Billion In A New Round"),
 ("flock-safety", "Valued at $8.4 Billion Amid"),
 ("flock-safety", "evaluating a sale"),
 ("chainguard", "raises $800M"),
 ("avoca", "Avoca Raises $125M+ at $1B Valuation"),
 ("garner-health", "Closes $100 Million Series E at a $2.74B Valuation to Continue"),
 ("huntress", "Huntress Captures $150M Series D"),
 ("epic-games", "What is Epic Games now worth"),
 ("interos", "raises $20M to expand"),
 ("interos", "Interos.ai Raises Funding"),
 ("built", "raises capital to tackle construction lending"),
 ("built", "Led by Goldman Sachs"),
 ("harvey", "Harvey Raises $550m at $15.5bn Val"),
 ("applied-compute", "Watkins Represents Applied Compute"),
 ("houzz", "Houzz Closes $400 Million Round"),
]
out = {}
for slug, sub in want:
    try:
        out[f"{slug}|{sub}"] = jl.NEWS(slug, sub)
    except SystemExit as e:
        out[f"{slug}|{sub}"] = "ERR " + str(e)
    print(slug, "|", sub, "->", out[f"{slug}|{sub}"], flush=True)
json.dump(out, open("scratchpad/ab1a/dec.json", "w"), indent=1)
