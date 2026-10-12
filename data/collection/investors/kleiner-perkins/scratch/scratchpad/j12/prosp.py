import importlib.util,re,sys,json
sp=importlib.util.spec_from_file_location('sg','secget.py'); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
ciks=dict(a.split('=') for a in sys.argv[1:])
for k,c in ciks.items():
    t=m.get(f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={c}&type=424B&dateb=&owner=include&count=40&output=atom")
    ents=re.findall(r'(\d{4}-\d{2}-\d{2})\s+(https://www\.sec\.gov/Archives/edgar/data/\S+?-index\.html?)\s+(424B\d)', t)
    ents=sorted(ents)
    print('##',k,c,[(d,f) for d,u,f in ents][:6])
    if not ents: continue
    d,u,f=ents[0]
    full=re.sub(r'-index\.html?$','.txt',u)
    doc=m.get(full)
    print('   doc',full,len(doc))
    for mm in list(re.finditer(r'Kleiner', doc))[:4]:
        s=max(0,mm.start()-500); print('   ...',re.sub(r'\s+',' ',doc[s:s+900]))
