# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow"]
# ///
# G94 – Montag 16.11.2026: FLUX.1-dev-Bilder (1024x1280) fuer 16 Rezepte + neue Kacheln Proteinpulver, Maultaschen
import io, os, sys, time, json
from huggingface_hub import InferenceClient, HfApi
TOK=os.environ["HF_TOKEN"]; cl=InferenceClient(api_key=TOK); api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
S=" Homemade, standing on a light wooden table, behind it a plain warm beige wall with soft golden bokeh fairy lights out of focus, cozy warm Christmas market mood, natural soft warm light, shallow depth of field, professional food photography, realistic, appetizing, already served, no hands, no people, no text, nothing else on the table, the upper third of the image is plain warm beige background with a few bokeh lights."
P=json.loads(r"""{
"KipferlOats": "Two glass jars with overnight oats seen from the side at eye level, creamy pale vanilla oats visible through the glass, each topped with a thick layer of toasted golden flaked almonds and a light dusting of white powdered sugar, two small crescent-shaped vanilla cookies (Vanillekipferl) and a vanilla pod lying beside the jars, a spoon beside.",
"Bratkartoffeln": "A black cast iron pan filled with crispy golden brown fried potato slices with browned onions and small pink ham cubes, two fried eggs sunny side up with bright orange yolks lying on top, sprinkled with fresh chopped green chives, two pickled gherkins on a small plate beside, a fork beside.",
"Nussecken": "Several triangular German nut corner pastries (Nussecken) stacked on a wooden board: a thin shortcrust base, a thin layer of apricot jam and a thick golden brown caramelized chopped hazelnut topping, two corners of each triangle dipped in glossy dark chocolate, one triangle leaning in front showing the layers from the side, a few whole hazelnuts beside.",
"Quarkbaellchen": "A white paper bag lying on its side on the table with many round golden brown German quark doughnut balls (Quarkbällchen) rolled in cinnamon sugar spilling out onto a wooden board, one ball in front broken open showing the fluffy pale yellow crumb inside, a small bowl of cinnamon sugar beside.",
"Maultaschen": "A rectangular white ceramic baking dish with a casserole of thick slices of Swabian filled pasta squares (Maultaschen, pale pasta dough with a green-speckled meat and spinach filling visible on the cut sides) baked in a set egg custard with golden brown fried onion rings and a golden melted cheese crust, sprinkled with fresh chopped chives, one portion served on a white plate in front, a fork beside.",
"Zitronenkuchen": "A round golden yellow lemon almond cake about 5 cm tall on a white cake stand seen from the side, the top covered with a white lemon icing glaze dripping slightly over the edge and decorated with three thin lemon slices and fine yellow lemon zest, one slice cut and placed on a small white plate in front showing the moist golden crumb from the side, half a lemon beside, a fork beside.",
"GyrosLasagne": "A rectangular white ceramic baking dish with a lasagne with a golden brown melted cheese crust, one square portion served on a white plate in front clearly showing the layers from the side: pasta sheets, strips of browned gyros-seasoned chicken with onions in red tomato sauce and layers of thick white yogurt cream, a few red onion rings and a little oregano on top, a fork beside.",
"BrownieBowl": "A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, both handles of the dish fully visible, layers visible through the glass; about one quarter eaten from the back corner, an empty clean teaspoon resting inside, plain and simple, nothing on the spoon. Inside: a baked dark chocolate brownie with a shiny crackled dark brown top and melted dark chocolate chunks, the moist fudgy dark crumb visible through the glass and where it was eaten, two small pieces of dark chocolate beside the dish.",
"HuettenEis": "A white ceramic bowl with three round scoops of creamy pale beige cinnamon ice cream sprinkled with brown spiced biscuit crumbs, two thin flat rectangular brown spiced biscuits (German Spekulatius) with an embossed windmill pattern stuck into the ice cream, a metal loaf tin with more ice cream and an ice cream scoop blurred behind, a cinnamon stick and a spoon beside.",
"Doener": "Two homemade doner kebabs in golden brown oval flatbread pockets standing upright on a wooden board, generously filled with crispy browned strips of chicken, shredded green iceberg lettuce, tomato slices, cucumber slices and red onion rings, with white garlic yogurt sauce drizzled on top, a small bowl of white yogurt sauce beside.",
"MandarinenBowl": "A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, both handles of the dish fully visible, layers visible through the glass; about one quarter eaten from the back corner, an empty clean teaspoon resting inside, plain and simple, nothing on the spoon. Inside: a baked creamy pale yellow cheesecake with a thin golden biscuit crumb base at the bottom visible through the glass, the top completely covered with bright orange mandarin segments, a few mandarin segments and one rectangular butter biscuit beside the dish.",
"Kartoffelgratin": "A rectangular white ceramic baking dish with a creamy potato gratin made of thin overlapping potato slices with a golden brown bubbly cheese crust, one portion lifted out and served on a white plate in front clearly showing the thin creamy potato layers from the side, a sprig of fresh thyme on top, a fork beside.",
"Haferplaetzchen": "Many small round rustic golden brown oatmeal cookies with a rough textured surface of visible oat flakes on a white plate, a stack of five cookies in front and one cookie broken in half showing the soft inside, a few cookies lying on the light wooden table, a small bowl of rolled oats and a cinnamon stick beside.",
"ApfelStreusel": "Square pieces of German apple crumble cheesecake on a wooden board: a thin golden crumb base, a thick creamy white cheesecake layer, thin soft apple slices with cinnamon and golden crumble streusel on top, one piece in front on a small white plate clearly showing the three layers from the side, the rest of the cake blurred behind, a red apple and a fork beside.",
"RoteGruetze": "Four small clear dessert glasses filled with dark red berry compote (German Rote Grütze) with whole cherries, raspberries and red currants visible through the glass, each topped with a thick layer of creamy pale yellow vanilla sauce running down into the red fruit, one glass standing in front with a teaspoon beside it, a few fresh raspberries and red currants on the table.",
"MacCheese": "A round white ceramic baking dish with creamy macaroni and cheese with small browned chicken pieces under a golden brown bubbly melted cheese crust, one portion served on a white plate in front with stretchy melted cheese and creamy elbow macaroni clearly visible, a fork beside."
}""")
T=json.loads(r"""{
"proteinpulver": "A plastic measuring scoop heaped with fine pale cream-colored vanilla protein powder, a little powder spilled beside it, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else, no text, no label.",
"maultaschen": "Three square Swabian filled pasta pockets (German Maultaschen, pale yellow pasta dough squares with a visible green-speckled filling at the cut edge) lying side by side, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else."
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
J=[(P[k]+S,f"g94/{k}_s{sd}.jpg",1024,1280,sd) for k in keys for sd in seeds]
if os.environ.get("TILES","1")=="1": J+=[(T[t],f"tiles/{t}.jpg",1024,1024,7) for t in T]
with ThreadPoolExecutor(6) as ex: list(ex.map(lambda t: gen(*t),J))
print("done")
