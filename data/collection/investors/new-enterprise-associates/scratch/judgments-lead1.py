"""Lead rows after the scheduled rebuild (PRO-100 NEA): Glacier Bay (split from Glacier; the rebuild's rename step
had moved Serious Materials' answers onto it, removed before prepare), Viracta (the resurfaced twin of Sunesis),
Northern Power Systems (its control tag), Cohere Technologies (the Cohere Networks mix-up). Every citation read."""
import judge_lib as jl

GB_FORMD = "https://www.sec.gov/Archives/edgar/data/1470797/000147079709000001/0001470797-09-000001-index.htm"
GB_BLUECREST = "https://www.sec.gov/Archives/edgar/data/1516970/000104746911007707/a2204627zn-2a.htm"
SUNESIS_8K = "https://www.sec.gov/Archives/edgar/data/1061027/000114420409018324/v145069_8k.htm"

L = []
L.append(jl.verdict("glacier-bay-inc", "member",
    "The firm's own 2008 Energy Technology list (captured July 2008) and its 2013 detail page (CompanyDetail.aspx?id=1347, "
    "Current, Private) list Glacier Bay, Inc., 'an energy technology platform company'; its August 2009 Form D names NEA's "
    "Mark Perry and Arno Penzias as directors.", ec="site_listing", conf="high", cite=jl.ARCH("glacier-bay-inc")))
L.append(jl.cls("glacier-bay-inc", status="unknown", rng="below_1b", stage="Series A", stage_src="model",
    stage_conf="medium", stage_cite=GB_BLUECREST, entry_date="2008", country="US", country_src="formd_address",
    city="Union City", city_src="formd_address", focus="Climate & Energy",
    rounds=[jl.rnd("2009-08-11", "unnamed (Form D)", 4300000, source=GB_FORMD, source_type="filing")],
    note=("Energy-efficiency products maker in Union City, California (incorporated 2006), not the recycling-robotics "
          "Glacier the firm backed in 2022. The firm listed it by July 2008 (the entry year). A lender's 2011 schedule "
          "(BlueCrest Capital Finance N-2/A) holds a warrant on its Series A preferred, the only preferred series on "
          "record, so NEA's entry reads as the Series A; the 2009 Form D sold $4.3M of a $10M offering. Nothing names "
          "the company after the firm's 2013 page, so its fate is unknown.")))
L.append(jl.verdict("viracta-therapeutics-formerly-sunesis", "not_member",
    "X1, one company with the not_member Sunesis row: Sunesis Pharmaceuticals merged with private Viracta in 2021 and "
    "took its name, and the firm's own 2024-2026 page names it 'Viracta Therapeutics (formerly Sunesis)'. NEA's "
    "position is the April 2009 private placement into already listed Sunesis (8-K of 2009-04-01), with no earlier "
    "NEA private round, so the listed company's later name is out on the same test.",
    ec="fund_filing", conf="high", cite=SUNESIS_8K))
L.append(jl.cls("cohere-technologies", stage="undetermined", entry_date="2013", flags=["stage_disputes_band"],
    note=("The Growth band rode the company's first own Form D (a $50M offering, March 2015), but the firm's own entry "
          "year is 2013 and Lightspeed's card has the seed in 2011, so NEA entered in a round between the two that no "
          "source names: the stage is undetermined.")))
jl.write("lead1", L)
