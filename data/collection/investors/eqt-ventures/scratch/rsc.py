import re, json, sys
def rsc_stream(html):
    chunks = re.findall(r'self\.__next_f\.push\(\[1,(".*?")\]\)</script>', html, re.S)
    return ''.join(json.loads(c) for c in chunks)
def find_objs(obj, key, out):
    if isinstance(obj, dict):
        if key in obj: out.append(obj)
        for v in obj.values(): find_objs(v, key, out)
    elif isinstance(obj, list):
        for v in obj: find_objs(v, key, out)
def rsc_records(stream):
    recs = {}
    for line in stream.split('\n'):
        m = re.match(r'^([0-9a-f]+):(.*)$', line)
        if not m: continue
        body = m.group(2)
        if body[:1] in '[{"':
            try: recs[m.group(1)] = json.loads(body)
            except Exception: pass
    return recs
if __name__ == '__main__':
    html = open(sys.argv[1], encoding='utf-8').read()
    st = rsc_stream(html)
    recs = rsc_records(st)
    out = []
    for r in recs.values(): find_objs(r, sys.argv[2], out)
    seen = {}
    for o in out:
        k = o.get('_id') or json.dumps(o)[:80]
        seen[k] = o
    print(len(out), len(seen))
    json.dump(list(seen.values()), open(sys.argv[3], 'w'), indent=1, ensure_ascii=False)
