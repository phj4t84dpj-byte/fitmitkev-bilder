# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow>=10.1"]
# ///
# G102: Auswahlbögen – je Rezept 6 Rohbilder (512x640) auf einem Bogen 3x2 mit Seed-Nummer -> g102/_m_<Key>_<n>.jpg (spart das Einzel-Ansehen von 84 Bildern)
import io, os
from huggingface_hub import HfApi, hf_hub_download
from PIL import Image, ImageDraw
TOK=os.environ["HF_TOKEN"]; api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"; PRE=os.environ.get("PRE","g102")
keys=[k for k in os.environ.get("KEYS","").split(",") if k]
by={}
for f in api.list_repo_files(REPO,repo_type="dataset"):
    if f.startswith(PRE+"/") and "_s" in f and "/_m_" not in f:
        k,s=f[len(PRE)+1:-4].rsplit("_s",1)
        if not keys or k in keys: by.setdefault(k,[]).append(int(s))
for k,seeds in sorted(by.items()):
    seeds=sorted(seeds)
    for i in range(0,len(seeds),6):
        ch=seeds[i:i+6]; sh=Image.new("RGB",(3*512,2*640),"white"); d=ImageDraw.Draw(sh)
        for j,s in enumerate(ch):
            p=hf_hub_download(REPO,f"{PRE}/{k}_s{s}.jpg",repo_type="dataset",token=TOK)
            im=Image.open(p).convert("RGB").resize((512,640),Image.LANCZOS); x,y=(j%3)*512,(j//3)*640; sh.paste(im,(x,y))
            d.rectangle((x,y,x+120,y+46),fill=(0,0,0)); d.text((x+8,y+4),f"s{s}",fill=(255,255,0),font_size=32)
        b=io.BytesIO(); sh.save(b,"JPEG",quality=88); b.seek(0)
        api.upload_file(path_or_fileobj=b,path_in_repo=f"{PRE}/_m_{k}_{i//6+1}.jpg",repo_id=REPO,repo_type="dataset"); print("ok",k,i//6+1,ch,flush=True)
print("done")
