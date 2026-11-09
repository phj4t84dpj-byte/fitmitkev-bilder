# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow"]
# ///
import io, os, sys, time
from huggingface_hub import InferenceClient, HfApi
TOK=os.environ["HF_TOKEN"]; cl=InferenceClient(api_key=TOK); api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
S=' Homemade, standing on a light wooden table, behind it a plain warm beige wall with soft golden bokeh fairy lights out of focus, cozy warm Christmas market mood, natural soft warm light, shallow depth of field, professional food photography, realistic, appetizing, already served, no hands, no people, no text, nothing else on the table, the upper third of the image is plain warm beige background with a few bokeh lights.'
P={
"BratapfelPorridge": "A white bowl of creamy warm oatmeal porridge topped with cinnamon-stewed apple cubes, raisins, a dollop of white skyr and toasted almond flakes, seen from the side slightly elevated, a spoon beside, half an apple and a cinnamon stick beside the bowl.",
"KoernerBroetchen": "Homemade rustic seeded bread rolls on baking paper on a light wooden board, golden brown crust covered with sesame seeds, pumpkin seeds and oat flakes, one roll in front cut open showing a soft light crumb with seeds, a small dish of cream cheese beside.",
"Kaiserschmarrn": "A white plate with fluffy golden torn pieces of Kaiserschmarrn, a shredded Austrian pancake with raisins, dusted with white powdered sweetener, a small bowl of apple sauce beside, a fork beside.",
"LaugenBrezeln": "Homemade golden chestnut-brown glossy pretzels with coarse salt on baking paper on a light wooden board, warm bakery color not dark, one pretzel in front torn open showing a soft white crumb, a small dish of butter beside.",
"Apfeltaschen": "Homemade golden baked apple turnovers, half-moon shaped hand pies with crimped edges and a glossy egg-washed crust, on baking paper on a light wooden board, one in front cut open showing soft apple cubes with cinnamon and raisins inside, half an apple beside.",
"KaeseSchinkenWaffeln": "A stack of three golden savory waffles with visible pieces of ham and melted cheese and chopped chives on a white plate, one waffle broken to show the fluffy inside, a small bowl of cream cheese dip beside.",
"KirschStreuselBowl": "A single portion baked in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, layers visible through the glass; about one quarter eaten from the back corner, an empty clean teaspoon resting inside, empty counter behind, plain and simple, nothing on the spoon. Inside: a soft golden oat base, a layer of dark red sour cherries in creamy pudding, topped with golden crumble streusel, a few cherries beside the dish.",
"KaeseLauchSuppe": "A single white bowl of creamy pale yellow cheese and leek soup with minced beef and green leek rings visible, grated cheese on top, a spoon beside, nothing else on the table, a piece of bread beside the bowl.",
"KokosMandelBowl": "A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, layers visible through the glass; about one quarter eaten from the back corner, an empty clean teaspoon resting inside, empty counter behind, plain and simple, nothing on the spoon. Inside: a pale golden almond sponge base, a thick white coconut cream layer, topped with toasted shredded coconut and a few whole almonds, a few shredded coconut flakes beside the dish.",
"Hackbraten": "A sliced juicy homemade meatloaf on a white plate with two slices cut showing the tender inside, a scoop of creamy mashed potatoes beside, dark brown gravy poured over, chopped parsley on top, a fork beside, the rest of the meatloaf blurred in the background.",
"MandarinenSchmand": "A rectangular sheet cake slice of mandarin sour cream cake on a small white plate seen from the side, showing a thin golden base, bright orange mandarin segments and a thick creamy white set topping, the rest of the sheet cake on a board in the background, a few mandarin segments beside.",
"GefuelltePaprika": "A white ceramic baking dish with halved red bell peppers stuffed with minced beef and rice, baked in red tomato sauce, topped with melted golden cheese, one stuffed pepper half served on a white plate in front with tomato sauce, a fork beside.",
"EierlikoerSkyrKuchen": "A round pale yellow cheesecake on a white cake stand seen from the side, one slice cut and placed on a small white plate in front showing the creamy smooth pale yellow filling from the side, a thin drizzle of yellow egg liqueur on top, a small glass of egg liqueur beside the plate.",
"HaehnchenJaegersosse": "A white plate with pan-seared chicken breast slices (no crust, no breading) covered in a creamy light brown mushroom sauce with sliced mushrooms, served with pasta, chopped parsley on top, a fork beside, the pan blurred in the background.",
"Zupfkuchen": "A round Russian Zupfkuchen cake on a white cake stand seen from the side, one slice cut and placed on a small white plate in front showing from the side a thin dark chocolate base, a thick creamy white cheesecake filling and dark chocolate dough crumbs scattered on top, a fork beside.",
"CurrywurstAuflauf": "A white ceramic rectangular baking dish with a casserole of sliced potatoes and pieces of sausage in a glossy red-orange curry tomato sauce, melted cheese on top, one portion served on a white plate in front, a sprinkle of curry powder on top, a fork beside.",
"MohnStreuselkuchen": "A square slice of poppy seed streusel sheet cake on a small white plate seen from the side, showing a thin golden base, a thick dark grey-black poppy seed filling and golden crumble streusel on top, the rest of the sheet cake on a board in the background, a fork beside.",
"ZuercherGeschnetzeltes": "A white plate with creamy chicken strips in a light mushroom cream sauce with sliced mushrooms, served next to a mound of white rice, chopped parsley on top, a fork beside, the pan blurred in the background.",
"ZimtschneckenSkyrKuchen": "A round pale cheesecake on a white cake stand seen from the side with a visible cinnamon swirl pattern on top and white cream cheese glaze drizzled over it, one slice cut and placed on a small white plate in front showing the creamy filling with a cinnamon swirl from the side, a cinnamon stick beside.",
"Senfeier": "A white plate with halved hard-boiled eggs in a creamy pale yellow mustard sauce next to a scoop of mashed potatoes, chopped parsley on top, a fork beside, the sauce pot blurred in the background."
}
T={
"kokosraspel": "A small round light wooden bowl filled with white desiccated shredded coconut flakes, seen from a 45 degree angle, product photo, soft studio light, isolated on a pure white background, nothing else.",
"eierlikoer": "A small clear glass filled with thick creamy pale yellow egg liqueur (advocaat), seen from a 45 degree angle, product photo, soft studio light, isolated on a pure white background, nothing else."
}
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
J=[(P[k]+S,f"g88/{k}_s{sd}.jpg",1024,1280,sd) for k in keys for sd in seeds]
if os.environ.get("TILES","1")=="1": J+=[(T[t],f"tiles/{t}.jpg",1024,1024,7) for t in T]
with ThreadPoolExecutor(6) as ex: list(ex.map(lambda t: gen(*t),J))
print("done")
