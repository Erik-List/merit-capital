"""The six companies known only from the fund-holdings disclosure, and Avalanche's value (Erik, 2026-10-07)."""
from jl import *
U = "https://s3.documentcloud.org/documents/25971902/howery-kenneth-final278.pdf"
R("appcard", "private", "New York", SAAS, stage="undetermined", co="US", note="Loyalty and shopper analytics for grocers. Held by Fund IV per the 2025 disclosure; the round the fund first bought (about 2013) was not established.")
R("five-apes", "unknown", "Palo Alto", AI, stage="undetermined", co="US", note="Image-recognition software. Held by Fund III per the 2025 disclosure; nothing else about the company or its round was found.")
R("indigo-technologies", "private", "Woburn", IND, stage="undetermined", co="US", note="Nucleus Scientific until 2019: in-wheel motors and light electric vehicles. Held by Fund IV per the 2025 disclosure; the round is not established.")
R("instapray", "unknown", "San Francisco", CON, stage="undetermined", co="US", note="Prayer social network. Held by Fund IV per the 2025 disclosure; the round is not established and the app has left no recent trace.")
R("neurotrack", "private", "Redwood City", HB, stage="undetermined", co="US", note="Cognitive-health testing. Held by Fund IV per the 2025 disclosure; Founders Fund is named in its 2012 and later rounds, the first of which was not pinned.")
R("theaudience", "unknown", "Los Angeles", MED, stage="undetermined", co="US", note="Social-media publishing for entertainers, co-founded by Sean Parker in 2011. Held by Fund III per the 2025 disclosure; the business was reported sold to Al Ahli Holding in 2015, which the continued holding does not confirm.")
C("avalanche", valuation_usd=None, valuation_range="below_1b", valuation_source=None, valuation_citation=None, valuation_asof=None,
  note="Ava Labs. The position came through the Avalanche Foundation's token sales (2021), not a priced equity round, so stage and graduation read undetermined. No priced round of the company carries a citable figure (the $5.25B of 2022 was a report of talks), and the AVAX network's market value ($2.97B in August 2026) is a token price, not a mark on the company: below $1B, the network value kept here as context (Erik, 2026-10-07).")
write("c8-oge-avalanche")
