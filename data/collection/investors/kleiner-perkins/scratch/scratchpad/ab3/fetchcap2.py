import re, subprocess, sys, time, json, os
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128.0 Safari/537.36"
res=json.load(open('caps-ab3.json')) if os.path.exists('caps-ab3.json') else {}
for path in sys.argv[1:]:
    url=f"https://stockanalysis.com/{path}/market-cap/"
    r=subprocess.run(["curl","-sL","-m","40","-A",UA,url],capture_output=True)
    page=r.stdout.decode('utf-8','replace')
    t=re.search(r"<title>([^<]*)</title>", page)
    i=page.find('market cap or net worth')
    s=re.sub(r'<[^>]+>','',page[max(0,i-150):i+120]) if i>=0 else None
    m=re.search(r"market cap or net worth of (\S+?) ?([\d.,]+) (trillion|billion|million) as of ([A-Z][a-z]+ \d{1,2}, \d{4})", s or '')
    res[path]={"url":url,"title":t.group(1) if t else None,"sentence":s,
               "ccy":m.group(1) if m else None,"amt":float(m.group(2).replace(',',''))*{"trillion":1e12,"billion":1e9,"million":1e6}[m.group(3)] if m else None,
               "date":m.group(4) if m else None}
    print(path,'|',res[path]['title'],'|',res[path]['ccy'],res[path]['amt'],res[path]['date'])
    time.sleep(1)
json.dump(res,open('caps-ab3.json','w'),indent=1)
