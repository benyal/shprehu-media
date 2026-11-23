import os, json
OUT = os.path.dirname(os.path.abspath(__file__))
SK = '/home/user/Shprehu-3.5/.claude/skills/shprehu-social-ads'
HEAD = f'<!doctype html><html lang="sq"><head><meta charset="utf-8"><link rel="stylesheet" href="file://{SK}/assets/brand.css"><style>html,body{{margin:0;width:1080px;height:1920px;overflow:hidden}}*{{box-sizing:border-box}}'
END = lambda bg, fg, line: f'''<div style="position:absolute;inset:0;background:{bg};display:flex;flex-direction:column;justify-content:center;padding:0 110px;color:{fg};font-family:Inter">
<div style="font-weight:800;font-size:76px;line-height:1.15">{line}</div>
<div style="display:flex;align-items:center;gap:26px;margin-top:60px;font-weight:700;font-size:54px"><img src="file://{SK}/assets/logo-mark.png" style="width:120px;height:120px;border-radius:30px">shprehu.cc</div>
<div style="margin-top:24px;font-size:38px;opacity:.75">Anonim, falas, në shqip</div>
<div style="margin-top:34px;font-size:30px;opacity:.65">Shprehu nuk është shërbim urgjence. Në rrezik, telefono&nbsp;112.</div></div>'''

# A: POV, tekst i bardhë me kontur, sfond i errët, pa serif
def pov(text, small=''):
    return HEAD + '''body{background:radial-gradient(900px 1200px at 50% 40%,#2B3A36,#0F1513);font-family:Inter}
.t{position:absolute;left:90px;right:90px;top:640px;color:#fff;font-weight:900;font-size:92px;line-height:1.12;text-align:center;-webkit-text-stroke:3px #000;paint-order:stroke fill;text-shadow:0 6px 0 #000}
.s{position:absolute;left:120px;right:120px;top:1260px;color:#E8B96C;font-weight:800;font-size:46px;text-align:center}</style></head><body>''' + f'<div class="t">{text}</div><div class="s">{small}</div></body></html>'
A = [pov('POV: je fëmija i madh në një familje&nbsp;shqiptare', 'rrëshqit →'),
     pov('Je „prindi i dytë“ <br>që në moshën 12&nbsp;vjeç', ''),
     pov('Përkthen letrat e bankës <br>për gjithë&nbsp;familjen', ''),
     pov('Je ai që „s’ka hall“', 'sepse s’pyet askush'),
     pov('Kur je mirë, s’të pyet askush. <br>Kur je keq, s’ia thua&nbsp;askujt.', ''),
     pov('Edhe fëmija i madh <br>ka nevojë të&nbsp;dëgjohet.', 'Tag fëmijën e madh të familjes&nbsp;tënde'),
     HEAD + '</style></head><body>' + END('#0F1513', '#fff', 'Fol këtu, pa emër. <span style="color:#E8B96C">Edhe fëmija i madh.</span>') + '</body></html>']

