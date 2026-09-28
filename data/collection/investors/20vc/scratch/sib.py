import csv, glob, re, sys
def key(n): return re.sub(r"[^a-z0-9]", "", n.lower())
want = {key(a): a for a in sys.argv[1:]}
for f in sorted(glob.glob("data/collection/investors/*/companies/base.csv")):
    inv = f.split("/")[3]
    if inv == "20vc": continue
    for row in csv.DictReader(open(f, newline="")):
        k = key(row["name"])
        if k in want:
            print(f"{want[k]} | {inv} | {row['status']} {row['valuation_range']} {row['valuation_usd']} asof={row['valuation_asof']} src={row['valuation_source']} | {row['valuation_citation']}")
            print(f"     stage {row['entry_stage']} {row['entry_stage_source']} {row['entry_date']} {row['entry_stage_citation']} | S2A {row['seed_to_a_graduation']} {row['graduation_source']} {row['graduation_citation']}")
            print(f"     {row['hq_country']}/{row['hq_city']} {row['focus']} | {row['note'][:300]}")
