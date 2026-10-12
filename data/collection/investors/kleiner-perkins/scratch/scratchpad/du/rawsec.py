import sys, subprocess, re
from pathlib import Path
HERE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
import shared_throttle
UA = "Merit Capital research erik@meritcapit.al"
def raw(url):
    shared_throttle.wait("sec")
    return subprocess.run(["curl","-sL","-m","60","-H",f"User-Agent: {UA}",url],capture_output=True,text=True).stdout
if __name__=="__main__":
    for u in sys.argv[1:]:
        t=raw(u)
        m=re.search(r"<yearOfInc>[\s\S]*?</yearOfInc>",t)
        n=re.search(r"<entityName>(.*?)</entityName>",t)
        print(n.group(1) if n else None,'|',re.sub(r"\s+","",m.group(0)) if m else t[:200])
