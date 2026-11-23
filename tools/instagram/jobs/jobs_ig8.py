# /// script
# dependencies = ["gradio_client>=1.5", "huggingface_hub>=0.30", "pillow"]
# ///
# Instagram-Karussells 23.11. (Top 3 vom So 22.11., ohne den Kalten Hund, der am 16.11. schon als Karussell lief): Pizza-Kartoffeln (pk), 1 Teig – 5 Sorten Plaetzchen (tp), Doener-Kuchen (dk). Aufruf: python jobs_ig8.py <praefix>
# Statt des kleinen Kontaktbogens lädt der Job je Rezept ein Mosaik in voller Größe hoch (_mosaik_<praefix>.jpg, 5520 x 1472) – 3 Anhänge statt 15.
import os, sys, time, urllib.request
from huggingface_hub import HfApi, hf_hub_download
from gradio_client import Client, handle_file
from PIL import Image
TOK=os.environ["HF_TOKEN"]; api=HfApi(token=TOK)
SRC="kevrsztorm/fitmitkev-karussells"; OUT="ig-2026-11-23/roh/"
A=hf_hub_download(SRC,"cheeseburger-taschen/roh/v2/base_A.jpg",repo_type="dataset",token=TOK)
urllib.request.urlretrieve("https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/misc/karussell_pfanne_kev.jpg","/tmp/pan.jpg"); P="/tmp/pan.jpg"
KEEP=" Keep the hand, the kitchen background, the lighting and the camera angle exactly the same. Photorealistic smartphone photo, natural colors, not oversaturated, homemade and slightly imperfect."
NOC=" No spoon, no cutlery."
KEEPP=" Keep the grey speckled pan, the black hob, the grey worktop, the lighting and the camera angle exactly the same. No hands. Photorealistic smartphone photo, natural colors, not oversaturated."
TRAY="Replace the ceramic bowl: the hand now holds a dark metal baking tray lined with white baking paper"
LOAF="Replace the ceramic bowl: the hand now holds a rectangular metal loaf tin (25 cm long) lined with white baking paper"
GLAS="Replace the ceramic bowl: the hand now holds a small rectangular clear glass baking dish (15 x 10 cm)"
AUFL="Replace the ceramic bowl: the hand now holds a white rectangular ceramic baking dish (20 x 30 cm)"
SPRING="Replace the ceramic bowl: the hand now holds a round metal springform cake tin (24 cm) lined with white baking paper"
BOARD="Replace the ceramic bowl: the hand now holds a small light wooden board"
PLAN=[
("pk0_hook",A,AUFL+" filled with golden-brown roasted potato cubes, the middle topped like a pizza with red tomato sauce, melted golden-brown cheese, round salami slices and small red bell pepper cubes, at the edge plain crispy potato cubes without sauce."+NOC+KEEP,511),
("pk1_blech",A,TRAY+", on it many 2 cm potato cubes roasted golden brown and crisp, lightly dusted with red paprika powder, spread in one layer."+NOC+KEEP,512),
("pk2_sosse",A,"Fill the ceramic bowl with a smooth, creamy, light red tomato sauce with tiny green herb flecks, a metal spoon resting in the bowl."+KEEP,513),
("pk3_belegt",A,AUFL+" filled with golden roasted potato cubes, in the middle a layer of creamy red tomato sauce, sprinkled with pale grated cheese that is not melted yet, round salami slices and small red bell pepper cubes on top, not baked yet."+NOC+KEEP,514),
("pk4_gebacken",A,AUFL+" with freshly baked pizza potatoes: golden-brown bubbling melted cheese in the middle, round salami slices with crisp edges and small red bell pepper cubes on top, crispy golden potato cubes around the edge."+NOC+KEEP,515),
("tp0_hook",A,"Replace the ceramic bowl: the hand now holds a white plate with five kinds of small Christmas cookies arranged in groups: pale golden star-shaped butter cookies, star cookies sprinkled with brown cinnamon sugar, dark brown chocolate star cookies, small round pale thumbprint cookies rolled in white coconut flakes with a red jam centre, and small round dark chocolate thumbprint cookies with a red jam centre."+NOC+KEEP,521),
("tp1_teig",A,"Fill the ceramic bowl with one smooth, firm, pale yellow ball of shortcrust cookie dough."+NOC+KEEP,522),
("tp2_teilen",A,BOARD+", on it five equal round balls of cookie dough in a row: three pale yellow dough balls and two dark brown cocoa dough balls."+NOC+KEEP,523),
("tp3_blech",A,TRAY+", on it unbaked cookies in neat rows: pale star-shaped cut-out cookies, dark brown chocolate star-shaped cut-out cookies and small round thumbprint cookies with a dot of red jam in the middle, some of them rolled in white coconut flakes, not baked yet."+NOC+KEEP,524),
("tp4_gebacken",A,TRAY+", on it freshly baked cookies in neat rows: light golden star cookies, dark brown chocolate star cookies and small round thumbprint cookies with a glossy red jam centre, some of them coated with lightly toasted coconut flakes."+NOC+KEEP,525),
("dk0_hook",A,"Replace the ceramic bowl: the hand now holds a white plate with one large wedge of a savoury doner pie: a golden-brown bread crust with a high rim, filled with spiced browned chicken strips and melted golden cheese, topped with shredded pale green iceberg lettuce, small tomato and cucumber pieces and a drizzle of white garlic yogurt sauce."+NOC+KEEP,531),
("dk1_teig",A,"Fill the ceramic bowl with one smooth, soft, pale white ball of bread dough, a little flour dusted on it."+NOC+KEEP,532),
("dk2_form",A,SPRING+", in it raw pale dough pressed flat onto the bottom and pulled up into a 4 cm high rim all around, the bottom pricked many times with a fork, not baked yet, empty inside."+NOC+KEEP,533),
("dk3_pfanne",P,"Fill the pan with thin strips of chicken breast and onion rings, fried golden brown and coated with red-brown paprika spices, sizzling."+KEEPP,534),
("dk4_gebacken",A,SPRING+", in it a freshly baked savoury pie: golden-brown crust with a high rim, filled to the top with spiced browned chicken strips and onion rings under golden-brown melted cheese."+NOC+KEEP,535),
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
