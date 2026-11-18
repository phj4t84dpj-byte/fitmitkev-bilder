# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow"]
# ///
# GTA VI (19.11.2026): FLUX.1-dev-Bilder (1024x1280) fuer 3 Themen-Rezepte + Kachel Limette
import io, os, sys, time, json
from huggingface_hub import InferenceClient, HfApi
TOK=os.environ["HF_TOKEN"]; cl=InferenceClient(api_key=TOK); api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
S=" Homemade, standing on a light wooden table, behind it a plain warm beige wall with soft golden bokeh fairy lights out of focus, cozy warm Christmas market mood, natural soft warm light, shallow depth of field, professional food photography, realistic, appetizing, already served, no hands, no people, no text, nothing else on the table, the upper third of the image is plain warm beige background with a few bokeh lights."
P=json.loads(r"""{
"KeyLimeBowl": "A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, both handles of the dish fully visible, layers visible through the glass; about one quarter eaten from the back corner, an empty clean teaspoon resting inside, plain and simple, nothing on the spoon. Inside: a thin golden biscuit crumb base at the bottom, a thick smooth pale lime-green creamy baked cheesecake layer, on top a few swirls of white whipped cream, fine bright green lime zest and two thin fresh lime slices, two halved green limes beside the dish.",
"Cubano": "Two pressed toasted Cuban sandwiches on a wooden board, golden crispy flattened white bread rolls with grill marks, each cut diagonally in half and the halves stacked so the filling is clearly visible from the side: many thin pink ham slices, thin slices of roast meat, melted yellow cheese, green pickle slices and a stripe of yellow mustard, a small white bowl of pickle slices beside.",
"OfenNachos": "A black baking tray piled with homemade crispy oven-baked tortilla chip triangles topped with browned ground beef, golden melted cheese, small red bell pepper cubes, yellow sweet corn and fresh chopped green chives, a small white bowl of thick white yogurt dip and a small white bowl of red tomato salsa beside the tray, one portion served on a white plate in front."
}""")
T=json.loads(r"""{
"limette": "Two whole fresh bright green limes and one lime cut in half showing the juicy pale green inside, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else, no text."
}""")
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
J=[(P[k]+S,f"gta/{k}_s{sd}.jpg",1024,1280,sd) for k in keys for sd in seeds]
if os.environ.get("TILES","1")=="1": J+=[(T[t],f"tiles/{t}.jpg",1024,1024,7) for t in T]
with ThreadPoolExecutor(6) as ex: list(ex.map(lambda t: gen(*t),J))
print("done")