# B: aplikacioni „Shënime“, listë e shkruar si në telefon
def note(lines, title='Gjëra që s’ia kam thënë askujt', foot=''):
    li = ''.join(f'<div class="l">{l}</div>' for l in lines)
    return HEAD + '''body{background:#FFFFFF;font-family:-apple-system,Inter}
.bar{position:absolute;top:0;left:0;right:0;height:200px;display:flex;align-items:flex-end;padding:0 50px 30px;color:#E0A300;font-size:44px;font-weight:600}
.h{position:absolute;top:240px;left:60px;right:60px;font-size:68px;font-weight:800;color:#111}
.d{position:absolute;top:430px;left:60px;font-size:34px;color:#999}
.list{position:absolute;top:530px;left:60px;right:60px}
.l{font-size:52px;line-height:1.35;color:#222;margin-bottom:34px;padding-left:46px;position:relative}
.l:before{content:"";position:absolute;left:0;top:26px;width:18px;height:18px;border-radius:50%;border:4px solid #E0A300}
.f{position:absolute;bottom:260px;left:60px;right:60px;font-size:38px;color:#999}
.cur{display:inline-block;width:4px;height:56px;background:#E0A300;vertical-align:middle;margin-left:6px}</style></head><body>''' + f'<div class="bar">‹ Shënimet</div><div class="h">{title}</div><div class="d">E hënë, 23 nëntor</div><div class="list">{li}</div><div class="f">{foot}</div></body></html>'
L = ['Që ndonjëherë lodhem nga të qenit „i&nbsp;fortë“.', 'Që e dëgjoj mesazhin zanor të nënës kur s’jam&nbsp;mirë.', 'Që qesh më shumë kur jam më keq.', 'Që s’di nga t’ia filloj kur dikush pyet „si&nbsp;je?“', 'Që do t’i kisha thënë, po të kisha&nbsp;kujt.']
B = [note(L[:1], foot='rrëshqit →'), note(L[:2]), note(L[:3]), note(L[:4]), note(L[:5] , foot='Ti çfarë do të shtoje? Shkruaje në koment.'),
     HEAD + '</style></head><body>' + END('#FFFFFF', '#111', 'Ke ku ta thuash. <span style="color:#3F6259">Pa emër, në shqip.</span>') + '</body></html>']

# C: „Zgjidh një derë“, ndërveprim: tri dyer, secila hapet në slide-in e vet
def doors(open_i=None, msg=''):
    cols = ['#B04A2C', '#3F6259', '#D9A441']
    d = ''
    for i in range(3):
        x = 110 + i * 300
        if open_i == i:
            d += f'<div style="position:absolute;left:{x}px;top:820px;width:260px;height:520px;background:#FFF3D6;box-shadow:0 0 80px rgba(255,214,140,.8);border-radius:10px"></div>'
        else:
            d += f'<div style="position:absolute;left:{x}px;top:820px;width:260px;height:520px;background:{cols[i]};border-radius:10px"><div style="position:absolute;right:26px;top:260px;width:22px;height:22px;border-radius:50%;background:#F3E6C8"></div></div>'
        d += f'<div style="position:absolute;left:{x}px;top:1360px;width:260px;text-align:center;font:900 72px Inter;color:#fff">{i+1}</div>'
    return HEAD + '''body{background:#1B2422;font-family:Inter}
.t{position:absolute;top:300px;left:90px;right:90px;text-align:center;color:#fff;font-weight:900;font-size:84px;line-height:1.1}
.m{position:absolute;top:1520px;left:90px;right:90px;text-align:center;color:#E8B96C;font-weight:800;font-size:54px;line-height:1.25}</style></head><body>''' + f'<div class="t">{"Zgjidh një derë." if open_i is None else "Dera " + str(open_i+1)}</div>{d}<div class="m">{msg}</div></body></html>'
C = [doors(None, 'Mbaje mend numrin.<br>Pastaj rrëshqit →'),
     doors(0, '„Sot mjafton që u ngrite.<br>Pjesa tjetër pret.“'),
     doors(1, '„Dikush po mendon për ty<br>tani, edhe pse s’ta thotë.“'),
     doors(2, '„Ajo që mban brenda<br>është më e lehtë kur e thua.“'),
     doors(None, 'Cilën zgjodhe? Shkruaj numrin<br>në koment dhe dërgoja dikujt.'),
     HEAD + '</style></head><body>' + END('#1B2422', '#fff', 'Cilëndo derë që zgjodhe, <span style="color:#E8B96C">këtu dikush të dëgjon, pa emër.</span>') + '</body></html>']

for name, pages in (('A-pov', A), ('B-shenimet', B), ('C-dyert', C)):
    d = os.path.join(OUT, '..', name); os.makedirs(d, exist_ok=True)
    for i, h in enumerate(pages):
        open(os.path.join(OUT, f'{name}-{i+1}.html'), 'w').write(h)
print('ok')
