# /// script
# dependencies = ["gradio_client>=1.5", "huggingface_hub>=0.30", "pillow"]
# ///
# Instagram-Karussells 20.11. (Top 3 vom Do 19.11., GTA-VI-Tag): Donuts (dn), Erdbeer-Milchshake (sh), Smash-Burger-Wrap (sw). Aufruf: python jobs_ig5.py <praefix>
import os, sys, time, urllib.request
from huggingface_hub import HfApi, hf_hub_download
from gradio_client import Client, handle_file
from PIL import Image
TOK=os.environ["HF_TOKEN"]; api=HfApi(token=TOK)
SRC="kevrsztorm/fitmitkev-karussells"; OUT="ig-2026-11-20/roh/"
A=hf_hub_download(SRC,"cheeseburger-taschen/roh/v2/base_A.jpg",repo_type="dataset",token=TOK)
KEEP=" Keep the hand, the kitchen background, the lighting and the camera angle exactly the same. Photorealistic smartphone photo, natural colors, not oversaturated, homemade and slightly imperfect."
NOC=" No spoon, no cutlery."
urllib.request.urlretrieve("https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/misc/karussell_pfanne_kev.jpg","/tmp/pan.jpg"); P="/tmp/pan.jpg"
KEEPP=" Keep the grey speckled pan, the black hob, the grey worktop, the lighting and the camera angle exactly the same. No hands. Photorealistic smartphone photo, natural colors, not oversaturated."
TRAY="Replace the ceramic bowl: the hand now holds a dark metal baking tray lined with white baking paper"
GLAS="Replace the ceramic bowl: the hand now holds a small rectangular clear glass baking dish (15 x 10 cm)"
PLAN=[
("dn0_hook",A,"Replace the ceramic bowl: the hand now holds a small white plate with three baked ring donuts stacked on it, each with a hole in the middle, the top of each donut dipped in glossy dark chocolate glaze and decorated with a few colorful sugar sprinkles, golden baked sides visible."+NOC+KEEP,211),
("dn1_teig",A,"Fill the ceramic bowl with a thick, smooth, pale cream-colored cake batter, a metal whisk resting in the bowl."+KEEP,212),
("dn2_form",A,"Replace the ceramic bowl: the hand now holds a dark metal donut baking pan with six ring-shaped molds, each mold filled with pale unbaked batter around the raised center, not baked yet."+NOC+KEEP,213),
("dn3_gebacken",A,"Replace the ceramic bowl: the hand now holds a dark metal donut baking pan with six ring-shaped molds, in each mold a plain golden-brown baked ring donut, without glaze."+NOC+KEEP,214),
("dn4_glasur",A,"Replace the ceramic bowl: the hand now holds a metal wire cooling rack with six baked ring donuts in two rows, the top of each donut dipped in glossy dark chocolate glaze with a few colorful sugar sprinkles."+NOC+KEEP,215),
("sh0_hook",A,"Replace the ceramic bowl: the hand now holds one tall clear glass filled to the top with a thick, creamy pink strawberry milkshake, a striped paper straw in it and one fresh red strawberry on the rim of the glass."+NOC+KEEP,221),
("sh1_erdbeeren",A,"Fill the ceramic bowl with whole frozen red strawberries covered in light white frost."+NOC+KEEP,222),
("sh2_mixer",A,"Replace the ceramic bowl: the hand now holds a clear blender jug filled with frozen red strawberries at the bottom, thick white skyr yogurt and white milk on top, not blended yet, the layers clearly visible through the jug."+NOC+KEEP,223),
("sh3_puriert",A,"Replace the ceramic bowl: the hand now holds a clear blender jug filled with a thick, smooth, creamy pink strawberry milkshake, freshly blended, evenly pink."+NOC+KEEP,224),
("sh4_glaeser",A,"Replace the ceramic bowl: the hand now holds a small wooden tray with two tall clear glasses filled with thick, creamy pink strawberry milkshake, each glass with a striped paper straw."+NOC+KEEP,225),
("sw0_hook",A,"Replace the ceramic bowl: the hand now holds a white plate with a folded smash burger tortilla wrap cut in half, the cut sides facing the camera, showing a thin crispy browned ground beef layer, melted orange cheddar cheese, green pickle slices, onion rings, green lettuce and a light orange burger sauce inside the golden toasted wheat tortilla."+NOC+KEEP,231),
("sw1_hack",A,"Replace the ceramic bowl: the hand now holds a white plate with one round flat wheat tortilla, its whole surface evenly spread with a thin layer of raw red seasoned ground beef, a little black pepper on top."+NOC+KEEP,232),
("sw2_pfanne",P,"Put one round wheat tortilla flat into the pan, the pale tortilla side facing up with a few light brown toasted spots, at the edge a thin rim of sizzling browned ground beef visible underneath the tortilla."+KEEPP,233),
("sw3_belag",P,"Put one round wheat tortilla flat into the pan, its top side covered with a thin crispy dark browned ground beef layer, on the beef two slices of melting orange cheddar cheese, a few raw onion rings and green pickle slices."+KEEPP,234),
("sw4_sosse",A,"Fill the ceramic bowl with a smooth, creamy light orange burger sauce made from yogurt, ketchup and mustard, one plain straight metal teaspoon resting in the bowl."+KEEP,235),
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
