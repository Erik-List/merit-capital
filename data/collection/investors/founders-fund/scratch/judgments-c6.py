"""Own-row corrections after reading the sibling books' evidence for shared companies."""
from jl import *
C("workstream", status="private", flags=["model_disputes_source"], note="Hourly-hiring software. Founders Fund led the $10M Series A of October 2020; the band anchored on the 2021 Series B. Private; the pre-filled 'acquired' was a wrong join.")
for s, n in [("amicus", "Fundraising software for non-profits (Y Combinator, 2012); on the firm's list 2013 to 2014. No closure report found."),
             ("frogmetrics", "Customer-feedback devices (Y Combinator, summer 2008); FF Angel seed. No closure report found."),
             ("readyforce", "College recruiting network listed under FF Angel. No closure report found.")]:
    C(s, status="unknown", note=n)
C("carwoo", status="defunct", note="Car-buying marketplace (Y Combinator) listed under FF Angel. TrueCar hired the team in 2012 and the service closed: defunct under the acqui-hire rule.")
C("all-day-technologies-inc", status="defunct", note="All Day Kitchens (Virtual Kitchen Co. until 2021). Founders Fund led the $20M Series B of September 2020. Wound down during 2024: locations closed and the company stopped responding (the a16z book's A/B evidence, San Francisco Chronicle).")
C("fanbridge", status="acquired", entry_stage="Seed", entry_stage_source="model", entry_stage_confidence="medium", entry_date="2009-03",
  note="Fan-relationship tools for musicians. The $350K seed of March 2009 came from Dave McClure (then running FF Angel), Jeff Clavier and Chris Sacca; the firm lists it under FF Angel. Merged into Amplify.ai, 2018.")
C("backplane", status="acquired", note="Lady Gaga's community platform. Seed of $1.8M 'including Google Ventures, Founders Fund Angel, Menlo Ventures, SV Angel' (TechCrunch, 2012-02-16). Assets sold to an investor group in 2016.")
C("avalanche", **sibling_val("a16z", "avalanche"), note="Ava Labs. The position came through the Avalanche Foundation's token sales (2021), not a priced equity round, so stage and graduation read undetermined. Value is the AVAX network's market capitalisation, as the a16z book reads the same position.")
C("dynamic", status="private", note="Dynamic Labs, wallet authentication. Founders Fund and a16z crypto led the $13.5M Series A of December 2023. Fireblocks agreed to buy it in 2025; the closing is not confirmed in a source read, so it stays private, as the sibling books read it.")
C("bolt-threads", status="public", note="Biomaterials. Founders Fund led the Series A (announced with the 2015 Series B). Public since the August 2024 SPAC merger, trading far below $1B (the 8VC book's A/B check).")
write("c6-fixes")
