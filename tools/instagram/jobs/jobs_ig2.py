# /// script
# dependencies = ["gradio_client>=1.5", "huggingface_hub>=0.30", "pillow"]
# ///
# Instagram-Karussells 17.11. (Ersatz, da Montagszahlen fehlen): Hefezopf (hz), Eiersalat (es), Lahmacun (lc). Aufruf: python jobs_ig2.py <praefix>
import os, sys, time, urllib.request
from huggingface_hub import HfApi, hf_hub_download
from gradio_client import Client, handle_file
from PIL import Image
TOK=os.environ["HF_TOKEN"]; api=HfApi(token=TOK)
SRC="kevrsztorm/fitmitkev-karussells"; OUT="ig-2026-11-17/roh/"
A=hf_hub_download(SRC,"cheeseburger-taschen/roh/v2/base_A.jpg",repo_type="dataset",token=TOK)
urllib.request.urlretrieve("https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/misc/karussell_pfanne_kev.jpg","/tmp/pan.jpg")
KEEP=" Keep the hand, the kitchen background, the lighting and the camera angle exactly the same. Photorealistic smartphone photo, natural colors, not oversaturated, homemade and slightly imperfect."
KEEPP=" Keep the grey speckled pan, the black hob, the grey worktop, the lighting and the camera angle exactly the same. No hands. Photorealistic smartphone photo, natural colors, not oversaturated."
TRAY="Replace the ceramic bowl: the hand now holds a dark metal baking tray lined with white baking paper"
PLAN=[
("hz0_hook",A,"Replace the ceramic bowl: the hand now holds a wooden cutting board with a golden brown braided German yeast bread loaf (Hefezopf, classic three-strand braid), glossy egg-washed crust sprinkled with toasted flaked almonds, two thick slices cut off in front showing the soft fluffy pale yellow crumb."+KEEP,51),
("hz1_zutaten",A,"Fill the ceramic bowl with a heap of light spelt flour, a large spoonful of thick white skyr yogurt, a few small cubes of soft butter and a little milk, not yet mixed."+KEEP,52),
("hz2_teig",A,"Fill the ceramic bowl with one large smooth, soft, risen pale yeast dough ball, slightly domed and airy, lightly floured surface."+KEEP,53),
("hz3_zopf",A,TRAY+", on it one unbaked pale raw yeast dough loaf neatly braided from three thick round strands, about 40 cm long."+KEEP,54),
("hz4_mandeln",A,TRAY+", on it one unbaked raw braided yeast dough loaf from three strands, brushed shiny yellow with egg yolk and generously sprinkled with raw white flaked almonds, not baked yet."+KEEP,55),
("es0_hook",A,"Fill the ceramic bowl with creamy German egg salad: chopped hard-boiled eggs with visible yellow yolks in a light creamy white dressing with small diced green pickles, generously sprinkled with fresh chopped green chives and a pinch of red paprika powder, one plain straight metal spoon in the bowl."+KEEP,61),
("es1_eier","/tmp/pan.jpg","Fill the pan with simmering water with small bubbles and eight whole white eggs in their shells lying in the water."+KEEPP,62),
("es2_gewuerfelt",A,"Fill the ceramic bowl with peeled hard-boiled eggs roughly chopped into chunks, white egg white pieces and bright yellow yolk pieces clearly visible."+KEEP,63),
("es3_creme",A,"Fill the ceramic bowl halfway with a smooth thick creamy white dressing made of skyr yogurt and cream cheese with a swirl of yellow mustard, a light dusting of red paprika powder and black pepper on top, a metal whisk resting in the bowl."+KEEP,64),
("es4_mix",A,"Fill the ceramic bowl with a smooth creamy white dressing, on top lie roughly chopped hard-boiled eggs, small diced green pickles and finely chopped fresh green chives, not yet mixed."+KEEP,65),
("lc0_hook",A,"Replace the ceramic bowl: the hand now holds a white plate with a thin round Turkish flatbread (Lahmacun) with a thin layer of spiced minced meat and tomato baked on, crispy browned edges, topped with fresh green lettuce, tomato slices, red onion rings and parsley, half rolled up, a lemon wedge beside."+KEEP,71),
("lc1_teig",A,"Fill the ceramic bowl with a heap of light spelt flour and a large spoonful of thick white skyr yogurt, a little white baking powder on top, not yet mixed."+KEEP,72),
("lc2_hack",A,"Fill the ceramic bowl with raw red minced beef mixed with finely chopped onion, finely diced red bell pepper, chopped green parsley and red tomato passata, a reddish moist meat mixture."+KEEP,73),
("lc3_fladen",A,TRAY+", on it two very thin oval raw pale dough flatbreads, each thinly and evenly spread with raw red minced meat and tomato topping almost to the edges, not baked yet."+KEEP,74),
("lc4_gebacken",A,TRAY+", on it two thin oval baked Turkish flatbreads (Lahmacun) with crispy golden browned edges and a thin baked layer of spiced minced meat and tomato, a few lemon wedges and parsley beside."+KEEP,75),
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
            p=getpath(res); local=f"/tmp/{name}.jpg"
            Image.open(p).convert("RGB").save(local,quality=94)
            api.upload_file(path_or_fileobj=local,path_in_repo=OUT+name+".jpg",repo_id=SRC,repo_type="dataset")
            print("ok",name,flush=True); break
        except Exception as e:
            print("retry",name,repr(e)[:300],flush=True); time.sleep(30)
    else:
        print("FAIL",name,flush=True)
print("done")
