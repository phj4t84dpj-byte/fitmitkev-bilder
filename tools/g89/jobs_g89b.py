# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow"]
# ///
# G89b – Nachbesserungen (genauere Prompts) fuer 5 Motive
import io, os, sys, time
from huggingface_hub import InferenceClient, HfApi
TOK=os.environ["HF_TOKEN"]; cl=InferenceClient(api_key=TOK); api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
S=" Homemade, standing on a light wooden table, behind it a plain warm beige wall with soft golden bokeh fairy lights out of focus, cozy warm Christmas market mood, natural soft warm light, shallow depth of field, professional food photography, realistic, appetizing, already served, no hands, no people, no text, nothing else on the table, the upper third of the image is plain warm beige background with a few bokeh lights."
P={
"Weckmann": "Three flat homemade sweet yeast bread figures (German Weckmann, also called Stutenkerl) lying flat on baking paper on a baking tray, seen from above at a 45 degree angle, each figure about 18 cm long and flat like a bread roll, simple hand-shaped body with a round head, two arms and two legs slightly spread, matte golden brown baked crust with a light egg wash shine, two raisins pressed in as eyes and three raisins as buttons, no mouth, no icing, no decoration, slightly irregular rustic handmade shapes, real bakery bread texture, a few raisins beside.",
"Kaesebroetchen": "Homemade round bread rolls with a thick crust of melted and browned grated cheese baked on top (German cheese rolls from the bakery), the cheese crust golden with darker crispy spots and running slightly down the sides, on baking paper on a light wooden board, one roll in front cut in half showing a soft white fluffy crumb, a small dish of butter beside.",
"GebratenerReis": "A black wok pan filled with Asian egg fried rice: golden glossy rice with small irregular bite-sized pieces of golden-brown pan-fried chicken breast meat (clearly real chicken with a fibrous texture, not tofu, not cubes), fluffy yellow scrambled egg pieces clearly visible, green peas, tiny diced orange carrots and sliced green spring onions, one portion served in a white bowl in front, wooden chopsticks beside.",
"SchokoKaesekuchen": "A round baked dark chocolate cheesecake about 5 cm tall on a white cake stand seen from the side, matte baked dark brown top without glaze sprinkled with small flat dark chocolate chips, a very thin 3 mm light brown cookie crumb base, one slice cut and placed on a small white plate in front showing the creamy dense dark brown chocolate cheesecake filling and the very thin base from the side, a few small chocolate chips beside, a fork beside.",
"Flammkuchen": "A very thin crispy rustic Alsatian tarte flambee (German Flammkuchen) on a wooden board, paper-thin flat crust with no raised rim, irregular oval shape with browned blistered edges, spread with white sour cream only (no tomato sauce, no melted yellow cheese), topped with thin red onion rings, small strips of pink ham and thin slices of white mushrooms, cut into rectangular pieces with one piece pulled slightly away in front, a pizza cutter beside."
}
T={"loeffelbiskuit": "Four ladyfinger sponge biscuits (savoiardi, long pale golden finger-shaped sponge biscuits with a sugar-dusted top) lying side by side in a neat small pile, seen from a 45 degree angle, product photo, soft studio light, isolated on a pure white background, nothing else."}
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
keys=sys.argv[1:] or list(P)
seeds=[int(x) for x in os.environ.get("SEEDS","1,2").split(",")]
J=[(P[k]+S,f"g89/{k}_b{sd}.jpg",1024,1280,sd) for k in keys for sd in seeds]
if os.environ.get("TILES","1")=="1": J+=[(T[t],f"tiles/{t}.jpg",1024,1024,7) for t in T]
with ThreadPoolExecutor(6) as ex: list(ex.map(lambda t: gen(*t),J))
print("done")
