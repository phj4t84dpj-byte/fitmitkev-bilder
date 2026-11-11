# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow"]
# ///
# G90 Nachlauf: Tiramisu-Skyr-Kuchen (ohne falsche Kekse), Kaesespaetzle (kurze Spaetzle statt langer Nudeln), Maulwurf-Bowl (beide Griffe im Bild)
import io, os, sys, time, json
from huggingface_hub import InferenceClient, HfApi
TOK=os.environ["HF_TOKEN"]; cl=InferenceClient(api_key=TOK); api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
S=" Homemade, standing on a light wooden table, behind it a plain warm beige wall with soft golden bokeh fairy lights out of focus, cozy warm Christmas market mood, natural soft warm light, shallow depth of field, professional food photography, realistic, appetizing, already served, no hands, no people, no text, nothing else on the table, the upper third of the image is plain warm beige background with a few bokeh lights."
BOWL="A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, both handles of the dish fully visible, the whole dish centered with empty table space left and right of it, layers visible through the glass; about one quarter eaten from the back corner, an empty clean teaspoon resting inside, plain and simple, nothing on the spoon. "
J0={
"TiramisuSkyrKuchen": ([3,4,5], "A round pale cheesecake about 5 cm tall on a white cake stand seen from the side, the top thickly dusted with dark brown cocoa powder, one slice cut and placed on a small white plate in front showing from the side a thin base of soft pale sponge and a thick creamy white filling with a dark cocoa top, a small white cup of black espresso beside, a fork beside."),
"KaesespaetzleA": ([3,4], "A white ceramic rectangular baking dish with German Käsespätzle: short stubby knobbly pale yellow egg dumpling noodles (Swabian spaetzle, each piece only about three centimeters long) baked with melted stretchy golden cheese, topped with a heap of golden brown crispy roasted onions and chopped green chives, one portion served on a white plate in front showing the short stubby noodles with melted cheese strings, a fork beside."),
"KaesespaetzleB": ([3,4], "A black cast iron skillet filled with German Käsespätzle: short stubby knobbly pale yellow egg dumpling noodles (Swabian spaetzle, each piece only about three centimeters long) in melted stretchy golden cheese, topped with a heap of golden brown crispy roasted onions and chopped green chives, one portion served on a white plate in front showing the short stubby noodles with melted cheese, a fork beside."),
"MaulwurfBowl": ([3,4,5], BOWL+"Inside: a dark chocolate sponge cake base, a layer of banana slices visible through the glass, a thick mound of white cream on top completely covered with dark chocolate cake crumbs and dark chocolate shavings, one banana beside the dish."),
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
J=[(p+S,f"g90/{k}_s{sd}.jpg",1024,1280,sd) for k,(sds,p) in J0.items() for sd in sds]
with ThreadPoolExecutor(5) as ex: list(ex.map(lambda t: gen(*t),J))
print("done")
