#!/usr/bin/env python3
"""Post-close delta (2026-09-06): the three companies the corrected 2002-2003
sector-page parser recovered, plus the identity flags those pages resolve."""
import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from emit import build

PW = ("Pre-window position on the firm's own archived listings; entry_stage and "
      "graduation are null by the 2006 policy constant.")
REC = ("Recovered 2026-09-06 by the corrected sector-page parser: the 2002-2003 "
       "sector pages render each company as a summary card, not the bare <li> the "
       "all_alpha and prior_investments pages use, so the era read as empty.")

build([
 ("bravanta-com", "defunct", "US", "San Francisco", None,
  "Bravanta (listed as Bravanta.com in 2002), 'provider of global Enterprise "
  "Incentive and Recognition (EIR) programs' in Menlo's own words; a dot-com-era "
  "enterprise incentives platform. First and only listed 2002-2003, then absent "
  "from every later Menlo surface including the Prior Investments page, with no "
  "priced exit on record — read as a write-off rather than an exit. " + REC + " " + PW,
  {"flags": ["pre_window"], "focus": "SaaS", "focus_source": "model",
   "valuation_range": "below_1b"}),

 ("covalent-technologies", "acquired", "US", "San Francisco", None,
  "Covalent Technologies, 'enterprise solutions for the Apache web server' in "
  "Menlo's own words: commercial support and the Enterprise Ready Server "
  "distribution, and a major Apache Software Foundation contributor. SpringSource "
  "acquired Covalent in January 2008 on undisclosed terms; VMware bought "
  "SpringSource the following year. Listed 2002-2003. " + REC + " " + PW,
  {"flags": ["pre_window"], "focus": "DevTools & APIs", "focus_source": "model",
   "valuation_range": "below_1b"}),

 ("lantern-communications", "defunct", "US", "San Jose", None,
  "Lantern Communications, a 'next generation metro Ethernet company' in Menlo's "
  "own words: optical metro transport equipment built for the 2000-2001 carrier "
  "build-out. Listed 2002-2003 and absent from every later surface; wound down in "
  "the optical bust with no recorded exit. " + REC + " " + PW,
  {"flags": ["pre_window"], "focus": "Data Infrastructure", "focus_source": "model",
   "valuation_range": "below_1b"}),

 # Identity flags the recovered descriptions resolve — outcomes untouched.
 ("big-bear-networks", None, "US", "Sunnyvale", None,
  "Identity resolved 2026-09-06: the recovered 2002 sector page names this row "
  "'Big Bear Networks' and describes it as 'opto-electronic modules for high-speed "
  "optical networks', a Sunnyvale optical-components startup. That retires the "
  "thin-identification note and the disputed GB namesake pre-fill.",
  {"clear_flags": ["identity_uncertain", "model_disputes_source"]}),

 ("parama-networks", None, None, None, None,
  "Identity confirmed 2026-09-06: the recovered 2002 sector page describes Parama "
  "Networks as 'state-of-the-art, dense, scalable Optical Transport Management "
  "solutions', matching the SONET-over-storage switching identification already on "
  "the record. Outcome unchanged.",
  {"clear_flags": ["identity_uncertain"]}),

 ("phiar-corporation", None, None, None, None,
  "Identity confirmed 2026-09-06: the recovered 2002 sector page describes Phiar "
  "Corporation as 'high-speed photonic switching applications', matching the "
  "metal-insulator tunnelling diode identification already on the record and "
  "confirming it is not the later Phiar Technologies AR startup. That pair is now "
  "ruled distinct in cross-investor.json. Outcome unchanged.",
  {"clear_flags": ["identity_uncertain"]}),
], "delta-001.out.jsonl")
