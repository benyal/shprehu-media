import os
BASE_FILE = '/home/user/Shprehu-3.5/Claude outputs/reklama/2026-11-13-reels/gen.py'
OUT = os.path.dirname(os.path.abspath(__file__))
ns = {'__file__': BASE_FILE}
exec(open(BASE_FILE, encoding='utf-8').read().split('# 1. Qilimat')[0], ns)
page = ns['page']

# 1. Ftonjtë mbi dollap: dollapi, tre ftonj të verdhë, era që ngjitet
f_css = '''
body{background:#F3ECDF;color:#221F1C}
.lab{color:#B07A1C}.h{color:#221F1C}.h em{color:#B07A1C}
.floor{position:absolute;left:0;right:0;top:1700px;bottom:0;background:#B99A72}
.cab{position:absolute;left:200px;top:1240px;width:680px;height:460px;background:#8C6A4A;border-radius:10px}
.door{position:absolute;top:1270px;width:300px;height:400px;background:#7A5A3A;border-radius:6px}
.knob{position:absolute;top:1450px;width:22px;height:22px;border-radius:50%;background:#E8B96C}
.q{position:absolute;width:120px;height:110px;background:#E8C24C;border-radius:55% 45% 50% 50%;box-shadow:inset -10px -10px 0 rgba(0,0,0,.08)}
.q:after{content:"";position:absolute;left:52px;top:-14px;width:10px;height:20px;background:#6E5A2F;border-radius:4px}
.scent{position:absolute;width:20px;height:140px;border-radius:10px;background:rgba(232,194,76,.35);filter:blur(6px);animation:up 4s ease-in-out infinite}
@keyframes up{0%{transform:translateY(0);opacity:0}30%{opacity:1}100%{transform:translateY(-220px);opacity:0}}
'''
f_scene = ('<div class="floor"></div><div class="cab"></div><div class="door" style="left:230px"></div><div class="door" style="left:550px"></div>'
  '<div class="knob" style="left:500px"></div><div class="knob" style="left:570px"></div>'
  + ''.join(f'<div class="q" style="left:{x}px;top:1132px"></div>' for x in (270, 420, 570))
  + ''.join(f'<div class="scent" style="left:{x}px;top:1000px;animation-delay:{d}s"></div>' for x, d in ((320, 0), (470, 1.3), (620, 2.6))))

# 2. Biçikleta: vëllai mban shalën, pastaj e lëshon
b_css = '''
body{background:#E9F0EC;color:#221F1C}
.lab{color:#3F6259}.h{color:#221F1C}.h em{color:#3F6259}
.road{position:absolute;left:0;right:0;top:1680px;bottom:0;background:#9AA59D}
.line{position:absolute;left:0;right:0;top:1780px;height:10px;background:repeating-linear-gradient(90deg,#F3EFE7 0 80px,transparent 80px 160px);animation:roll 19s linear both}
@keyframes roll{0%{background-position:0 0}100%{background-position:-1600px 0}}
.bike{position:absolute;left:330px;top:1460px;width:420px;height:230px;animation:ride 19s ease-in-out both}
@keyframes ride{0%,35%{transform:translateX(0)}100%{transform:translateX(160px)}}
.w{position:absolute;top:100px;width:130px;height:130px;border:12px solid #221F1C;border-radius:50%;box-sizing:border-box}
.fr{position:absolute;left:65px;top:120px;width:290px;height:12px;background:#B04A2C;transform:rotate(-12deg);transform-origin:left}
.seat{position:absolute;left:110px;top:40px;width:90px;height:22px;background:#221F1C;border-radius:10px}
.post{position:absolute;left:150px;top:55px;width:10px;height:90px;background:#B04A2C}
.hb{position:absolute;left:330px;top:30px;width:12px;height:100px;background:#B04A2C}
.hand{position:absolute;left:180px;top:1400px;width:220px;height:28px;background:#3F6259;border-radius:14px;animation:let 19s ease-in-out both}
@keyframes let{0%,35%{transform:translateX(0);opacity:1}55%,100%{transform:translateX(-120px);opacity:0}}
'''
b_scene = ('<div class="road"></div><div class="line"></div><div class="hand"></div><div class="bike"><div class="w" style="left:0"></div><div class="w" style="left:290px"></div>'
  '<div class="fr"></div><div class="post"></div><div class="seat"></div><div class="hb"></div></div>')

