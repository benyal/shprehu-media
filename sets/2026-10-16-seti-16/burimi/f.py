from gen import *
# Fëmija i fqinjit: fletë fletoreje me vija dhe laps; nota e kuqe, pastaj të dyja të barabarta në të gjelbër
INK = 'var(--ink)'
def tx(i, k, h, sub, top=250):
    return f'''<div class="sl" style="left:{i*1080}px"><div class="hd" style="top:{top}px;color:{INK}">
<div class="k" style="color:#B04A2C">{k}</div><div class="h">{h}</div><div class="sub" style="color:var(--ink-2)">{sub}</div></div></div>'''
def em(t): return f'<em style="color:var(--green)">{t}</em>'
paper = f'<rect width="{W}" height="1920" fill="#FBF7EC"/>' + ''.join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#D8E3E6" stroke-width="3"/>' for y in range(120, 1920, 76)) + ''.join(f'<line x1="{i*1080+70}" y1="0" x2="{i*1080+70}" y2="1920" stroke="#E5A8A0" stroke-width="4"/>' for i in range(6))
def circ(cx, cy, r, color, txt, fs=190, w=12, op=1):
    return f'<g opacity="{op}"><path d="M{cx-r} {cy-10}C{cx-r} {cy-r-30} {cx+r+20} {cy-r} {cx+r+14} {cy+8}C{cx+r+6} {cy+r+30} {cx-r+10} {cy+r+20} {cx-r-10} {cy+10}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round"/><text x="{cx}" y="{cy+fs*0.34:.0f}" text-anchor="middle" font-family="Fraunces" font-weight="600" font-size="{fs}" fill="{color}">{txt}</text></g>'
obj = []
RED, GRY, GRN = '#C2412D', '#8A8073', '#3F6259'
# s1: dhjeta e fqinjit me laps të kuq
obj.append(circ(1080+640, 1290, 190, RED, '10'))
obj.append(f'<text x="{1080+640}" y="{1290+270}" text-anchor="middle" font-family="Fraunces" font-style="italic" font-size="52" fill="{RED}">fëmija i fqinjit</text>')
# s2: një 7 i vogël, i lapsit
obj.append(circ(2160+400, 1330, 120, GRY, '7', 130, 9))
obj.append(f'<text x="{2160+400}" y="{1330+210}" text-anchor="middle" font-family="Fraunces" font-style="italic" font-size="46" fill="{GRY}">ti</text>')
# s3: shumë „10“ të zbehta, si zëra
import random
random.seed(7)
for _ in range(14):
    x = 3240 + random.randint(120, 960); y = random.randint(1080, 1700); sz = random.randint(70, 150)
    obj.append(f'<text x="{x}" y="{y}" font-family="Fraunces" font-weight="600" font-size="{sz}" fill="{RED}" opacity="{random.uniform(.12,.3):.2f}" transform="rotate({random.randint(-16,16)} {x} {y})">10</text>')
# s4: të dyja në të gjelbër, të barabarta
obj.append(circ(4320+330, 1330, 140, GRN, '10', 150, 10))
obj.append(circ(4320+700, 1330, 140, GRN, '7', 150, 10))
obj.append(f'<text x="{4320+515}" y="{1330+250}" text-anchor="middle" font-family="Fraunces" font-style="italic" font-size="50" fill="{GRN}">të dyja vlejnë</text>')
s = []
s.append(f'''<div class="sl" style="left:0"><div class="hd" style="color:{INK}"><div class="k" style="color:#B04A2C">Në çdo lagje shqiptare</div>
<div class="h" style="font-size:98px;margin-top:34px">Kishte një fëmijë që na e përmendnin <em style="color:var(--green)">çdo ditë.</em></div></div>
<div class="hint" style="color:var(--green)">Rrëshqit {arrow('#3F6259')}</div></div>''')
s.append(tx(1, 'Ai fëmijë', '„Shiko të fqinjit.“', 'Ai i mbaroi detyrat. Ai s’bërtet. Ai e mori dhjetën.'))
s.append(tx(2, 'Dhe ti e dëgjoje', 'Të thoshin se ishte ' + em('për të mirën tënde.'), 'Mësove një gjë pa e kuptuar: që „mirë“ nuk mjaftonte kurrë.'))
s.append(tx(3, 'Sot, si i rritur', 'Ende e dëgjon atë zë ' + em('kur krahason veten.'), 'Në Instagram, në punë, në dasma. Fqinji ka ndërruar fytyrë, zëri është i njëjti.'))
s.append(tx(4, 'Një e vërtetë e qetë', 'Ai fëmijë ' + em('nuk ishte kurrë gara jote.'), 'Askush s’e di sa i kushtoi ajo dhjeta. As ti s’e ke parë çfarë mbante brenda.'))
s.append(end_slide(5, 'l', 'Nëse e mban ende atë krahasim, <em>thuaje pa emër.</em>', 'Në Shprehu flet me dikë që të dëgjon, pa të krahasuar me askënd. Falas, në shqip.'))
html = HEAD + f'''</style></head><body><div class="pano"><svg style="position:absolute;left:0;top:0;z-index:1" width="{W}" height="1920">{paper}{''.join(obj)}</svg>{''.join(s)}</div></body></html>'''
open('f.html', 'w').write(html)
