import sys,re,subprocess,html,urllib.parse
q=sys.argv[1]
u='https://techcrunch.com/?s='+urllib.parse.quote(q)
r=subprocess.run(['curl','-sL','-m','40','-A','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36',u],capture_output=True)
t=r.stdout.decode('utf-8','replace')
seen=[]
for m in re.finditer(r'href="(https://techcrunch\.com/(20\d\d)/\d\d/\d\d/[^"]+)"',t):
    if m.group(1) not in seen: seen.append(m.group(1))
print(len(t)); [print('  ',s) for s in seen[:int(sys.argv[2]) if len(sys.argv)>2 else 12]]