# 3. Sanka në kodër: kodra me borë, sanka zbret, gjurmët
s_css = '''
body{background:#DDE6EE;color:#221F1C}
.lab{color:#3F6259}.h{color:#221F1C}.h em{color:#3F6259}
.hill{position:absolute;left:-200px;top:1180px;width:1500px;height:900px;background:#FAFBFC;border-radius:50% 50% 0 0;transform:rotate(-8deg)}
.sled{position:absolute;left:140px;top:1260px;width:180px;height:40px;background:#B04A2C;border-radius:8px;box-shadow:0 18px 0 -10px #8C3A22;animation:down 19s ease-in both}
@keyframes down{0%,20%{transform:translate(0,0) rotate(8deg)}55%{transform:translate(560px,300px) rotate(8deg)}56%{transform:translate(0,0) rotate(8deg)}90%,100%{transform:translate(560px,300px) rotate(8deg)}}
.flake{position:absolute;width:12px;height:12px;border-radius:50%;background:#fff;animation:fall 7s linear infinite}
@keyframes fall{0%{transform:translateY(0)}100%{transform:translateY(900px)}}
.tree{position:absolute;width:0;height:0;border-left:60px solid transparent;border-right:60px solid transparent;border-bottom:170px solid #3F6259}
'''
s_scene = ('<div class="hill"></div><div class="tree" style="left:820px;top:1150px"></div><div class="tree" style="left:900px;top:1210px"></div><div class="sled"></div>'
  + ''.join(f'<div class="flake" style="left:{x}px;top:1000px;animation-delay:-{d}s"></div>' for x, d in ((80,0),(240,2),(420,4),(600,1),(780,3),(960,5))))

reels = {
    'ftonjte': page('Chopin, Mazurka në sol maxhor, op. 50 nr. 1 (Musopen, CC0)', f_css, f_scene,
                    'Në vjeshtë, te gjyshja', 'Gjyshja vinte tre ftonj mbi&nbsp;dollap.', 'Jo për t’i ngrënë.',
                    'Që gjithë shtëpia <em>të mbante erë të&nbsp;mirë.</em>',
                    'Disa gjëra të mira nuk duken. <em>Ndihen.</em>',
                    'Edhe një fjalë e mirë mbetet. <em>Fol këtu, pa&nbsp;emër.</em>'),
    'bicikleta': page('Chopin, Mazurka në do maxhor, op. 56 nr. 2 (Musopen, CC0)', b_css, b_scene,
                      'Rruga para shtëpisë', 'Vëllai i madh më mbante shalën e&nbsp;biçikletës.', '„Mos ki frikë, të&nbsp;mbaj.“',
                      'Nuk e kuptova kur më lëshoi. <em>Po ecja&nbsp;vetë.</em>',
                      'Ndihma më e mirë <em>të lë të ecësh vetë, dhe rri pas&nbsp;teje.</em>',
                      'Kur të duhet dikush pas teje, <em>fol këtu, pa&nbsp;emër.</em>'),
    'sanka': page('Chopin, Mazurka në la minor, op. 59 nr. 1 (Musopen, CC0)', s_css, s_scene,
                  'Bora e parë', 'Gjithë lagjja dilte në kodër me&nbsp;sanka.', 'Rrëzoheshim në çdo&nbsp;zbritje.',
                  'Dhe ngjiteshim prapë. <em>Gjithmonë&nbsp;bashkë.</em>',
                  'Rrëzimi s’ishte fundi. <em>Ishte gjysma e&nbsp;lojës.</em>',
                  'Kur rrëzohesh, <em>dikush të ndihmon të ngjitesh, pa&nbsp;emër.</em>'),
}
for name, html in reels.items():
    open(os.path.join(OUT, f'reel-{name}.html'), 'w', encoding='utf-8').write(html)
