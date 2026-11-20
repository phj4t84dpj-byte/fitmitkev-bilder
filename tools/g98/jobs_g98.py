# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow"]
# ///
# G98 (Sa 21.11.2026): FLUX.1-dev-Bilder (1024x1280) fuer die 4 neuen Fast-Food-Klassiker im hellen Standard-Look
import io, os, sys, time, json
from huggingface_hub import InferenceClient, HfApi
TOK=os.environ["HF_TOKEN"]; cl=InferenceClient(api_key=TOK); api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
S=" Homemade, standing on a light wooden table, behind it a plain warm beige wall with soft golden bokeh fairy lights out of focus, cozy warm Christmas market mood, natural soft warm light, shallow depth of field, professional food photography, realistic, appetizing, already served, no hands, no people, no text, nothing else on the table, the upper third of the image is plain warm beige background with a few bokeh lights."
P=json.loads(r"""{
"CrispyBurger": "Two homemade crispy chicken burgers on a wooden board: toasted sesame burger buns, in each a thick golden brown crunchy cornflake-crusted chicken breast fillet, crisp green iceberg lettuce, a red tomato slice and creamy pale pink burger sauce, one burger cut in half and turned to the camera showing the juicy white chicken inside the crunchy golden crust, a small white bowl of pale pink sauce beside.",
"OfenTacos": "A rectangular white ceramic baking dish with eight small soft flour tortillas folded into taco shape, standing upright side by side in a row, baked until the edges are golden and crispy, each taco filled with browned ground beef in a little tomato sauce, yellow sweet corn and golden melted cheese, topped with shredded green iceberg lettuce and a small spoonful of white yogurt cream, two tacos served on a white plate in front.",
"SchokoShake": "Two tall classic milkshake glasses filled to the top with thick creamy chocolate brown milkshake with a light foamy surface, sprinkled with fine dark chocolate shavings and a little cocoa powder, a paper straw in each glass, a few pieces of dark chocolate and one whole banana lying beside the glasses.",
"Churros": "A pile of homemade golden brown baked churros on brown baking paper on a wooden board: straight pastry sticks about ten centimeters long, piped through a star nozzle, each with deep parallel ridges running along its whole length, coated in fine cinnamon sugar, a small white bowl of glossy dark chocolate dipping sauce beside, one churro standing in the bowl dipped halfway into the chocolate sauce."
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
J=[(P[k]+S,f"g98/{k}_s{sd}.jpg",1024,1280,sd) for k in keys for sd in seeds]
with ThreadPoolExecutor(6) as ex: list(ex.map(lambda t: gen(*t),J))
print("done")
