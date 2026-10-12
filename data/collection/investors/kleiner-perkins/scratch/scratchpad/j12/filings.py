import importlib.util,re,sys,json
sp=importlib.util.spec_from_file_location('sg','secget.py'); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
ciks={'individual':1002536,'keravision':946154,'mslo':1091801,'nextcard':1081015,'onsale':1026506,'platinum':891178,'preview':1047121,'prism':1008129,'raster':753081,'resonate':1026380,'rhythms':1065869,'seec':925524,'silicongaming':1013170}
for k,c in ciks.items():
    out=[]
    for typ in ['424B','S-1']:
        try:
            t=m.get(f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={c}&type={typ}&dateb=&owner=include&count=40&output=atom")
        except SystemExit as e:
            out.append(f'{typ} FAIL'); continue
        rows=re.findall(r'(\d{4}-\d{2}-\d{2})\s.*?(https://www\.sec\.gov/Archives/edgar/data/\S+?-index\.htm)', t)
        out.append(f"{typ}: {[(d,u) for d,u in rows[:4]]}")
    print(k, c, out)
