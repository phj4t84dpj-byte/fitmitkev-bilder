# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow", "requests"]
# ///
# ESN: Mosaike in voller Auflösung (3 Seeds nebeneinander, 5 Rezepte untereinander) -> gesnsheets/mosaik_N.jpg + Kacheln
import os, io, json, time, requests
from huggingface_hub import HfApi
from PIL import Image
TOK=os.environ["HF_TOKEN"]; api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
K=["SchokoMousseESN","TiramisuBowlESN","BratapfelQuarkESN","SchwarzwaelderGlasESN","VanillepuddingPflaumenESN","SchokoKugelnESN","SpekulatiusMousseESN",
   "ErdbeerBowlESN","DarkSchokoPuddingESN","SpekulatiusTiramisuESN","ErdbeerCheesecakeGlasESN","ZimtGriessbreiESN","SchokoEisESN"]
S=[71,72,73]
def get(p):
    for a in range(4):
        try:
            r=requests.get(f"https://huggingface.co/datasets/{REPO}/resolve/main/{p}",headers={"Authorization":f"Bearer {TOK}"},timeout=60); r.raise_for_status()
            return Image.open(io.BytesIO(r.content)).convert("RGB")
        except Exception as e: print("retry",p,repr(e)[:150],flush=True); time.sleep(5)
    return Image.new("RGB",(1024,1280),"grey")
def up(im,p,q=90):
    b=io.BytesIO(); im.save(b,"JPEG",quality=q); b.seek(0); api.upload_file(path_or_fileobj=b,path_in_repo=p,repo_id=REPO,repo_type="dataset"); print("ok",p,flush=True)
for m in range(0,len(K),5):
    grp=K[m:m+5]; M=Image.new("RGB",(3*1024,len(grp)*1280),"white")
    for i,k in enumerate(grp):
        for j,s in enumerate(S): M.paste(get(f"gesn/{k}_s{s}.jpg"),(j*1024,i*1280))
    up(M,f"gesnsheets/mosaik_{m//5}.jpg",92)
T=Image.new("RGB",(2048,1024),"white")
for i,t in enumerate(["pflaumen","griess"]): T.paste(get(f"tiles/{t}.jpg"),(i*1024,0))
up(T,"gesnsheets/kacheln.jpg",92)
print("done")
