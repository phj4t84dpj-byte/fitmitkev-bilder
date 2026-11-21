# Mosaik (5 x 1104 x 1472) in Einzelbilder schneiden: python3 schneiden.py <blob-kennung> name0 name1 ...
import sys, glob
from PIL import Image
k=sys.argv[1]; names=sys.argv[2:]
f=glob.glob(f'/root/.claude/projects/-home-claude/62a14d94-6bfc-5e5c-b2da-15988fbe030e/tool-results/mcp-Hugging_Face_Spaces-blob-*-{k}.jpg')[0]
im=Image.open(f); assert im.size==(1104*len(names),1472), im.size
for i,n in enumerate(names): im.crop((i*1104,0,(i+1)*1104,1472)).save(f'roh/{n}.jpg',quality=95)
print('ok',names)
