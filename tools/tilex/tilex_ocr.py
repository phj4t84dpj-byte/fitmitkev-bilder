# -*- coding: utf-8 -*-
"""Kacheln aus Boards ohne JSON-Rezept (G81–G86): Zutatennamen per OCR aus der Textspalte lesen."""
import numpy as np, json, os, re, sys, glob
from PIL import Image
import pytesseract
from scipy import ndimage as ndi
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from tilex import REPO, OUT, X0, Y0, Y1, HI, norm, extract, merge_to, split_to, cut

AMT=re.compile(r'^(\d|[½¼¾⅓]|ein|eine|etwas|Saft|Abrieb|Prise|Msp)',re.I)

def ocr_rows(im_pil, tx1):
    """liefert Liste (y_top, y_bottom, name) pro Zutat aus der Textspalte"""
    box=im_pil.crop((tx1,Y0,780,Y1))
    # Kontrast: dunkler Text auf hellem Grund -> ok
    data=pytesseract.image_to_data(box,lang='deu',config='--psm 6',output_type=pytesseract.Output.DICT)
    lines={}
    for i,t in enumerate(data['text']):
        if not t.strip() or int(data['conf'][i])<0: continue
        k=(data['block_num'][i],data['par_num'][i],data['line_num'][i])
        l=lines.setdefault(k,dict(words=[],top=10**9,bot=0,h=[]))
        l['words'].append(t); l['top']=min(l['top'],data['top'][i]); l['bot']=max(l['bot'],data['top'][i]+data['height'][i]); l['h'].append(data['height'][i])
    L=sorted(lines.values(),key=lambda l:l['top'])
    rows=[]
    for l in L:
        words=[w for w in l['words'] if re.search(r'[A-Za-zÄÖÜäöüß0-9½¼¾]',w)]
        if not words: continue
        txt=' '.join(words).strip()
        hmed=float(np.median([h for w,h in zip(l['words'],l['h']) if re.search(r'[A-Za-zÄÖÜäöüß0-9]',w)] or [0]))
        is_amt=(hmed>=36 and len(txt)<=14) or (AMT.match(txt) and hmed>=30)
        if is_amt and (not rows or l['top']-rows[-1]['top']>60):
            rows.append(dict(top=l['top']+Y0,bot=l['bot']+Y0,amt=txt,name=[]))
        elif rows:
            w2=[w for w in words if re.search(r'[A-Za-zÄÖÜäöüß]{2,}',w)]
            if w2: rows[-1]['name'].append(' '.join(w2)); rows[-1]['bot']=l['bot']+Y0
    return rows

if __name__=='__main__':
    files=sorted(glob.glob(f'{REPO}/boards/G8[1-6]-*.jpg'))
    log=open(f'{OUT}/../log_ocr.txt','w'); meta=[]
    for f in files:
        base=os.path.basename(f)[:-4]
        res,st=extract(f)
        if res is None: log.write(f'{base}\t{st}\n'); continue
        im,bg,diff,rows,tx1=res
        pil=Image.open(f).convert('RGB')
        orows=ocr_rows(pil,tx1)
        n=len(orows)
        if n<3 or n>8: log.write(f'{base}\tOCR {n} Zeilen\n'); continue
        if len(rows)>n: rows=merge_to(rows,n)
        if len(rows)<n: rows=split_to(rows,n,diff,X0,tx1)
        if len(rows)!=n or any(b-a>300 for a,b,_,_ in rows):
            log.write(f'{base}\tReihen {len(rows)} != OCR {n}\n'); continue
        # Plausibilität: Kachelmitte nahe Textblockmitte
        ok=True
        for row,o in zip(rows,orows):
            cy=(row[0]+row[1])/2; ty=(o['top']+o['bot'])/2
            if abs(cy-ty)>110: ok=False
        if not ok: log.write(f'{base}\tVersatz Kachel/Text\n'); continue
        for i,(row,o) in enumerate(zip(rows,orows)):
            raw=' '.join(o['name']).strip() or o['amt']
            name=norm(raw)
            if not name: continue
            ytop=rows[i-1][1] if i>0 else 0
            ybot=rows[i+1][0] if i+1<len(rows) else im.shape[0]
            t=cut(im,bg,diff,row,tx1=tx1,ytop=ytop,ybot=ybot)
            fn=f'{OUT}/{name}__{base}_{i}.png'; t.save(fn)
            meta.append(dict(name=name,zutat=raw,amt=o['amt'],board=base,i=i,row=row,w=t.width,h=t.height,ocr=True))
        log.write(f'{base}\tok {n}\n')
    json.dump(meta,open(f'{OUT}/../meta_ocr.json','w'),ensure_ascii=False)
    print('crops',len(meta))
