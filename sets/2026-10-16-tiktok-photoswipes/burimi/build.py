from gen import *
N = 7
Wd = N * 1080
def S(i, k, h, sub='', dark=True, num=None):
    c = '#F5EFE4' if dark else 'var(--ink)'
    kc = 'var(--sage)' if dark else 'var(--green)'
    m = 'rgba(250,247,241,.86)' if dark else 'var(--ink-2)'
    n = f'<div class="clock" style="color:{"var(--gold-soft)" if dark else "#B04A2C"}">{num}</div>' if num else ''
    return f'''<div class="sl" style="left:{i*1080}px"><div class="hd" style="color:{c}">{n}<div class="k" style="color:{kc};margin-top:{26 if num else 0}px">{k}</div><div class="h">{h}</div><div class="sub" style="color:{m}">{sub}</div></div></div>'''
def hook(k, h, dark=True, hint='#F5EFE4'):
    c = '#F5EFE4' if dark else 'var(--ink)'
    return f'''<div class="sl" style="left:0"><div class="hd" style="color:{c}"><div class="k" style="color:{'var(--gold-soft)' if dark else '#B04A2C'}">{k}</div><div class="h" style="font-size:104px;margin-top:34px">{h}</div></div><div class="hint" style="top:1170px;color:{hint}">Rrëshqit {arrow(hint)}</div></div>'''
def page(bg, svg, slides):
    return HEAD.replace('width:{W}px!important', f'width:{Wd}px!important') if False else (
        HEAD.replace('6480px', f'{Wd}px') + f'</style></head><body><div class="pano" style="background:{bg};width:{Wd}px">{svg}{"".join(slides)}</div></body></html>')
def em(t, c='var(--gold-soft)'): return f'<em style="color:{c}">{t}</em>'
# ---------------- A: fjalite me te cilat na rriten (dërrasa e shkollës) ----------------
dust = ''.join(f'<circle cx="{200+(i*613)%(Wd-300)}" cy="{300+(i*277)%1000}" r="{3+i%4}" fill="#EDE7D6" opacity="{.10+(i%5)*.05:.2f}"/>' for i in range(70))
svgA = f'''<svg style="position:absolute;left:0;top:0;z-index:1" width="{Wd}" height="1920">
<rect x="0" y="0" width="{Wd}" height="1920" fill="#25423B"/>
<rect x="0" y="1500" width="{Wd}" height="420" fill="#8C5F37"/><rect x="0" y="1500" width="{Wd}" height="28" fill="#B07A47"/>
{dust}
<path transform="translate(0,170)" d="M40 1210C500 1150 900 1260 1500 1180S2600 1130 3300 1220S4700 1160 5400 1230S6900 1180 7520 1210" stroke="#EDE7D6" stroke-width="5" fill="none" opacity=".35" stroke-dasharray="26 18"/>
<rect x="260" y="1440" width="150" height="46" rx="10" fill="#F2EEE2"/><rect x="470" y="1456" width="96" height="30" rx="8" fill="#E8B96C"/>
<rect x="2380" y="1446" width="130" height="40" rx="10" fill="#F2EEE2"/><rect x="2570" y="1450" width="190" height="36" rx="8" fill="#6F7F5A"/>
<rect x="4500" y="1440" width="150" height="46" rx="10" fill="#F2EEE2"/><rect x="6700" y="1450" width="190" height="36" rx="8" fill="#B8803F"/>
<g fill="#F2EEE2" opacity=".5"><rect x="1500" y="1472" width="120" height="14" rx="7"/><rect x="3600" y="1468" width="100" height="18" rx="9"/><rect x="5600" y="1470" width="140" height="16" rx="8"/></g>
</svg>'''
sl = [hook('Fjali që i dëgjuam të gjithë', '5 fjali me të cilat na rritën. ' + em('Sa prej tyre i ke dëgjuar?'))]
sl.append(S(1, 'E para', '„Mos qaj, ' + em('s’ka gjë.') + '“', 'Sa herë e dëgjove këtë, kur kishte gjë?', True, '1'))
sl.append(S(2, 'E dyta', '„Mos bëj hall, ' + em('ke gjithçka.') + '“', 'Ke gjithçka. Dhe prapë diçka të rëndon.', True, '2'))
sl.append(S(3, 'E treta', '„Të tjerët e kanë ' + em('më keq.') + '“', 'Dhe kjo e bën tëndin më të vogël? Jo.', True, '3'))
sl.append(S(4, 'E katërta', '„Do të të ' + em('kalojë vetë.') + '“', 'Nganjëherë kalon. Nganjëherë mbetet, i heshtur, vite me radhë.', True, '4'))
sl.append(S(5, 'E pesta', '„Mos u bëj ' + em('merak.') + '“', 'Kush të mësoi ta mbash merakun vetëm për vete?', True, '5'))
sl.append(end_slide(6, 'd', 'Sonte mund ta thuash ' + '<em>me zë.</em>', 'Në Shprehu flet pa emër me dikë që të dëgjon. Falas, në shqip.'))
CSS2 = '<style>.h{font-size:100px}.sub{font-size:44px}.hd{top:330px}.clock{font-size:170px}</style>'
def write(name, bg, svg, slides, extra=''):
    open(name, 'w').write(page(bg, svg, slides).replace('</head>', CSS2 + ('<style>' + extra + '</style>' if extra else '') + '</head>'))
