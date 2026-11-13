import os
OUT = os.path.dirname(os.path.abspath(__file__))
SK = '/home/user/Shprehu-3.5/.claude/skills/shprehu-social-ads'

BASE = '''
html,body{width:1080px;height:1920px;overflow:hidden;margin:0}
body{position:relative}
.safe{position:absolute;z-index:6;top:220px;left:96px;right:150px;height:760px}
.scene{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:flex-start;opacity:0}
.lab{font-weight:800;font-size:34px;letter-spacing:.18em;text-transform:uppercase;margin-bottom:34px}
.h{font-family:'Fraunces',serif;font-weight:600;font-size:92px;line-height:1.07;letter-spacing:-.02em}
.h em{font-style:italic;font-weight:500}
@keyframes inout{0%{opacity:0;transform:translateY(36px)}12%,86%{opacity:1;transform:none}100%{opacity:0;transform:translateY(-26px)}}
@keyframes inhold{0%{opacity:0;transform:translateY(36px)}28%,100%{opacity:1;transform:none}}
@keyframes late{0%,40%{opacity:0;transform:translateY(24px)}100%{opacity:1;transform:none}}
.s1{animation:inout 4.3s ease-out .4s both}
.s1 .l2{display:inline-block;animation:late 4.3s ease-out .4s both}
.s2{animation:inout 4.6s ease-out 4.9s both}
.s3{animation:inout 4.5s ease-out 9.7s both}
.s4{animation:inhold 4.6s ease-out 14.4s both}
.endbg{position:absolute;inset:0;z-index:5;background:#2E4A43;opacity:0;animation:endbg 4.6s ease-out 14.2s both}
@keyframes endbg{0%{opacity:0}30%,100%{opacity:.96}}
.s4 .h{color:#FAF7F1}.s4 .h em{color:#E8B96C}
.brand{display:flex;align-items:center;gap:26px;font-weight:700;font-size:54px;margin-top:48px;color:#FAF7F1}
.brand img{width:120px;height:120px;border-radius:30px}
.tags{margin-top:22px;font-size:38px;color:#8FB8A8;font-weight:500}
.fine{margin-top:30px;font-size:30px;line-height:1.4;color:rgba(250,247,241,.8)}
'''

def page(music, css, scene, lab, s1a, s1b, s2, s3, end):
    return f'''<!-- muzika: {music} -->
<!doctype html>
<html lang="sq"><head><meta charset="utf-8">
<link rel="stylesheet" href="file://{SK}/assets/brand.css">
<style>{BASE}{css}</style></head><body>
{scene}
<div class="endbg"></div>
<div class="safe">
 <div class="scene s1"><div class="lab">{lab}</div><div class="h">{s1a}<br><span class="l2"><em>{s1b}</em></span></div></div>
 <div class="scene s2"><div class="h">{s2}</div></div>
 <div class="scene s3"><div class="h">{s3}</div></div>
 <div class="scene s4"><div class="h">{end}</div><div class="brand"><img src="file://{SK}/assets/logo-mark.png" alt="">shprehu.cc</div><div class="tags">Anonim, falas, në shqip</div><div class="fine">Shprehu nuk është shërbim urgjence. Në rrezik, telefono&nbsp;112.</div></div>
</div>
</body></html>'''

