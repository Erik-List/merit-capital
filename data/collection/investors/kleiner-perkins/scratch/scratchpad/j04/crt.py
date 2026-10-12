import hashlib,re,sys,subprocess
from pathlib import Path
u=sys.argv[1]; pat=sys.argv[2] if len(sys.argv)>2 else r'KPCB|Kleiner'
f=Path('sec-cache',hashlib.sha1(u.encode()).hexdigest()+'.txt')
if not f.exists():
    subprocess.run(['python3','secget.py',u,'--grep','zzzzqqq'],capture_output=True)
t=f.read_text()
t=re.sub(r'<[^>]+>',' ',t); t=re.sub(r'&nbsp;|&#160;|&#xa0;',' ',t); t=re.sub(r'&#8217;|&rsquo;',"'",t); t=re.sub(r'\s+',' ',t)
i=t.find('CERTAIN RELATIONSHIPS AND RELATED')
j=t.find('CERTAIN RELATIONSHIPS AND RELATED',i+100)
k=j if j>0 else i
print('len',len(t),'crt at',i,j)
seg=t[k:k+6000]
print(seg)
