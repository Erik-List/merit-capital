"""Reproducible text extraction of public SEC and OGE source documents."""
import json
import re
import sys
from pathlib import Path
from pypdf import PdfReader
sys.path.insert(0, str(Path(__file__).resolve().parents[5] / 'scripts'))
from paths import Paths, write_atomic
p = Paths('founders-fund')
src = p.root / 'sources' / 'web'
for file, key, select, url in [
 ('/tmp/founders-fund-inspect/adv-155462.pdf', 'adv-155462', None, 'https://reports.adviserinfo.sec.gov/reports/ADV/155462/PDF/155462.pdf'),
 ('/tmp/founders-fund-inspect/howery-2025.pdf', 'howery-2025-fund-notes', [26,27,28], 'https://s3.documentcloud.org/documents/25971902/howery-kenneth-final278.pdf')
]:
 r=PdfReader(file)
 pages=[]
 for i in (select if select is not None else range(len(r.pages))):
  t=r.pages[i].extract_text()
  if select is not None:
   # Preserve complete relevant source pages and labels; no personal asset values needed.
   pass
  pages.append({'page':i+1,'text':t})
 write_atomic(src / f'{key}.json', json.dumps({'url':url,'fetched_at':'2026-09-27','pages':pages},indent=2)+'\n')
 print(key,len(pages),'pages')
