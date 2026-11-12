# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow"]
# ///
# G92 – Samstag 14.11.2026: FLUX.1-dev-Bilder (1024x1280) fuer 20 Rezepte + neue Kacheln Erdnussmus, Datteln, Ajvar
import io, os, sys, time, json
from huggingface_hub import InferenceClient, HfApi
TOK=os.environ["HF_TOKEN"]; cl=InferenceClient(api_key=TOK); api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
S=" Homemade, standing on a light wooden table, behind it a plain warm beige wall with soft golden bokeh fairy lights out of focus, cozy warm Christmas market mood, natural soft warm light, shallow depth of field, professional food photography, realistic, appetizing, already served, no hands, no people, no text, nothing else on the table, the upper third of the image is plain warm beige background with a few bokeh lights."
P=json.loads(r"""{
"Donauwelle": "A round German Donauwelle cheesecake about 5 cm tall on a white cake stand seen from the side, the top covered with a thin glossy dark chocolate glaze with a wavy fork pattern, one slice cut and placed on a small white plate in front clearly showing the creamy pale vanilla and dark chocolate marbled filling with dark red sour cherries inside from the side, a few sour cherries beside, a fork beside.",
"Hoernchen": "Golden brown crescent-shaped savory rolls made from quark dough on a wooden board, glossy egg-washed tops, one cut in half in front showing pink ham and melted yellow cheese rolled inside, a few more crescents behind, a small dish of butter beside.",
"NougatBowl": "A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, both handles of the dish fully visible, layers visible through the glass; about one quarter eaten from the back corner, an empty clean teaspoon resting inside, plain and simple, nothing on the spoon. Inside: a baked dark chocolate hazelnut cake with a moist dark brown crumb clearly visible through the glass, a glossy melted chocolate center visible where it was eaten, the top sprinkled with a few chopped toasted hazelnuts, a few whole hazelnuts beside the dish.",
"Zwiebelkuchen": "Square slices of German onion tart (Zwiebelkuchen) on a wooden board, a thin golden crust with a thick creamy filling of soft golden onion rings and small pink ham cubes, golden brown baked top with a few caraway seeds, one slice in front on a small white plate showing the creamy onion filling from the side, the rest of the baking tray blurred behind.",
"Marzipan": "A round pale golden marzipan cheesecake about 5 cm tall on a white cake stand seen from the side, the top golden brown and covered with toasted flaked almonds, one slice cut and placed on a small white plate in front showing the creamy pale filling and a thin golden cookie crumb base from the side, a small block of marzipan and a few almonds beside, a fork beside.",
"Reispfanne": "A large black pan with a one-pan dish of tomato rice with browned minced beef and diced red bell pepper, topped with melted golden cheese and chopped green parsley, one portion served on a white plate in front, a wooden spoon in the pan.",
"Vanillekipferl": "Many small crescent-shaped German vanilla cookies (Vanillekipferl) generously dusted with white powdered sugar, arranged on a white plate and a few lying on the light wooden table in front, a vanilla pod beside.",
"PizzaHawaii": "A round homemade thin crust pizza Hawaii on a wooden pizza board, golden crispy edge, red tomato sauce, melted golden cheese, pink ham pieces and yellow pineapple chunks, sprinkled with dried oregano, one slice pulled out slightly with stretchy cheese, a second pizza blurred in the background.",
"LavaCookies": "Several thick round dark chocolate cookies with chocolate chips on a white plate, the cookie in front broken in half with a gooey flowing creamy light brown peanut butter center running out, a small glass jar of peanut butter and a few peanuts beside.",
"Pastitsio": "A rectangular white ceramic baking dish of Greek pastitsio with a thick golden brown baked bechamel top, one square portion cut out and served on a white plate in front clearly showing the layers from the side: tube pasta at the bottom, a layer of rich minced beef tomato sauce and a thick creamy white bechamel layer on top, a fork beside.",
"Dominosteine": "Homemade German Dominosteine: small square chocolate-coated cubes on a white plate, one cube in front cut in half clearly showing three layers from the side: a soft brown gingerbread base, a dark red jelly layer and a pale yellow marzipan layer under the glossy dark chocolate coating, a few more cubes beside, a cinnamon stick beside.",
"Curry": "A white bowl of creamy yellow-orange chicken curry with tender chicken pieces, red bell pepper strips and green peas in coconut curry sauce, next to a portion of fluffy white rice in the same bowl, sprinkled with fresh coriander, a spoon beside, a pan of curry blurred in the background.",
"Rotweinkuchen": "A dark chocolate loaf cake (German red wine cake) on a wooden board with a light dusting of powdered sugar on top, several slices cut in front showing the moist dark brown crumb with small chocolate pieces, one slice on a small white plate, a cinnamon stick beside.",
"Kartoffelsalat": "A white plate with a generous portion of creamy German potato salad with sliced potatoes, diced pickles and fresh chopped chives, two warm pale pink sausages (Wiener Würstchen) beside it, a small dab of mustard, a large glass bowl of potato salad blurred in the background, a fork beside.",
"Butterstollen": "A classic German Christmas stollen loaf thickly dusted with white powdered sugar on a wooden board, several slices cut in front showing the soft pale yellow crumb studded with dark raisins and chopped almonds, one slice on a small white plate, a few raisins and almonds beside.",
"SuessSauer": "A white plate with crispy golden chicken pieces coated in a glossy bright red-orange sweet and sour sauce with chunks of yellow pineapple, red bell pepper and carrot slices, next to a portion of fluffy white rice, sprinkled with sesame seeds and green spring onion rings, chopsticks beside.",
"Crossies": "Many homemade chocolate cornflake clusters (Schoko-Crossies) with toasted flaked almonds on a white plate and a few on the light wooden table in front, glossy dark chocolate, a cinnamon stick beside.",
"KaeseNudeln": "A large pot of creamy one-pot pasta with short fusilli pasta in a light creamy cheese sauce with pink ham strips, sprinkled with chopped green chives, one portion served on a white plate in front, a wooden spoon in the pot.",
"Rumkugeln": "Many small round homemade chocolate rum balls (Rumkugeln) on a white plate, some rolled in white desiccated coconut and some in dark cocoa powder, a few on the light wooden table in front, a small bowl of desiccated coconut beside.",
"Cevapcici": "A white plate with several grilled cevapcici (small finger-shaped grilled minced beef rolls with dark grill marks), crispy golden oven potato wedges, a small bowl of creamy orange-red ajvar yogurt dip and raw red onion rings, a fork beside."
}""")
T=json.loads(r"""{
"erdnussmus": "A small open glass jar filled with smooth creamy light brown peanut butter, a few roasted peanuts beside, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else.",
"datteln": "A small pile of soft glossy brown pitted Medjool dates, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else.",
"ajvar": "A small open glass jar filled with orange-red ajvar (smooth roasted red pepper relish), seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else."
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
J=[(P[k]+S,f"g92/{k}_s{sd}.jpg",1024,1280,sd) for k in keys for sd in seeds]
if os.environ.get("TILES","1")=="1": J+=[(T[t],f"tiles/{t}.jpg",1024,1024,7) for t in T]
with ThreadPoolExecutor(6) as ex: list(ex.map(lambda t: gen(*t),J))
print("done")
