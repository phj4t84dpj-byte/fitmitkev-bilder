# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow"]
# ///
# G91 – Donnerstag 12.11.2026: FLUX.1-dev-Bilder (1024x1280) fuer 16 Rezepte + neue Kacheln Banane, Gnocchi, Vollkornbrot
import io, os, sys, time, json
from huggingface_hub import InferenceClient, HfApi
TOK=os.environ["HF_TOKEN"]; cl=InferenceClient(api_key=TOK); api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
S=" Homemade, standing on a light wooden table, behind it a plain warm beige wall with soft golden bokeh fairy lights out of focus, cozy warm Christmas market mood, natural soft warm light, shallow depth of field, professional food photography, realistic, appetizing, already served, no hands, no people, no text, nothing else on the table, the upper third of the image is plain warm beige background with a few bokeh lights."
P=json.loads(r"""{
"MarmorBowl": "A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, both handles of the dish fully visible, layers visible through the glass; about one quarter eaten from the back corner, an empty clean teaspoon resting inside, plain and simple, nothing on the spoon. Inside: a baked marble cake with distinct swirls of light golden vanilla sponge and dark brown chocolate sponge clearly visible through the glass and on the top surface, a light dusting of cocoa powder on top.",
"Pide": "Two boat-shaped Turkish pide flatbreads on baking paper on a wooden board, golden brown crispy dough edges folded up, filled with browned minced beef with diced red bell pepper and onion and crumbled white feta, each with a baked egg with a bright yellow yolk in the center, the pide in front cut into slices.",
"Poffertjes": "A white plate piled high with many small fluffy round Dutch mini pancakes (poffertjes), golden brown on top, generously dusted with white powdered sugar, a small fork stuck in one, a few poffertjes lying on the wooden table in front.",
"OfenOmelett": "A white ceramic rectangular baking dish with a fluffy golden baked oven omelette (frittata) with visible pink ham cubes, red bell pepper pieces and sliced mushrooms, melted golden cheese on top, sprinkled with chopped green chives, one square piece cut and served on a white plate in front showing the fluffy yellow egg inside, a fork beside.",
"Milchreis": "A white ceramic bowl of creamy German rice pudding (Milchreis) seen from the side slightly elevated, thick creamy white short-grain rice pudding generously sprinkled with brown cinnamon, a spoonful of dark red sour cherries in their juice on top at the side, a spoon beside, a second bowl blurred in the background.",
"SmashWrap": "Two folded smash burger tacos on a wooden board: wheat tortillas with a thin crispy seared minced beef patty pressed on, melted orange cheddar cheese, thin onion rings, pickle slices, shredded green lettuce and creamy pink burger sauce, one cut in half showing the layers, a small bowl of pickles beside.",
"HimbeerSkyr": "A round pale vanilla cheesecake about 5 cm tall on a white cake stand seen from the side, the top completely covered with a glossy bright red raspberry glaze layer with a few whole raspberries, one slice cut and placed on a small white plate in front showing the creamy white filling, a thin golden cookie crumb base and the red raspberry layer on top from the side, a few fresh raspberries beside, a fork beside.",
"Champignons": "A small white oval serving dish piled with golden brown pan-fried halved button mushrooms with diced onions, topped with a big dollop of thick white garlic herb sauce and chopped fresh green parsley, a small wooden fork stuck in, a few mushrooms beside the dish.",
"ApfelkuchenBowl": "A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, both handles of the dish fully visible, layers visible through the glass; about one quarter eaten from the back corner, an empty clean teaspoon resting inside, plain and simple, nothing on the spoon. Inside: a baked apple cake with soft golden oat sponge and juicy apple pieces clearly visible through the glass, the top golden brown with toasted flaked almonds and a dusting of cinnamon, a fresh red apple beside the dish.",
"Rouladen": "A white plate with two German beef roulades (Rinderrouladen) in rich dark brown gravy, one cut open showing the spiral filling of onion and pickle inside, served with boiled peeled yellow potatoes and a portion of glossy purple red cabbage, a fork beside, a dark roasting pan with more roulades blurred in the background.",
"FrankfurterKranz": "A round ring-shaped Frankfurter Kranz cake on a white cake stand seen from the side, covered all over with pale vanilla cream and golden brown caramelized chopped hazelnut brittle, small pale cream rosettes on top, one slice cut and placed on a small white plate in front showing three light golden sponge layers with thin red strawberry jam and pale cream from the side, a fork beside.",
"Souvlaki": "A white plate with two grilled chicken souvlaki skewers with golden brown charred edges, a portion of fluffy white rice, a generous dollop of thick white tzatziki with grated cucumber, thin red onion rings and a lemon wedge, a fork beside.",
"LebkuchenBlech": "Square soft German gingerbread slices (Lebkuchen) with a glossy dark chocolate glaze on top, stacked on a white plate, one piece in front broken open showing the soft dark brown spiced crumb, a few whole almonds and a cinnamon stick beside.",
"Crepes": "Thin golden crepes folded into triangles, stacked overlapping on a white plate, generously dusted with cinnamon sugar, one crepe in front partly unfolded, a small bowl of cinnamon sugar and a cinnamon stick beside.",
"Schupfnudeln": "A black cast iron pan with golden pan-fried German finger-shaped noodles (Schupfnudeln, thick finger-shaped dumplings with pointed ends and golden brown roasted spots) mixed with pale yellow sauerkraut and small pink ham cubes, one portion served on a white plate in front, a wooden spoon beside.",
"Plaetzchen": "Homemade cut-out butter cookies in shapes of stars, hearts and Christmas trees with a thin shiny white icing glaze, spread on a white plate and on the light wooden table in front, a metal star cookie cutter beside.",
"Langos": "A round golden brown crispy Hungarian flatbread (langos) with puffy bubbly edges on a white plate, spread with a layer of thick white sour cream and generously topped with grated yellow cheese and a little chopped garlic, one piece torn off in front, a second langos blurred in the background.",
"Eierschecke": "A round German Eierschecke cake on a white cake stand seen from the side: a thin golden shortcrust base, a thick white quark cheesecake layer with a few raisins and a golden yellow custard top layer with a light brown baked surface, one slice cut and placed on a small white plate in front clearly showing the three layers from the side, a fork beside.",
"Gulasch": "A dark rustic pot of rich dark red-brown beef goulash with tender beef chunks and red bell pepper strips, one portion served on a white plate in front with boiled peeled yellow potatoes and a small dollop of thick white yogurt on the goulash, a fork beside."
}""")
T=json.loads(r"""{
"tortilla": "Three round soft wheat flour tortillas stacked and slightly fanned out, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else.",
"rinderrouladen": "Four thin raw beef roulade slices (thin flat wide slices of raw red beef topside) lying slightly overlapping, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else.",
"rotkohl": "A small round light wooden bowl filled with cooked glossy shredded purple red cabbage, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else.",
"sauerkraut": "A small round light wooden bowl filled with pale yellow sauerkraut (finely shredded fermented white cabbage), seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else.",
"milchreis": "A small round light wooden bowl filled with raw uncooked short round grain white pudding rice, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else."
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
J=[(P[k]+S,f"g91/{k}_s{sd}.jpg",1024,1280,sd) for k in keys for sd in seeds]
if os.environ.get("TILES","1")=="1": J+=[(T[t],f"tiles/{t}.jpg",1024,1024,7) for t in T]
with ThreadPoolExecutor(6) as ex: list(ex.map(lambda t: gen(*t),J))
print("done")
