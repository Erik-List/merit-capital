"""Dry-run a judgments file: build the lines, print a summary, record nothing. NQ_TAG=j05 python3 scratchpad/j05/dry.py judgments-j05a.py"""
import sys, re, json
sys.path.insert(0, ".")
import judge_lib as jl
def fake(name, lines, record=True):
    print("DRY", name, len(lines), "lines")
    for l in lines:
        n = l.get("note") or l.get("basis") or ""
        bad = [w for w in ("—", "–", " prior ", "invariant", "C2A") if w in n]
        print(" ", l["slug"], "| keys", len(l), "| BAD" if bad else "", bad or "")
jl.write = fake
exec(open(sys.argv[1]).read())
