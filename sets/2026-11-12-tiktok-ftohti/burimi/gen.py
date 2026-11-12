import os
SK = '/home/user/Shprehu-3.5/.claude/skills/shprehu-social-ads'
OUT = os.path.dirname(os.path.abspath(__file__))
CSS = '''
html,body{width:WWpx;height:1920px;overflow:hidden;margin:0}
.pano{position:absolute;left:0;top:0;width:WWpx;height:1920px;overflow:hidden}
.slide{position:absolute;top:0;width:1080px;height:1920px}
.safe{position:absolute;left:96px;right:150px;top:250px;bottom:460px;display:flex;flex-direction:column}
.tag{font-size:30px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;margin-bottom:44px}
h1{font-family:'Fraunces',serif;font-weight:600;font-size:104px;line-height:1.06;letter-spacing:-0.02em;margin:0}
h1 em{font-style:italic;font-weight:500}
p{font-size:46px;line-height:1.38;margin:40px 0 0}
.hint{margin-top:auto;font-size:34px;font-weight:600}
.dk{color:#FAF7F1}.dk p{color:rgba(250,247,241,.86)}.dk .tag{color:#8FB8A8}.dk h1 em{color:#E8B96C}.dk .hint{color:#E8B96C}
.lt{color:#221F1C}.lt p{color:#4A443C}.lt .tag{color:#3F6259}.lt h1 em{color:#3F6259}.lt .hint{color:#3F6259}
.end{position:absolute;top:0;width:1080px;height:1920px;background:#2E4A43;color:#FAF7F1}
.end .safe{justify-content:center}
.end img{width:150px;height:150px;border-radius:38px;box-shadow:0 16px 50px rgba(0,0,0,.3)}
.end h1{margin-top:56px;font-size:100px}.end h1 em{color:#E8B96C}
.end .tags{margin-top:34px;font-size:38px;color:#8FB8A8;font-weight:500}
.end .url{margin-top:48px;font-size:60px;font-weight:700}
.end .fine{margin-top:44px;font-size:28px;line-height:1.45;color:rgba(250,247,241,.72)}
.abs{position:absolute}
'''

def page(w, bg, body):
    return (f'<!doctype html><html lang="sq"><head><meta charset="utf-8"><link rel="stylesheet" href="file://{SK}/assets/brand.css">'
            f'<style>{CSS.replace("WW", str(w))}</style></head><body><div class="pano" style="background:{bg}">{body}</div></body></html>')

def slide(i, cls, tag, h, sub='', hint=''):
    return (f'<div class="slide {cls}" style="left:{i*1080}px"><div class="safe"><div class="tag">{tag}</div><h1>{h}</h1>'
            f'{f"<p>{sub}</p>" if sub else ""}{f"<div class=hint>{hint}</div>" if hint else ""}</div></div>')

def end(i, h):
    return (f'<div class="end" style="left:{i*1080}px"><div class="safe"><img src="file://{SK}/assets/logo-mark.png" alt=""><h1>{h}</h1>'
            '<div class="tags">Anonim, falas, në shqip</div><div class="url">shprehu.cc</div>'
            '<div class="fine">Shprehu nuk është shërbim urgjence. Në rrezik, telefono&nbsp;112.</div></div></div>')

def D(x, y, w, h, style='', inner=''):
    return f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;{style}">{inner}</div>'

H = 'Rrëshqit →'

