import os
BASE_FILE = '/home/user/Shprehu-3.5/Claude outputs/reklama/2026-11-13-reels/gen.py'
OUT = os.path.dirname(os.path.abspath(__file__))
ns = {'__file__': BASE_FILE}
exec(open(BASE_FILE, encoding='utf-8').read().split('# 1. Qilimat')[0], ns)
page = ns['page']

# 1. Kapelja e leshit: varëse, kapelja që rregullohet dy herë
k_css = '''
body{background:#EFE8DE;color:#221F1C}
.lab{color:#B04A2C}.h{color:#221F1C}.h em{color:#B04A2C}
.wall{position:absolute;left:0;right:0;top:1080px;bottom:0;background:#E3D6C3}
.door{position:absolute;left:620px;top:1100px;width:340px;height:820px;background:#8C6A4A;border-radius:8px 8px 0 0}
.peg{position:absolute;top:1200px;width:26px;height:26px;border-radius:50%;background:#5E4632}
.hat{position:absolute;left:220px;top:1300px;width:260px;height:180px;background:#B04A2C;border-radius:130px 130px 20px 20px;animation:fix 19s ease-in-out both}
.hat:before{content:"";position:absolute;left:0;right:0;bottom:0;height:46px;background:repeating-linear-gradient(90deg,#8C3A22 0 14px,#B04A2C 14px 28px);border-radius:0 0 20px 20px}
.hat:after{content:"";position:absolute;left:100px;top:-50px;width:60px;height:60px;border-radius:50%;background:#F3E6C8}
@keyframes fix{0%,30%{transform:rotate(0)}36%{transform:rotate(-8deg)}42%{transform:rotate(6deg)}48%,60%{transform:rotate(0)}66%{transform:rotate(-6deg)}72%,100%{transform:rotate(0)}}
'''
k_scene = '<div class="wall"></div><div class="door"></div><div class="peg" style="left:180px"></div><div class="peg" style="left:520px"></div><div class="hat"></div>'

# 2. Zilja e derës: butoni dhe valët e zërit, të gjata ose të shkurtra
z_css = '''
body{background:#E7EEEA;color:#221F1C}
.lab{color:#3F6259}.h{color:#221F1C}.h em{color:#3F6259}
.wall{position:absolute;left:0;right:0;top:1080px;bottom:0;background:#D6E0DA}
.plate{position:absolute;left:420px;top:1300px;width:240px;height:340px;background:#F3EFE7;border-radius:30px;box-shadow:0 20px 40px rgba(0,0,0,.12)}
.btn{position:absolute;left:490px;top:1410px;width:100px;height:100px;border-radius:50%;background:#E8B96C;box-shadow:inset 0 -8px 0 #C99A4C}
.wave{position:absolute;left:540px;top:1460px;width:20px;height:20px;border:8px solid #3F6259;border-radius:50%;opacity:0;animation:ring 2.4s ease-out infinite}
@keyframes ring{0%{transform:translate(-50%,-50%) scale(1);opacity:.8}100%{transform:translate(-50%,-50%) scale(22);opacity:0}}
'''
z_scene = '<div class="wall"></div>' + ''.join(f'<div class="wave" style="animation-delay:{d}s"></div>' for d in (0, .3, 1.2)) + '<div class="plate"></div><div class="btn"></div>'

# 3. Aeroplani prej letre: nga ballkoni, bie, palosja, fluturon më larg
a_css = '''
body{background:#DCE8F0;color:#221F1C}
.lab{color:#3F6259}.h{color:#221F1C}.h em{color:#3F6259}
.bal{position:absolute;left:0;top:1260px;width:300px;height:30px;background:#8C6A4A}
.rail{position:absolute;left:0;top:1170px;width:300px;height:90px;background:repeating-linear-gradient(90deg,#8C6A4A 0 10px,transparent 10px 40px)}
.ground{position:absolute;left:0;right:0;top:1760px;bottom:0;background:#9DB39A}
.plane{position:absolute;left:240px;top:1170px;width:0;height:0;border-top:30px solid transparent;border-bottom:30px solid transparent;border-left:130px solid #FAFBFC;filter:drop-shadow(0 6px 6px rgba(0,0,0,.15));animation:fly 19s ease-in-out both}
@keyframes fly{0%,8%{transform:translate(0,0) rotate(0)}30%{transform:translate(220px,520px) rotate(40deg)}40%{transform:translate(0,0) rotate(0)}48%{transform:translate(0,0) rotate(-6deg)}75%,100%{transform:translate(680px,260px) rotate(8deg)}}
'''
a_scene = '<div class="ground"></div><div class="rail"></div><div class="bal"></div><div class="plane"></div>'

reels = {
    'kapelja': page('Chopin, Mazurka në do maxhor, op. 24 nr. 2 (Musopen, CC0)', k_css, k_scene,
                    'Para se të dilnim', 'Nëna na e vinte kapelen e leshit te&nbsp;dera.', 'Dhe e rregullonte dy&nbsp;herë.',
                    'Edhe kur ishte mirë. <em>Edhe kur vonoheshim.</em>',
                    'Disa „të dua“ <em>thuhen me duar, jo me&nbsp;fjalë.</em>',
                    'Kur të duhet pak kujdes, <em>dikush të dëgjon, pa&nbsp;emër.</em>'),
    'zilja': page('Chopin, Mazurka në la bemol maxhor, op. 17 nr. 3 (Musopen, CC0)', z_css, z_scene,
                  'Në shtëpinë tonë', 'E dinim kush ishte te&nbsp;dera.', 'Nga mënyra si binte&nbsp;zilja.',
                  'Tezja binte gjatë. <em>Fqinja dy herë&nbsp;shkurt.</em>',
                  'Njerëzit që na duan <em>i njohim nga gjërat më të&nbsp;vogla.</em>',
                  'Edhe ti njihesh nga fjalët e tua. <em>Fol këtu, pa&nbsp;emër.</em>'),
    'aeroplani': page('Chopin, Mazurka në si maxhor, op. 56 nr. 1 (Musopen, CC0)', a_css, a_scene,
                      'Nga ballkoni', 'E hidhnim aeroplanin prej&nbsp;letre.', 'Binte pranë&nbsp;pallatit.',
                      'E merrnim, e palosnim prapë. <em>Dhe fluturonte më&nbsp;larg.</em>',
                      'Çdo rënie <em>na mësonte një palosje më të&nbsp;mirë.</em>',
                      'Kur bie, <em>dikush të ndihmon ta provosh prapë, pa&nbsp;emër.</em>'),
}
for name, html in reels.items():
    open(os.path.join(OUT, f'reel-{name}.html'), 'w', encoding='utf-8').write(html)
