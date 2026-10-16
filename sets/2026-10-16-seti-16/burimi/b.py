from gen import *
# Autobusi i së premtes: drita e pasdites që bëhet e ngrohtë, autobusi shkon drejt shtëpisë me dritare të ndezur
def tx(i, clock, k, h, sub, dark):
    c = '#F5EFE4' if dark else 'var(--ink)'
    cc = 'var(--gold-soft)' if dark else '#B04A2C'
    m = 'rgba(250,247,241,.85)' if dark else 'var(--ink-2)'
    return f'''<div class="sl" style="left:{i*1080}px"><div class="hd" style="color:{c}">
<div class="clock" style="color:{cc};font-size:120px">{clock}</div><div class="k" style="margin-top:30px;color:{'var(--sage)' if dark else 'var(--green)'}">{k}</div>
<div class="h">{h}</div><div class="sub" style="color:{m}">{sub}</div></div></div>'''
def em(t, dark): return f'<em style="color:{"var(--gold-soft)" if dark else "var(--green)"}">{t}</em>'
bg = 'linear-gradient(90deg,#F8EBCB 0%,#F3DDA9 16%,#EBC384 30%,#E0A878 47%,#4B4352 53%,#35384A 66%,#27303F 82%,#1B2430 100%)'
stars = ''.join(f'<circle cx="{4300+int((i*397)%2100)}" cy="{80+int((i*211)%780)}" r="{3+(i%3)}" fill="#FAF7F1" opacity="{.3+(i%4)*.15:.2f}"/>' for i in range(60))
road_y = 1500
def bus(x, lit=True):
    win = ''.join(f'<rect x="{x+60+i*92}" y="{road_y-250}" width="70" height="78" rx="10" fill="{"#F2D58B" if lit else "#5b6a74"}"/>' for i in range(5))
    return (f'<rect x="{x}" y="{road_y-290}" width="520" height="230" rx="34" fill="#3F6259"/><rect x="{x}" y="{road_y-150}" width="520" height="22" fill="#2E4A43"/>'
            f'{win}<circle cx="{x+120}" cy="{road_y-56}" r="46" fill="#17222E"/><circle cx="{x+120}" cy="{road_y-56}" r="20" fill="#8A8073"/>'
            f'<circle cx="{x+400}" cy="{road_y-56}" r="46" fill="#17222E"/><circle cx="{x+400}" cy="{road_y-56}" r="20" fill="#8A8073"/>')
def suitcase(x, y):
    return (f'<rect x="{x}" y="{y}" width="190" height="150" rx="20" fill="#B8803F"/><rect x="{x}" y="{y+60}" width="190" height="14" fill="#8F5F28"/>'
            f'<path d="M{x+60} {y}v-26h70v26" fill="none" stroke="#8F5F28" stroke-width="12" stroke-linecap="round"/>'
            f'<rect x="{x+82}" y="{y+52}" width="26" height="30" rx="6" fill="#F2D58B"/>')
def house(x, base):
    return (f'<rect x="{x}" y="{base-300}" width="420" height="300" fill="#4A3F46"/><path d="M{x-40} {base-300}L{x+210} {base-480}L{x+460} {base-300}Z" fill="#2E2830"/>'
            f'<rect x="{x+60}" y="{base-220}" width="110" height="120" rx="8" fill="#F2D58B"/><rect x="{x+250}" y="{base-220}" width="110" height="120" rx="8" fill="#F2D58B" opacity=".55"/>'
            f'<rect x="{x+170}" y="{base-150}" width="70" height="150" rx="6" fill="#2A2228"/>'
            f'<circle cx="{x+125}" cy="{base-160}" r="150" fill="#F2D58B" opacity=".14"/>')
svg = f'''<svg style="position:absolute;left:0;top:0;z-index:1" width="{W}" height="1920">
{stars}
<circle cx="760" cy="900" r="140" fill="#F2C46E" opacity=".95"/><circle cx="760" cy="900" r="230" fill="#F2C46E" opacity=".16"/>
<path d="M0 1380C700 1320 1300 1420 2000 1360S3300 1300 4000 1380S5400 1330 6480 1390V1920H0Z" fill="#3B4A55" opacity=".6"/>
<rect x="0" y="{road_y}" width="{W}" height="420" fill="#1F2B36"/>
<line x1="0" y1="{road_y+190}" x2="{W}" y2="{road_y+190}" stroke="#E8B96C" stroke-width="10" stroke-dasharray="90 70" opacity=".8"/>
{bus(300)}{bus(1080+260)}{bus(2160+380)}{bus(3240+40,True)}
{suitcase(1080+120, road_y+110)}{suitcase(2160+90, road_y+120)}
{house(3240+690, road_y)}{house(4320+520, road_y)}
</svg>'''
s = []
s.append(f'''<div class="sl" style="left:0"><div class="hd" style="color:var(--ink)"><div class="k" style="color:#B04A2C">E premte, ora 15:20</div>
<div class="h" style="font-size:98px;margin-top:34px">Autobusi i së premtes ka <em style="color:#8A4A2C">një gëzim dhe një provë.</em></div></div><div class="hint" style="color:#6B3F22;top:1060px">Rrëshqit {arrow('#6B3F22')}</div></div>''')
s.append(tx(1, '15:20', 'Ke ikur nga qyteti', 'Gjithë javën the „mirë“. Tani po shkon ' + em('te ata që të njohin.', False), 'Në autobus ka valixhe, qese dhe një gëzim që nuk shpjegohet. Edhe pak, dhe je në shtëpi.', False))
s.append(tx(2, '17:10', 'Rruga', 'Po e përgatit përgjigjen: ' + em('„jam mirë, vetëm pak i lodhur.“', False), 'S’do të shqetësosh askënd. Do të ulesh në tryezë dhe do të buzëqeshësh.', False))
s.append(tx(3, '19:40', 'Shtëpia', 'Nëna të hap derën, të shikon një sekondë ' + em('dhe e kupton gjithçka.', True), 'Por jo çdo ndjenjë gjen kë ta thotë. Dhe jo çdo i premte e ka një dritare të ndezur që të pret.', True))
s.append(tx(4, '22:00', 'Dhe ti', 'Ishe gati t’ia thoshe. ' + em('E the prapë „mirë“.', True), 'Shumë njerëz e bëjnë këtë të premte pas të premteje. Mund ta thuash një herë këtu, para se ta thuash aty.', True))
s.append(end_slide(5, 'd', 'Para se ta thuash në shtëpi, <em>provoje këtu.</em>', 'Në Shprehu flet pa emër me dikë që të dëgjon. Falas, në shqip.'))
html = HEAD + f'''</style></head><body><div class="pano" style="background:{bg}">{svg}{''.join(s)}</div></body></html>'''
open('b.html', 'w').write(html)
