# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow"]
# ///
# G89c – dritter Anlauf Flammkuchen: nur positive Beschreibungen (Verneinungen erzeugten Tomatensauce), flach wie ein Fladen
import io, os, sys, time
from huggingface_hub import InferenceClient, HfApi
TOK=os.environ["HF_TOKEN"]; cl=InferenceClient(api_key=TOK); api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
S=" Homemade, standing on a light wooden table, behind it a plain warm beige wall with soft golden bokeh fairy lights out of focus, cozy warm Christmas market mood, natural soft warm light, shallow depth of field, professional food photography, realistic, appetizing, already served, the upper third of the image is plain warm beige background with a few bokeh lights."
P={
"FlammkuchenA": "A wafer-thin crispy flatbread lying completely flat on a sheet of brown baking paper on a wooden board, photographed from a 45 degree angle. The base is as thin and flat as a crispy tortilla, with thin dark-browned brittle edges. The whole surface is spread right to the edge with a layer of pure white sour cream, the white cream is clearly visible everywhere between the toppings. On the white cream lie thin red onion rings, small strips of pink cooked ham and thin slices of white mushrooms, lightly browned in a few spots. The flatbread is cut into four pieces and one piece is pulled slightly forward.",
"FlammkuchenB": "A rectangular Alsatian Flammkuchen with rounded corners lying flat on brown baking paper on a dark baking tray, photographed from a 45 degree angle. Paper-thin cracker-like dough, completely flat, with thin dark crispy blistered edges. Covered edge to edge with white creme fraiche, the surface is mostly white. Scattered on the white cream: thin red onion half-rings, small pink ham strips and thin white mushroom slices, a little black pepper. One rectangular piece is cut off and pulled slightly forward."
}
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
seeds=[int(x) for x in os.environ.get("SEEDS","6,7").split(",")]
J=[(P[k]+S,f"g89/{k}_c{sd}.jpg",1024,1280,sd) for k in P for sd in seeds]
with ThreadPoolExecutor(4) as ex: list(ex.map(lambda t: gen(*t),J))
print("done")
