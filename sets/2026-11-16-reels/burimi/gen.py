import os
BASE_FILE = '/home/user/Shprehu-3.5/Claude outputs/reklama/2026-11-13-reels/gen.py'
OUT = os.path.dirname(os.path.abspath(__file__))
ns = {'__file__': BASE_FILE}
exec(open(BASE_FILE, encoding='utf-8').read().split('# 1. Qilimat')[0], ns)
page = ns['page']

# 1. Goma e biçikletës: legeni me ujë, goma e zhytur, flluskat dalin nga një pikë
g_css = '''
body{background:#E9F0EE;color:#221F1C}
.lab{color:#3F6259}.h{color:#221F1C}.h em{color:#3F6259}
.yard{position:absolute;inset:0;background:linear-gradient(#EAF1EF 0%,#E3ECE8 60%,#C9BFA8 61%,#BDB298 100%)}
.basin{position:absolute;left:170px;top:1380px;width:740px;height:330px;background:linear-gradient(#5B8DB8,#3C6E9A);border-radius:30px 30px 300px 300px;box-shadow:0 22px 40px rgba(20,40,60,.25)}
.basin:before{content:"";position:absolute;left:-20px;right:-20px;top:-16px;height:36px;background:#2E5A82;border-radius:20px}
.water{position:absolute;left:200px;top:1400px;width:680px;height:120px;background:rgba(190,225,240,.85);border-radius:50%}
.tube{position:absolute;left:250px;top:1330px;width:580px;height:200px;border:52px solid #2A2A2A;border-radius:50%;box-sizing:border-box}
.wline{position:absolute;left:200px;top:1440px;width:680px;height:80px;background:rgba(150,200,225,.75);border-radius:0 0 50% 50%}
.patch{position:absolute;left:600px;top:1340px;width:40px;height:30px;background:#B04A2C;border-radius:6px;opacity:0;animation:patch 19s ease-out both}
@keyframes patch{0%,60%{opacity:0}70%,100%{opacity:1}}
.bub{position:absolute;border-radius:50%;border:4px solid rgba(255,255,255,.9);background:rgba(255,255,255,.25);animation:bub 1.6s ease-out infinite}
@keyframes bub{0%{opacity:0;transform:translateY(0) scale(.5)}20%{opacity:1}100%{opacity:0;transform:translateY(-120px) scale(1.2)}}
.wheel{position:absolute;left:820px;top:1060px;width:220px;height:220px;border:14px solid #3A3A3A;border-radius:50%;box-sizing:border-box;opacity:.5}
.wheel:after{content:"";position:absolute;left:50%;top:0;bottom:0;width:4px;margin-left:-2px;background:#3A3A3A}
'''
bubbles = ''.join(f'<div class="bub" style="left:{610 + dx}px;top:1350px;width:{w}px;height:{w}px;animation-delay:{d}s"></div>'
                  for dx, w, d in [(0, 36, 0), (14, 24, .5), (-10, 30, 1.0), (8, 20, 1.3)])
g_scene = f'''<div class="yard"></div><div class="basin"></div><div class="water"></div>
<div class="tube"></div><div class="wline"></div>{bubbles}<div class="patch"></div>'''

# 2. Kaseta dhe lapsi: kaseta e madhe, lapsi në rrotë që sillet, shiriti jashtë që zvogëlohet
k_css = '''
body{background:#20262A;color:#FAF7F1}
.lab{color:#8FB8A8}.h{color:#FAF7F1}.h em{color:#E8B96C}
.desk{position:absolute;inset:0;background:linear-gradient(#20262A 0%,#252D31 62%,#5E4632 63%,#4E3A2A 100%)}
.lamp{position:absolute;left:600px;top:900px;width:600px;height:600px;border-radius:50%;background:radial-gradient(circle,rgba(255,214,150,.28),rgba(255,214,150,0) 65%)}
.cas{position:absolute;left:190px;top:1260px;width:700px;height:440px;background:#2E2A26;border-radius:26px;box-shadow:0 24px 40px rgba(0,0,0,.45)}
.cas .lbl{position:absolute;left:50px;right:50px;top:40px;height:230px;background:#E8B96C;border-radius:12px}
.cas .lbl i{position:absolute;left:30px;top:30px;font-style:italic;font-family:'Fraunces',serif;font-size:44px;color:#2E2A26}
.cas .win{position:absolute;left:170px;top:120px;width:360px;height:110px;background:#151515;border-radius:55px}
.reel{position:absolute;top:135px;width:80px;height:80px;border-radius:50%;background:repeating-conic-gradient(#FAF7F1 0 30deg,#CFC8BC 30deg 60deg)}
.r1{left:205px;animation:spin 1.2s linear infinite}.r2{left:415px}
@keyframes spin{to{transform:rotate(-360deg)}}
.pencil{position:absolute;left:236px;top:1080px;width:22px;height:330px;background:linear-gradient(90deg,#E8B96C,#F2CC85,#E8B96C);border-radius:4px;transform-origin:50% 100%}
.pencil:after{content:"";position:absolute;left:0;top:-30px;width:22px;height:30px;background:#F1D9CF;border-radius:4px 4px 0 0}
.tape{position:absolute;left:520px;top:1700px;width:320px;height:120px;border:9px solid #8C6A4A;border-top:0;border-radius:0 0 160px 160px;transform-origin:50% 0;animation:wind 19s ease-in-out both}
@keyframes wind{0%,10%{transform:scale(1)}90%,100%{transform:scale(.05);opacity:0}}
'''
k_scene = '''<div class="desk"></div><div class="lamp"></div>
<div class="cas"><div class="lbl"><i>Këngët e mia</i></div><div class="win"></div><div class="reel r1"></div><div class="reel r2"></div></div>
<div class="tape"></div><div class="pencil"></div>'''

