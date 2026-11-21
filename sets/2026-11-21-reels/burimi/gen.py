import os
BASE_FILE = '/home/user/Shprehu-3.5/Claude outputs/reklama/2026-11-13-reels/gen.py'
OUT = os.path.dirname(os.path.abspath(__file__))
ns = {'__file__': BASE_FILE}
exec(open(BASE_FILE, encoding='utf-8').read().split('# 1. Qilimat')[0], ns)
page = ns['page']

# 1. Buka e mëngjesit: furra e lagjes, qesja e letrës, avulli
b_css = '''
body{background:#F3E9DA;color:#221F1C}
.lab{color:#B04A2C}.h{color:#221F1C}.h em{color:#B04A2C}
.wall{position:absolute;left:0;right:0;top:1080px;height:520px;background:#E3D2B8}
.oven{position:absolute;left:560px;top:1150px;width:400px;height:330px;background:#7A4A2F;border-radius:200px 200px 20px 20px}
.mouth{position:absolute;left:650px;top:1290px;width:220px;height:150px;background:#2A1A12;border-radius:110px 110px 6px 6px;box-shadow:inset 0 -30px 40px rgba(240,140,60,.7)}
.counter{position:absolute;left:0;right:0;top:1600px;bottom:0;background:#8C6A4A}
.bag{position:absolute;left:170px;top:1340px;width:240px;height:270px;background:#D9BC8C;border-radius:8px 8px 14px 14px;box-shadow:0 14px 30px rgba(40,30,20,.25)}
.loaf{position:absolute;left:200px;top:1280px;width:180px;height:110px;background:#C98B47;border-radius:90px 90px 30px 30px}
.steam{position:absolute;width:16px;height:120px;border-radius:8px;background:rgba(255,255,255,.75);filter:blur(5px);animation:st 3s ease-in-out infinite}
@keyframes st{0%{transform:translateY(0);opacity:0}30%{opacity:.9}100%{transform:translateY(-140px);opacity:0}}
.clock{position:absolute;left:560px;top:1520px;font-family:'Courier New',monospace;font-weight:700;font-size:56px;color:#FAF7F1}
'''
b_scene = ('<div class="wall"></div><div class="oven"></div><div class="mouth"></div><div class="counter"></div><div class="bag"></div><div class="loaf"></div>'
  + ''.join(f'<div class="steam" style="left:{x}px;top:1150px;animation-delay:{d}s"></div>' for x, d in [(240, 0), (290, 1), (340, 2)])
  + '<div class="clock">06:30</div>')

# 2. Lulet në dimër: gjyshja i fut vazot brenda kur vjen ngrica
l_css = '''
body{background:#E4EBEE;color:#221F1C}
.lab{color:#3F6259}.h{color:#221F1C}.h em{color:#3F6259}
.out{position:absolute;left:0;right:0;top:1060px;height:560px;background:linear-gradient(#C9D6DE,#EEF2F4)}
.frost{position:absolute;left:0;right:0;top:1060px;height:560px;background:repeating-linear-gradient(45deg,rgba(255,255,255,.5) 0 2px,transparent 2px 22px);opacity:0;animation:fr 19s linear both}
@keyframes fr{0%,15%{opacity:0}40%,100%{opacity:1}}
.sill{position:absolute;left:0;right:0;top:1600px;height:40px;background:#8C6A4A}
.floor{position:absolute;left:0;right:0;top:1640px;bottom:0;background:#EFE5D4}
.pot{position:absolute;left:380px;top:1480px;width:150px;height:120px;background:#B04A2C;border-radius:6px 6px 30px 30px;animation:move 19s ease-in-out both}
.pot:before{content:"";position:absolute;left:30px;top:-130px;width:14px;height:130px;background:#3F6259}
.pot:after{content:"";position:absolute;left:4px;top:-200px;width:70px;height:70px;background:#D95A6A;border-radius:50%;box-shadow:60px 20px 0 -6px #E8B96C}
@keyframes move{0%,40%{transform:translate(0,0)}60%,100%{transform:translate(-80px,210px)}}
.snow{position:absolute;width:12px;height:12px;border-radius:50%;background:#fff;animation:fall 6s linear infinite}
@keyframes fall{0%{transform:translateY(0)}100%{transform:translateY(520px)}}
.clock{position:absolute;left:700px;top:1520px;font-family:'Courier New',monospace;font-weight:700;font-size:56px;color:#3F6259}
'''
l_scene = ('<div class="out"></div>' + ''.join(f'<div class="snow" style="left:{x}px;top:1070px;animation-delay:-{d}s"></div>' for x, d in [(80,0),(220,2),(360,4),(520,1),(660,3),(820,5),(960,2.5)])
  + '<div class="frost"></div><div class="sill"></div><div class="floor"></div><div class="pot"></div><div class="clock">−3°</div>')

