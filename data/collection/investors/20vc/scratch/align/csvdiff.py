"""Row-level diff of an investor's companies/base.csv: HEAD vs the working tree.
Prints every changed slug with the columns that changed; added/removed slugs too."""
import csv, io, subprocess, sys
inv = sys.argv[1]
path = f"data/collection/investors/{inv}/companies/base.csv"
head = subprocess.run(["git", "show", f"HEAD:{path}"], capture_output=True, text=True).stdout
a = {r["slug"]: r for r in csv.DictReader(io.StringIO(head))}
b = {r["slug"]: r for r in csv.DictReader(open(path))}
added, removed = sorted(set(b) - set(a)), sorted(set(a) - set(b))
changed = {s: [k for k in b[s] if a[s].get(k) != b[s].get(k)] for s in set(a) & set(b)}
changed = {s: v for s, v in changed.items() if v}
print(f"{inv}: {len(a)} -> {len(b)} rows; added {added}; removed {removed}; changed {len(changed)}")
for s, cols in sorted(changed.items()):
    print(f"   {s}: {cols}")
