# -*- coding: utf-8 -*-
"""Muster „Rezept im Bild“: gewohntes G90-Board + Box „So geht's“ mit 3 kurzen Schritten (nur Muster, nicht für Metricool)."""
import sys, html, re
import rib_render as R
NAVY=R.NAVY; RED=R.RED
STEPS={
 'Lasagne':(470,468,590,['Hack mit Zwiebel und Karotten anbraten, Tomaten dazu, würzen, 10 Min. köcheln.',
                         'Skyr mit Ei verrühren. Soße, Platten und Creme schichten, Mozzarella drauf.',
                         'Bei 180 °C Ober-/Unterhitze 35 Min. backen.']),
 'ZimtstreuselSkyr':(452,392,608,['Mehl, 30 g Erythrit, Zimt und kalte Butter zu Streuseln reiben, ⅓ als Boden in die Form (20 cm) drücken.',
                         'Skyr, Eier, Puddingpulver und 60 g Erythrit verrühren, einfüllen, restliche Streusel drauf.',
                         'Bei 170 °C Ober-/Unterhitze 50 Min. backen, 3 Std. kalt stellen.']),
 'TiramisuSkyrKuchen':(452,442,608,['Löffelbiskuits kurz in Espresso tunken und als Boden in die Form (20 cm) legen.',
                         'Skyr, Eier, Puddingpulver und Erythrit verrühren, auf den Boden füllen.',
                         'Bei 170 °C Ober-/Unterhitze 50 Min. backen, 3 Std. kalt stellen, mit Kakao bestäuben.']),
}
CSS=f"""<style>
.rib{{position:absolute;background:rgba(255,249,240,.90);border-radius:24px;padding:62px 22px 18px 20px;box-shadow:0 8px 24px rgba(40,25,10,.22);border:3px solid rgba(255,255,255,.95)}}
.ribh{{position:absolute;left:22px;top:6px;transform:rotate(-3deg)}}
.ribh div{{font-family:K;font-size:42px;line-height:1.1;white-space:nowrap}}
.ribh .f{{position:relative;color:#fff;z-index:2}}
.ribh .b{{position:absolute;left:0;top:0;color:{NAVY};-webkit-text-stroke:8px {NAVY};text-shadow:3px 4px 0 {NAVY};z-index:1}}
.st{{display:flex;gap:12px;align-items:flex-start;margin-top:9px}}
.st:first-of-type{{margin-top:0}}
.no{{flex:none;width:36px;height:36px;border-radius:50%;background:{RED};color:#fff;font-family:A;font-size:24px;line-height:36px;text-align:center;margin-top:1px}}
.tx2{{font-size:21px;font-weight:600;color:{NAVY};line-height:1.24}}
</style>"""
orig=R.board_html
def board(r,hero,cut):
    h=orig(r,hero,cut)
    left,top,w,steps=STEPS[r['key']]
    st=''.join(f'<div class="st"><div class="no">{i}</div><div class="tx2">{html.escape(re.sub(r'(\d+) (?=cm|Std\.|Min\.|°C|g\b)', '\\1\u00a0', s))}</div></div>' for i,s in enumerate(steps,1))
    box=(f'<div class="rib" style="left:{left}px;top:{top}px;width:{w}px">'
         f'<div class="ribh"><div class="b">So geht\'s:</div><div class="f" style="position:absolute;left:0;top:0">So geht\'s:</div><div style="visibility:hidden">So geht\'s:</div></div>{st}</div>')
    return h.replace('</style>',CSS.replace('<style>','').replace('</style>','')+'</style>',1).replace('</body>',box+'</body>')
R.board_html=board
if __name__=='__main__':
    R.render(sys.argv[1:] or list(STEPS))
