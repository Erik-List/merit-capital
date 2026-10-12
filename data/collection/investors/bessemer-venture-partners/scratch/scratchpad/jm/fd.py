import json,sys,re,subprocess
sys.path.insert(0,'.')
import secget
base={r['slug']:r for r in json.load(open('../companies/base.json'))}
for s in sys.argv[1:]:
    links=[l.strip() for l in (base[s].get('formd_links') or '').split(';') if l.strip()]
    print('###',s,base[s]['name'],len(links),'filings')
    for l in links[-2:]:
        u=l.rsplit('/',1)[0]+'/primary_doc.xml'
        try:
            raw=subprocess.run(["curl","-sL","-m","60","-H","User-Agent: Merit Capital research erik@meritcapit.al",u],capture_output=True).stdout.decode('utf-8','replace') if False else None
            t=secget.get(u)
        except SystemExit as e:
            print('  fail',u); continue
        t=re.sub(r'\s+',' ',t)
        print('  ',u)
        print('   ',t[:1400])
