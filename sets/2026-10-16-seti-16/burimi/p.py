from gen import *
# Pastrimi në mes të natës: nata e thellë, flluska sapuni që shtohen dhe rriten, ora në qoshe; në fund ato ngrihen drejt hënës
def tx(i, clock, k, h, sub):
    return f'''<div class="sl" style="left:{i*1080}px"><div class="hd" style="color:#F5EFE4">
<div class="clock" style="color:var(--gold-soft);font-size:120px">{clock}</div><div class="k" style="margin-top:30px;color:var(--sage)">{k}</div>
<div class="h">{h}</div><div class="sub" style="color:rgba(250,247,241,.85)">{sub}</div></div></div>'''
def em(t): return f'<em style="color:var(--gold-soft)">{t}</em>'
import random
random.seed(11)
stars = ''.join(f'<circle cx="{int((i*733)%W)}" cy="{60+int((i*307)%700)}" r="{2+(i%3)}" fill="#FAF7F1" opacity="{.2+(i%4)*.12:.2f}"/>' for i in range(90))
def bubble(cx, cy, r, op=.5):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#8FB8A8" opacity="{op*0.35:.2f}" stroke="#CFE3DA" stroke-width="3" stroke-opacity="{op:.2f}"/>'
            f'<circle cx="{cx-r*0.35:.0f}" cy="{cy-r*0.35:.0f}" r="{max(r*0.18,3):.0f}" fill="#FAF7F1" opacity="{op*0.8:.2f}"/>')
obj = []
# numri i flluskave rritet në çdo slide
counts = [3, 7, 14, 24, 36]
for i, n in enumerate(counts):
    for _ in range(n):
        cx = i*1080 + random.randint(60, 1020)
        cy = random.randint(1080, 1820)
        r = random.randint(18, 70)
        obj.append(bubble(cx, cy, r, random.uniform(.35, .85)))
# lavamani: një gotë dhe një pjatë te slide-i 1
obj.append('<g transform="translate(1080,0)"><rect x="150" y="1460" width="150" height="190" rx="14" fill="#CFE3DA" opacity=".35" stroke="#CFE3DA" stroke-width="5"/><ellipse cx="640" cy="1630" rx="230" ry="46" fill="#F5EFE4" opacity=".55"/></g>')
# slide-i i fundit: flluska që ngjiten drejt hënës
for _ in range(16):
    obj.append(bubble(5400 + random.randint(40, 1040), random.randint(1300, 1800), random.randint(14, 44), .5))
svg = f'''<svg style="position:absolute;left:0;top:0;z-index:1" width="{W}" height="1920">{stars}
<circle cx="{5400+850}" cy="300" r="80" fill="#F2EBD8"/><circle cx="{5400+898}" cy="274" r="72" fill="#16241F"/>
{''.join(obj)}</svg>'''
s = []
s.append(f'''<div class="sl" style="left:0"><div class="hd" style="color:#F5EFE4"><div class="k" style="color:var(--sage)">Ora 01:12, s’të zë gjumi</div>
<div class="h" style="font-size:98px;margin-top:34px">Pastrimi i orës 2 të natës <em style="color:var(--gold-soft)">s’është pastërti.</em></div></div><div class="hint" style="color:var(--gold-soft)">Rrëshqit {arrow('#E8B96C')}</div></div>''')
s.append(tx(1, '01:12', 'Fillon me një gotë', 'Ke larë një gotë. ' + em('Pastaj enët e tjera.'), 'S’e kishe planifikuar. Duart kërkonin diçka për të bërë.'))
s.append(tx(2, '01:48', 'Pastaj', 'Ke rregulluar një raft që s’e kishte parë askush ' + em('prej muajsh.'), 'Dollapi i këpucëve. Sirtari me kabllo. Çdo gjë gjen vendin e vet.'))
s.append(tx(3, '02:26', 'Shtëpia shkëlqen', 'Por ' + em('diçka brenda s’gjen vend.'), 'Kur mendja s’ka ku të ulet, trupi kërkon rregull jashtë.'))
s.append(tx(4, '02:40', 'Mos ia mbyll vetes', 'S’je i çuditshëm. ' + em('Po e mban një ditë të rëndë me duart.'), 'Shumë njerëz e bëjnë këtë natën dhe pak e thonë: duart punojnë kur mendja s’mund të flasë.'))
s.append(end_slide(5, 'd', 'Nëse mendja s’ka vend, <em>lëre këtu një fjali.</em>', 'Në Shprehu flet pa emër me dikë që të dëgjon. Falas, në shqip.'))
html = HEAD + f'''</style></head><body><div class="pano" style="background:linear-gradient(90deg,#1B2A24 0%,#162620 50%,#13201B 100%)">{svg}{''.join(s)}</div></body></html>'''
open('p.html', 'w').write(html)