# 1. Qilimat në oborr: qilimi i varur në litar, shkopi që e rrah, re pluhuri
q_css = '''
body{background:#EAF0F2;color:#221F1C}
.lab{color:#3F6259}.h{color:#221F1C}.h em{color:#3F6259}
.sky{position:absolute;inset:0;background:linear-gradient(#DCE7EC 0%,#EEF2F0 55%,#E9DDC6 72%,#D9C7A3 100%)}
.ground{position:absolute;left:0;right:0;top:1500px;bottom:0;background:#CDB78F}
.post{position:absolute;top:1010px;width:22px;height:560px;background:#7A5A3A;border-radius:6px}
.rope{position:absolute;left:60px;right:60px;top:1030px;height:6px;background:#8C6A4A}
.rug{position:absolute;left:190px;top:1032px;width:700px;height:470px;background:#9E2F2A;border:16px solid #6E1F1C;transform-origin:50% 0;animation:sway 1.1s ease-in-out infinite alternate}
@keyframes sway{0%{transform:rotate(-.6deg)}100%{transform:rotate(.6deg)}}
.rug:before{content:"";position:absolute;inset:26px;border:10px solid #E8B96C}
.rug i{position:absolute;width:110px;height:110px;background:#E8B96C;transform:rotate(45deg)}
.rug i:after{content:"";position:absolute;inset:28px;background:#1F332E}
.fringe{position:absolute;left:190px;top:1518px;width:732px;height:40px;background:repeating-linear-gradient(90deg,#E9DEC8 0 6px,transparent 6px 14px);transform-origin:50% 0;animation:sway 1.1s ease-in-out infinite alternate}
.stick{position:absolute;left:820px;top:1180px;width:24px;height:330px;background:#B98A5E;border-radius:12px;transform-origin:50% 100%;animation:hit .9s ease-in infinite}
@keyframes hit{0%,100%{transform:rotate(28deg)}45%{transform:rotate(-8deg)}55%{transform:rotate(-8deg)}}
.dust{position:absolute;border-radius:50%;background:radial-gradient(circle,rgba(210,190,150,.75),rgba(210,190,150,0) 70%);opacity:0;animation:puff .9s ease-out infinite}
@keyframes puff{0%,40%{opacity:0;transform:scale(.4)}55%{opacity:1;transform:scale(1)}100%{opacity:0;transform:scale(1.6) translateY(-60px)}}
'''
rug_motifs = ''.join(f'<i style="left:{x}px;top:{y}px"></i>' for x, y in [(110, 140), (285, 140), (460, 140)])
dust = ''.join(f'<div class="dust" style="left:{x}px;top:{y}px;width:{w}px;height:{w}px;animation-delay:{d}s"></div>' for x, y, w, d in [(620, 1150, 220, 0), (520, 1250, 260, .1), (700, 1300, 200, .05), (440, 1120, 180, .15), (600, 1380, 240, .08)])
q_scene = f'''<div class="sky"></div><div class="ground"></div>
<div class="post" style="left:60px"></div><div class="post" style="left:1000px"></div><div class="rope"></div>
<div class="rug">{rug_motifs}</div><div class="fringe"></div>{dust}<div class="stick"></div>'''

# 2. Çelësi te fqinja: korridori i pallatit, dy dyer, çelësi kalon nga një dorë te një gozhdë te dera fqinje
c_css = '''
body{background:#E9E1D2;color:#221F1C}
.lab{color:#3F6259}.h{color:#221F1C}.h em{color:#3F6259}
.wall{position:absolute;inset:0;background:linear-gradient(#EDE5D6 0%,#E3D7C2 70%,#CFC0A4 100%)}
.stripe{position:absolute;left:0;right:0;top:1460px;height:30px;background:#8FB8A8;opacity:.6}
.floor{position:absolute;left:0;right:0;top:1780px;bottom:0;background:repeating-linear-gradient(90deg,#B9A27E 0 120px,#AE9670 120px 240px)}
.door{position:absolute;top:1060px;width:330px;height:720px;background:#7A5338;border-radius:8px 8px 0 0;box-shadow:inset 0 0 0 16px #5E3E28}
.door b{position:absolute;right:40px;top:380px;width:26px;height:26px;border-radius:50%;background:#E8B96C}
.door s{position:absolute;left:110px;top:90px;width:110px;height:34px;background:#E8DCC4;border-radius:4px;text-decoration:none}
.mat{position:absolute;top:1760px;width:300px;height:40px;background:#9E2F2A;border-radius:6px}
.hook{position:absolute;left:820px;top:1200px;width:12px;height:30px;background:#5E5E5E;border-radius:4px}
.key{position:absolute;left:470px;top:1250px;width:160px;height:60px;animation:key 19s ease-in-out both}
@keyframes key{0%,22%{transform:translate(0,0) rotate(0)}40%,100%{transform:translate(330px,-40px) rotate(90deg)}}
.key i{position:absolute;left:0;top:0;width:60px;height:60px;border-radius:50%;border:14px solid #D6A24C;box-sizing:border-box}
.key u{position:absolute;left:52px;top:22px;width:108px;height:16px;background:#D6A24C;border-radius:4px}
.key u:after{content:"";position:absolute;right:10px;top:12px;width:12px;height:22px;background:#D6A24C}
.light{position:absolute;left:340px;top:960px;width:400px;height:400px;border-radius:50%;background:radial-gradient(circle,rgba(255,226,160,.55),rgba(255,226,160,0) 65%)}
'''
c_scene = '''<div class="wall"></div><div class="stripe"></div><div class="light"></div><div class="floor"></div>
<div class="door" style="left:60px"><s></s><b></b></div><div class="mat" style="left:75px"></div>
<div class="door" style="left:690px"><s></s><b></b></div><div class="mat" style="left:705px"></div>
<div class="hook"></div><div class="key"><i></i><u></u></div>'''

