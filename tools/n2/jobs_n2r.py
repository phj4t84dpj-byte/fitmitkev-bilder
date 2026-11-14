# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow"]
# ///
# N2 – Nachlauf: Kaiserschmarrn (zerrupft), Pfannkuchen (dünn), Gyros (nicht paniert), Krustenbraten (aufgepoppte Kruste)
import io, os, time
from huggingface_hub import InferenceClient, HfApi
TOK=os.environ["HF_TOKEN"]; cl=InferenceClient(api_key=TOK); api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
PZ=" Homemade, on a rustic dark brown wooden table with a beige linen cloth with a thin red stripe and a few fir branches, cozy German Christmas kitchen mood, warm soft natural light, shallow depth of field, professional food photography, realistic, appetizing, already served, no hands, no people, no text, no labels. The food is large and fills the lower 60 percent of the image, seen from a slightly elevated angle; the upper 40 percent of the image is a softly blurred warm brown kitchen background."
PH=" The basket is the square pull-out drawer basket of a modern matte black air fryer: the drawer has been pulled out and stands on the table in the lower right, and the black air fryer itself with its round control dial stands directly behind it and is clearly recognizable. Homemade, on a light wooden table, behind it a plain warm beige wall with soft golden bokeh fairy lights out of focus, cozy warm Christmas mood, natural soft warm light, shallow depth of field, professional food photography, realistic, appetizing, no hands, no people, no text, the upper third of the image is plain warm beige background with a few bokeh lights."
P={'OKKaiserschmarrn': ('Z', 'A black cast iron pan full of German Kaiserschmarrn: a fluffy golden pancake torn into many small irregular bite-sized pieces with browned caramelized edges and raisins, heavily dusted with powdered sugar, a portion of the torn pieces on a white plate in front, a small bowl of pale yellow-beige apple sauce beside.'), 'OKPfannkuchen': ('Z', 'Several very thin large golden German crepe-like pancakes with lacy browned spots, each folded into a quarter triangle, overlapping on a white plate, sprinkled with cinnamon sugar, a small bowl of pale yellow-beige apple sauce beside, a black pan behind.'), 'HHGyros': ('H', 'A heap of thinly sliced Greek gyros pork meat strips, not breaded, juicy brown seasoned meat with dark crispy caramelized edges and soft onion strips, in the basket and on a plate in front, a bowl of white tzatziki with grated cucumber and a few red onion rings beside.'), 'HHKrustenbraten': ('H', 'A thick piece of roast pork belly with a very puffed, bubbly, golden crunchy crackling rind like popcorn on top, cut into thick slices showing juicy meat and fat layers under the crackling, on a wooden board in front of the basket, a small bowl of mustard beside.')}
def gen(prompt,path,seed):
    for a in range(3):
        try:
            img=cl.text_to_image(prompt,model="black-forest-labs/FLUX.1-dev",width=1024,height=1280,seed=seed)
            b=io.BytesIO(); img.convert("RGB").save(b,"JPEG",quality=92); b.seek(0)
            api.upload_file(path_or_fileobj=b,path_in_repo=path,repo_id=REPO,repo_type="dataset"); print("ok",path,flush=True); return
        except Exception as e:
            print("retry",path,repr(e)[:200],flush=True); time.sleep(15)
    print("FAIL",path,flush=True)
from concurrent.futures import ThreadPoolExecutor
J=[(p+(PZ if st=="Z" else PH),f"n2/{k}_s{sd}.jpg",sd) for k,(st,p) in P.items() for sd in (3,4,5)]
with ThreadPoolExecutor(6) as ex: list(ex.map(lambda t: gen(*t),J))
print("done")
