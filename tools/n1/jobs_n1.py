# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow"]
# ///
# N1 – Nischenseiten (Kuchenherz, Heissluftheld, Omas Kochtopf) Sonntag 15.11.2026: 15 Rezepte + 6 Kacheln
import io, os, sys, time, json
from huggingface_hub import InferenceClient, HfApi
TOK=os.environ["HF_TOKEN"]; cl=InferenceClient(api_key=TOK); api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
S=" Homemade, standing on a light wooden table, behind it a plain warm beige wall with soft golden bokeh fairy lights out of focus, cozy warm Christmas market mood, natural soft warm light, shallow depth of field, professional food photography, realistic, appetizing, already served, no hands, no people, no text, nothing else on the table, the upper third of the image is plain warm beige background with a few bokeh lights."
P={
"KHZimtschnecken": "A rectangular white ceramic baking dish filled with twelve large golden brown cinnamon rolls baked close together, generously covered with thick white cream cheese frosting melting into the swirls, one cinnamon roll lifted out and placed on a small white plate in front showing the soft fluffy spiral with brown cinnamon sugar filling, a cinnamon stick beside.",
"KHBienenstich": "Square pieces of German bee sting cake (Bienenstich) on a wooden board: a fluffy yeast dough base, a thick layer of pale yellow vanilla custard cream and a top layer with a shiny golden caramelized honey almond crust of flaked almonds, one piece in front on a small white plate clearly showing all layers from the side, the rest of the cake blurred behind, a small jar of honey beside.",
"KHKirschStreusel": "Square pieces of German sour cherry crumble sheet cake on a wooden board: a golden yellow sponge base with many dark red sour cherries and a thick layer of golden butter crumble streusel on top, one piece in front on a small white plate clearly showing the cherries and the crumble from the side, the rest of the cake blurred behind, a small bowl of cherries beside.",
"KHVanillekipferl": "Many small crescent-shaped German vanilla cookies (Vanillekipferl), pale golden and heavily dusted with white powdered vanilla sugar, piled on a white plate, a few crescents lying in front on the light wooden table, one broken in half showing the tender pale crumb, a vanilla pod and a small bowl of powdered sugar beside.",
"KHStollen": "A whole traditional German Christmas stollen loaf thickly dusted with white powdered sugar on a wooden board, two thick slices cut and lying in front showing the yeast dough studded with raisins, candied peel and almonds and a round marzipan core in the middle, a few pine sprigs and a star anise beside.",
"HHEierMuffins": "Six golden fluffy egg muffins with visible pieces of pink ham, red bell pepper and melted cheese, sprinkled with chopped chives, sitting in colorful silicone muffin cups on a wooden board, one muffin cut in half in front showing the fluffy egg inside, a black air fryer basket blurred behind.",
"HHGebrannteMandeln": "A paper cone and a small white bowl overflowing with shiny caramelized cinnamon sugar coated almonds (German gebrannte Mandeln), crunchy uneven sugar crust, many almonds scattered on the light wooden table in front, a cinnamon stick and a star anise beside.",
"HHHaehnchenschenkel": "Four crispy golden brown roasted chicken legs with paprika seasoned crackling skin on a white plate, sprinkled with fresh rosemary, a few garlic cloves beside, one leg in front cut open showing juicy white meat, a black air fryer basket blurred behind.",
"HHBratapfel": "Four baked red apples with slightly wrinkled soft skin on a white plate, filled with marzipan, raisins and chopped hazelnuts, their small lids leaning on top, one apple in front cut in half showing the soft baked flesh and filling, a small jug of warm vanilla sauce pouring over it, a cinnamon stick beside.",
"HHCurrywurst": "A white paper tray with sliced grilled German bratwurst covered in thick glossy red curry ketchup sauce and dusted with yellow curry powder, next to a big portion of crispy golden french fries, a small wooden fork stuck in the sausage, on a light wooden table.",
"OKArmeRitter": "A stack of golden brown pan fried French toast slices (German Arme Ritter) coated in cinnamon sugar on a white plate, a small bowl of apple sauce beside, a few more slices behind, a light dusting of cinnamon sugar on the plate.",
"OKRouladen": "A white plate with two German beef roulades (Rinderrouladen) in rich dark brown gravy, one roulade cut in half showing the spiral of beef with bacon, pickle and onion filling, a round potato dumpling and a portion of glossy red braised red cabbage beside, more gravy in a small gravy boat behind.",
"OKErbseneintopf": "A large rustic white soup bowl filled with thick creamy yellow-green German split pea stew with potato cubes, carrot pieces, leek rings and sliced Wiener sausages on top, sprinkled with parsley, a cast iron pot with more stew blurred behind, a slice of rustic bread beside.",
"OKApfelstrudel": "A long golden brown apple strudel dusted with powdered sugar on a wooden board, two thick slices cut and placed on a white plate in front showing thin flaky pastry layers and a juicy filling of apple slices with cinnamon and raisins, warm pale yellow vanilla sauce poured beside the slices on the plate.",
"OKKohlrouladen": "A rustic cast iron braising pan with eight German cabbage rolls (Kohlrouladen) tied with kitchen twine, golden browned pale green cabbage leaves, in a creamy light brown gravy with small crispy bacon cubes, one cabbage roll served on a white plate in front cut open showing the minced meat filling, boiled potatoes beside."
}
T={
"bratwurst": "Four raw pale pink German bratwurst sausages lying side by side, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else.",
"haehnchenschenkel": "Two raw chicken legs (whole chicken thigh with drumstick, pale skin) lying side by side, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else.",
"schaelerbsen": "A small round light wooden bowl filled with dried yellow-green split peas, a few split peas scattered beside it, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else.",
"semmelbroesel": "A small round light wooden bowl filled with fine golden breadcrumbs, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else.",
"speck": "Several thin raw slices of streaky smoked bacon with pink meat and white fat stripes, slightly fanned out, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else.",
"weisskohl": "A whole fresh pale green white cabbage head with one cabbage leaf peeled off lying beside it, seen from the side at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else."
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
keys=[k for k in os.environ.get("KEYS","").split(",") if k] or list(P)
seeds=[int(x) for x in os.environ.get("SEEDS","1,2").split(",")]
J=[(P[k]+S,f"n1/{k}_s{sd}.jpg",1024,1280,sd) for k in keys for sd in seeds]
if os.environ.get("TILES","1")=="1": J+=[(T[t],f"tiles/{t}.jpg",1024,1024,7) for t in T]
with ThreadPoolExecutor(6) as ex: list(ex.map(lambda t: gen(*t),J))
print("done")
