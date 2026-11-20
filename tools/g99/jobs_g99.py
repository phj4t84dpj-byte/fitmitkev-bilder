# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow"]
# ///
# G99 (So 22.11.2026): FLUX.1-dev-Bilder (1024x1280) fuer 7 neue Rezepte nach Mitbewerber-Auswertung; TILES=1 erzeugt zusaetzlich die 2 neuen Kacheln
import io, os, sys, time, json
from huggingface_hub import InferenceClient, HfApi
TOK=os.environ["HF_TOKEN"]; cl=InferenceClient(api_key=TOK); api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
S=" Homemade, standing on a light wooden table, behind it a plain warm beige wall with soft golden bokeh fairy lights out of focus, cozy warm Christmas market mood, natural soft warm light, shallow depth of field, professional food photography, realistic, appetizing, already served, no hands, no people, no text, nothing else on the table, the upper third of the image is plain warm beige background with a few bokeh lights."
P=json.loads(r"""{
"NutellaBanane": "One tall clear dessert glass filled with layers of smooth pale brown chocolate hazelnut yogurt cream and fresh banana slices, several round banana slices pressed flat against the inside of the glass wall, on top a fan of banana slices and a small glossy swirl of dark brown chocolate hazelnut spread, one plain straight teaspoon lying beside the glass, one whole yellow banana and a few banana slices beside the glass.",
"DoenerKuchen": "A round savory pie standing on a wooden board, baked in a springform and the ring removed: a golden brown bread dough crust with a four centimeter high rim, filled with browned spiced chicken strips and golden melted cheese, the top covered with fresh shredded green iceberg lettuce, diced red tomato, diced cucumber, thin red onion rings and drizzled stripes of white garlic yogurt sauce, one quarter slice cut out and served on a white plate in front showing the chicken filling inside the crust, a small white bowl of white garlic sauce beside.",
"PizzaKartoffeln": "Close view of a rectangular white ceramic baking dish filled to the top with many small golden brown crispy roasted potato cubes, the middle of the dish covered with a blanket of golden browned bubbling melted mozzarella cheese, round slices of red salami lying on top of the cheese, a little red tomato sauce showing under the cheese, small red bell pepper cubes, crispy bare potato cubes clearly visible all around the edge of the dish, sprinkled with dried oregano. In front a white plate with one portion of crispy potato cubes with stretchy melted cheese and two salami slices, a fork beside the plate.",
"EinTeig": "A large round white plate piled with five different kinds of small homemade Christmas cookies arranged in five neat groups: pale golden star-shaped butter cookies, star-shaped cookies sprinkled with brown cinnamon, dark brown chocolate heart-shaped cut-out cookies, round cookies coated in white shredded coconut, and round thumbprint cookies with a glossy red jam center. A few cookies lying on the table in front of the plate, a small star-shaped metal cookie cutter beside.",
"QuarkWoelkchen": "A white plate piled high with many small round pale cream-colored soft melt-in-the-mouth cookies, each cookie a slightly flattened ball with fork tine marks pressed on top, thickly dusted with white powdered sugar like snow, a few cookies lying on the table in front of the plate, one cookie broken in half showing the soft tender pale crumb inside, a small metal sieve with powdered sugar beside.",
"Sonntagsbraten": "A white dinner plate with three thick slices of tender braised beef roast covered with glossy dark brown gravy, beside the meat a portion of shiny purple braised red cabbage and two round pale yellow German potato dumplings with a little chopped parsley on top. Behind the plate a small white gravy boat filled with dark brown gravy.",
"Blumenkohlsuppe": "A deep white soup bowl standing on a flat white plate, filled with creamy pale ivory cauliflower soup, in the soup several small white cauliflower florets and many round slices of pink sausage, sprinkled with fresh chopped green parsley and a little black pepper, a spoon lying on the plate beside the bowl. On the right side behind the bowl one small whole white cauliflower. The left side of the table is empty."
}""")
T=json.loads(r"""{
"rinderbraten": "One raw lean beef roast, a compact oval piece of raw dark red beef topside tied with white butcher's twine, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else, no plate, no board.",
"kartoffelkloesse": "Three raw round pale yellow German potato dumplings, smooth balls of potato dough each about the size of a tennis ball, lying close together, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else, no plate, no bowl."
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
if os.environ.get("TILES","0")=="1": J+=[(T[t],f"tiles/{t}.jpg",1024,1024,7) for t in T]
with ThreadPoolExecutor(6) as ex: list(ex.map(lambda t: gen(*t),J))
print("done")
