# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow"]
# ///
# G99 (So 22.11.2026): FLUX.1-dev-Bilder (1024x1280) fuer 3 neue Rezepte nach Mitbewerber-Auswertung
import io, os, sys, time, json
from huggingface_hub import InferenceClient, HfApi
TOK=os.environ["HF_TOKEN"]; cl=InferenceClient(api_key=TOK); api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
S=" Homemade, standing on a light wooden table, behind it a plain warm beige wall with soft golden bokeh fairy lights out of focus, cozy warm Christmas market mood, natural soft warm light, shallow depth of field, professional food photography, realistic, appetizing, already served, no hands, no people, no text, nothing else on the table, the upper third of the image is plain warm beige background with a few bokeh lights."
P=json.loads(r"""{
"NutellaBanane": "One tall clear dessert glass filled with layers of smooth pale brown chocolate hazelnut yogurt cream and fresh banana slices, several round banana slices pressed flat against the inside of the glass wall, on top a fan of banana slices and a small glossy swirl of dark brown chocolate hazelnut spread, one plain straight teaspoon lying beside the glass, one whole yellow banana and a few banana slices beside the glass.",
"DoenerKuchen": "A round savory pie standing on a wooden board, baked in a springform and the ring removed: a golden brown bread dough crust with a four centimeter high rim, filled with browned spiced chicken strips and golden melted cheese, the top covered with fresh shredded green iceberg lettuce, diced red tomato, diced cucumber, thin red onion rings and drizzled stripes of white garlic yogurt sauce, one quarter slice cut out and served on a white plate in front showing the chicken filling inside the crust, a small white bowl of white garlic sauce beside.",
"PizzaKartoffeln": "A rectangular white ceramic baking dish filled with golden brown crispy roasted potato cubes, topped like a pizza: red tomato sauce in the middle, golden browned bubbling melted cheese, round slices of red salami and small red bell pepper cubes, crispy potato cubes without sauce visible around the edge, sprinkled with dried oregano, one portion served on a white plate in front, a fork beside."
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
J=[(P[k]+S,f"g99/{k}_s{sd}.jpg",1024,1280,sd) for k in keys for sd in seeds]
with ThreadPoolExecutor(6) as ex: list(ex.map(lambda t: gen(*t),J))
print("done")
