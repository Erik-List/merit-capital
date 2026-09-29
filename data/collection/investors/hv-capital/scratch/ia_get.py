"""Fetch archived captures through ia_fetch (machine-wide IA throttle) in raw id_ mode.
Usage: ia_get.py <ts> <original-url> <dest>"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
import ia_fetch
ts, orig, dest = sys.argv[1:4]
body, st = ia_fetch.get(f"https://web.archive.org/web/{ts}id_/{orig}")
if st.startswith("2") and body:
    Path(dest).write_bytes(body)
print(st, len(body or b""), dest)
