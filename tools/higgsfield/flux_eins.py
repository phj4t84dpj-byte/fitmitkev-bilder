# /// script
# dependencies = ["huggingface_hub>=0.30", "pillow"]
# ///
# Vergleichsbild mit unserem normalen Weg (FLUX.1-dev, 1024x1280). env PROMPT, OUT (Pfad im Datensatz), SEEDS (z. B. "1,2")
import io, os
from huggingface_hub import InferenceClient, HfApi
TOK = os.environ["HF_TOKEN"]; cl = InferenceClient(api_key=TOK); api = HfApi(token=TOK)
S = " Homemade, standing on a light wooden table, behind it a plain warm beige wall with soft golden bokeh fairy lights out of focus, cozy warm Christmas market mood, natural soft warm light, shallow depth of field, professional food photography, realistic, appetizing, already served, no hands, no people, no text, nothing else on the table, the upper third of the image is plain warm beige background with a few bokeh lights."
for sd in [int(x) for x in os.environ.get("SEEDS", "1,2").split(",")]:
    img = cl.text_to_image(os.environ["PROMPT"] + S, model="black-forest-labs/FLUX.1-dev", width=1024, height=1280, seed=sd)
    b = io.BytesIO(); img.convert("RGB").save(b, "JPEG", quality=92)
    p = os.environ["OUT"].replace(".jpg", f"_s{sd}.jpg")
    api.upload_file(path_or_fileobj=b.getvalue(), path_in_repo=p, repo_id="kevrsztorm/fitmitkev-bilder", repo_type="dataset"); print("OK", p)
