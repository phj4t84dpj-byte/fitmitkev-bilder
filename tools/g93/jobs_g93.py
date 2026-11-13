# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow"]
# ///
# G93 – Sonntag 15.11.2026: FLUX.1-dev-Bilder (1024x1280) fuer 20 Rezepte (keine neuen Kacheln)
import io, os, sys, time, json
from huggingface_hub import InferenceClient, HfApi
TOK=os.environ["HF_TOKEN"]; cl=InferenceClient(api_key=TOK); api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
S=" Homemade, standing on a light wooden table, behind it a plain warm beige wall with soft golden bokeh fairy lights out of focus, cozy warm Christmas market mood, natural soft warm light, shallow depth of field, professional food photography, realistic, appetizing, already served, no hands, no people, no text, nothing else on the table, the upper third of the image is plain warm beige background with a few bokeh lights."
P=json.loads(r"""{
"Hefezopf": "A golden brown braided yeast bread loaf (German Hefezopf, classic three-strand braid) sprinkled with toasted flaked almonds lying on a wooden board, glossy egg-washed crust, two thick slices cut off in front showing the soft fluffy pale yellow crumb, one slice on a small white plate, a small dish of butter beside.",
"Eiersalat": "A white ceramic bowl filled with creamy German egg salad made of chopped hard-boiled eggs in a light creamy white dressing with small diced pickles, generously sprinkled with fresh chopped green chives and a little paprika powder, a spoon in the bowl, two halved hard-boiled eggs and a small bunch of chives lying beside on the table.",
"KalterHund": "A loaf-shaped no-bake chocolate biscuit cake (German Kalter Hund) on a wooden board, several slices cut in front clearly showing many thin horizontal layers alternating pale rectangular butter biscuits and dark chocolate cream from the side, one slice lying flat on a small white plate, a few rectangular butter biscuits lying beside.",
"PizzaSchnecken": "Many round flat spiral pizza rolls (pinwheels) baked golden brown lying on a sheet of baking paper on a wooden board, each with a clearly visible spiral of dough with red tomato sauce, pink ham and melted golden cheese, sprinkled with dried oregano, one roll in front leaning against another showing the spiral, a small bowl of tomato sauce beside.",
"SpekSkyr": "A round pale golden cheesecake about 5 cm tall on a white cake stand seen from the side, smooth golden brown top lightly dusted with cinnamon, a thin brown biscuit crumb base, one slice cut and placed on a small white plate in front showing the creamy pale filling and the thin brown base from the side, three thin flat rectangular brown spiced biscuits (German Spekulatius) with a fine embossed windmill pattern lying flat on the wooden table beside, a cinnamon stick, a fork beside.",
"BamiGoreng": "A large black wok pan with fried thin egg noodles (Bami Goreng) with browned chicken breast strips with seared edges, orange carrot strips, green leek rings, red bell pepper strips and small pieces of yellow scrambled egg, glossy from soy sauce, one portion served in a white bowl in front, chopsticks beside.",
"KaeseSahne": "A round German Käsesahnetorte (cheese cream cake) about 7 cm tall on a white cake stand seen from the side: a thin pale sponge base, a thick layer of firm white quark cream with small orange mandarin segments visible inside, and a thin pale golden sponge layer on top dusted with white powdered sugar, one slice cut and placed on a small white plate in front clearly showing the three layers from the side, a few mandarin segments beside, a fork beside.",
"ZwiebelSahne": "A rectangular white ceramic baking dish with chicken schnitzel fillets baked in a creamy white onion sauce with soft golden onion rings and small pink ham cubes, golden brown melted cheese on top, one portion served on a white plate in front next to a portion of fluffy white rice, a fork beside.",
"ZimtBowl": "A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, both handles of the dish fully visible, layers visible through the glass; about one quarter eaten from the back corner, an empty clean teaspoon resting inside, plain and simple, nothing on the spoon. Inside: a baked golden oat cake with dark brown cinnamon swirls on top and a thin white cream cheese glaze drizzled over it in thin lines, the moist golden crumb with cinnamon swirls visible through the glass, a cinnamon stick beside the dish.",
"HackPfannkuchen": "A rectangular white ceramic baking dish with rolled thin pancakes filled with minced beef and tomato filling lying side by side, topped with red tomato sauce and golden brown melted cheese, two filled pancake rolls served on a white plate in front, one cut open clearly showing the minced beef filling inside, a fork beside.",
"Windbeutel": "Several golden brown choux pastry cream puffs (German Windbeutel) on a white plate, each cut in half horizontally and filled with thick white cream and dark red sour cherries, the golden pastry lids placed on top and lightly dusted with white powdered sugar, one cream puff in front clearly showing the white cream and cherries filling, a few sour cherries lying beside.",
"Handbrot": "Rustic oblong hand-sized stuffed bread rolls (German Handbrot from the Christmas market) on a wooden board, golden brown crust lightly dusted with flour, one bread torn open in front showing lots of melted stretchy golden cheese and pink ham cubes inside, each bread topped with a small spoonful of white sour cream and chopped green chives.",
"PuddingStreusel": "Square pieces of German pudding streusel sheet cake on a wooden board: a thin pale dough base, a thick creamy pale yellow vanilla pudding layer and golden crumble streusel on top, one piece in front on a small white plate clearly showing the three layers from the side, the rest of the baking tray blurred behind, a fork beside.",
"Schlafrock": "Sausages wrapped in golden brown baked dough (German Würstchen im Schlafrock, pigs in a blanket) on a wooden board, the dough wrapped around the middle of each sausage with both sausage ends sticking out, glossy egg-washed and sprinkled with sesame seeds, one cut in half in front showing the sausage and a little melted cheese inside, a small bowl of mustard beside.",
"Waffeln": "A stack of golden brown heart-shaped German waffles on a white plate lightly dusted with white powdered sugar, one whole flower-shaped waffle made of five hearts leaning in front, a black waffle iron blurred in the background, a small sieve with powdered sugar beside.",
"Lahmacun": "Thin round Turkish flatbreads (Lahmacun) with a thin layer of spiced minced meat, tomato and finely chopped red pepper baked on, with crispy browned edges, lying flat on a wooden board, one lahmacun in front topped with fresh green lettuce, tomato slices, red onion rings and parsley and half rolled up, lemon wedges beside.",
"Spritzgebaeck": "Many German piped butter cookies (Spritzgebäck) in S-shapes and short straight sticks with a clearly visible ridged star-nozzle pattern, pale golden, one end of each cookie dipped in glossy dark chocolate, arranged on a white plate and a few lying on the light wooden table in front, a small bowl of melted dark chocolate beside.",
"Tortellini": "A large pan of cheese tortellini in a light creamy white sauce with pink ham strips and green peas, one portion served in a white deep plate in front, sprinkled with coarse black pepper, a fork beside.",
"MandarinenQuark": "Four small clear dessert glasses filled with layers: crumbled golden butter biscuits at the bottom, thick white quark cream with orange mandarin segments, topped with a few bright orange mandarin segments, one glass standing in front with a teaspoon beside it, a few mandarin segments and one rectangular butter biscuit lying on the table.",
"Tortilla": "Golden brown crispy folded flour tortilla quesadillas cut into triangles and stacked on a wooden board, the cut sides clearly showing melted stretchy cheese, browned chicken pieces, red bell pepper cubes and yellow corn inside, a small bowl of white yogurt dip beside."
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
J=[(P[k]+S,f"g93/{k}_s{sd}.jpg",1024,1280,sd) for k in keys for sd in seeds]
if os.environ.get("TILES","0")=="1": J+=[(T[t],f"tiles/{t}.jpg",1024,1024,7) for t in T]
with ThreadPoolExecutor(6) as ex: list(ex.map(lambda t: gen(*t),J))
print("done")
