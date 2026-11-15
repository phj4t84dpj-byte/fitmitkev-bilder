# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow", "requests"]
# ///
# G95: baut aus g95/*_s1/_s2.jpg Prüfbögen (klein, beschriftet) und Mosaike in voller Auflösung (zum verlustfreien Zerlegen),
# lädt sie nach g95sheets/ hoch. Mosaik: 5 × 3 Bilder à 1024 × 1280, Reihenfolge siehe g95sheets/_index.json.
import os, io, json, urllib.request
from huggingface_hub import HfApi, hf_hub_download
from PIL import Image, ImageDraw, ImageFont
TOK=os.environ["HF_TOKEN"]; api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
src=urllib.request.urlopen("https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/tools/g95/jobs_g95.py").read()
import re; src=src.decode(); P=json.loads(src[src.index('P=json.loads(r"""')+17:src.index('""")')]); R=[dict(key=k) for k in P]
files=set(api.list_repo_files(REPO,repo_type="dataset"))
def get(p):
    import time
    for a in range(4):
        try:
            import requests
            r=requests.get(f"https://huggingface.co/datasets/{REPO}/resolve/main/{p}",headers={"Authorization":f"Bearer {TOK}"},timeout=60); r.raise_for_status()
            return Image.open(io.BytesIO(r.content)).convert("RGB")
        except Exception as e:
            print("retry",p,repr(e)[:150],flush=True); time.sleep(5)
    raise SystemExit("FAIL "+p)
def up(im,p,q=90):
    b=io.BytesIO(); im.save(b,"JPEG",quality=q); b.seek(0); api.upload_file(path_or_fileobj=b,path_in_repo=p,repo_id=REPO,repo_type="dataset"); print("ok",p,flush=True)
try: font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",22)
except Exception: font=ImageFont.load_default()
names=[]
for r in R:
    for sd in (1,2):
        p=f"g95/{r['key']}_s{sd}.jpg"
        if p in files: names.append(p)
idx={}
# Mosaike in voller Auflösung
for m in range(0,len(names),15):
    grp=names[m:m+15]; M=Image.new("RGB",(5*1024,3*1280),"white")
    for i,p in enumerate(grp):
        M.paste(get(p).resize((1024,1280)),((i%5)*1024,(i//5)*1280)); idx[p]=dict(mosaik=m//15,pos=i)
    up(M,f"g95sheets/mosaik_{m//15}.jpg",93)
# Kacheln
tl=["aubergine","erdbeeren","zuckerstreusel"]
K=Image.new("RGB",(3*1024,1024),"white")
for i,t in enumerate(tl):
    if f"tiles/{t}.jpg" in files: K.paste(get(f"tiles/{t}.jpg"),((i%3)*1024,(i//3)*1024))
up(K,"g95sheets/kacheln.jpg",93)
b=io.BytesIO(json.dumps(dict(idx=idx,kacheln=tl)).encode()); api.upload_file(path_or_fileobj=b,path_in_repo="g95sheets/_index.json",repo_id=REPO,repo_type="dataset")
print("done",len(names))
