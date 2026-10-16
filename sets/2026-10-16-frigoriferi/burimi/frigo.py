SK = '/home/user/Shprehu-3.5/.claude/skills/shprehu-social-ads'
W, H = 6480, 1350
def arrow(c):
    return f'<svg width="60" height="24" viewBox="0 0 60 24"><path d="M2 12h52M44 3l10 9-10 9" stroke="{c}" stroke-width="3.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def tx(i, clock, k, h, sub):
    return f'''<div class="sl" style="left:{i*1080}px"><div class="hd">
<div class="clock">{clock}</div><div class="k">{k}</div><div class="h">{h}</div><div class="sub">{sub}</div></div></div>'''
def shelf(y, x0=1000, x1=5400):
    return (f'<rect x="{x0}" y="{y}" width="{x1-x0}" height="14" rx="7" fill="#BFD3CB" opacity=".55"/>'
            f'<rect x="{x0}" y="{y+14}" width="{x1-x0}" height="40" fill="#BFD3CB" opacity=".08"/>')
def milk(x, y):
    return (f'<path d="M{x} {y}h110v-120l-30-40h-50l-30 40z" fill="#F4F1EA"/><path d="M{x} {y-120}l30-40h50l30 40z" fill="#9CB9C7"/>'
            f'<rect x="{x+22}" y="{y-92}" width="66" height="44" rx="8" fill="#9CB9C7" opacity=".75"/>')
def jar(x, y, c='#E8C98C'):
    return (f'<rect x="{x}" y="{y-150}" width="120" height="150" rx="18" fill="{c}" opacity=".9"/><rect x="{x-6}" y="{y-176}" width="132" height="34" rx="10" fill="#D6A24C"/>'
            f'<rect x="{x+16}" y="{y-120}" width="20" height="90" rx="10" fill="#fff" opacity=".25"/>')
def eggs(x, y):
    return f'<rect x="{x}" y="{y-34}" width="330" height="34" rx="12" fill="#CDBB9C"/>' + ''.join(f'<ellipse cx="{x+46+i*74}" cy="{y-56}" rx="30" ry="40" fill="#F1E4CB"/>' for i in range(4))
def bowl(x, y):
    return (f'<path d="M{x} {y-90}h300a150 90 0 0 1-300 0z" fill="#E7E1D6" opacity=".92"/><path d="M{x-6} {y-100}h312" stroke="#C7CDD1" stroke-width="16" stroke-linecap="round"/>'
            f'<path d="M{x+30} {y-112}c70-30 170-30 240 0" fill="#CFD6DB" opacity=".9"/>')
def lemon(x, y):
    return f'<ellipse cx="{x}" cy="{y-32}" rx="48" ry="34" fill="#E9D25C"/><circle cx="{x+46}" cy="{y-32}" r="8" fill="#C9B23F"/>'
def bottle(x, y, c='#6F8F7C'):
    return f'<rect x="{x}" y="{y-190}" width="82" height="190" rx="22" fill="{c}"/><rect x="{x+22}" y="{y-250}" width="38" height="70" rx="10" fill="{c}"/><rect x="{x+16}" y="{y-120}" width="50" height="64" rx="6" fill="#F3E9D2" opacity=".85"/>'
