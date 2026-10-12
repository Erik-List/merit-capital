import subprocess, re, sys
for cik in sys.argv[1:]:
    out = subprocess.run(["python3","secget.py",f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik}&type=S-1&dateb=&owner=include&count=40","--grep","Acc-no","--max","50","--width","6000"],capture_output=True,text=True).stdout
    accs = re.findall(r"(S-1/A|S-1|424B\d)\s+Documents.{0,120}?Acc-no: (\d{10}-\d\d-\d{6}).{0,40}?(\d{4}-\d\d-\d\d)", out)
    seen = {}
    for f,a,d in accs: seen[a]=(f,d)
    print("CIK", cik, sorted(((d,f,a) for a,(f,d) in seen.items()))[:4])
