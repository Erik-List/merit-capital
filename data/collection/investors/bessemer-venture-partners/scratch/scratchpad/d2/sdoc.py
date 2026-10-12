import re, sys
sys.path.insert(0, '.')
import secget
def doc(cik, hid, pat, width=700, mx=3):
    adsh, fn = hid.split(":")
    u = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{adsh.replace('-','')}/{fn}"
    try:
        t = secget.get(u)
    except SystemExit as e:
        print("FAILED", u, e); return
    print("##", u)
    n=0
    for m in re.finditer(pat, t, re.I):
        s=max(0,m.start()-width//2)
        print("   ...", re.sub(r"\s+"," ",t[s:s+width]), "...")
        n+=1
        if n>=mx: break
    if not n: print("   (no match)")
if __name__ == "__main__":
    doc(sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]) if len(sys.argv)>4 else 700, int(sys.argv[5]) if len(sys.argv)>5 else 3)
