# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow"]
# ///
# Baut aus n2/*_s1/_s2.jpg Prüfbögen (klein, beschriftet) und Mosaike in voller Auflösung (zum verlustfreien Zerlegen),
# lädt sie nach n2sheets/ hoch. Mosaik: 5 × 3 Bilder à 1024 × 1280, Reihenfolge siehe n2sheets/_index.json.
import os, io, json, urllib.request
from huggingface_hub import HfApi, hf_hub_download
from PIL import Image, ImageDraw, ImageFont
TOK=os.environ["HF_TOKEN"]; api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
src=urllib.request.urlopen("https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/tools/n2/n2_data.py").read()
ns={}; exec(src.decode(),ns); R=ns['R']
files=set(api.list_repo_files(REPO,repo_type="dataset"))
def get(p): return Image.open(hf_hub_download(REPO,p,repo_type="dataset",token=TOK)).convert("RGB")
def up(im,p,q=90):
    b=io.BytesIO(); im.save(b,"JPEG",quality=q); b.seek(0); api.upload_file(path_or_fileobj=b,path_in_repo=p,repo_id=REPO,repo_type="dataset"); print("ok",p,flush=True)
try: font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",22)
except Exception: font=ImageFont.load_default()
names=[]
for r in R:
    for sd in (1,2):
        p=f"n2/{r['key']}_s{sd}.jpg"
        if p in files: names.append(p)
idx={}
# Mosaike in voller Auflösung
for m in range(0,len(names),15):
    grp=names[m:m+15]; M=Image.new("RGB",(5*1024,3*1280),"white")
    for i,p in enumerate(grp):
        M.paste(get(p).resize((1024,1280)),((i%5)*1024,(i//5)*1280)); idx[p]=dict(mosaik=m//15,pos=i)
    up(M,f"n2sheets/mosaik_{m//15}.jpg",93)
# Prüfbögen: je Rezept s1|s2 nebeneinander (je 300 × 375), 6 Rezepte pro Bogen (3 Spalten × 2 Reihen)
keys=[r['key'] for r in R]
for b in range(0,len(keys),6):
    S=Image.new("RGB",(3*620,2*415),"white"); d=ImageDraw.Draw(S)
    for i,k in enumerate(keys[b:b+6]):
        x=(i%3)*620; y=(i//3)*415
        for j,sd in enumerate((1,2)):
            p=f"n2/{k}_s{sd}.jpg"
            if p in files: S.paste(get(p).resize((300,375)),(x+j*305,y+35))
        d.text((x+4,y+6),f"{k}  (s1 | s2)",fill="black",font=font)
    up(S,f"n2sheets/bogen_{b//6}.jpg",88)
# Kacheln
tl=["toastbrot","haehnchenfluegel","sojasauce","blaetterteig","puderzucker","schweineschnitzel","kaesescheiben","nuss_nougat_creme","schweinebauch"]
K=Image.new("RGB",(3*1024,3*1024),"white")
for i,t in enumerate(tl):
    if f"tiles/{t}.jpg" in files: K.paste(get(f"tiles/{t}.jpg"),((i%3)*1024,(i//3)*1024))
up(K,"n2sheets/kacheln.jpg",93)
b=io.BytesIO(json.dumps(dict(idx=idx,kacheln=tl)).encode()); api.upload_file(path_or_fileobj=b,path_in_repo="n2sheets/_index.json",repo_id=REPO,repo_type="dataset")
print("done",len(names))
