# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow"]
# ///
# G100 (Mo 23.11.2026): FLUX.1-dev-Bilder (1024x1280) fuer 4 neue Rezepte (Kokos-Woelkchen, Schichtsalat ueber Nacht, Gebratene Nudeln mit Hack, Pizza-Wrap); keine neuen Kacheln
import io, os, sys, time, json
from huggingface_hub import InferenceClient, HfApi
TOK=os.environ["HF_TOKEN"]; cl=InferenceClient(api_key=TOK); api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
S=" Homemade, standing on a light wooden table, behind it a plain warm beige wall with soft golden bokeh fairy lights out of focus, cozy warm Christmas market mood, natural soft warm light, shallow depth of field, professional food photography, realistic, appetizing, already served, no hands, no people, no text, nothing else on the table, the upper third of the image is plain warm beige background with a few bokeh lights."
P=json.loads(r"""{
"KokosWoelkchen": "A white plate piled high with many small round snow-white coconut cookies, each cookie a soft slightly domed mound with a rough surface of fine white shredded coconut, lightly dusted with white powdered sugar, the bottoms pale golden, a few cookies lying on the table in front of the plate, one cookie broken in half showing the soft moist white crumb inside, a small white bowl of shredded coconut beside.",
"Schichtsalat": "A large straight-sided clear glass salad bowl seen from the side, filled with clearly separated horizontal layers visible through the glass: at the bottom finely shredded pale green iceberg lettuce, then thin green and white leek rings, yellow sweet corn, small diced apple, pink diced cooked ham, round slices of hard-boiled egg pressed against the glass, on top a thick smooth white creamy dressing layer covered with finely grated pale yellow cheese. A large serving spoon lies beside the bowl.",
"HackNudeln": "A black wok with Chinese stir-fried egg noodles mixed with plenty of browned crumbled minced beef, thin orange carrot strips, red bell pepper strips and pale green cabbage strips, glossy with soy sauce, sprinkled with green spring onion rings, one portion served in a white bowl in front with chopsticks resting on it.",
"PizzaWrap": "Two rolled wraps made of thin golden brown baked flatbread with a slightly blistered speckled surface, each cut in half diagonally, the halves stacked on a wooden board with the cut sides facing the camera, showing a filling of red tomato sauce, stretchy melted white mozzarella cheese and round slices of red salami, a little melted cheese pulling between the halves, a few dried oregano flakes on top, a small white bowl of red tomato sauce beside."
}""")
T={}
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
J=[(P[k]+S,f"g100/{k}_s{sd}.jpg",1024,1280,sd) for k in keys for sd in seeds]
if os.environ.get("TILES","0")=="1": J+=[(T[t],f"tiles/{t}.jpg",1024,1024,7) for t in T]
with ThreadPoolExecutor(6) as ex: list(ex.map(lambda t: gen(*t),J))
print("done")
