from gen import *
# Statusi: rrethi i statusit (si story), një pamje që ngushtohet nga slide-i në slide; fundi: rrethi i plotë i mbyllur me një mesazh
INK = 'var(--ink)'
def tx(i, k, h, sub, top=250):
    return f'''<div class="sl" style="left:{i*1080}px"><div class="hd" style="top:{top}px;color:{INK}">
<div class="k" style="color:#B04A2C">{k}</div><div class="h">{h}</div><div class="sub" style="color:var(--ink-2)">{sub}</div></div></div>'''
def em(t): return f'<em style="color:var(--green)">{t}</em>'
GRN = '#3F6259'
def ring(cx, cy, r, segs=1, color=GRN, w=16, gap=0.12):
    import math
    if segs == 1:
        return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" stroke-width="{w}"/>'
    out = []
    arc = 2 * math.pi / segs
    for i in range(segs):
        a0 = i * arc + gap / 2; a1 = (i + 1) * arc - gap / 2
        x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        out.append(f'<path d="M{x0:.1f} {y0:.1f}A{r} {r} 0 0 1 {x1:.1f} {y1:.1f}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round"/>')
    return ''.join(out)
def avatar(cx, cy, r, fill='#C9D8D0'):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"/><circle cx="{cx}" cy="{cy-r*0.15:.0f}" r="{r*0.33:.0f}" fill="#FAF7F1"/><path d="M{cx-r*0.62:.0f} {cy+r*0.72:.0f}q{r*0.62:.0f} -{r*0.75:.0f} {r*1.24:.0f} 0" fill="#FAF7F1"/>'
def bubble(x, y, w, h, txt, fill=GRN, col='#FAF7F1', fs=46, tail='l'):
    t = f'<path d="M{x+10} {y+h-24}l-34 34 62 -14z" fill="{fill}"/>' if tail == 'l' else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="34" fill="{fill}"/>{t}<text x="{x+34}" y="{y+h/2+fs*0.34:.0f}" font-family="Inter" font-weight="500" font-size="{fs}" fill="{col}">{txt}</text>'
obj = []
cy = 1350
# s0: rrethi i statusit te hook-u
obj.append(avatar(540, cy, 150) + ring(540, cy, 190, 4))
obj.append(f'<text x="540" y="{cy+300}" text-anchor="middle" font-family="Fraunces" font-style="italic" font-size="50" fill="#8A8073">statusi i tij, 21:13</text>')
# s1: pesë ditë radhazi, e shikon çdo ditë
for j, d in enumerate(['E hënë', 'E martë', 'E mërkurë', 'E enjte', 'E premte']):
    x = 1080 + 150 + j * 170
    obj.append(avatar(x, cy, 52) + ring(x, cy, 70, 1, GRN, 8))
    obj.append(f'<text x="{x}" y="{cy+130}" text-anchor="middle" font-family="Inter" font-weight="500" font-size="22" fill="#8A8073">{d[:4]}.</text>')
obj.append(f'<text x="{1080+540}" y="{cy+240}" text-anchor="middle" font-family="Fraunces" font-style="italic" font-size="50" fill="#8A8073">e shikon. çdo ditë.</text>')
# s2: katër versione të një „Hej“ që fshihen
for j, (tt, op) in enumerate([('Hej, si je?', .35), ('Përshëndetje! Kohë…', .5), ('Ke kohë të flasim?', .7), ('Hej', 1)]):
    obj.append(f'<g opacity="{op}">' + bubble(2160+150, 1060+j*130, 620 if j < 3 else 220, 98, tt, '#E9F0EC', '#2E4A43', 44, 'n') + '</g>')
obj.append(f'<rect x="{2160+150}" y="{1060+4*130+20}" width="4" height="56" fill="{GRN}"/>')
# s3: dy rrathë, dy telefona të heshtur, me vijë të ndërprerë mes tyre
obj.append(avatar(3240+280, cy, 110) + ring(3240+280, cy, 145, 1, '#C9B894', 10))
obj.append(avatar(3240+800, cy, 110, '#E5D2B0') + ring(3240+800, cy, 145, 1, '#C9B894', 10))
obj.append(f'<line x1="{3240+450}" y1="{cy}" x2="{3240+630}" y2="{cy}" stroke="#B9AE96" stroke-width="8" stroke-dasharray="4 22" stroke-linecap="round"/>')
# s4: një mesazh që del: „Hej, m’u kujtove.“
obj.append(avatar(4320+250, cy+40, 100) + ring(4320+250, cy+40, 134, 4))
obj.append(bubble(4320+400, cy-90, 560, 150, 'Hej, m’u kujtove.', GRN, '#FAF7F1', 50))
obj.append(f'<text x="{4320+680}" y="{cy+130}" text-anchor="middle" font-family="Inter" font-weight="500" font-size="30" fill="#8A8073">dërguar</text>')
s = []
s.append(f'''<div class="sl" style="left:0"><div class="hd" style="color:{INK}"><div class="k" style="color:#B04A2C">Çdo mbrëmje, 21:13</div>
<div class="h" style="font-size:98px;margin-top:34px">E sheh statusin e tij. <em style="color:var(--green)">S’i shkruan kurrë.</em></div></div>
<div class="hint" style="color:var(--green)">Rrëshqit {arrow('#3F6259')}</div></div>''')
s.append(tx(1, 'Dikur ishit miq', 'Dikur i shkruaje çdo ditë. Tani ' + em('vetëm i shikon statuset.'), 'Një rreth i gjelbër. Një prekje. Dhe një „mos, do të mendojë“.'))
s.append(tx(2, 'Pse nuk i shkruan', '„Do të duket çudi.“ ' + em('„Po sikur të mos kujtohet?“'), 'Mendon katër versione të një „hej“. Asnjë s’dërgohet.'))
s.append(tx(3, 'Ndërkohë', 'Edhe ai mund të ' + em('ta shohë tëndin.'), 'Ndoshta pret që ta bësh ti të parin. Dy njerëz që e kanë mungesën, dy telefona të heshtur.'))
s.append(tx(4, 'Një ide e vogël', 'Një „hej, m’u kujtove“ ' + em('s’ka kushtuar kurrë shumë.'), 'Ose thuaje fillimisht këtu, pa emër, që ta gjesh fjalinë e duhur.'))
s.append(end_slide(5, 'l', 'Para se t’i shkruash atij, <em>thuaje këtu.</em>', 'Në Shprehu flet pa emër me dikë që të dëgjon. Falas, në shqip.'))
bg = 'linear-gradient(90deg,#F6EFE2 0%,#F1E7D3 50%,#F6EFE2 100%)'
html = HEAD + f'''</style></head><body><div class="pano" style="background:{bg}"><svg style="position:absolute;left:0;top:0;z-index:1" width="{W}" height="1920">{''.join(obj)}</svg>{''.join(s)}</div></body></html>'''
open('s.html', 'w').write(html)
