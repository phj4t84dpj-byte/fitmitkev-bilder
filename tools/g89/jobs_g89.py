# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow"]
# ///
# G89 – Mittwoch 11.11.2026: FLUX.1-dev-Bilder (1024x1280) fuer 20 Rezepte + neue Kachel Loeffelbiskuit
import io, os, sys, time
from huggingface_hub import InferenceClient, HfApi
TOK=os.environ["HF_TOKEN"]; cl=InferenceClient(api_key=TOK); api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
S=" Homemade, standing on a light wooden table, behind it a plain warm beige wall with soft golden bokeh fairy lights out of focus, cozy warm Christmas market mood, natural soft warm light, shallow depth of field, professional food photography, realistic, appetizing, already served, no hands, no people, no text, nothing else on the table, the upper third of the image is plain warm beige background with a few bokeh lights."
P={
"NusseckenOats": "Two glass jars with overnight oats seen from the side at eye level, creamy light brown hazelnut oats with skyr, each topped with a spoonful of orange apricot jam, roasted chopped hazelnuts and dark chocolate shavings, a few whole hazelnuts and a small piece of dark chocolate beside the jars, a spoon beside.",
"Kaesebroetchen": "Homemade round cheese bread rolls on baking paper on a light wooden board, golden brown crust with a crispy melted golden cheese topping, one roll in front cut open showing a soft white fluffy crumb, a small dish of butter beside.",
"Weckmann": "Three homemade golden baked sweet bread men (German Weckmann: soft sweet bread figures shaped like a simple person with a round head, two short arms and two legs) lying side by side on baking paper on a light wooden board, shiny golden egg-washed crust, each with two raisins as eyes and three raisins as buttons down the body, a few raisins beside.",
"Bauernfruehstueck": "A black cast iron skillet with a German farmer's breakfast: golden fried potato slices with diced ham and onions, bound with set scrambled egg like a thick rustic omelette, sprinkled with chopped chives, two pickled gherkins on a small white plate beside, a fork beside.",
"Mutzen": "A white bowl piled high with small golden brown irregular rustic dough nuggets (German Mutzen, bite-sized baked quark doughnut pieces), generously dusted with white powdered sugar and a little cinnamon, one piece in front broken open showing a fluffy light inside, a little powdered sugar dusted on the wooden table, a cinnamon stick beside.",
"PizzaMuffins": "Homemade savory pizza muffins on a light wooden board, golden brown tops with melted cheese, visible pieces of red bell pepper, yellow corn and salami, one muffin in front broken open showing the fluffy savory inside with corn and pepper pieces, a small dish of red tomato dip beside.",
"Zimtschnecken": "Homemade cinnamon rolls baked close together in a white rectangular baking dish, golden brown spirals with clearly visible dark cinnamon swirls, drizzled with white cream cheese glaze, one cinnamon roll lifted out onto a small white plate in front showing the swirl, a cinnamon stick beside.",
"KoenigsbergerKlopse": "A white deep plate with three tender pale boiled meatballs (German Königsberger Klopse, not browned) in a creamy white sauce with small green capers, served next to boiled peeled yellow potatoes, a fork beside, the pot blurred in the background.",
"ZitronenBowl": "A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, both handles of the dish fully visible, layers visible through the glass; about one quarter eaten from the back corner, an empty clean teaspoon resting inside, plain and simple, nothing on the spoon. Inside: a golden yellow fluffy lemon sponge cake covered with a thick white lemon icing glaze and a little fine yellow lemon zest on top, half a lemon beside the dish.",
"Schinkennudeln": "A large pan with German ham noodles: short pasta with diced pink ham bound with set egg, topped with melted golden cheese and chopped parsley, one portion served on a white plate in front, a fork beside.",
"KokosMandelTiramisu": "A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, both handles of the dish fully visible, layers visible through the glass; about one quarter eaten from the back corner, an empty clean teaspoon resting inside, plain and simple, nothing on the spoon. Inside: a tiramisu with two layers of pale ladyfinger sponge biscuits alternating with thick white coconut cream, the top covered with toasted golden shredded coconut and a few whole almonds, a few shredded coconut flakes and two ladyfinger biscuits beside the dish.",
"GebratenerReis": "A black wok pan with Asian fried rice with golden seared chicken breast cubes with browned edges clearly visible, scrambled egg pieces, green peas, small orange carrot cubes and sliced green spring onions, one portion served in a white bowl in front, wooden chopsticks beside.",
"BlitzKaesekuchen": "A round crustless baked cheesecake about 5 cm tall on a white cake stand seen from the side, smooth golden-brown top, one slice cut and placed on a small white plate in front showing the creamy white smooth filling from the side, a fork beside.",
"Frikadellen": "A white plate with two juicy browned oven-baked meat patties (German Frikadellen) covered with a creamy light brown mushroom sauce with sliced mushrooms, nothing else on the plate, a fork beside, a pan with more meat patties in mushroom sauce blurred in the background.",
"Gewuerzkuchen": "A rectangular dark brown spice sheet cake on a baking tray lined with baking paper, covered with a glossy dark chocolate glaze, cut into squares, one square piece lifted out onto a small white plate in front showing the moist dark brown crumb from the side, a cinnamon stick and a star anise beside.",
"Reibekuchen": "A white plate with three crispy golden brown potato pancakes (German Reibekuchen, flat round grated potato fritters with crispy lacy edges) slightly overlapping, a small white bowl of pale yellow apple sauce beside the plate, a fork beside.",
"Zimtsterne": "Homemade cinnamon star cookies (German Zimtsterne): brown six-pointed star-shaped cookies, each covered with a smooth white icing glaze on top, piled on a white plate, a few stars lying on the wooden table in front, two cinnamon sticks beside.",
"GyrosAuflauf": "A white ceramic rectangular baking dish with a gyros casserole: sliced potatoes, seasoned browned chicken strips, red bell pepper strips and onion rings, topped with melted golden cheese, one portion served on a white plate in front with a dollop of white tzatziki with grated cucumber on the side, a fork beside.",
"SchokoKaesekuchen": "A round dark chocolate cheesecake about 5 cm tall on a white cake stand seen from the side, with a thin light brown cookie crumb base and dark chocolate drops on top, one slice cut and placed on a small white plate in front showing the creamy dark brown chocolate filling and the thin base from the side, a few chocolate drops beside, a fork beside.",
"Flammkuchen": "A thin crispy oval flatbread tart (Alsatian Flammkuchen) on a wooden board, very thin crust with browned crispy edges, topped with white cream, thin red onion rings, strips of pink ham and sliced mushrooms, one piece cut off in front, a pizza cutter beside."
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
J=[(P[k]+S,f"g89/{k}_s{sd}.jpg",1024,1280,sd) for k in keys for sd in seeds]
if os.environ.get("TILES","1")=="1": J+=[(T[t],f"tiles/{t}.jpg",1024,1024,7) for t in T]
with ThreadPoolExecutor(6) as ex: list(ex.map(lambda t: gen(*t),J))
print("done")
