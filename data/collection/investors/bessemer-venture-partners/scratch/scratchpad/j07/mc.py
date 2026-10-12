import sys,re,subprocess
for t in sys.argv[1:]:
    h=subprocess.run(["curl","-s","-A","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36",f"https://stockanalysis.com/stocks/{t}/market-cap/"],capture_output=True,text=True).stdout
    x=re.sub(r'<[^>]+>',' ',h); x=re.sub(r'\s+',' ',x)
    m=re.search(r'market cap[^.]{0,300}',x,re.I)
    print(t, m.group(0) if m else x[:200]); print()