# 3. Kabina telefonike: telefoni i postës me ekranin e impulseve që bie 50, 12, 3, 1
t_css = '''
body{background:#ECE7DE;color:#221F1C}
.lab{color:#B04A2C}.h{color:#221F1C}.h em{color:#B04A2C}
.booth{position:absolute;inset:0;background:linear-gradient(#ECE7DE 0%,#E6DFD2 66%,#9C8B70 67%,#8E7E64 100%)}
.glass{position:absolute;left:90px;top:960px;width:900px;height:900px;border:22px solid #B04A2C;border-bottom:0;border-radius:24px 24px 0 0;background:rgba(255,255,255,.25)}
.phone{position:absolute;left:380px;top:1100px;width:320px;height:520px;background:#5B6066;border-radius:24px;box-shadow:0 20px 40px rgba(0,0,0,.25)}
.screen{position:absolute;left:410px;top:1140px;width:260px;height:110px;background:#9FB59A;border-radius:10px;box-shadow:inset 0 0 0 6px #3E4448}
.num{position:absolute;left:410px;top:1150px;width:260px;text-align:center;font-family:'Courier New',monospace;font-weight:700;font-size:78px;color:#22301F;opacity:0}
.n1{animation:show 4.9s steps(1) 0s forwards}.n2{animation:show 4.8s steps(1) 4.9s forwards}.n3{animation:show 4.7s steps(1) 9.7s forwards}.n4{animation:showlast 4.6s steps(1) 14.4s forwards}
@keyframes show{0%,99%{opacity:1}100%{opacity:0}}
@keyframes showlast{0%,100%{opacity:1}}
.keys{position:absolute;left:430px;top:1290px;width:220px;height:240px;background:repeating-linear-gradient(90deg,transparent 0 10px,#DCDCD6 10px 62px,transparent 62px 80px)}
.keys:after{content:"";position:absolute;inset:0;background:repeating-linear-gradient(180deg,#5B6066 0 14px,transparent 14px 60px)}
.handset{position:absolute;left:250px;top:1180px;width:110px;height:330px;background:#2E2A26;border-radius:50px}
.cord{position:absolute;left:290px;top:1500px;width:120px;height:140px;border:8px dotted #2E2A26;border-radius:50%}
.card{position:absolute;left:720px;top:1560px;width:220px;height:140px;background:#E8B96C;border-radius:12px;transform:rotate(-8deg);box-shadow:0 8px 16px rgba(0,0,0,.2)}
.card:after{content:"50";position:absolute;right:18px;bottom:10px;font-family:'Fraunces',serif;font-weight:700;font-size:40px;color:#8C4A2F}
'''
t_scene = '''<div class="booth"></div><div class="glass"></div><div class="phone"></div><div class="screen"></div>
<div class="num n1">50</div><div class="num n2">12</div><div class="num n3">3</div><div class="num n4">1</div>
<div class="keys"></div><div class="handset"></div><div class="cord"></div><div class="card"></div>'''

reels = {
    'goma': page('Chopin, Mazurka në si bemol minor, op. 24 nr. 4 (CC0)', g_css, g_scene,
                 'Në oborr', 'Kur shpohej goma e biçikletës, s’e&nbsp;hidhnim.', 'E zhytnim në legen me&nbsp;ujë.',
                 'Aty ku dilnin flluskat, <em>ishte&nbsp;vrima.</em>',
                 'Edhe brenda nesh, ajo që dhemb del kur flasim. <em>Pastaj mund të&nbsp;arnohet.</em>',
                 'Thuaje ku të dhemb. <em>Dikush të dëgjon, pa&nbsp;emër.</em>'),
    'kaseta': page('Bach, Partita nr. 2 BWV 826, Allemanda (CC0)', k_css, k_scene,
                   'Ora 21:10, në dhomë', 'Kur shiriti i kasetës dilte&nbsp;jashtë,', 's’e&nbsp;hidhnim.',
                   'E mbështillnim ngadalë me një&nbsp;laps. <em>Kthesë pas&nbsp;kthese.</em>',
                   'Disa gjëra ngatërrohen. <em>Nuk duan forcë, duan&nbsp;durim.</em>',
                   'Kur diçka ngatërrohet brenda, <em>fol ngadalë me dikë, pa&nbsp;emër.</em>'),
    'kabina': page('Chopin, Nocturne në do minor, B. 108 (Musopen, CC0)', t_css, t_scene,
                   'Në postë', 'Kartela telefonike kishte vetëm 50&nbsp;impulse.', 'Dhe ne flisnim&nbsp;shpejt.',
                   'Gjënë më të rëndësishme e linim për fund. <em>„Të dua“ dilte kur ekrani tregonte&nbsp;1.</em>',
                   'Sot s’ka impulse që mbarojnë. <em>Mos e lër më për&nbsp;fund.</em>',
                   'Thuaje sot atë që e lë gjithmonë për fund. <em>Dikush të dëgjon, pa&nbsp;emër.</em>')
}
for name, html in reels.items():
    open(os.path.join(OUT, f'reel-{name}.html'), 'w', encoding='utf-8').write(html)
    print(name)
