# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow"]
# ///
# G95 – Dienstag 17.11.2026: FLUX.1-dev-Bilder (1024x1280) fuer 14 Rezepte + neue Kacheln Aubergine, Erdbeeren (TK), Zuckerstreusel
import io, os, sys, time, json
from huggingface_hub import InferenceClient, HfApi
TOK=os.environ["HF_TOKEN"]; cl=InferenceClient(api_key=TOK); api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
S=" Homemade, standing on a light wooden table, behind it a plain warm beige wall with soft golden bokeh fairy lights out of focus, cozy warm Christmas market mood, natural soft warm light, shallow depth of field, professional food photography, realistic, appetizing, already served, no hands, no people, no text, nothing else on the table, the upper third of the image is plain warm beige background with a few bokeh lights."
P=json.loads(r"""{
"BratapfelPorridge": "A white ceramic bowl of creamy warm oatmeal porridge seen from the side slightly elevated, topped with a generous heap of soft golden cinnamon-stewed apple cubes with raisins, a dollop of thick white skyr and toasted golden flaked almonds, a light dusting of cinnamon, steam rising, a second bowl blurred behind, half a red apple and a cinnamon stick beside the bowl, a spoon beside.",
"Laugenbroetchen": "Six round German pretzel rolls (Laugenbrötchen) with a glossy golden chestnut-brown pretzel crust, warm bakery color, not dark, a cross cut on top showing the pale soft inside, sprinkled with coarse white salt crystals, on a wooden board, one roll cut in half in front showing the soft fluffy white crumb with a little butter, a small bowl of coarse salt beside.",
"Elisenlebkuchen": "Several round German Elisen gingerbread cookies (Elisenlebkuchen) on a white plate and on the wooden table, each a thick domed round nut gingerbread about 7 cm wide on a thin white wafer base, the top coated with glossy dark chocolate, one cookie broken in half in front showing the moist light brown nutty inside, a few whole almonds, an orange and a cinnamon stick beside.",
"KaeseSchinkenWaffeln": "A stack of four golden brown savory heart-shaped waffles on a white plate, small pink ham cubes and melted golden cheese visible in the waffle surface, sprinkled with fresh chopped green chives, one waffle broken in front showing the fluffy inside with ham and cheese, a small bowl of white herb cream cheese dip beside.",
"ApfelstrudelTiramisu": "Four small clear dessert glasses seen from the side at eye level, layered dessert clearly visible through the glass: pale golden soaked sponge finger biscuits, thick white vanilla cream layers and golden cinnamon apple cubes with raisins, topped with more cinnamon apple cubes, toasted golden flaked almonds and a dusting of cinnamon, one glass standing in front with a teaspoon beside it, a red apple and a cinnamon stick on the table.",
"Moussaka": "A rectangular white ceramic baking dish with Greek moussaka with a thick golden brown baked creamy topping, one square portion served on a white plate in front clearly showing the layers from the side: soft dark purple-skinned eggplant slices, potato slices and browned minced beef in red tomato sauce under the thick creamy white topping, a little fresh oregano on top, a fork beside.",
"KirschStreuselBowl": "A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, both handles of the dish fully visible, layers visible through the glass; about one quarter eaten from the back corner, an empty clean teaspoon resting inside, plain and simple, nothing on the spoon. Inside: a soft golden oat base, a thick layer of glossy dark red sour cherries in creamy pale yellow pudding, topped with golden crumble streusel, a few dark red cherries beside the dish.",
"HaehnchenNudelauflauf": "A rectangular white ceramic baking dish with a creamy pasta bake of penne, tender chicken pieces and bright green broccoli florets in a creamy white sauce under a golden brown bubbly melted cheese crust, one portion served on a white plate in front showing the creamy penne, chicken and broccoli, a fork beside.",
"Schichtsalat": "Four tall clear glass jars filled with a German layered salad (Schichtsalat) seen from the side at eye level, distinct colorful horizontal layers clearly visible through the glass: shredded pale green iceberg lettuce, bright green peas, yellow corn kernels, chopped hard-boiled egg, pink diced ham and thin white creamy dressing layers, topped with grated cheese and fresh chopped chives, one jar in front with a fork beside it.",
"BenjaminBowl": "A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, both handles of the dish fully visible, layers visible through the glass; about one quarter eaten from the back corner, an empty clean teaspoon resting inside, plain and simple, nothing on the spoon. Inside: a dark brown chocolate sponge cake layer at the bottom, a thick layer of smooth pastel pink strawberry cream on top, several small piped dollops of light brown chocolate cream on the pink cream and colorful rainbow sugar sprinkles scattered on top, two halved red strawberries beside the dish.",
"CurrywurstAuflauf": "A white ceramic rectangular baking dish with a casserole of sliced potatoes and pieces of sausage in a glossy red-orange curry tomato sauce, melted cheese on top, one portion served on a white plate in front, a sprinkle of curry powder on top, a fork beside.",
"Nuggets": "Many crispy golden brown oven-baked chicken nuggets with a crunchy cornflake crust piled on a white plate, one nugget broken open in front showing the juicy white chicken inside, a small bowl of creamy pale yellow honey mustard dip and a small bowl of ketchup beside the plate.",
"GefuelltePaprika": "A white ceramic baking dish with halved red bell peppers generously stuffed with minced beef and rice, baked in a red tomato sauce, topped with melted golden brown cheese and a little fresh parsley, one stuffed pepper half served on a white plate in front with tomato sauce, a fork beside.",
"SalamiPizza": "A whole round thin-crust homemade salami pizza about 22 cm on a wooden board, golden brown crispy edge, melted golden cheese, slightly crispy round salami slices and red and green bell pepper strips, a little oregano on top, one slice cut and pulled slightly out with stretchy melted cheese, a pizza cutter beside."
}""")
T=json.loads(r"""{
"aubergine": "Two whole fresh glossy dark purple eggplants (aubergines) with green stems lying side by side, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else.",
"erdbeeren": "A small heap of frozen whole red strawberries with a light white frost coating, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else, no bowl.",
"zuckerstreusel": "A small heap of colorful rainbow sugar sprinkles (short round sprinkles in pink, yellow, blue, green, white and orange), seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else, no bowl."
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
J=[(P[k]+S,f"g95/{k}_s{sd}.jpg",1024,1280,sd) for k in keys for sd in seeds]
if os.environ.get("TILES","1")=="1": J+=[(T[t],f"tiles/{t}.jpg",1024,1024,7) for t in T]
with ThreadPoolExecutor(6) as ex: list(ex.map(lambda t: gen(*t),J))
print("done")