# 01: 5 gjëra kur bie i ftohti i parë (listë me boshllëk), shkalla e temperaturës bie nga slide-i në slide
def set1():
    W = 7560
    b = []
    temps = ['14°', '11°', '8°', '6°', '3°', '1°']
    for i, t in enumerate(temps):
        x = i * 1080
        b.append(D(x + 96, 1540, 600, 200, f'font-family:Fraunces,serif;font-weight:600;font-size:170px;color:rgba(63,98,89,{.22 + i*.08:.2f})', t))
    b.append(D(0, 1500, W - 1080, 6, 'background:linear-gradient(90deg,#D6A24C,#8FB8A8 60%,#5B8FC9)'))
    import random
    random.seed(12)
    for i in range(1, 6):
        for _ in range(i * 7):
            x = i * 1080 + random.randint(40, 1020); y = random.randint(1520, 1880); r = random.randint(8, 18)
            b.append(D(x, y, r, r, 'border-radius:50%;background:#AFC6D6;opacity:.85'))
    b.append(slide(0, 'lt', 'Listë', '5 gjëra kur bie i ftohti i parë. <em>E katërta s’ka të bëjë me&nbsp;motin.</em>', hint=H))
    b.append(slide(1, 'lt', '1', 'Ndezim sobën për herë të parë. <em>Shtëpia mban erë pluhuri të&nbsp;djegur.</em>'))
    b.append(slide(2, 'lt', '2', 'Nëna i nxjerr çorapet e leshit <em>nga&nbsp;sënduku.</em>'))
    b.append(slide(3, 'lt', '3', 'Ballkoni mbushet me lakër <em>për&nbsp;turshi.</em>'))
    b.append(slide(4, 'lt', '4', 'Rrimë më shumë brenda. <em>Dhe mendimet na gjejnë më&nbsp;lehtë.</em>', 'Netët zgjaten, dhe ka më shumë kohë për të&nbsp;menduar.'))
    b.append(slide(5, 'lt', '5', 'Kuptojmë që na duhet ngrohtësi. <em>Jo vetëm nga&nbsp;soba.</em>'))
    b.append(end(6, 'Kur netët zgjaten, <em>fol me dikë që të&nbsp;dëgjon.</em>'))
    return W, page(W, 'linear-gradient(90deg,#F6EEDF 0%,#EEF0EC 55%,#DFE8EE 86%)', ''.join(b))

