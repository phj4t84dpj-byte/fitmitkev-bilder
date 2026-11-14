# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow"]
# ///
# N2 – Nischenseiten Mo 16.–Mi 18.11.2026: 45 Rezepte (Kuchenherz/Omas Kochtopf im Zettel-Stil, Heißluftheld mit gut sichtbarem Airfryer) + 9 Kacheln
import io, os, time
from huggingface_hub import InferenceClient, HfApi
TOK=os.environ["HF_TOKEN"]; cl=InferenceClient(api_key=TOK); api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
PZ=" Homemade, on a rustic dark brown wooden table with a beige linen cloth with a thin red stripe and a few fir branches, cozy German Christmas kitchen mood, warm soft natural light, shallow depth of field, professional food photography, realistic, appetizing, already served, no hands, no people, no text, no labels. The food is large and fills the lower 60 percent of the image, seen from a slightly elevated angle; the upper 40 percent of the image is a softly blurred warm brown kitchen background."
PH=" The basket is the square pull-out drawer basket of a modern matte black air fryer: the drawer has been pulled out and stands on the table in the lower right, and the black air fryer itself with its round control dial stands directly behind it and is clearly recognizable. Homemade, on a light wooden table, behind it a plain warm beige wall with soft golden bokeh fairy lights out of focus, cozy warm Christmas mood, natural soft warm light, shallow depth of field, professional food photography, realistic, appetizing, no hands, no people, no text, the upper third of the image is plain warm beige background with a few bokeh lights."
import importlib.util, urllib.request
src=urllib.request.urlopen("https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/tools/n2/n2_data.py").read()
ns={}; exec(src.decode(),ns); R=ns['R']
T={
"toastbrot":"Four slices of soft white sandwich toast bread stacked slightly fanned out, golden crust, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else, no packaging.",
"haehnchenfluegel":"Six raw chicken wings with pale skin lying side by side, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else.",
"sojasauce":"A small round white dipping bowl filled with dark brown soy sauce, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else, no bottle.",
"blaetterteig":"A partly unrolled sheet of raw pale puff pastry dough lying flat, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else, no packaging.",
"puderzucker":"A small round light wooden bowl heaped with fine white powdered sugar, a little powdered sugar dusted beside it, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else.",
"schweineschnitzel":"Two raw thin pink pork escalopes lying side by side, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else.",
"kaesescheiben":"Four square slices of pale yellow gouda cheese stacked slightly fanned out, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else, no packaging.",
"nuss_nougat_creme":"A small round light wooden bowl filled with smooth glossy brown chocolate hazelnut spread, a teaspoon with spread beside it and two hazelnuts, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else, no jar, no label.",
"schweinebauch":"A raw piece of pork belly with white rind on top and visible layers of pink meat and white fat, seen from the side at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else."
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
keys=[k for k in os.environ.get("KEYS","").split(",") if k]
seeds=[int(x) for x in os.environ.get("SEEDS","1,2").split(",")]
J=[(r['prompt']+(PZ if r['stil']=='zettel' else PH),f"n2/{r['key']}_s{sd}.jpg",1024,1280,sd) for r in R if (not keys or r['key'] in keys) for sd in seeds]
if os.environ.get("TILES","1")=="1": J+=[(T[t],f"tiles/{t}.jpg",1024,1024,7) for t in T]
print(len(J),"Bilder",flush=True)
with ThreadPoolExecutor(6) as ex: list(ex.map(lambda t: gen(*t),J))
print("done")
