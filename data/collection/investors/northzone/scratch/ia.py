"""Tiny helpers over scripts/ia_fetch for this run: cdx(prefix) and replay(ts, url)."""
import json, sys, gzip
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
import ia_fetch
CACHE = Path(__file__).resolve().parents[5] / "data" / "filings" / "northzone" / "ia-cache"
CACHE.mkdir(exist_ok=True)

def cdx(q):
    body, code = ia_fetch.get("https://web.archive.org/cdx/search/cdx?" + q)
    if code != "200":
        raise RuntimeError(f"cdx {code}")
    return json.loads(body or b"[]")

def replay(ts, url):
    import hashlib
    key = CACHE / (hashlib.sha1(f"{ts} {url}".encode()).hexdigest() + ".html")
    if key.exists():
        return key.read_text()
    body, code = ia_fetch.get(f"https://web.archive.org/web/{ts}id_/{url}")
    if body[:2] == b"\x1f\x8b":
        try: body = gzip.decompress(body)
        except OSError: pass
    if code != "200":
        raise RuntimeError(f"replay {code} {ts} {url}")
    t = body.decode("utf-8", "replace")
    if not t.strip():
        raise RuntimeError(f"empty {ts} {url}")
    key.write_text(t)
    return t