# 02: „Mos dil me flokë të lagura“ (rregull i pashkruar), një shall i thurur kalon nëpër të gjitha slide-et
def set2():
    W = 6480
    b = []
    path = 'M -40 1640 C 600 1480, 900 1800, 1500 1640 S 2500 1480, 3000 1660 S 4200 1820, 4700 1620 S 5400 1500, 5500 1600'
    b.append(f'<svg class="abs" style="left:0;top:0" width="{W}" height="1920" viewBox="0 0 {W} 1920">'
             '<defs><pattern id="st" width="120" height="120" patternUnits="userSpaceOnUse"><rect width="40" height="120" fill="#B5443A"/><rect x="40" width="40" height="120" fill="#E8B96C"/><rect x="80" width="40" height="120" fill="#FAF7F1"/></pattern></defs>'
             f'<path d="{path}" fill="none" stroke="#8F3229" stroke-width="150" stroke-linecap="round"/>'
             f'<path d="{path}" fill="none" stroke="url(#st)" stroke-width="130" stroke-linecap="round" opacity=".95"/>'
             f'<path d="{path}" fill="none" stroke="rgba(0,0,0,.12)" stroke-width="130" stroke-dasharray="6 18"/></svg>')
    for k in range(9):
        b.append(D(5480 + k * 16, 1560 + (k % 2) * 6, 6, 120, 'background:#B5443A;border-radius:3px;transform:rotate(-8deg)'))
    b.append(slide(0, 'lt', 'Rregull i pashkruar', '„Mos dil me flokë të lagura, se&nbsp;ftohesh!“ <em>E ke dëgjuar, apo&nbsp;jo?</em>', hint=H))
    b.append(slide(1, 'lt', 'Në derë', '„Vure kapelën?“ „Mbylle xhaketën.“ <em>„Merre&nbsp;shallin.“</em>'))
    b.append(slide(2, 'lt', 'E vërteta', 'Nëna kujdesej që të mos ftoheshim jashtë. <em>Po brenda, kush&nbsp;pyeste?</em>'))
    b.append(slide(3, 'lt', 'Sot', 'Për trupin kishim një mijë rregulla. <em>Për mendjen, asnjë.</em>'))
    b.append(slide(4, 'lt', 'Një rregull i ri', 'Pyete veten si je, <em>jo vetëm a ke&nbsp;ftohtë.</em>'))
    b.append(end(5, 'Kur s’di si je, <em>fol me dikë që të dëgjon, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(90deg,#F3EFE7,#EFE6D6)', ''.join(b))

# 03: Albumi pa asnjë foto të keqe (ritual/urtësi), faqet e albumit me qoshe fotografish, gjithnjë e më bosh
def corners(x, y, w, h, c='#2E2A26'):
    s = 54
    cs = [(x - 10, y - 10, 'clip-path:polygon(0 0,100% 0,0 100%)'), (x + w - s + 10, y - 10, 'clip-path:polygon(0 0,100% 0,100% 100%)'),
          (x - 10, y + h - s + 10, 'clip-path:polygon(0 0,0 100%,100% 100%)'), (x + w - s + 10, y + h - s + 10, 'clip-path:polygon(100% 0,0 100%,100% 100%)')]
    return ''.join(D(a, b2, s, s, f'background:{c};{st}') for a, b2, st in cs)

def photo(x, y, w, h, inner):
    return D(x, y, w, h, 'background:linear-gradient(#D9C29A,#B9976A);box-shadow:0 10px 24px rgba(40,25,10,.25);border:14px solid #FBF6EA', inner) + corners(x, y, w + 28, h + 28)

def set3():
    W = 6480
    b = []
    cake = D(130, 170, 200, 110, 'background:#FBF6EA;border-radius:10px') + ''.join(D(160 + k * 45, 120, 10, 50, 'background:#B5443A;border-radius:4px') for k in range(4))
    lights = ''.join(D(20 + k * 60, 40 + (k % 2) * 18, 22, 22, 'border-radius:50%;background:#F6E2A8;box-shadow:0 0 18px #F6E2A8') for k in range(7)) + D(120, 120, 80, 180, 'background:#6E4E33;border-radius:40px 40px 6px 6px') + D(240, 130, 80, 170, 'background:#3F6259;border-radius:40px 40px 6px 6px')
    b.append(photo(330, 1500, 440, 300, cake))
    b.append(photo(1400, 1500, 440, 300, lights))
    b.append(D(2480, 1500, 468, 328, 'background:rgba(251,246,234,.6);border:4px dashed rgba(46,42,38,.25)') + corners(2480, 1500, 468, 328))
    b.append(D(3560, 1500, 468, 328, 'background:rgba(251,246,234,.6);border:4px dashed rgba(46,42,38,.25)') + corners(3560, 1500, 468, 328))
    b.append(D(4640, 1500, 468, 328, 'background:#FBF6EA;border:4px solid rgba(63,98,89,.35)', D(140, 120, 190, 80, 'font-family:Sacramento,cursive;font-size:84px;color:#3F6259', 'sot')) + corners(4640, 1500, 468, 328, '#3F6259'))
    b.append(slide(0, 'lt', 'Te ne', 'Në albumin e familjes s’kishte asnjë foto të keqe. <em>Por kishte ditë të&nbsp;këqija.</em>', hint=H))
    b.append(slide(1, 'lt', 'Fotot', 'Ditëlindje, festa, rrobat më të mira. <em>Të gjithë duke&nbsp;qeshur.</em>'))
    b.append(slide(2, 'lt', 'Faqet bosh', 'Askush s’e fotografonte natën kur s’na zinte gjumi nga&nbsp;hallet. <em>Ato faqe mbetën&nbsp;bosh.</em>'))
    b.append(slide(3, 'lt', 'E vërteta', 'Faqja bosh s’do të thotë që s’ndodhi. <em>Do të thotë që e mbajtëm&nbsp;vetë.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'Edhe ditët që s’dalin në foto <em>meritojnë një vend ku&nbsp;thuhen.</em>'))
    b.append(end(5, 'Për ditët që s’dalin në album, <em>ka dikë që të dëgjon, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(90deg,#EFE6D3,#E7DCC5)', ''.join(b))

for name, fn in [('01-ftohti', set1), ('02-floket', set2), ('03-albumi', set3)]:
    w, html = fn()
    open(os.path.join(OUT, f'set-{name}.html'), 'w', encoding='utf-8').write(html)
    print(name, w)
