import re,sys
f=sys.argv[1]; names=set(sys.argv[2].split(','))
for blk in open(f).read().split('\n### '):
    n=blk.split(' | ')[0].lstrip('# ')
    if n in names:
        out=[]
        for l in blk.split('\n'):
            if 'researchPost' in l: continue
            l=re.sub(r"first capture \S+","",l)
            out.append(l[:int(sys.argv[3]) if len(sys.argv)>3 else 420])
        print('### '+'\n'.join(out))
