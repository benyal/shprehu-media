from gen import *
# Autobusi i së dielës: perëndim që bëhet natë, autobusi ecën përgjatë rrugës nga slide-i në slide
def tx(i, clock, k, h, sub, dark):
    c = '#F5EFE4' if dark else 'var(--ink)'
    cc = 'var(--gold-soft)' if dark else '#B04A2C'
    m = 'rgba(250,247,241,.85)' if dark else 'var(--ink-2)'
    return f'''<div class="sl" style="left:{i*1080}px"><div class="hd" style="color:{c}">
<div class="clock" style="color:{cc};font-size:120px">{clock}</div><div class="k" style="margin-top:30px;color:{'var(--sage)' if dark else 'var(--green)'}">{k}</div>
<div class="h">{h}</div><div class="sub" style="color:{m}">{sub}</div></div></div>'''
def em(t, dark): return f'<em style="color:{"var(--gold-soft)" if dark else "var(--green)"}">{t}</em>'
bg = 'linear-gradient(90deg,#F4DDB0 0%,#E9B97A 18%,#C98A6A 34%,#4A5F6E 52%,#26384A 70%,#17222E 100%)'
stars = ''.join(f'<circle cx="{3300+int((i*397)%3000)}" cy="{80+int((i*211)%820)}" r="{3+(i%3)}" fill="#FAF7F1" opacity="{.3+(i%4)*.15:.2f}"/>' for i in range(80))
road_y = 1500
def bus(x, lit=True):
    win = ''.join(f'<rect x="{x+60+i*92}" y="{road_y-250}" width="70" height="78" rx="10" fill="{"#F2D58B" if lit else "#3a4a57"}"/>' for i in range(5))
    return (f'<rect x="{x}" y="{road_y-290}" width="520" height="230" rx="34" fill="#3F6259"/><rect x="{x}" y="{road_y-150}" width="520" height="22" fill="#2E4A43"/>'
            f'{win}<circle cx="{x+120}" cy="{road_y-56}" r="46" fill="#17222E"/><circle cx="{x+120}" cy="{road_y-56}" r="20" fill="#8A8073"/>'
            f'<circle cx="{x+400}" cy="{road_y-56}" r="46" fill="#17222E"/><circle cx="{x+400}" cy="{road_y-56}" r="20" fill="#8A8073"/>')
def qese(x, y):
    return (f'<path d="M{x} {y}h150l-14 190h-122z" fill="#F7F1E3" stroke="#CFC4AC" stroke-width="5"/>'
            f'<path d="M{x+30} {y}q45-90 90 0" fill="none" stroke="#CFC4AC" stroke-width="9" stroke-linecap="round"/>'
            f'<circle cx="{x+76}" cy="{y+90}" r="26" fill="#D6A24C" opacity=".85"/>')
svg = f'''<svg style="position:absolute;left:0;top:0;z-index:1" width="{W}" height="1920">
{stars}
<circle cx="900" cy="980" r="150" fill="#E8B96C" opacity=".95"/><circle cx="900" cy="980" r="240" fill="#E8B96C" opacity=".16"/>
<circle cx="6290" cy="250" r="80" fill="#F2EBD8"/><circle cx="6338" cy="224" r="72" fill="#1C2B38"/>
<path d="M0 1380C700 1320 1300 1420 2000 1360S3300 1300 4000 1380S5400 1330 6480 1390V1920H0Z" fill="#2A3D4C" opacity=".75"/>
<rect x="0" y="{road_y}" width="{W}" height="420" fill="#1F2B36"/>
<line x1="0" y1="{road_y+190}" x2="{W}" y2="{road_y+190}" stroke="#E8B96C" stroke-width="10" stroke-dasharray="90 70" opacity=".8"/>
{bus(300)}{bus(1080+260)}{bus(2160+380)}{bus(3240+200,True)}{bus(4320+330,True)}
{qese(1080+180, road_y+120)}{qese(2160+110, road_y+120)}
</svg>'''
s = []
s.append(f'''<div class="sl" style="left:0"><div class="hd" style="color:var(--ink)"><div class="k" style="color:#B04A2C">E diel, ora 16:40</div>
<div class="h" style="font-size:98px;margin-top:34px">Autobusi i së dielës ka <em style="color:#8A4A2C">një heshtje të vetën.</em></div></div><div class="hint" style="color:#6B3F22;top:1060px">Rrëshqit {arrow('#6B3F22')}</div></div>''')
s.append(tx(1, '16:40', 'Ke ikur nga shtëpia', 'Nëna të futi një qese. ' + em('Nuk e pyete çfarë ka brenda.', False), 'Byrek, djathë, dy mollë. Dhe një „kur të mbërrish, më shkruaj“.', False))
s.append(tx(2, '17:55', 'Rruga', 'Dritaret errësohen. ' + em('Edhe mendja.', False), 'Të gjithë shikojnë jashtë ose vënë kufjet. Askush s’flet. Secili po lë diçka pas.', False))
s.append(tx(3, '19:10', 'Qyteti', 'Të pret një dhomë me ' + em('dritë të ndezur dhe askënd.', True), 'Qesja e nënës ende mban ngrohtësinë. Ti ende s’i ke thënë që të mungon.', True))
s.append(tx(4, '22:40', 'Dhe mesazhi', '„Mbërrita mirë.“ Dy fjalë që ' + em('mbajnë shumë më tepër.', True), 'Ata që ikin për shkollë, punë ose jetë e njohin këtë të dielë. Nuk është dobësi.', True))
s.append(end_slide(5, 'd', 'Nëse të mungon dikush dhe s’ia thua, <em>thuaje këtu.</em>', 'Në Shprehu flet pa emër me dikë që të dëgjon. Falas, në shqip.'))
html = HEAD + f'''</style></head><body><div class="pano" style="background:{bg}">{svg}{''.join(s)}</div></body></html>'''
open('a.html', 'w').write(html)
