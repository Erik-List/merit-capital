"""Fetch one capture (raw id_ form) through the shared IA throttle. usage: get.py <ts> <url> <outfile>"""
import importlib.util, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[6]
sys.path.insert(0, str(ROOT / "scripts"))
spec = importlib.util.spec_from_file_location("wp", ROOT / "scripts" / "wayback-pull.py")
wp = importlib.util.module_from_spec(spec); spec.loader.exec_module(wp)
ts, url, out = sys.argv[1:4]
dest = Path(__file__).parent / "raw" / out
dest.parent.mkdir(exist_ok=True)
wp.fetch(wp.wb(ts, url, raw=True), dest); print(dest.name, dest.stat().st_size if dest.exists() else None)
