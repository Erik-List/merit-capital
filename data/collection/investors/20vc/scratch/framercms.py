"""Decode a Framer CMS chunk (.framercms) into a list of dict items.

Format (read off the bytes, 2026-09-28): u32 item count; per item a u16 field
count; per field a u32 name length + name, a u8 type tag and the value.
Tags: 0x01 array (u16 count, then tagged elements), 0x02 bool (u8),
0x04 date (u64 ms since epoch), 0x05 enum / 0x07 link / 0x0a image /
0x0c string (u32 length + UTF-8 bytes; link and image are JSON text).
"""
import json, struct, sys, datetime

def read_value(b, p, tag):
    if tag == 0x02:
        return bool(b[p]), p + 1
    if tag == 0x04:
        ms = struct.unpack(">Q", b[p:p+8])[0]
        return datetime.datetime.utcfromtimestamp(ms / 1000).strftime("%Y-%m-%dT%H:%M:%SZ"), p + 8
    if tag in (0x05, 0x07, 0x0a, 0x0c, 0x03, 0x06, 0x08, 0x09, 0x0b):
        n = struct.unpack(">I", b[p:p+4])[0]; p += 4
        s = b[p:p+n].decode("utf-8")
        if tag in (0x07, 0x0a):
            try: s = json.loads(s)
            except Exception: pass
        return s, p + n
    if tag == 0x01:
        n = struct.unpack(">H", b[p:p+2])[0]; p += 2
        out = []
        for _ in range(n):
            t = b[p]; p += 1
            v, p = read_value(b, p, t)
            out.append(v)
        return out, p
    if tag == 0x00:
        return None, p
    raise ValueError(f"unknown tag {tag:#x} at {p}")

def decode(b):
    p = 0
    count = struct.unpack(">I", b[p:p+4])[0]; p += 4
    items = []
    for _ in range(count):
        nf = struct.unpack(">H", b[p:p+2])[0]; p += 2
        it = {}
        for _ in range(nf):
            n = struct.unpack(">I", b[p:p+4])[0]; p += 4
            name = b[p:p+n].decode("utf-8"); p += n
            tag = b[p]; p += 1
            it[name], p = read_value(b, p, tag)
        items.append(it)
    return items, p

if __name__ == "__main__":
    b = open(sys.argv[1], "rb").read()
    items, end = decode(b)
    print(f"items {len(items)}, consumed {end} of {len(b)} bytes", file=sys.stderr)
    json.dump(items, sys.stdout, indent=1, ensure_ascii=False)
