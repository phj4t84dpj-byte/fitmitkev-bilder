# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow"]
# ///
import io, os, time
from huggingface_hub import InferenceClient, HfApi
TOK=os.environ["HF_TOKEN"]; cl=InferenceClient(api_key=TOK); api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
S=', centered, seen from slightly above, isolated on a pure white background, soft even studio light, photorealistic product photo, clean, nothing else, no text, no labels.'
P={
"backpulver": "A small heap of fine white baking powder in a small round light wooden bowl",
"bruehe": "A small white ceramic bowl of clear golden beef broth with a spoon",
"gurke": "One whole fresh green cucumber with a few cucumber slices next to it",
"gurken": "Three small pickled gherkins, one sliced",
"gyrosgewuerz": "A small heap of reddish-brown gyros spice mix with visible oregano flakes in a small round light wooden bowl",
"hack": "A mound of raw lean minced beef in a small white ceramic bowl",
"haehnchen": "Two raw chicken breast fillets, pale pink, on a white surface",
"haferflocken": "A small heap of rolled oats in a small round light wooden bowl",
"haselnuesse": "A small heap of finely ground hazelnuts with a few whole hazelnuts in a small round light wooden bowl",
"kartoffeln": "Three raw yellow potatoes, one cut in half",
"ketchup": "A small white ceramic bowl of red tomato ketchup next to a small bowl of yellow mustard",
"kochschinken": "Two slices of pale pink cooked ham, rolled, on a white surface",
"lasagneplatten": "A small stack of dry rectangular lasagna pasta sheets",
"mandelblaettchen": "A small heap of sliced almond flakes in a small round light wooden bowl",
"milch": "A small glass of milk next to a small glass milk bottle",
"natron": "A small heap of fine white baking soda powder in a small round light wooden bowl",
"nudeln": "A small heap of dry spiral pasta (fusilli) in a small round light wooden bowl",
"oregano": "A small heap of dried oregano leaves with a fresh oregano sprig in a small round light wooden bowl",
"paprika": "One whole red bell pepper with a few red pepper strips next to it",
"puddingpulver": "A small heap of pale yellow vanilla custard powder with a vanilla pod in a small round light wooden bowl",
"quark": "Thick white quark (curd cheese) in a small white ceramic bowl with a spoon",
"reibekaese": "A small heap of grated light yellow cheese in a small round light wooden bowl",
"reis": "A small heap of raw white long grain rice in a small round light wooden bowl",
"rosinen": "A small heap of dark raisins in a small round light wooden bowl",
"salami": "A few thin slices of poultry salami, slightly fanned out",
"salz": "A small heap of coarse white sea salt in a small round light wooden bowl",
"senf": "A small white ceramic bowl of yellow mustard with a small spoon",
"sesam": "A small heap of white sesame seeds in a small round light wooden bowl",
"spekulatius": "A small stack of brown speculoos cookies with embossed pattern, one leaning in front",
"tomaten": "A small white ceramic bowl of smooth red strained tomato passata with a spoon, two fresh tomatoes beside",
"tomatenmark": "A small white ceramic bowl of thick dark red tomato paste with a small spoon",
"vanille": "Two vanilla pods and a small glass bottle of vanilla extract",
"wasser": "A clear glass of water on a white surface",
"zwiebel": "One whole brown onion with one onion half next to it"
}
def gen(k,p):
    for a in range(3):
        try:
            img=cl.text_to_image(p+S,model="black-forest-labs/FLUX.1-schnell",width=768,height=768,seed=7)
            b=io.BytesIO(); img.convert("RGB").save(b,"JPEG",quality=94); b.seek(0)
            api.upload_file(path_or_fileobj=b,path_in_repo=f"kb/t_{k}.jpg",repo_id=REPO,repo_type="dataset"); print("ok",k,flush=True); return
        except Exception as e:
            print("retry",k,repr(e)[:200],flush=True); time.sleep(15)
    print("FAIL",k,flush=True)
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(5) as ex: list(ex.map(lambda kv: gen(*kv),P.items()))
print("done")
