import sys,re,html,subprocess,hashlib,os
from pathlib import Path
C=Path(__file__).resolve().parent/'cache'; C.mkdir(exist_ok=True)
def get(url):
    f=C/(hashlib.sha1(url.encode()).hexdigest()+'.txt')
    if f.exists(): return f.read_text()
    r=subprocess.run(['curl','-sL','-m','40','-A','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36',url],capture_output=True)
    t=r.stdout.decode('utf-8','replace')
    t=re.sub(r'<script[\s\S]*?</script>|<style[\s\S]*?</style>',' ',t)
    t=re.sub(r'</(p|div|li|h\d|tr|br)>|<br\s*/?>','\n',t)
    t=html.unescape(re.sub(r'<[^>]+>',' ',t))
    t=re.sub(r'[ \t\r\f\v]+',' ',t)
    f.write_text(t); return t
if __name__=='__main__':
    url=sys.argv[1]; pat=sys.argv[2] if len(sys.argv)>2 else r'Kleiner|KPCB'
    t=get(url); print('len',len(t))
    n=0
    for para in t.split('\n'):
        if re.search(pat,para,re.I) and len(para.strip())>30:
            print('  >',para.strip()[:700]); n+=1
            if n>=12: break
