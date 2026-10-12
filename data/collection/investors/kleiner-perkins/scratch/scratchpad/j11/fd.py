import subprocess, re, sys
want = set(sys.argv[1:])
for line in open("scratchpad/j11/formd_links.txt"):
    s, rest = line.split(" ", 1)
    if want and s not in want: continue
    u = rest.strip().rsplit(" ", 1)[-1]
    p = rest.strip().rsplit(" ", 1)[0]
    last = p.split(";")[0].split()[-1]
    out = subprocess.run(["python3", "secget.py", u, "--grep", ".", "--max", "1", "--width", "3000"], capture_output=True, text=True).stdout
    out = re.sub(r"\s+", " ", out)
    m = re.search(r"D LIVE \d+ (.{0,110})", out)
    c = re.search(r".{0,20}" + re.escape(last) + r".{0,130}", out, re.I)
    print(s, "|", m.group(1) if m else "", "||", c.group(0) if c else "")
