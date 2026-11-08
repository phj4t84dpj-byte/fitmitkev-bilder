# -*- coding: utf-8 -*-
"""Einzelne Kacheln aus G81–G86-Boards (ohne JSON-Rezept) per Textblock-Erkennung + OCR holen."""
import sys,os,re; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from tilex import *
from bytext import text_blocks, rows_from_blocks, ocr_block
WANT={'G84-GyrosPfanne':['gurke','gyros'],'G81-CheeseburgerBowl':['gurken','tomatenmark'],'G83-GyrosNudelauflauf':['gurke','gyros'],
      'G86-GyrosReisauflauf':['gyros'],'G86-CheeseburgerWraps':['gurken'],'G85-HaehnchenBurger':['gurken']}
for b,keys in WANT.items():
    f=f'{REPO}/boards/{b}.jpg'
    res,st=extract(f); im,bg,diff,rows,tx1=res
    pil=Image.open(f).convert('RGB')
    bl=text_blocks(im,tx1); rws=rows_from_blocks(diff,bl,tx1)
    for i,(blk,row) in enumerate(zip(bl,rws)):
        if row is None: continue
        amt,name=ocr_block(pil,blk,tx1); nl=name.lower()
        if any(k in nl for k in keys):
            ytop=rws[i-1][1] if i>0 and rws[i-1] else 0
            ybot=rws[i+1][0] if i+1<len(rws) and rws[i+1] else im.shape[0]
            t=cut(im,bg,diff,row,tx1=tx1,ytop=ytop,ybot=ybot)
            nm=norm(re.sub(r'\(.*','',name).split('+')[0])
            t.save(f'{OUT}/{nm}__{b}_{i}.png'); print(b,i,amt,name,'->',nm,t.size)
