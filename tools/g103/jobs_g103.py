# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow"]
# ///
# G103 (Do 26.11.2026): FLUX.1-dev-Bilder (1024x1280) fuer 6 neue Rezepte (3 aus der Klossteig-Reihe) und 7 Wiederholer mit NEUEM Foto (Wiederholer-Test, Gruppe NEU); 2 neue Kacheln (hirschgulasch, preiselbeeren)
import io, os, sys, time, json
from huggingface_hub import InferenceClient, HfApi
TOK=os.environ["HF_TOKEN"]; cl=InferenceClient(api_key=TOK); api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
S=" Homemade, standing on a light wooden table, behind it a plain warm beige wall with soft golden bokeh fairy lights out of focus, cozy warm Christmas market mood, natural soft warm light, shallow depth of field, professional food photography, realistic, appetizing, already served, no hands, no people, no text, nothing else on the table, the upper third of the image is plain warm beige background with a few bokeh lights."
P=json.loads(r"""{
"KlossHirsch": "A round white dinner plate, the whole plate fully visible with empty table space left and right of it, with a generous portion of dark brown braised venison goulash: tender chunks of dark meat without any breading in a glossy dark brown gravy, a small spoonful of bright red lingonberry jam on top of the meat, next to it a heap of glossy dark purple-red braised red cabbage, and beside it on the same plate exactly four small round pale yellow matte German potato dumplings, each about the size of a golf ball, lying close together in a group, all four clearly visible.",
"KlossPilz": "A round white dinner plate, the whole plate fully visible with empty table space left and right of it, with exactly four small round pale yellow matte German potato dumplings, each about the size of a golf ball, lying close together in a group, all four clearly visible, lying in the middle of the plate, generously surrounded and half covered by a creamy light beige mushroom cream sauce with very many sliced golden-browned button mushrooms and soft onion pieces, sprinkled with plenty of fresh chopped green parsley, no meat on the plate.",
"KlossFrikadellen": "A round white dinner plate, the whole plate fully visible with empty table space left and right of it, with two plump round browned German meat patties (Frikadellen) made of minced beef, with a browned seared surface, without any breading, partly covered with a glossy brown onion gravy with many soft golden-brown onion strips, and beside it on the same plate exactly four small round pale yellow matte German potato dumplings, each about the size of a golf ball, lying close together in a group, all four clearly visible, a little chopped green parsley on the dumplings.",
"Schneewittchen": "Two square pieces of German Schneewittchen sheet cake on a small white plate seen from the side at eye level, the cut side facing the camera showing clearly separated layers: a marbled light and dark chocolate sponge base with dark red sour cherries baked into it, a thick layer of smooth pale yellow vanilla cream on top, and a thin layer of dark chocolate with a wavy pattern made with a fork on the very top, the rest of the sheet cake on a baking tray blurred in the background, a small cake fork beside the plate.",
"JapanKaesekuchen": "A tall round fluffy Japanese cotton cheesecake on a white cake plate seen from the front at eye level, very tall and airy with straight smooth pale golden sides and an evenly golden-brown top lightly dusted with white powdered sugar, one wedge cut out and lying on a small white plate in front showing a very airy, soft, pale yellow, fine and spongy crumb, a lemon half beside the plate.",
"ToastHawaii": "A white plate with two slices of golden toasted whole grain toast bread, each topped with a slice of pink cooked ham, one round yellow pineapple ring and a slice of melted golden-brown bubbling cheese flowing over the edges, the pineapple ring shape visible under the melted cheese, sprinkled with a little paprika powder and chopped green chives, nothing else on the toast, a knife and fork beside the plate.",
"MandarinenSchmand": "Several square pieces of mandarin sour cream sheet cake on a rectangular white platter seen from above at a 45 degree angle, each piece with a thin golden sponge base, a thick creamy white smooth set topping and bright orange mandarin segments arranged in neat rows on and in the topping, the cut edges clearly showing the layers, a few loose mandarin segments on the table beside the platter.",
"BratapfelSkyrKuchen": "Two slices of crustless baked apple cheesecake on a small white plate seen from the front at eye level, the cut side facing the camera showing a thin cookie crumb base and a tall creamy pale filling with soft apple cubes, raisins and swirls of cinnamon, toasted golden almond flakes on top, a small cake fork on the plate, a red apple and a cinnamon stick lying beside the plate.",
"Apfeltaschen": "Six golden baked apple turnovers arranged in a circle on a round white plate seen from above at a 45 degree angle, half-moon shaped hand pies with fork-crimped edges and a glossy golden egg-washed crust, the one in front broken in half showing a filling of soft apple cubes with cinnamon and raisins, a fresh red apple lying beside the plate.",
"Fruehstuecksbroetchen": "A round woven bread basket lined with a white linen napkin, filled with homemade round bread rolls with a golden brown crust and one long slash on top, some rolls topped with blue-black poppy seeds and some with golden sesame seeds, one roll cut in half lying on the table in front of the basket showing a soft white fluffy crumb.",
"GnocchiAuflauf": "Close-up of a white rectangular ceramic baking dish with a freshly baked gnocchi casserole seen from above at a 45 degree angle, the dish fully visible: bubbling golden brown melted mozzarella cheese on top, small potato gnocchi and red tomato minced beef sauce with red bell pepper pieces peeking out between the cheese, a serving spoon lifting one portion out of the corner with stretchy melted cheese.",
"CordonBleu": "Two golden crispy breaded chicken cordon bleu lying on a white plate, the front one cut through the middle showing layers of white chicken, pink ham and melted cheese flowing out of the center, next to a few boiled peeled yellow potatoes, a fork and knife beside the plate.",
"LasagneSuppe": "A deep white soup plate seen from above at a 45 degree angle, the whole plate fully visible, filled with chunky rich red tomato and minced beef soup with many wavy broken lasagna pasta sheets, a spoonful of white cream cheese melting in the middle, melted grated cheese and a few fresh green basil leaves on top, a spoon lying beside the plate."
}""")
T=json.loads(r"""{
"hirschgulasch": "A heap of raw dark red venison goulash meat cubes, lean deer meat cut into bite-sized chunks, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else, no plate, no bowl.",
"preiselbeeren": "A small open glass jar filled with bright red lingonberry jam with whole small red lingonberries, a small heap of the jam in front, product photo, soft studio light, isolated on a pure white background, nothing else, no label, no text."
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
J=[(P[k]+S,f"g103/{k}_s{sd}.jpg",1024,1280,sd) for k in keys for sd in seeds]
if os.environ.get("TILES","0")=="1": J+=[(T[t],f"tiles/{t}.jpg",1024,1024,7) for t in T]
with ThreadPoolExecutor(6) as ex: list(ex.map(lambda t: gen(*t),J))
print("done")