# 3. Kavanozat e gjyshes: rafti i kuzhinës me etiketa që s’përputhen me përmbajtjen
k_css = '''
body{background:#F3EBDD;color:#221F1C}
.lab{color:#B04A2C}.h{color:#221F1C}.h em{color:#B04A2C}
.wall{position:absolute;inset:0;background:#F3EBDD;background-image:linear-gradient(rgba(176,74,44,.06) 2px,transparent 2px),linear-gradient(90deg,rgba(176,74,44,.06) 2px,transparent 2px);background-size:90px 90px}
.shelf{position:absolute;left:40px;right:40px;top:1610px;height:34px;background:#8C6A4A;box-shadow:0 12px 20px rgba(60,40,20,.25)}
.jar{position:absolute;top:1300px;width:210px;height:310px;border-radius:26px 26px 30px 30px;background:rgba(255,255,255,.55);box-shadow:inset 0 0 0 6px rgba(255,255,255,.8),0 10px 18px rgba(60,40,20,.15)}
.jar .lid{position:absolute;left:-6px;right:-6px;top:-4px;height:46px;background:#B04A2C;border-radius:14px}
.jar .fill{position:absolute;left:6px;right:6px;bottom:6px;height:60%;border-radius:0 0 24px 24px}
.jar .tag{position:absolute;left:28px;right:28px;top:96px;height:64px;background:#FBF6EA;border:3px solid #2E2A26;border-radius:6px;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:30px;color:#2E2A26;letter-spacing:.06em}
.peek{animation:peek 19s ease-in-out both}
@keyframes peek{0%,26%{transform:none}36%,100%{transform:translateY(-70px) rotate(-6deg)}}
.lidoff{animation:lidoff 19s ease-in-out both}
@keyframes lidoff{0%,26%{transform:none}36%,100%{transform:translate(70px,-90px) rotate(18deg)}}
'''
def jar(x, label, fill, extra=''):
    return f'<div class="jar {extra}" style="left:{x}px"><div class="fill" style="background:{fill}"></div><div class="tag">{label}</div><div class="lid{" lidoff" if extra else ""}"></div></div>'
sugar = 'repeating-radial-gradient(circle at 30% 40%,#FFFFFF 0 3px,#F1EDE6 3px 6px)'
salt = 'repeating-radial-gradient(circle at 60% 30%,#F7F7F5 0 2px,#E6E6E2 2px 4px)'
rice = 'repeating-linear-gradient(35deg,#F6F0DE 0 8px,#E9DFC3 8px 12px)'
beans = 'radial-gradient(circle at 30% 30%,#C7703C 0 14px,transparent 15px) 0 0/40px 40px,#8A4A26'
k_scene = f'''<div class="wall"></div><div class="shelf"></div>
{jar(70, 'KAFE', sugar, 'open')}{jar(320, 'SHEQER', salt)}{jar(570, 'KRIPË', rice)}{jar(820, 'ORIZ', beans)}'''

reels = {
    'qilimat': page('Chopin, Valsi B. 133 në mi bemol maxhor (Musopen, CC0)', q_css, q_scene,
                    'Një herë në vit', 'Nëna i nxirrte qilimat në oborr.', 'Dhe i rrihte me&nbsp;shkop.',
                    'Shtëpia dukej e pastër. <em>Pluhuri që dilte s’kishte&nbsp;fund.</em>',
                    'Edhe brenda nesh mblidhet pluhur pa e parë. <em>S’ka turp ta&nbsp;shkundësh.</em>',
                    'Thuaje atë që ke mbledhur. <em>Me dikë që të dëgjon, pa&nbsp;emër.</em>'),
    'celesi': page('Chopin, Mazurka op. 24 nr. 3 në la bemol maxhor (Musopen, CC0)', c_css, c_scene,
                   'Ora 18:40, te dera', 'Te ne, çelësi i shtëpisë rrinte te&nbsp;fqinja.', 'Për çdo&nbsp;rast.',
                   'Askush s’e quante rrezik. <em>E&nbsp;quanin&nbsp;besim.</em>',
                   'Edhe për ditët e rënda na duhet një „fqinjë“. <em>Dikush ku e lëmë pak&nbsp;peshë.</em>',
                   'Kur s’ke ku ta lësh, <em>lëre këtu, pa&nbsp;emër.</em>'),
    'kavanozat': page('Chopin, Valsi op. 64 nr. 1 në re bemol maxhor (Musopen, CC0)', k_css, k_scene,
                      'Te gjyshja', 'Kavanozi i kafesë kishte&nbsp;sheqer.', 'Dhe ai i sheqerit,&nbsp;kripë.',
                      'Vetëm ajo e dinte çfarë kishte brenda. <em>Etiketa s’të tregonte&nbsp;asgjë.</em>',
                      'Edhe ty të vunë etiketa: „s’ka hall“, „gjithmonë mirë“. <em>Brenda mund të ketë tjetër&nbsp;gjë.</em>',
                      'Thuaje çfarë ka vërtet brenda. <em>Dikush të dëgjon, pa&nbsp;emër.</em>')
}
for name, html in reels.items():
    open(os.path.join(OUT, f'reel-{name}.html'), 'w', encoding='utf-8').write(html)
    print(name)
