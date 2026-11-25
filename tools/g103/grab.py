# Kopiert angehängte Hugging-Face-Blobs (hf_fs attach) unter dem Rezeptnamen nach raw/.
# WICHTIG: Zuordnung nur über die Blob-Kennung aus der Tool-Ausgabe (Name=Kennung) – die Dateinamen sortieren NICHT in Aufruf-Reihenfolge.
import sys, os, glob, shutil
from PIL import Image
TR='/root/.claude/projects/-home-claude/62a14d94-6bfc-5e5c-b2da-15988fbe030e/tool-results'
D=os.path.dirname(os.path.abspath(__file__))
for a in sys.argv[1:]:
    name,bid=a.split('=')
    f=glob.glob(f'{TR}/mcp-Hugging_Face_Spaces-blob-*-{bid}.*'); assert len(f)==1,(a,f)
    dst=f'{D}/raw/{name}.jpg'; shutil.copy(f[0],dst); print(name, Image.open(dst).size, os.path.basename(f[0]))
