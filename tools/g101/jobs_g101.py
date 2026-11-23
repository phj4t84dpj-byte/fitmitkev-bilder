# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow"]
# ///
# G101 (Di 24.11.2026): FLUX.1-dev-Bilder (1024x1280) fuer die vier neuen Rezepte: KlossJaeger, KlossSauerbraten (Klossteig-Reihe), EierlikoerWoelkchen, Buletten
import io, os, sys, time, json
from huggingface_hub import InferenceClient, HfApi
TOK=os.environ["HF_TOKEN"]; cl=InferenceClient(api_key=TOK); api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
S=" Homemade, standing on a light wooden table, behind it a plain warm beige wall with soft golden bokeh fairy lights out of focus, cozy warm Christmas market mood, natural soft warm light, shallow depth of field, professional food photography, realistic, appetizing, already served, no hands, no people, no text, nothing else on the table, the upper third of the image is plain warm beige background with a few bokeh lights."
P=json.loads(r"""{
"KlossJaeger": "A round white dinner plate, the whole plate fully visible with empty table space left and right of it, with one thin golden-brown seared chicken cutlet covered with a creamy light brown mushroom cream sauce with many sliced browned mushrooms, sprinkled with fresh chopped green parsley, and beside it on the same plate exactly four small round pale yellow matte German potato dumplings, each about the size of a golf ball, lying close together in a group, all four clearly visible.",
"KlossSauerbraten": "A round white dinner plate, the whole plate fully visible with empty table space left and right of it, with thin slices of tender braised beef in a glossy dark brown sweet-and-sour gravy with a few dark raisins and soft browned onion rings, and beside it on the same plate exactly four small round pale yellow matte German potato dumplings, each about the size of a golf ball, lying close together in a group, all four clearly visible, a little chopped green parsley on the dumplings.",
"EierlikoerWoelkchen": "A white plate piled high with many small round pale cream-coloured soft cookies, each cookie a smooth slightly domed mound with fine cracks, thickly dusted with white powdered sugar, the bottoms pale golden, a few cookies lying on the table in front of the plate, one cookie broken in half showing the soft pale yellow crumb inside, a small glass of thick pale yellow egg liqueur beside the plate.",
"Buletten": "A round white dinner plate, the whole plate fully visible with empty table space left and right of it, with two thick round golden-brown pan-fried German meat patties with a crisp crust and beside them a large portion of warm potato salad made of sliced boiled potatoes glistening with broth, with small diced onions, tiny browned ham cubes and chopped green chives, a small dollop of yellow mustard on the rim of the plate.",
"KlossJaegerB": "A round white dinner plate, the whole plate fully visible with empty table space left and right of it, with one thin flat pan-seared natural chicken breast fillet without any breading, its surface smooth and glossy golden brown like grilled chicken breast, half covered with a creamy light brown mushroom cream sauce with many sliced browned mushrooms, sprinkled with fresh chopped green parsley, and beside it on the same plate exactly four small round pale yellow matte German potato dumplings, each about the size of a golf ball, lying close together in a group, all four clearly visible."
}""")
T={}   # alle Kacheln fuer G101 gibt es schon (semmelbroesel, eierlikoer, putenschinken, senf ...)
def gen(prompt,path,w,h,seed):
    for a in range(3):
        try:
            img=cl.text_to_image(prompt,model="black-forest-labs/FLUX.1-dev",width=w,height=h,seed=seed)
            b=io.BytesIO(); img.convert("RGB").save(b,"JPEG",quality=92); b.seek(0)
            api.upload_file(path_or_fileobj=b,path_in_repo=path,repo_id=REPO,repo_type="dataset"); print("ok",path,flush=True); return
        except Exception as e:
            print("retry",path,repr(e)[:200],flush=True); time.sleep(15)
    print("FAIL",path,flush=True)
from concurrent.futures import ThreadPoolExecutor
keys=[k for k in os.environ.get("KEYS","").split(",") if k] or list(P)
seeds=[int(x) for x in os.environ.get("SEEDS","1,2").split(",")]
J=[(P[k]+S,f"g101/{k}_s{sd}.jpg",1024,1280,sd) for k in keys for sd in seeds]
if os.environ.get("TILES","0")=="1": J+=[(T[t],f"tiles/{t}.jpg",1024,1024,7) for t in T]
with ThreadPoolExecutor(6) as ex: list(ex.map(lambda t: gen(*t),J))
print("done")
