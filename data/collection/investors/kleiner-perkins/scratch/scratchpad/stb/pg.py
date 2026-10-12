import json,re,html,sys
P=json.load(open('/Users/erik/Developer/merit-capital/data/collection/investors/kleiner-perkins/sources/site/raw/posts.json'))
def txt(p):
    t=html.unescape(re.sub(r'<[^>]+>',' ',(p['content'] or {}).get('rendered','')))
    return re.sub(r'\s+',' ',t)
for n in sys.argv[1:]:
    for p in P:
        t=txt(p); title=html.unescape(p['title']['rendered'])
        if re.search(r'\b'+re.escape(n)+r'\b', title+' '+t):
            sents=[s for s in re.split(r'(?<=[.!?])\s+',t) if n.lower() in s.lower() or re.search(r'(?i)series [a-f]|seed|first invest|led the|our investment|round',s)]
            sents=[s for s in sents if n.lower() in s.lower() or re.search(r'(?i)series [a-f]|seed round|first invest|led the',s)]
            print('##',n,p['date'][:10],p['link'],'|',title[:80])
            for s in sents[:8]: print('   >',s[:300])
