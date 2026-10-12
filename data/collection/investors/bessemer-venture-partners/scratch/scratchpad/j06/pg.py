import sys,re,html,subprocess
url,pat=sys.argv[1],sys.argv[2]
n=int(sys.argv[3]) if len(sys.argv)>3 else 8
t=subprocess.run(["curl","-sL","-m","40","-A","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36",url],capture_output=True).stdout.decode("utf-8","replace")
t=re.sub(r'<script[\s\S]*?</script>|<style[\s\S]*?</style>',' ',t)
t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\s+',' ',t)
print("len",len(t))
k=0
for m in re.finditer(r'[^.]{0,260}('+pat+r')[^.]{0,260}\.',t):
    print('  >',m.group(0)[:520]); k+=1
    if k>=n: break