S1, S2 = 1020, 1270
svg = f'''<svg style="position:absolute;left:0;top:0;z-index:1" width="{W}" height="{H}">
<defs><radialGradient id="glow" cx="2700" cy="900" r="2100" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FFF1CC" stop-opacity=".30"/><stop offset=".55" stop-color="#FFF1CC" stop-opacity=".12"/><stop offset="1" stop-color="#FFF1CC" stop-opacity="0"/></radialGradient>
<linearGradient id="slit" x1="0" x2="1"><stop offset="0" stop-color="#FFF1CC" stop-opacity="0"/><stop offset="1" stop-color="#FFF1CC" stop-opacity=".85"/></linearGradient></defs>
<rect x="0" y="0" width="{W}" height="{H}" fill="url(#glow)"/>
<rect x="840" y="0" width="240" height="{H}" fill="url(#slit)"/>
{shelf(S1)}{shelf(S2)}
{milk(1180, S1)}{jar(1420, S1)}{bowl(1700, S1)}{eggs(2160, S1)}{lemon(2620, S1)}{bottle(2780, S1)}{jar(3020, S1, '#C98F6B')}{milk(3280, S1)}{bowl(3560, S1)}{eggs(4000, S1)}{jar(4420, S1)}{bottle(4600, S1, '#8C6F5E')}{lemon(4840, S1)}
{bowl(1240, S2)}{jar(1640, S2, '#B7C9A0')}{bottle(1860, S2)}{milk(2080, S2)}{lemon(2380, S2)}{lemon(2470, S2)}{eggs(2700, S2)}{jar(3180, S2)}{bowl(3420, S2)}{bottle(3820, S2, '#8C6F5E')}{milk(4060, S2)}{jar(4340, S2, '#C98F6B')}{bowl(4640, S2)}
<rect x="5230" y="0" width="1250" height="{H}" fill="url(#cream)"/>
</svg>'''
svg = svg.replace('<defs>', '<defs><linearGradient id="cream" x1="5230" x2="5410" y1="0" y2="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FAF7F1" stop-opacity="0"/><stop offset="1" stop-color="#FAF7F1" stop-opacity="1"/></linearGradient>', 1)
slides = []
slides.append(f'''<div class="sl" style="left:0"><div class="hd" style="top:150px"><div class="k" style="color:var(--gold-soft)">Ora 23:40, kuzhina</div>
<div class="h" style="font-size:112px;margin-top:40px">Hap frigoriferin. <em>Nuk ke uri.</em></div></div><div class="hint" style="top:1090px;color:#FFF1CC">Rrëshqit {arrow('#FFF1CC')}</div></div>''')
slides.append(tx(1, '23:40', 'Drita e vogël', 'Kavanozi, qumështi, <em>pjata e djeshme.</em>', 'Gjithçka është aty si dje. Vetëm mendimet nuk e kanë mbyllur ditën.'))
slides.append(tx(2, '23:46', 'Çfarë po kërkon', 'Nuk po kërkon ushqim. <em>Po kërkon një pushim.</em>', 'Diçka që e ndan mendjen nga mendimet, për një minutë.'))
slides.append(tx(3, '23:52', 'Rrethi', 'E mbyll. E hap prapë. <em>E mbyll sërish.</em>', 'Dhe s’e di mirë ç’ke dashur të gjesh.'))
slides.append(tx(4, '00:05', 'Nuk je i vetmi', 'Shumë njerëz e bëjnë këtë natën. <em>Nuk është dobësi.</em>', 'Është një mënyrë e vogël për të mos qenë vetëm me mendimet.'))
slides.append(f'''<div class="sl" style="left:{5*1080}px"><div class="hd" style="color:var(--ink);top:120px;left:100px">
<img class="logo" src="file://{SK}/assets/logo-mark.png" alt="">
<div class="h" style="margin-top:44px;color:var(--ink)">Sonte mund ta thuash <em style="color:var(--green)">me zë.</em></div>
<div class="sub" style="color:var(--ink-2)">Në Shprehu flet pa emër me dikë që të dëgjon. Falas, në shqip.</div>
<div class="cta">shprehu.cc</div>
<div class="fine" style="color:var(--ink-2)">Shprehu nuk është shërbim urgjence.<br>Në rrezik, telefono 112.</div></div></div>''')
html = f'''<!doctype html><html lang="sq"><head><meta charset="utf-8"><link rel="stylesheet" href="file://{SK}/assets/brand.css"><style>
html,body{{margin:0;height:{H}px;overflow:hidden;width:{W}px!important}}
.pano{{position:absolute;left:0;top:0;width:{W}px;height:{H}px;overflow:hidden;background:linear-gradient(180deg,#101C19 0%,#172A25 55%,#1D332D 100%)}}
.sl{{position:absolute;top:0;width:1080px;height:{H}px;z-index:5}}
.hd{{position:absolute;left:96px;right:150px;top:130px;color:#F5EFE4}}
.k{{font-size:27px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--sage);margin-top:26px}}
.clock{{font-family:'Fraunces',serif;font-weight:500;font-style:italic;font-size:130px;line-height:1;color:var(--gold-soft)}}
.h{{font-family:'Fraunces',serif;font-weight:600;font-size:82px;line-height:1.07;letter-spacing:-.01em;margin-top:24px}}
.h em{{font-style:italic;font-weight:500;color:var(--gold-soft)}}
.sub{{font-size:38px;line-height:1.42;margin-top:26px;color:rgba(250,247,241,.86)}}
.hint{{position:absolute;left:96px;display:flex;gap:18px;align-items:center;font-size:32px;font-weight:600}}
.cta{{margin-top:44px;display:inline-block;background:var(--green);color:#fff;font-weight:800;font-size:44px;padding:28px 50px;border-radius:14px}}
.fine{{font-size:26px;line-height:1.45;margin-top:38px}}
.logo{{width:130px;height:130px;border-radius:34px}}
</style></head><body><div class="pano">{svg}{''.join(slides)}</div></body></html>'''
open('frigo.html', 'w').write(html)
