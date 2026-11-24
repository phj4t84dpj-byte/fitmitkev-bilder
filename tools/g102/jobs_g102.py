# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow"]
# ///
# G102 (Mi 25.11.2026): FLUX.1-dev-Bilder (1024x1280) fuer 6 neue Rezepte (3 aus der Klossteig-Reihe) und 6 Wiederholer mit NEUEM Foto (Wiederholer-Test, Gruppe NEU); 1 neue Kachel (kasseler)
import io, os, sys, time, json
from huggingface_hub import InferenceClient, HfApi
TOK=os.environ["HF_TOKEN"]; cl=InferenceClient(api_key=TOK); api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
S=" Homemade, standing on a light wooden table, behind it a plain warm beige wall with soft golden bokeh fairy lights out of focus, cozy warm Christmas market mood, natural soft warm light, shallow depth of field, professional food photography, realistic, appetizing, already served, no hands, no people, no text, nothing else on the table, the upper third of the image is plain warm beige background with a few bokeh lights."
P=json.loads(r"""{
"KlossKasseler": "A round white dinner plate, the whole plate fully visible with empty table space left and right of it, with two thick slices of juicy pink cured smoked pork loin (German Kasseler), smooth pink meat without any breading and without sauce, lying overlapping, next to a generous heap of pale golden braised sauerkraut, and beside it on the same plate exactly four small round pale yellow matte German potato dumplings, each about the size of a golf ball, lying close together in a group, all four clearly visible, a little chopped green parsley on the dumplings.",
"KlossScheiben": "A round white dinner plate, the whole plate fully visible with empty table space left and right of it, with six round golden-brown pan-fried slices cut from a potato dumpling roll, each slice a flat thick disc about as wide as a small orange with a crisp golden crust, arranged overlapping, mixed with small pink diced ham cubes and soft browned onion pieces, on top one sunny-side-up fried egg with a bright yellow yolk, sprinkled with chopped green chives.",
"KlossLauch": "Close-up food photo of a white rectangular ceramic baking dish with two handles, the whole dish fully visible and filling most of the frame, with a little empty table space left and right of it, seen from above at a 45 degree angle. In the dish eight large round pale yellow German potato dumplings, each the size of a tennis ball with a smooth matte surface, sitting side by side in two rows in a creamy white leek sauce with many green and white leek rings and small pink ham cubes, the round shape of every dumpling clearly visible. A light layer of melted cheese with golden brown spots from the oven on top of the dumplings and the sauce, the dumplings still clearly recognizable as round balls.",
"WinterWoelkchen": "A white plate piled high with many small round pale beige soft cookies, each cookie a smooth slightly domed mound with fine cracks, thickly dusted with white powdered sugar and a little brown cinnamon, the bottoms pale golden, a few cookies lying on the table in front of the plate, one cookie broken in half showing the soft light brown crumb inside, two cinnamon sticks lying beside the plate.",
"DoenerKartoffeln": "Close view of a dark baking tray lined with white baking paper, seen from above at a 45 degree angle, filled with many small golden brown crispy roasted potato cubes and browned thin strips of spiced chicken breast, the middle topped with finely shredded green iceberg lettuce, diced fresh red tomatoes and thin red onion rings, generously drizzled with white yogurt garlic sauce in zigzag lines, crispy bare potato cubes clearly visible all around the edge.",
"NudelsalatNacht": "A large clear glass salad bowl filled to the top with creamy pasta salad made of spiral fusilli pasta in a light white yogurt dressing, mixed with green peas, small red bell pepper cubes, small diced pickled gherkins and small pink ham cubes, quartered hard-boiled eggs with yellow yolks arranged on top, sprinkled with chopped green chives. A large serving spoon lies beside the bowl.",
"MilchschnitteBowl": "A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, both handles of the dish fully visible, seen from the front slightly from above, completely full and untouched, the layers clearly visible through the glass: a layer of moist dark chocolate sponge cake at the bottom and a thick layer of smooth white milk cream on top, the smooth top generously dusted with dark cocoa powder, a clean teaspoon lying on the table in front of the dish, plain and simple.",
"Gewuerzkuchen": "Three square pieces of moist dark brown spice sheet cake stacked on a small white plate, each piece covered with a glossy dark chocolate glaze on top, the moist dark brown crumb clearly visible from the side, a few cake crumbs on the plate, two cinnamon sticks lying beside the plate.",
"BlitzKaesekuchen": "One tall slice of baked cheesecake on a small white dessert plate seen from the front at eye level, the cut side facing the camera showing the creamy white smooth filling, a thin golden cookie crumb base at the bottom and a golden-brown top, a small fork lying on the plate, behind it out of focus the rest of the round cheesecake on a wooden board.",
"Zupfkuchen": "A whole round Russian Zupfkuchen cake on a round wooden board seen from above at a 45 degree angle, the top showing a pale yellow baked cheesecake surface with many irregular dark chocolate dough patches scattered over it and a dark chocolate rim, two slices cut and pulled slightly out of the cake showing the thick creamy white cheesecake filling and the thin dark chocolate base.",
"GyrosBowl": "A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, both handles of the dish fully visible, freshly baked, seen from above at a 45 degree angle, completely full and untouched: the top covered with a baked white tzatziki yogurt layer with golden browned melted cheese spots, browned spiced chicken gyros strips with red bell pepper strips and onion peeking out around the edges, white rice visible at the bottom through the glass, a few fresh cucumber slices lying beside the dish.",
"KaeseLauchSuppe": "A deep white soup plate, the whole plate fully visible, seen from above at a 45 degree angle, filled with thick creamy pale yellow cheese and leek soup with plenty of browned minced beef crumbles, many bright green and white leek rings and small soft potato cubes, a little grated cheese melting on top, freshly ground black pepper, a silver spoon lying beside the plate."
}""")
T=json.loads(r"""{
"kasseler": "Three thick slices of pink cured smoked pork loin (German Kasseler) with a thin darker smoked rim, lying overlapping, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else, no plate, no bowl."
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
J=[(P[k]+S,f"g102/{k}_s{sd}.jpg",1024,1280,sd) for k in keys for sd in seeds]
if os.environ.get("TILES","0")=="1": J+=[(T[t],f"tiles/{t}.jpg",1024,1024,7) for t in T]
with ThreadPoolExecutor(6) as ex: list(ex.map(lambda t: gen(*t),J))
print("done")
