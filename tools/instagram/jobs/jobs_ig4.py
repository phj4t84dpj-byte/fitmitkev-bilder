# /// script
# dependencies = ["gradio_client>=1.5", "huggingface_hub>=0.30", "pillow"]
# ///
# Instagram-Karussells 19.11. (Top 3 vom Mi 18.11.): Milchschnitte-Bowl (ms), Gewuerzkuchen (gk), Zimtsterne (zs). Aufruf: python jobs_ig4.py <praefix>
import os, sys, time
from huggingface_hub import HfApi, hf_hub_download
from gradio_client import Client, handle_file
from PIL import Image
TOK=os.environ["HF_TOKEN"]; api=HfApi(token=TOK)
SRC="kevrsztorm/fitmitkev-karussells"; OUT="ig-2026-11-19/roh/"
A=hf_hub_download(SRC,"cheeseburger-taschen/roh/v2/base_A.jpg",repo_type="dataset",token=TOK)
KEEP=" Keep the hand, the kitchen background, the lighting and the camera angle exactly the same. Photorealistic smartphone photo, natural colors, not oversaturated, homemade and slightly imperfect."
NOC=" No spoon, no cutlery."
TRAY="Replace the ceramic bowl: the hand now holds a dark metal baking tray lined with white baking paper"
GLAS="Replace the ceramic bowl: the hand now holds a small rectangular clear glass baking dish (15 x 10 cm)"
PLAN=[
("ms0_hook",A,GLAS+" with a two-layer dessert: at the bottom a dark brown chocolate sponge cake layer, on top a thick smooth white milk cream layer lightly dusted with cocoa powder, both layers clearly visible from the side through the glass, one corner already eaten, one plain straight metal teaspoon in it."+KEEP,111),
("ms1_teig",A,"Fill the ceramic bowl with a smooth, glossy dark brown chocolate cake batter, a metal whisk resting in the bowl."+KEEP,112),
("ms2_form",A,GLAS+" filled about one third with smooth unbaked dark brown chocolate batter, visible from the side through the glass, not baked yet."+NOC+KEEP,113),
("ms3_creme",A,"Fill the ceramic bowl with a smooth, thick, creamy white yogurt cream with a thin golden drizzle of honey on top, a metal whisk resting in the bowl."+KEEP,114),
("ms4_fertig",A,GLAS+" with a baked dark brown chocolate sponge cake layer at the bottom and a thick smooth white cream layer spread on top, a light dusting of dark cocoa powder over the white cream, both layers visible from the side through the glass, untouched."+NOC+KEEP,115),
("gk0_hook",A,"Replace the ceramic bowl: the hand now holds a small white plate with two square pieces of moist dark brown German spice sheet cake, each covered with a thin glossy dark chocolate glaze, the soft dark crumb visible at the cut sides."+NOC+KEEP,121),
("gk1_eier",A,"Fill the ceramic bowl with pale yellow foamy beaten eggs, on top a large spoonful of thick white skyr yogurt and a spoonful of golden applesauce, not yet mixed, a metal whisk resting in the bowl."+KEEP,122),
("gk2_teig",A,"Fill the ceramic bowl with a thick, smooth dark brown cocoa cake batter, a metal whisk resting in the bowl."+KEEP,123),
("gk3_blech",A,TRAY+", evenly spread with a layer of smooth unbaked dark brown cake batter covering the whole tray, not baked yet."+KEEP,124),
("gk4_glasur",A,TRAY+", on it a baked dark brown sheet cake, its top covered with glossy melted dark chocolate glaze, cut into square pieces."+KEEP,125),
("zs0_hook",A,"Replace the ceramic bowl: the hand now holds a white plate piled with about ten German cinnamon star cookies: six-pointed star-shaped light brown cookies, each topped with a smooth white meringue glaze."+NOC+KEEP,131),
("zs1_zutaten",A,"Fill the ceramic bowl with a heap of finely ground beige oat flour, a small heap of white granulated sweetener, a small heap of brown ground cinnamon, a spoonful of thick white skyr yogurt and one clear raw egg white, not yet mixed."+NOC+KEEP,132),
("zs2_teig",A,"Fill the ceramic bowl with one firm, smooth, light brown cinnamon cookie dough ball."+NOC+KEEP,133),
("zs3_sterne",A,TRAY+", on it about fifteen raw six-pointed star-shaped light brown cinnamon cookie dough pieces in neat rows, without glaze, not baked yet."+KEEP,134),
("zs4_guss",A,TRAY+", on it about fifteen six-pointed star-shaped light brown cinnamon cookies in neat rows, each star topped with a smooth white meringue glaze."+KEEP,135),
]
pre=sys.argv[1] if len(sys.argv)>1 else ""
cl=Client("Qwen/Qwen-Image-Edit-2511",token=TOK)
def getpath(o):
    if isinstance(o,str): return o
    if isinstance(o,dict):
        for k in ("image","path","url"):
            if k in o and o[k]: return getpath(o[k])
        for v in o.values():
            r=getpath(v)
            if r: return r
    if isinstance(o,(list,tuple)):
        for v in o:
            r=getpath(v)
            if isinstance(r,str) and "/" in r: return r
    return None
for name,src,prompt,seed in PLAN:
    if not name.startswith(pre): continue
    for a in range(4):
        try:
            res=cl.predict(images=[{"image":handle_file(src)}],prompt=prompt,seed=seed+a*100,randomize_seed=False,true_guidance_scale=4.0,num_inference_steps=32,height=1472,width=1104,rewrite_prompt=False,api_name="/infer")
            local=f"/tmp/{name}.jpg"; Image.open(getpath(res)).convert("RGB").save(local,quality=94)
            api.upload_file(path_or_fileobj=local,path_in_repo=OUT+name+".jpg",repo_id=SRC,repo_type="dataset")
            print("ok",name,flush=True); break
        except Exception as e:
            print("retry",name,repr(e)[:300],flush=True); time.sleep(30)
    else:
        print("FAIL",name,flush=True)
# Kontaktbogen fuer die schnelle Sichtung (5 Bilder nebeneinander)
try:
    names=[n for n,_,_,_ in PLAN if n.startswith(pre) and os.path.exists(f"/tmp/{n}.jpg")]
    if names:
        W,H=552,736; sh=Image.new("RGB",(W*len(names),H),"white")
        for i,n in enumerate(names): sh.paste(Image.open(f"/tmp/{n}.jpg").resize((W,H)),(i*W,0))
        sh.save("/tmp/_sheet.jpg",quality=88)
        api.upload_file(path_or_fileobj="/tmp/_sheet.jpg",path_in_repo=OUT+f"_sheet_{pre or 'all'}.jpg",repo_id=SRC,repo_type="dataset")
        print("ok sheet",flush=True)
except Exception as e:
    print("sheet-fail",repr(e)[:200],flush=True)
print("done")
