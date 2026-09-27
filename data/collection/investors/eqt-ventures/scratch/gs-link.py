"""Resolve a headline in scratch/graduation-surfaces.json to its publisher URL.
Usage: python3 gs-link.py <slug> "<title substring>" """
import json, subprocess, sys
from pathlib import Path
here = Path(__file__).resolve().parent
gs = json.load(open(here / 'graduation-surfaces.json'))
slug, sub = sys.argv[1], sys.argv[2].lower()
for svc, v in (gs[slug].get('surfaces') or {}).items():
    for it in v.get('items') or []:
        if sub in (it.get('title') or '').lower():
            url = it.get('link')
            if not url and it.get('gid'):
                out = subprocess.run([sys.executable, str(here.parents[4] / 'scripts' / 'graduation-surfaces.py'), 'decode', it['gid']],
                                     capture_output=True, text=True).stdout.strip()
                url = out.splitlines()[-1] if out else None
            print(svc, it.get('date'), it.get('title'), '->', url)
            sys.exit(0)
print('not found')
