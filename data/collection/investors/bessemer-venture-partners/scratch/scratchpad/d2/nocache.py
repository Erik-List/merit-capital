import re, sys, html, subprocess
from pathlib import Path
sys.path.insert(0, str(Path('.').resolve().parents[4] / "scripts"))
import shared_throttle
UA = "Merit Capital research erik@meritcapit.al"
def get(url):
    shared_throttle.wait("sec")
    r = subprocess.run(["curl", "-sL", "-m", "120", "-H", f"User-Agent: {UA}", url], capture_output=True)
    t = r.stdout.decode("utf-8", "replace")
    t = re.sub(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>", " ", t)
    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    return re.sub(r"[ \t\r\f\v]+", " ", t)
if __name__ == "__main__":
    t = get(sys.argv[1]); pat = sys.argv[2]; w = int(sys.argv[3]) if len(sys.argv) > 3 else 900; mx = int(sys.argv[4]) if len(sys.argv) > 4 else 6
    print("doc chars", len(t)); n = 0
    for m in re.finditer(pat, t, re.I):
        s = max(0, m.start() - w // 3); print("...", re.sub(r"\s+", " ", t[s:s + w]), "...\n"); n += 1
        if n >= mx: break
