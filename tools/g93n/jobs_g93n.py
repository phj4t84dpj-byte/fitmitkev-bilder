# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow"]
# ///
# G93N – Sonntag 15.11.2026: FLUX.1-dev-Bilder (1024x1280) fuer 6 neue Rezepte + Kacheln Haselnussmus, Haselnuss-Waffeln, Karamellkekse, Eisbergsalat
import io, os, sys, time, json
from huggingface_hub import InferenceClient, HfApi
TOK=os.environ["HF_TOKEN"]; cl=InferenceClient(api_key=TOK); api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
S=" Homemade, standing on a light wooden table, behind it a plain warm beige wall with soft golden bokeh fairy lights out of focus, cozy warm Christmas market mood, natural soft warm light, shallow depth of field, professional food photography, realistic, appetizing, already served, no hands, no people, no text, nothing else on the table, the upper third of the image is plain warm beige background with a few bokeh lights."
P={
"HanutaBowl": "A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, both handles of the dish fully visible, layers visible through the glass; about one quarter eaten from the back corner, an empty clean teaspoon resting inside, plain and simple, nothing on the spoon. Inside: a baked moist dark chocolate hazelnut cake with a smooth dark brown top, generously covered with coarsely crumbled thin crispy golden wafer pieces with light brown hazelnut cream between the thin wafer layers, the moist dark chocolate crumb visible through the glass and where it was eaten, two small rectangular golden hazelnut wafer bars and a few whole hazelnuts lying beside the dish.",
"BigMacSalat": "Two tall clear drinking glasses seen from the side at eye level, one in front and one behind, each filled with neat clearly visible horizontal layers from bottom to top: pale pink creamy burger sauce, browned crumbly minced beef, finely diced white onions and green pickle slices, shredded orange cheddar cheese, shredded crisp light green iceberg lettuce, topped with a dollop of pale pink burger sauce and two green pickle slices, a fork beside, a small glass bowl with pickle slices beside.",
"SpekKirschGlas": "Two clear glass tumblers seen from the side at eye level, one in front and one behind, each with a thin layer of brown spiced biscuit crumbs at the bottom, above it thick white vanilla cream with dark red sour cherries and glossy deep red cherry sauce swirled through it, clearly visible through the glass, topped with whole dark red sour cherries in glossy sauce, one thin flat rectangular brown spiced biscuit with an embossed windmill pattern (German Spekulatius) stuck upright into the top of each glass, a spoon beside, a few cherries on the table.",
"BiscoffBowl": "A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, both handles of the dish fully visible, layers visible through the glass; about one quarter eaten from the back corner, an empty clean teaspoon resting inside, plain and simple, nothing on the spoon. Inside: a baked creamy pale golden skyr cake, the top covered with a glossy smooth layer of light caramel brown spiced cookie butter spread, sprinkled with crumbled caramelized biscuit crumbs, the creamy pale crumb visible through the glass and where it was eaten, two plain smooth rectangular caramel brown caramelized biscuits with wavy edges lying beside the dish.",
"BratapfelSpekGlas": "Four clear glass tumblers seen from the side at eye level, one in front and three behind, each with a thin layer of brown spiced biscuit crumbs at the bottom, above it thick white vanilla cream layered with soft golden cinnamon apple cubes and a few raisins, the layers clearly visible through the glass, topped with soft golden cinnamon dusted apple cubes and raisins, one thin flat rectangular brown spiced biscuit with an embossed windmill pattern (German Spekulatius) stuck upright into the top of each glass, a red apple and a cinnamon stick beside, a spoon beside.",
"MilchschnitteBowl": "A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, both handles of the dish fully visible, layers visible through the glass; about one quarter eaten from the back corner, an empty clean teaspoon resting inside, plain and simple, nothing on the spoon. Inside: a thin layer of moist dark chocolate sponge cake at the bottom and a thick layer of smooth white milk cream on top, the top lightly dusted with cocoa powder, the dark brown sponge and the white cream layer clearly visible through the glass and where it was eaten, a small glass jar of golden honey beside the dish."
}
T={
"haselnussmus": "A small round light wooden bowl filled with smooth glossy light brown hazelnut butter, a teaspoon with hazelnut butter beside it and three whole hazelnuts, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else, no text.",
"haselnusswaffeln": "Four small rectangular golden crispy wafer bars stacked crosswise, each made of thin wafer sheets with light brown hazelnut cream layers visible on the cut side, two whole hazelnuts beside, seen from the side at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else, no text, no packaging.",
"karamellkekse": "Four plain smooth rectangular caramel brown caramelized biscuits with wavy edges stacked slightly fanned out, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else, no packaging.",
"eisbergsalat": "A small round light wooden bowl heaped with finely shredded crisp light green iceberg lettuce, seen from above at a slight angle, product photo, soft studio light, isolated on a pure white background, nothing else."
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
seeds=[int(x) for x in os.environ.get("SEEDS","1,2,3").split(",")]
J=[(P[k]+S,f"g93n/{k}_s{sd}.jpg",1024,1280,sd) for k in keys for sd in seeds]
if os.environ.get("TILES","1")=="1": J+=[(T[t],f"tiles/{t}.jpg",1024,1024,7) for t in T]
with ThreadPoolExecutor(6) as ex: list(ex.map(lambda t: gen(*t),J))
print("done")
