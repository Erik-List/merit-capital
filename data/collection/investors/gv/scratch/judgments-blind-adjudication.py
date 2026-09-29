#!/usr/bin/env python3
"""Duty 7 adjudication (COLLECTION.md s8; PRO-75, 2026-09-29). A blind second judge re-classified a seeded 5% sample
(38 rows, scratch/blind/) with no access to the record: 202 of 228 cells agree. Every row with a disagreement
carries `unstable`. Adopted where the blind judge's evidence was read and is stronger (named rounds the grind
missed, a newer filed address, an asset sale, a merger); kept where ours is better cited. Notes carry only the new
sentence (record appends)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl  # noqa: E402

U = ["unstable"]
D7 = "Duty 7 (blind 5%, 2026-09-29): "
L = [
 # adopted
 jl.cls("arda-therapeutics", stage="Seed", stage_src="model", stage_conf="low", entry_date="2021-12-17",
        grad="graduated", grad_src="web_verified", grad_conf="medium",
        grad_cite="https://www.businesswire.com/news/home/20241009367860/en/Arda-Therapeutics-Secures-%2443M-Series-A-Financing-to-Advance-Targeted-Cell-Depletion-Therapies",
        flags=U + ["stage_uncited"],
        note=D7 + "the firm listed Arda from its May 2022 capture, before the October 2024 Series A, and the only earlier "
             "financing is the December 2021 round a16z calls the Seed, so GV entered at the seed (model, low: no page "
             "names GV in it); the named $43M Series A graduates it."),
 jl.cls("blue-vision-labs", stage="Series A", stage_src="web_verified", stage_conf="high", entry_date="2018-03-15",
        stage_cite="https://techcrunch.com/2018/03/15/blue-vision-labs-which-builds-collaborative-ar-emerges-from-stealth-with-14-5m-led-by-gv/",
        flags=U, note=D7 + "TechCrunch (2018-03-15): '$14.5 million in a new Series A led by Alphabet's GV', after a $2.5M "
                          "seed, with Tom Hulme joining the board: GV's entry. Focus kept (the blind read DevTools)."),
 jl.cls("circuithub", country="US", country_src="formd_address", city="South Deerfield", city_src="formd_address",
        flags=U, note=D7 + "CircuitHub, Inc. (CIK 1708548) files its Form Ds from San Francisco (2017-2021) and South "
                          "Deerfield, Massachusetts (from 2023, https://www.sec.gov/Archives/edgar/data/1708548/"
                          "000170854823000004/0001708548-23-000004-index.htm): a US company whose YC directory entry "
                          "names its London team, so US, South Deerfield."),
 jl.cls("ipierian", stage="Growth", stage_src="formd_structural", stage_conf="medium",
        stage_cite="https://www.sec.gov/Archives/edgar/data/1468247/000146824710000001/0001468247-10-000001-index.htm",
        flags=U, note=D7 + "by s6's structural rule: Krishna Yeshwant first appears on the July 2010 filing ($28.97M "
                          "sold), after the company's 2009 round, and a 2010 round above the era's $12M Series A "
                          "ceiling reads Growth."),
 jl.cls("lifemine-therapeutics", stage="Series A", stage_src="model", stage_conf="medium", flags=U + ["stage_disputes_band"],
        note=D7 + "the band read the September 2017 filing ($70M sold, the first to list GV's Krishna Yeshwant) as Growth "
                  "by size, but the company named its January 2021 round the Series B (Business Wire, "
                  "https://www.businesswire.com/news/home/20210107005231/en/LifeMine-Therapeutics-Announces-%2450-Million-Series-B-Financing), "
                  "so the 2017 round, after a $5M single-investor round in 2016, is its Series A (model, medium). City "
                  "kept (the blind read Watertown from the company site, which did not load)."),
 jl.cls("modern-age", status="acquired", flags=U,
        note=D7 + "the clinic closed in March 2024 and reopened under new ownership, 'the company's IP having been "
                  "purchased by Dr. Ali Rashan', who runs it as Modern Age (WWD, 2024-08-16, https://wwd.com/"
                  "beauty-industry-news/wellness/longevity-clinic-modern-age-reopening-1236546132/): an asset sale with "
                  "the business continuing, acquired under s6."),
 jl.cls("mohawk", city="Summit", city_src="formd_address", flags=U,
        note=D7 + "the current principal office on EDGAR is 350 Springfield Avenue, Summit, New Jersey (Aterian, Inc., "
                  "CIK 1757715); New York was the 2019 S-1's address."),
 jl.cls("quettra", stage="Seed", stage_src="web_verified", stage_conf="high", entry_date="2014-08-08",
        stage_cite="https://techcrunch.com/2014/08/08/mobile-intelligence-startup-quettra-comes-out-of-stealth-raises-2-9m-seed-round/",
        grad="not_graduated", grad_src="web_verified", grad_conf="high", grad_asof="2026-09-29",
        grad_cite="https://techcrunch.com/2015/12/10/similarweb-buys-quettra-to-move-deeper-into-mobile-analytics-and-big-data/",
        surfaces=["firm: the firm's own posts and listings for Quettra -> listed 2014 and 2015 (M.G. Siegler); no post "
                  "names a later round",
                  "formd: EDGAR for Quettra -> no Form D by the company",
                  "techcrunch: TechCrunch's own search (Quettra) -> the 2014-08-08 seed, a 2015-05-15 product story and "
                  "the 2015-12-10 SimilarWeb purchase; no later round",
                  "googlenews: Google News (Quettra) -> The Information (2015-04-07) and Globes (2015-12-10) on the "
                  "SimilarWeb purchase; no later round"],
        flags=U, note=D7 + "TechCrunch (2014-08-08) names Google Ventures in the $2.9M seed round: GV's entry. SimilarWeb "
                          "bought the company in December 2015 (TechCrunch, 2015-12-10) with no later round, so the "
                          "seed was its last: not graduated on a cited end. City left open (the blind read Mountain View "
                          "from LinkedIn only)."),
 jl.cls("ribon-therapeutics", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2021-07-14",
        flags=U, note=D7 + "BioSpace (2021-07-14, https://www.biospace.com/ribon-therapeutics-snags-65-million-to-"
                          "advance-lead-candidates) lists GV among the new investors in the $65M round; with five earlier "
                          "Form Ds the round reads Growth (model, medium)."),
 jl.cls("scalus", status="acquired", flags=U,
        note=D7 + "TechCrunch (2016-10-26): the founder 'merged two of her companies, three-year-old Scalus and "
                  "six-year-old BackOps into a new company called HireAthena' "
                  "(https://techcrunch.com/2016/10/26/a-founder-seizes-on-anti-trump-sentiment-to-market-women-friendly-workflow-software/): "
                  "a merger into a successor, acquired."),
 jl.cls("tenxer", focus="DevTools & APIs", flags=U,
        note=D7 + "focus DevTools & APIs (engineering-productivity analytics for engineering teams), as the blind read."),
 # kept, flagged
 jl.cls("air-protein", flags=U, note=D7 + "city kept at Pleasanton (its 2020 Form D); the blind read San Leandro from LinkedIn."),
 jl.cls("amino", flags=U, note=D7 + "stage kept at Series A (USV's own post); TechCrunch and Wikipedia call the same $1.65M round a seed."),
 jl.cls("benson-hill", flags=U, note=D7 + "focus kept at Climate & Energy; the blind read Healthcare & Bio (crop genetics)."),
 jl.cls("creativelive", flags=U, note=D7 + "focus kept at Media, Gaming & Advertising; the blind read Consumer & Marketplaces."),
 jl.cls("hubspot", flags=U, note=D7 + "band kept at 10b_plus on the 2026-09-28 close ($10.11B); the blind read $9.92B on "
                                        "2026-09-29, within 1% of the edge."),
 jl.cls("locbox", flags=U, note=D7 + "city left open; the blind read San Francisco from LinkedIn only."),
 jl.cls("plangrid", flags=U, note=D7 + "stage kept at Seed (Fortune names Google Ventures in the $1.5M first round); the "
                                         "blind read undetermined from Wikipedia, which does not name GV."),
 jl.cls("puppet-labs", flags=U, note=D7 + "focus kept at DevTools & APIs; the blind read Data Infrastructure."),
 jl.cls("rodin-therapeutics", flags=U, note=D7 + "stage kept undetermined; the blind cites an Atlas (LifeSciVC) post "
                                                   "naming GV in the 2017 Series B, which could not be read to confirm."),
 jl.cls("spruce-finance", flags=U, note=D7 + "city kept at San Francisco (its own filings while independent); the blind "
                                               "read Houston, the successor Spruce Power Holding's address."),
]
jl.write("blind-adjudication", L)
