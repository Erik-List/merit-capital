import re, subprocess, sys, time, json
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128.0 Safari/537.36"
out={}
for path in sys.argv[1:]:
    url=f"https://stockanalysis.com/{path}/market-cap/"
    r=subprocess.run(["curl","-sL","-m","40","-A",UA,url],capture_output=True)
    page=r.stdout.decode('utf-8','replace')
    m=re.search(r"([^.>]{0,120}) has a market cap or net worth of ([^ ]+ [\d.,]+ (?:trillion|billion|million)|\$[\d.,]+ (?:trillion|billion|million)) as of ([A-Z][a-z]+ \d{1,2}, \d{4})", page)
    t=re.search(r"<title>([^<]*)</title>", page)
    out[path]={"url":url,"sentence":m.group(0)[-260:] if m else None,"title":t.group(1) if t else None, "len":len(page)}
    print(path, '|', t.group(1) if t else None, '|', m.group(0)[-200:] if m else 'NO MATCH')
    time.sleep(1)
