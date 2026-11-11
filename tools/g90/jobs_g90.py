# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow"]
# ///
# G90 – Donnerstag 12.11.2026: FLUX.1-dev-Bilder (1024x1280) fuer 16 Rezepte + neue Kacheln Banane, Gnocchi, Vollkornbrot
import io, os, sys, time, json
from huggingface_hub import InferenceClient, HfApi
TOK=os.environ["HF_TOKEN"]; cl=InferenceClient(api_key=TOK); api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
S=" Homemade, standing on a light wooden table, behind it a plain warm beige wall with soft golden bokeh fairy lights out of focus, cozy warm Christmas market mood, natural soft warm light, shallow depth of field, professional food photography, realistic, appetizing, already served, no hands, no people, no text, nothing else on the table, the upper third of the image is plain warm beige background with a few bokeh lights."
P=json.loads(r"""{
"ZimtschneckenOats": "Two glass jars with overnight oats seen from the side at eye level, creamy light beige cinnamon oats with visible brown cinnamon swirls through the glass, each topped with a thick white cream cheese frosting swirl and a dusting of brown cinnamon, two cinnamon sticks beside the jars, a spoon beside.",
"Fruehstuecksbroetchen": "Homemade round bread rolls on baking paper on a light wooden board, golden brown crust with one long slash on top, some rolls topped with blue-black poppy seeds and some with golden sesame seeds, one roll in front cut open showing a soft white fluffy crumb, a small dish of butter beside.",
"Engelsaugen": "Homemade thumbprint cookies (German Engelsaugen): small round pale golden shortbread cookies, each with a glossy red raspberry jam filled dimple in the center, piled on a white plate, a few cookies lying on the wooden table in front, a small glass jar of red raspberry jam beside.",
"StrammerMax": "A white plate with two slices of toasted rustic brown whole grain bread, each topped with slices of pink ham, a little melted cheese and a sunny-side-up fried egg with a bright yellow runny yolk, sprinkled with chopped chives, two pickled gherkins beside on the plate, a fork beside.",
"MaulwurfBowl": "A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, both handles of the dish fully visible, layers visible through the glass; about one quarter eaten from the back corner, an empty clean teaspoon resting inside, plain and simple, nothing on the spoon. Inside: a dark chocolate sponge cake base, a layer of banana slices visible through the glass, a thick mound of white cream on top completely covered with dark chocolate cake crumbs and dark chocolate shavings, half a banana beside the dish.",
"Lasagne": "A white ceramic rectangular baking dish with a classic lasagna with a golden brown melted cheese top, one square portion lifted out onto a white plate in front showing distinct layers of pasta sheets, red minced beef tomato sauce and white cream from the side, a fork beside.",
"SpekKaeseBowl": "A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, both handles of the dish fully visible, layers visible through the glass; about one quarter eaten from the back corner, an empty clean teaspoon resting inside, plain and simple, nothing on the spoon. Inside: a baked creamy pale cheesecake with a light golden top on a thin brown spiced cookie crumb base, the top sprinkled with crumbled brown speculoos cookies, two whole speculoos cookies (thin rectangular brown spiced Christmas biscuits with an embossed pattern) beside the dish.",
"CordonBleu": "A white plate with a golden crispy breaded chicken cordon bleu cut in half, showing melted cheese and pink ham inside flowing out, served next to boiled peeled yellow potatoes, a fork beside, a second whole golden breaded cordon bleu on a baking tray blurred in the background.",
"SchokoMousse": "Two small glasses of thick airy dark chocolate mousse seen from the side at eye level, smooth swirled top with a few dark chocolate shavings, a few squares of dark chocolate beside the glasses, a small spoon beside, two more glasses of chocolate mousse blurred in the background.",
"SchinkenLauchQuiche": "A round savory quiche in a white ceramic tart dish seen from the side slightly elevated, golden brown baked egg and cheese filling with visible pink ham cubes and green leek rings, a raised golden crust edge, one slice cut and placed on a small white plate in front showing the creamy pale yellow filling with ham and leek from the side, a fork beside.",
"ZimtstreuselSkyr": "A round cheesecake about 5 cm tall on a white cake stand seen from the side, the top completely covered with golden brown cinnamon crumble streusel, one slice cut and placed on a small white plate in front showing the creamy white filling, the thin crumb base and the thick streusel layer from the side, two cinnamon sticks beside, a fork beside.",
"GnocchiAuflauf": "A white ceramic rectangular baking dish with a gnocchi casserole: small potato gnocchi in a red minced beef tomato sauce with red bell pepper pieces, topped with melted golden brown mozzarella cheese, one portion served on a white plate in front, a fork beside.",
"Kokosmakronen": "Homemade coconut macaroons: small rough white mounds of shredded coconut with golden brown toasted tips, piled on a white plate, a few macaroons lying on the wooden table in front, one broken open showing the moist white inside, a little shredded coconut scattered beside.",
"CheeseburgerLasagne": "A white ceramic rectangular baking dish with a cheeseburger lasagna: golden orange melted cheddar cheese on top with round green pickle slices, one square portion lifted out onto a white plate in front showing layers of pasta sheets, browned minced beef in tomato sauce and white cream from the side, a few green pickle slices on top, a fork beside.",
"TiramisuSkyrKuchen": "A round pale cheesecake about 5 cm tall on a white cake stand seen from the side, the top thickly dusted with dark brown cocoa powder, one slice cut and placed on a small white plate in front showing from the side a thin base of coffee-soaked ladyfinger sponge biscuits and a thick creamy white filling with a dark cocoa top, two ladyfinger biscuits and a small white cup of espresso beside, a fork beside.",
"Kaesespaetzle": "A white ceramic rectangular baking dish with German cheese spaetzle (K\u00e4sesp\u00e4tzle): small soft irregular egg noodles in melted stretchy golden cheese, topped with golden brown roasted onion rings and chopped green chives, one portion served on a white plate in front with melted cheese strings, a fork beside."
}""")
T=json.loads(r"""{
"banane": "Two ripe yellow bananas lying side by side, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else.",
"gnocchi": "A small round wooden bowl filled with raw potato gnocchi (small pale yellow oval potato dumplings with fine ridges), seen from directly above, product photo, soft studio light, isolated on a pure white background, nothing else.",
"vollkornbrot": "Three slices of rustic brown whole grain bread with a dark crust, fanned out and overlapping, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else."
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
J=[(P[k]+S,f"g90/{k}_s{sd}.jpg",1024,1280,sd) for k in keys for sd in seeds]
if os.environ.get("TILES","1")=="1": J+=[(T[t],f"tiles/{t}.jpg",1024,1024,7) for t in T]
with ThreadPoolExecutor(6) as ex: list(ex.map(lambda t: gen(*t),J))
print("done")
