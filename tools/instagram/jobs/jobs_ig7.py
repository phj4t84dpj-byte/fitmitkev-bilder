# /// script
# dependencies = ["gradio_client>=1.5", "huggingface_hub>=0.30", "pillow"]
# ///
# Instagram-Karussells 22.11. (Top 3 vom Sa 21.11.): Rotweinkuchen (rw), Marmorkuchen-Bowl (mk), Churros aus dem Ofen (ch). Aufruf: python jobs_ig7.py <praefix>
# Statt des kleinen Kontaktbogens lädt der Job je Rezept ein Mosaik in voller Größe hoch (_mosaik_<praefix>.jpg, 5520 x 1472) – 3 Anhänge statt 15.
import os, sys, time, urllib.request
from huggingface_hub import HfApi, hf_hub_download
from gradio_client import Client, handle_file
from PIL import Image
TOK=os.environ["HF_TOKEN"]; api=HfApi(token=TOK)
SRC="kevrsztorm/fitmitkev-karussells"; OUT="ig-2026-11-22/roh/"
A=hf_hub_download(SRC,"cheeseburger-taschen/roh/v2/base_A.jpg",repo_type="dataset",token=TOK)
KEEP=" Keep the hand, the kitchen background, the lighting and the camera angle exactly the same. Photorealistic smartphone photo, natural colors, not oversaturated, homemade and slightly imperfect."
NOC=" No spoon, no cutlery."
KEEPP=" Keep the grey speckled pan, the black hob, the grey worktop, the lighting and the camera angle exactly the same. No hands. Photorealistic smartphone photo, natural colors, not oversaturated."
TRAY="Replace the ceramic bowl: the hand now holds a dark metal baking tray lined with white baking paper"
LOAF="Replace the ceramic bowl: the hand now holds a rectangular metal loaf tin (25 cm long) lined with white baking paper"
GLAS="Replace the ceramic bowl: the hand now holds a small rectangular clear glass baking dish (15 x 10 cm)"
PLAN=[
("rw0_hook",A,"Replace the ceramic bowl: the hand now holds a small white plate with two thick slices of a moist dark brown chocolate loaf cake, lightly dusted with white powdered sugar on the top crust, small pieces of dark chocolate visible in the soft dark crumb at the cut sides."+NOC+KEEP,411),
("rw1_eier",A,"Fill the ceramic bowl with pale yellow foamy beaten eggs, on top a large spoonful of thick white skyr yogurt, not yet mixed, a metal whisk resting in the bowl."+KEEP,412),
("rw2_teig",A,"Fill the ceramic bowl with a thick, smooth dark brown cocoa cake batter with coarsely chopped dark chocolate pieces scattered on top, a metal whisk resting in the bowl."+KEEP,413),
("rw3_form",A,LOAF+", filled about two thirds with smooth unbaked dark brown chocolate cake batter, not baked yet."+NOC+KEEP,414),
("rw4_gebacken",A,LOAF+", in it a baked dark brown chocolate loaf cake, risen with a domed top and a crack along the middle, lightly dusted with white powdered sugar."+NOC+KEEP,415),
("mk0_hook",A,GLAS+" with a baked marble cake filling the dish: light golden cake with dark brown cocoa swirls on the surface, slightly risen, one corner already eaten showing the soft marbled crumb, one plain straight metal teaspoon in it."+KEEP,421),
("mk1_teig",A,"Fill the ceramic bowl with a thick, pale cream-coloured batter with visible small oat flakes, a metal whisk resting in the bowl."+KEEP,422),
("mk2_form",A,GLAS+" filled about one third with a thick pale cream-coloured unbaked batter with small oat flakes, visible from the side through the glass, not baked yet."+NOC+KEEP,423),
("mk3_marmor",A,GLAS+" filled with unbaked batter: pale cream-coloured batter and dark brown cocoa batter swirled together in a clear spiral marble pattern on the surface, a plain metal fork resting on the rim, not baked yet."+KEEP,424),
("mk4_gebacken",A,GLAS+" with a freshly baked marble cake filling the dish, light golden with dark brown cocoa swirls on the surface, slightly risen, untouched."+NOC+KEEP,425),
("ch0_hook",A,"Replace the ceramic bowl: the hand now holds a white plate piled with golden-brown baked churros, short straight ridged pastry sticks about 10 cm long, coated with fine brown cinnamon, next to them on the plate a small white dip bowl with glossy dark chocolate sauce."+NOC+KEEP,431),
("ch1_kloss",A,"Fill the ceramic bowl with one smooth, firm, pale yellow ball of cooked choux pastry dough, a wooden spoon resting in the bowl."+KEEP,432),
("ch2_teig",A,"Fill the ceramic bowl with a thick, smooth, glossy pale yellow choux pastry batter, a wooden spoon resting in the bowl."+KEEP,433),
("ch3_blech",A,TRAY+", on it many short straight sticks of raw pale yellow dough piped with a star nozzle, each about 10 cm long with clear ridges, set in neat parallel rows, not baked yet."+NOC+KEEP,434),
("ch4_gebacken",A,TRAY+", on it many short straight baked churros sticks with clear ridges, golden brown and crisp, set in neat parallel rows."+NOC+KEEP,435),
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
# Mosaik in voller Groesse (5 Bilder nebeneinander)
try:
    names=[n for n,_,_,_ in PLAN if n.startswith(pre) and os.path.exists(f"/tmp/{n}.jpg")]
    if names:
        W,H=1104,1472; sh=Image.new("RGB",(W*len(names),H),"white")
        for i,n in enumerate(names): sh.paste(Image.open(f"/tmp/{n}.jpg").resize((W,H)),(i*W,0))
        sh.save("/tmp/_mosaik.jpg",quality=93)
        api.upload_file(path_or_fileobj="/tmp/_mosaik.jpg",path_in_repo=OUT+f"_mosaik_{pre or 'all'}.jpg",repo_id=SRC,repo_type="dataset")
        print("ok mosaik",names,flush=True)
except Exception as e:
    print("mosaik-fail",repr(e)[:200],flush=True)
print("done")
