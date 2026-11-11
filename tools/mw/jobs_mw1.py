# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow"]
# ///
# Mehrwert-Post 1 "So viel sind 100 kcal": 6 Portionsfotos (FLUX.1-dev, 1024x1024)
import io, os, time
from huggingface_hub import InferenceClient, HfApi
TOK=os.environ["HF_TOKEN"]; cl=InferenceClient(api_key=TOK); api=HfApi(token=TOK); REPO="kevrsztorm/fitmitkev-bilder"
S=" Seen from slightly above at a 45 degree angle, standing on a light wooden table, plain warm beige background softly out of focus, natural soft warm light, professional food photography, realistic, appetizing, simple and clean, the plate fully visible in the center with space around it."
P={
"erdbeeren":"A large white bowl filled to the brim with about twenty fresh whole red strawberries with green leaves.",
"huettenkaese":"A white bowl filled with a generous portion of creamy white cottage cheese with small curds, a teaspoon beside the bowl.",
"kartoffeln":"A small white plate with two small boiled new potatoes in their thin light brown skins, one potato cut in half showing the matte pale yellow floury inside, a little coarse salt and chopped parsley on top.",
"chips":"A small white plate with a small handful of golden potato chips, about ten chips.",
"schokolade":"A small white plate with exactly three small squares of milk chocolate broken from a bar.",
"gummibaerchen":"A small white plate with a small heap of about twelve colorful fruit gummy bears.",
}
def gen(prompt,path,seed):
    for a in range(3):
        try:
            img=cl.text_to_image(prompt,model="black-forest-labs/FLUX.1-dev",width=1024,height=1024,seed=seed)
            b=io.BytesIO(); img.convert("RGB").save(b,"JPEG",quality=92); b.seek(0)
            api.upload_file(path_or_fileobj=b,path_in_repo=path,repo_id=REPO,repo_type="dataset"); print("ok",path,flush=True); return
        except Exception as e:
            print("retry",path,repr(e)[:200],flush=True); time.sleep(15)
    print("FAIL",path,flush=True)
from concurrent.futures import ThreadPoolExecutor
seeds=[int(x) for x in os.environ.get("SEEDS","1").split(",")]
KEYS=os.environ.get("KEYS","").split(",") if os.environ.get("KEYS") else list(P)
J=[(p+S,f"mw/100kcal_{k}_s{sd}.jpg",sd) for k,p in P.items() if k in KEYS for sd in seeds]
with ThreadPoolExecutor(6) as ex: list(ex.map(lambda t: gen(*t),J))
print("done")