# 3. Tavlla me gjyshin: zarët, pulat, karriget
t_css = '''
body{background:#F1EBE1;color:#221F1C}
.lab{color:#3F6259}.h{color:#221F1C}.h em{color:#3F6259}
.floor{position:absolute;left:0;right:0;top:1640px;bottom:0;background:#A88560}
.board{position:absolute;left:150px;top:1160px;width:780px;height:460px;background:#8C4A2F;border-radius:20px;box-shadow:0 24px 40px rgba(40,30,20,.3)}
.in{position:absolute;left:180px;top:1190px;width:720px;height:400px;background:#E9D7B5;border-radius:8px}
.bar{position:absolute;left:530px;top:1190px;width:20px;height:400px;background:#8C4A2F}
.tri{position:absolute;width:0;height:0;border-left:26px solid transparent;border-right:26px solid transparent}
.chk{position:absolute;width:46px;height:46px;border-radius:50%}
.die{position:absolute;width:70px;height:70px;background:#FAF7F1;border-radius:12px;box-shadow:0 6px 12px rgba(0,0,0,.25);font:700 44px/70px 'Courier New',monospace;text-align:center;color:#221F1C;animation:roll 19s ease-out both}
@keyframes roll{0%{transform:translate(-200px,-120px) rotate(-200deg);opacity:0}10%{opacity:1}22%,100%{transform:none;opacity:1}}
.clock{position:absolute;left:180px;top:1060px;font-family:'Courier New',monospace;font-weight:700;font-size:52px;color:#B04A2C}
'''
tri = ''
for i in range(12):
    x = 190 + i * 58 + (20 if i >= 6 else 0)
    col = '#3F6259' if i % 2 else '#B04A2C'
    tri += f'<div class="tri" style="left:{x}px;top:1190px;border-top:150px solid {col}"></div>'
    tri += f'<div class="tri" style="left:{x}px;top:1440px;border-bottom:150px solid {"#B04A2C" if i % 2 else "#3F6259"}"></div>'
chk = ''.join(f'<div class="chk" style="left:{x}px;top:{y}px;background:{c}"></div>' for x, y, c in
              [(193,1195,'#FAF7F1'),(193,1243,'#FAF7F1'),(483,1195,'#221F1C'),(483,1243,'#221F1C'),(483,1291,'#221F1C'),(681,1541,'#FAF7F1'),(681,1493,'#FAF7F1'),(855,1541,'#221F1C')])
t_scene = ('<div class="floor"></div><div class="board"></div><div class="in"></div><div class="bar"></div>' + tri + chk
  + '<div class="die" style="left:620px;top:1360px">5</div><div class="die" style="left:710px;top:1380px;animation-delay:.2s">3</div><div class="clock">19:00</div>')

reels = {
    'buka': page('Chopin, Mazurka në la bemol maxhor, op. 59 nr. 2 (Musopen, CC0)', b_css, b_scene,
                 'Ora 06:30', 'Gjyshi shkonte i pari te&nbsp;furra.', 'Dhe kthehej me bukën e&nbsp;ngrohtë.',
                 'Askush s’zgjohej mirë. <em>Por era e bukës na ngrinte nga&nbsp;shtrati.</em>',
                 'Edhe ditët e rënda <em>nisin më lehtë me diçka të&nbsp;ngrohtë.</em>',
                 'Një fjalë e ngrohtë, <em>edhe pa emër. Fol&nbsp;këtu.</em>'),
    'lulet': page('Chopin, Mazurka në la minor, op. 17 nr. 4 (Musopen, CC0)', l_css, l_scene,
                  'Natën e parë me ngricë', 'Gjyshja i fuste vazot me lule&nbsp;brenda.', '„Jashtë ngrijnë.“',
                  'Nuk ishin të dobëta. <em>Ishte vetëm dimër.</em>',
                  'Edhe ti, kur bie ngrica, <em>afrohu pranë dikujt që të&nbsp;ngroh.</em>',
                  'Kur të ftohet brenda, <em>dikush të dëgjon, pa&nbsp;emër.</em>'),
    'tavlla': page('Chopin, Nocturne në do minor, op. 48 nr. 1 (Musopen, CC0)', t_css, t_scene,
                   'Ora 19:00, pas darke', 'Gjyshi nxirrte tavllën dhe hidhte&nbsp;zarët.', 'Ndonjëherë më linte të&nbsp;fitoja.',
                   'Nuk luante për lojën. <em>Luante që të rrinim&nbsp;bashkë.</em>',
                   'S’ka rëndësi kush fiton. <em>Ka rëndësi kush ulet&nbsp;përballë.</em>',
                   'Dikush ulet përballë teje, <em>pa emër. Fol&nbsp;këtu.</em>'),
}
for name, html in reels.items():
    open(os.path.join(OUT, f'reel-{name}.html'), 'w', encoding='utf-8').write(html)
    print(name)
