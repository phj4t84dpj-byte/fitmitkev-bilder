# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow"]
# ///
import io, os, sys, time
from huggingface_hub import InferenceClient, HfApi
TOK=os.environ["HF_TOKEN"]; cl=InferenceClient(api_key=TOK); api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
S=' Homemade, light white marble kitchen counter, light grey wall, natural soft daylight, shallow depth of field, professional food photography, realistic, appetizing, already served, no hands, no people, no text, nothing else on the counter.'
P={
"SpekOats": "Two glass jars with overnight oats seen from the side at eye level, creamy oats with skyr, topped with grated apple, cinnamon and crumbled speculoos cookies, a whole speculoos cookie leaning against the glass, a spoon beside.",
"Quarkbroetchen": "Homemade round quark bread rolls on baking paper on a light wooden board, golden brown crust with a cross cut on top sprinkled with oat flakes, one roll in front cut open showing a soft white fluffy crumb, a small dish of butter beside.",
"ZimtschneckenPancakes": "A white plate with a stack of four golden fluffy pancakes with a cinnamon swirl pattern on top, drizzled with white cream cheese glaze, dusted with cinnamon, a cinnamon stick beside, a fork beside.",
"Pizzabroetchen": "Homemade pizza rolls on baking paper on a light wooden board: small round bread rolls topped with melted golden cheese, slices of poultry salami and diced red pepper, one in front torn open showing a soft crumb and melted cheese, a small bowl of herb dip beside.",
"ApfelQuarkbaellchen": "Homemade golden-brown baked quark balls rolled in cinnamon on a white plate, one in front broken in half showing small soft apple pieces inside the fluffy dough, half an apple and a cinnamon stick beside.",
"LasagneSuppe": "A white bowl of lasagna soup: rich red tomato and minced beef soup with broken lasagna pasta sheets, a dollop of white cream cheese melting in the middle, grated cheese and fresh basil leaves on top, a spoon beside, a pot blurred in the background.",
"NusseckenBowl": "A single portion baked in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, layers visible through the glass; about one quarter eaten from the back corner, an empty clean teaspoon resting inside, empty counter behind. No whipped cream, nothing on the spoon. Inside: a soft golden oat base topped with a crunchy baked hazelnut and almond flake layer, drizzled with dark chocolate, a few hazelnuts beside the dish.",
"CordonBleuAuflauf": "A white ceramic rectangular baking dish with a casserole of sliced potatoes, chicken pieces and strips of ham in a creamy pale sauce, covered with a golden bubbly melted cheese crust, one portion already served on a white plate in front showing the layers from the side, nothing above the dish.",
"BratapfelSkyrKuchen": "A round cheesecake on a white cake stand seen from the side, one slice cut and placed on a small white plate in front showing the creamy pale filling from the side, a crustless cheesecake with soft apple pieces, raisins and cinnamon baked into the creamy filling and toasted almond flakes on top, half an apple and a cinnamon stick beside the plate.",
"GyrosBowl": "A single portion baked in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, layers visible through the glass; about one quarter eaten from the back corner, an empty clean teaspoon resting inside, empty counter behind. No whipped cream, nothing on the spoon. Inside: rice at the bottom, seared spiced chicken gyros strips with red pepper and onion, topped with a baked white tzatziki-skyr layer with lightly browned cheese, a few cucumber slices beside the dish.",
"BienenstichBowl": "A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, layers visible through the glass: a golden cake base, a thick pale yellow vanilla pudding cream layer and a crunchy caramelized honey almond flake topping; about one quarter eaten from the back corner, an empty clean teaspoon resting inside, empty counter behind. No whipped cream, nothing on the spoon.",
"CheeseburgerAuflauf": "A white ceramic rectangular baking dish with a cheeseburger pasta bake: pasta and crumbled browned minced beef in tomato sauce under a golden melted cheese crust, topped with pickle slices and a drizzle of pale burger sauce, one portion already served on a white plate in front, nothing above the dish.",
"SchwarzwaelderSkyr": "A round cake on a white cake stand seen from the side, one slice cut and placed on a small white plate in front showing the layers from the side: a dark chocolate base, dark red sour cherries, a thick white creamy layer and dark chocolate shavings on top, a few cherries beside the plate.",
"LaugenKnoten": "Homemade pretzel knots (Laugenknoten) on baking paper on a light wooden board: knotted soft rolls with a glossy chestnut-brown lye crust, coarse salt, sesame and a golden baked melted cheese crust on top, one in front torn open showing a soft white crumb, warm bakery color, not black.",
"BrownieKaesekuchen": "A round brownie cheesecake on a white cake stand seen from the side, one slice cut and placed on a small white plate in front showing the layers from the side: a dark fudgy chocolate brownie base and a creamy pale cheesecake top with chocolate marbling, a few dark chocolate pieces beside the plate."
}
def gen(prompt,path,model,seed):
    for a in range(3):
        try:
            img=cl.text_to_image(prompt,model=model,width=1024,height=1280,seed=seed)
            b=io.BytesIO(); img.convert("RGB").save(b,"JPEG",quality=92); b.seek(0)
            api.upload_file(path_or_fileobj=b,path_in_repo=path,repo_id=REPO,repo_type="dataset"); print("ok",path,flush=True); return
        except Exception as e:
            print("retry",path,repr(e)[:200],flush=True); time.sleep(15)
    print("FAIL",path,flush=True)
from concurrent.futures import ThreadPoolExecutor
keys=sys.argv[1:] or list(P)
seed=int(os.environ.get("SEED","23")); v=os.environ.get("V","1")
T=[(P[k]+S,f"g87/{k}_v{v}.jpg","black-forest-labs/FLUX.1-dev",seed) for k in keys]
with ThreadPoolExecutor(6) as ex: list(ex.map(lambda t: gen(*t),T))
print("done")
