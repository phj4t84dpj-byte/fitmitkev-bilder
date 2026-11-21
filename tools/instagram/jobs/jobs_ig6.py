# /// script
# dependencies = ["gradio_client>=1.5", "huggingface_hub>=0.30", "pillow"]
# ///
# Instagram-Karussells 21.11. (Top 3 vom Fr 20.11.): Gebratene Nudeln (cm), Wrap aus körnigem Frischkäse (kw), Kokosmakronen (km). Aufruf: python jobs_ig6.py <praefix>
# Statt des kleinen Kontaktbogens lädt der Job je Rezept ein Mosaik in voller Größe hoch (_mosaik_<praefix>.jpg, 5520 x 1472) – 3 Anhänge statt 15.
import os, sys, time, urllib.request
from huggingface_hub import HfApi, hf_hub_download
from gradio_client import Client, handle_file
from PIL import Image
TOK=os.environ["HF_TOKEN"]; api=HfApi(token=TOK)
SRC="kevrsztorm/fitmitkev-karussells"; OUT="ig-2026-11-21/roh/"
A=hf_hub_download(SRC,"cheeseburger-taschen/roh/v2/base_A.jpg",repo_type="dataset",token=TOK)
KEEP=" Keep the hand, the kitchen background, the lighting and the camera angle exactly the same. Photorealistic smartphone photo, natural colors, not oversaturated, homemade and slightly imperfect."
NOC=" No spoon, no cutlery."
urllib.request.urlretrieve("https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/misc/karussell_pfanne_kev.jpg","/tmp/pan.jpg"); P="/tmp/pan.jpg"
KEEPP=" Keep the grey speckled pan, the black hob, the grey worktop, the lighting and the camera angle exactly the same. No hands. Photorealistic smartphone photo, natural colors, not oversaturated."
TRAY="Replace the ceramic bowl: the hand now holds a dark metal baking tray lined with white baking paper"
GLAS="Replace the ceramic bowl: the hand now holds a small rectangular clear glass baking dish (15 x 10 cm)"
PLAN=[
("cm0_hook",A,"Replace the ceramic bowl: the hand now holds a deep white bowl filled with fried thin wavy egg noodles glistening with soy sauce, mixed with golden-brown chicken breast strips, thin orange carrot strips, red bell pepper strips and shredded white cabbage, sprinkled with sliced green spring onions."+NOC+KEEP,311),
("cm1_nudeln",A,"Fill the ceramic bowl with cooked, drained thin wavy pale yellow egg noodles, plain without any sauce."+NOC+KEEP,312),
("cm2_haehnchen",P,"Fill the pan with many golden-brown seared chicken breast strips, evenly spread over the pan."+KEEPP,313),
("cm3_gemuese",P,"Fill the pan with golden-brown seared chicken breast strips mixed with thin orange carrot strips, red bell pepper strips and finely shredded white cabbage, lightly stir-fried."+KEEPP,314),
("cm4_fertig",P,"Fill the pan with fried thin wavy egg noodles glistening with dark soy sauce, mixed with golden-brown chicken breast strips, orange carrot strips, red bell pepper strips and shredded white cabbage, sprinkled with sliced green spring onions."+KEEPP,315),
("kw0_hook",A,"Replace the ceramic bowl: the hand now holds a white plate with two rolled wraps cut in half, the cut sides facing the camera. The wrap bread is a thin, soft, golden-brown baked egg flatbread speckled with dried herbs, rolled around pink turkey ham slices, green lettuce, cucumber slices and a little white cream cheese."+NOC+KEEP,321),
("kw1_mixer",A,"Replace the ceramic bowl: the hand now holds a clear blender jug filled with white grainy cottage cheese and two raw eggs with intact yellow yolks on top, not blended yet."+NOC+KEEP,322),
("kw2_blech",A,TRAY+", on it a thin, smooth, pale cream-yellow batter spread out into a thin even rectangle, sprinkled with dried green herbs, not baked yet."+NOC+KEEP,323),
("kw3_gebacken",A,TRAY+", on it one thin rectangular baked flatbread, golden brown and firm with slightly darker edges, speckled with dried green herbs."+NOC+KEEP,324),
("kw4_belegt",A,"Replace the ceramic bowl: the hand now holds a wooden cutting board with one thin golden-brown rectangular flatbread lying flat, spread with white cream cheese and topped with pink turkey ham slices, green lettuce leaves and cucumber slices, not rolled up yet."+NOC+KEEP,325),
("km0_hook",A,"Replace the ceramic bowl: the hand now holds a small white plate piled with many small coconut macaroons, rough white mounds of shredded coconut with golden-brown toasted tips."+NOC+KEEP,331),
("km1_eischnee",A,"Fill the ceramic bowl with stiff, glossy, pure white beaten egg whites with firm peaks, a metal whisk resting in the bowl. Only white foam, no yellow."+KEEP,332),
("km2_kokos",A,"Fill the ceramic bowl with a thick, rough, fluffy white mixture of beaten egg whites and lots of white shredded coconut, one plain metal tablespoon resting in the bowl."+KEEP,333),
("km3_blech",A,TRAY+", on it many small rough white mounds of raw shredded coconut mixture set in neat rows, pure white, not baked yet."+NOC+KEEP,334),
("km4_gebacken",A,TRAY+", on it many small baked coconut macaroons in neat rows, white with golden-brown toasted tips."+NOC+KEEP,335),
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