write('a.html', '#25423B', svgA, sl, '.hd{top:430px}')


# ---------------- B: burrat nuk qajne (oborri i shkolles) ----------------
lines = ''.join(f'<line x1="{x}" y1="1340" x2="{x}" y2="1920" stroke="#FFF6E8" stroke-width="8" opacity=".65"/>' for x in range(900, Wd, 2160))
svgB = f'''<svg style="position:absolute;left:0;top:0;z-index:1" width="{Wd}" height="1920">
<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FBEBD3"/><stop offset="1" stop-color="#F6D3A6"/></linearGradient></defs>
<rect width="{Wd}" height="1340" fill="url(#sky)"/><circle cx="3700" cy="1130" r="150" fill="#F2B866" opacity=".9"/><circle cx="3700" cy="1130" r="250" fill="#F2B866" opacity=".18"/>
<rect x="0" y="1340" width="{Wd}" height="580" fill="#C77A4B"/><rect x="0" y="1340" width="{Wd}" height="14" fill="#E0A070"/>
{lines}
<ellipse cx="2700" cy="1560" rx="260" ry="90" fill="none" stroke="#FFF6E8" stroke-width="8" opacity=".6"/><line x1="0" y1="1600" x2="{Wd}" y2="1600" stroke="#FFF6E8" stroke-width="8" opacity=".5"/>
<g transform="translate(2640,0)"><rect x="0" y="1010" width="520" height="330" fill="#8A5A3A"/><path d="M-30 1010L260 880L550 1010Z" fill="#6F4630"/>{''.join(f'<rect x="{50+i*150}" y="1070" width="90" height="110" rx="8" fill="#F6D58C"/>' for i in range(3))}<rect x="215" y="1230" width="90" height="110" rx="6" fill="#4F3223"/></g>
<g><circle cx="1750" cy="1700" r="64" fill="#F8F3E8"/><path d="M1750 1660l34 25-13 40h-42l-13-40z" fill="#3A3028"/><ellipse cx="1750" cy="1775" rx="70" ry="14" fill="#000" opacity=".15"/></g>
<g><rect x="4950" y="1000" width="14" height="340" fill="#FFF6E8"/><rect x="5550" y="1000" width="14" height="340" fill="#FFF6E8"/><rect x="4950" y="1000" width="614" height="14" fill="#FFF6E8"/><path d="M4964 1014H5550V1340H4964" fill="none" stroke="#FFF6E8" stroke-width="3" opacity=".5" stroke-dasharray="14 12"/></g>
</svg>'''
sb = [hook('Oborri i shkollës, 10:15', 'Na mësuan një rregull që s’ishte në libër: ' + em('burrat s’qajnë.', '#B04A2C'), False, '#6B3F22')]
sb.append(S(1, 'Pushimi i madh', 'Rrëzohet. Dhemb. ' + em('Dhe ngrihet duke qeshur.', '#B04A2C'), 'Sepse e dinte çfarë do të thonin të tjerët.', False))
sb.append(S(2, 'Në shtëpi', 'Mësoi të thotë ' + em('„s’ka gjë.“', '#B04A2C'), 'Edhe kur kishte.', False))
sb.append(S(3, '18 vjeç', 'Mësoi ta mbajë ' + em('brenda.', '#B04A2C'), 'Në punë, në rrugë, në heshtjen e natës.', False))
sb.append(S(4, '30 vjeç', 'Dhe ende pyet veten: ' + em('pse më rëndon?', '#B04A2C'), 'Askush nuk i tha se mund ta thoshte me zë.', False))
sb.append(S(5, 'E vërteta', 'Burrat flasin, kërkojnë dikë ' + em('dhe janë po aq burra.', '#B04A2C'), 'Rregulli nuk ishte kurrë i vërtetë.', False))
sb.append(end_slide(6, 'l', 'Fol me dikë që të dëgjon, ' + '<em>pa emër.</em>', 'Në Shprehu e thua pa e ditur kush je. Falas, në shqip.'))
write('b.html', '#F6D3A6', svgB, sb)
# ---------------- C: tryeza ----------------
zig = ''.join(f'<path d="M{x} 1854l30 -46l30 46z" fill="#D6A24C"/>' for x in range(0, Wd, 60))
plates = ''.join(f'<ellipse cx="{x}" cy="1500" rx="150" ry="52" fill="#EDE4D3"/><ellipse cx="{x}" cy="1496" rx="102" ry="32" fill="#F7F1E4"/>' for x in range(300, Wd - 200, 780))
bread = ''.join(f'<ellipse cx="{x}" cy="1430" rx="86" ry="38" fill="#C98F4A"/><path d="M{x-40} 1424q40 -22 80 0" stroke="#9E6A2C" stroke-width="5" fill="none"/>' for x in range(700, Wd - 600, 1560))
glass = ''.join(f'<path d="M{x} 1380h70l-10 110h-50z" fill="#CFE0E6" opacity=".7"/>' for x in range(520, Wd - 300, 1170))
svgC = f'''<svg style="position:absolute;left:0;top:0;z-index:1" width="{Wd}" height="1920">
<rect width="{Wd}" height="1920" fill="#4A2A28"/><rect y="1340" width="{Wd}" height="580" fill="#F2E8D6"/><rect y="1340" width="{Wd}" height="16" fill="#D6A24C"/>
<rect y="1790" width="{Wd}" height="64" fill="#B04A2C"/>{zig}
<g transform="translate(0,90)">{plates}{bread}{glass}</g>
<circle cx="{Wd-640}" cy="1496" r="1" fill="none"/><path d="M{Wd-460} 1470v110M{Wd-440} 1470v110M{Wd-420} 1470v110" stroke="#B8BDC2" stroke-width="7"/>
<rect x="0" y="0" width="{Wd}" height="220" fill="#3B201E"/>
</svg>'''
sc = [hook('Darka, ora 20:30', 'Në tryezën shqiptare flasim për gjithçka. ' + em('Përveç asaj që na rëndon.'))]
sc.append(S(1, 'Çfarë flasim', 'Çmimet. Motin. ' + em('Kush erdhi e kush shkoi.'), 'Gjithçka, përveç vetes.', True))
sc.append(S(2, 'Rregulli i pashkruar', 'Çka ndodh në shtëpi, ' + em('mbetet në shtëpi.'), 'Edhe kur dikush ka nevojë ta thotë me zë.', True))
sc.append(S(3, 'Pyetja', 'Nuk është gjithmonë fshehtësi. ' + em('Është diçka që s’ka ku të thuhet.'), '', True))
sc.append(S(4, 'Një mundësi', 'Ka gjëra që mund t’i thuash ' + em('jashtë tryezës.'), 'Pa emër, pa e ditur kush e njeh familjen tënde.', True))
sc.append(S(5, 'Në Shprehu', 'Një vend ku ' + em('s’të njeh') + ' askush.', 'Dhe prapë të dëgjon dikush. Në shqip, falas.', True))
sc.append(end_slide(6, 'd', 'Çka s’thuhet në tryezë, ' + '<em>thuaje këtu.</em>', 'Anonim dhe falas, në shqip. Dikush të dëgjon.'))
write('c.html', '#4A2A28', svgC, sc)
