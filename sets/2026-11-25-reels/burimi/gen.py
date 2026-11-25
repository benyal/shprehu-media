import os
BASE_FILE = '/home/user/Shprehu-3.5/Claude outputs/reklama/2026-11-13-reels/gen.py'
OUT = os.path.dirname(os.path.abspath(__file__))
ns = {'__file__': BASE_FILE}
exec(open(BASE_FILE, encoding='utf-8').read().split('# 1. Qilimat')[0], ns)
page = ns['page']

# 1. Vargu i specave: specat shtohen në varg një nga një, dielli i vjeshtës
pep = ''
for i in range(9):
    x = 150 + i * 88
    pep += f'<div class="pep" style="left:{x}px;top:{1300 + (i % 2) * 14}px;animation-delay:{0.6 + i * 1.1}s"></div>'
s_css = '''
body{background:#F4E9D8;color:#221F1C}
.lab{color:#B04A2C}.h{color:#221F1C}.h em{color:#B04A2C}
.sun{position:absolute;left:760px;top:1120px;width:200px;height:200px;border-radius:50%;background:#F2C66B;opacity:.85}
.wall{position:absolute;left:0;right:0;top:1500px;bottom:0;background:#E2CFB2}
.win{position:absolute;left:120px;top:1580px;width:300px;height:240px;background:#CFE0E6;border:16px solid #8C6A4A}
.rope{position:absolute;left:110px;top:1290px;width:860px;height:4px;background:#8C6A4A;border-radius:2px}
.pep{position:absolute;width:46px;height:150px;background:linear-gradient(90deg,#B8321F,#D8452A 60%,#A82A1A);border-radius:24px 24px 40px 40px/30px 30px 120px 120px;opacity:0;animation:hang 1.2s ease-out both}
.pep:before{content:"";position:absolute;left:16px;top:-16px;width:14px;height:22px;background:#4E7A3A;border-radius:5px}
@keyframes hang{0%{opacity:0;transform:translateY(-60px) rotate(-12deg)}70%{opacity:1;transform:translateY(6px) rotate(4deg)}100%{opacity:1;transform:none}}
'''
s_scene = '<div class="sun"></div><div class="wall"></div><div class="win"></div><div class="rope"></div>' + pep

# 2. Kova e pusit: litari, rrota, kova që ngjitet dorë pas dore
w_css = '''
body{background:#E4ECE6;color:#221F1C}
.lab{color:#3F6259}.h{color:#221F1C}.h em{color:#3F6259}
.grass{position:absolute;left:0;right:0;top:1560px;bottom:0;background:#9DB39A}
.post{position:absolute;top:1140px;width:26px;height:440px;background:#6E523A}
.beam{position:absolute;left:330px;top:1140px;width:420px;height:26px;background:#6E523A}
.wheel{position:absolute;left:500px;top:1110px;width:80px;height:80px;border-radius:50%;border:12px solid #5E4632;box-sizing:border-box;animation:spin 19s linear both}
@keyframes spin{to{transform:rotate(1080deg)}}
.well{position:absolute;left:300px;top:1440px;width:480px;height:200px;background:repeating-linear-gradient(180deg,#B9A58A 0 46px,#A8937A 46px 50px);border-radius:12px}
.hole{position:absolute;left:330px;top:1424px;width:420px;height:40px;background:#3B3A36;border-radius:50%}
.rope{position:absolute;left:536px;top:1180px;width:6px;height:300px;background:#8C6A4A;transform-origin:top;animation:rope 19s ease-in-out both}
@keyframes rope{0%,8%{transform:scaleY(1)}22%{transform:scaleY(.82)}26%{transform:scaleY(.82)}40%{transform:scaleY(.6)}44%{transform:scaleY(.6)}58%{transform:scaleY(.38)}62%{transform:scaleY(.38)}76%,100%{transform:scaleY(.12)}}
.bucket{position:absolute;left:500px;top:1440px;width:80px;height:90px;background:#8E9AA0;border-radius:6px 6px 16px 16px;animation:up 19s ease-in-out both}
.bucket:before{content:"";position:absolute;left:6px;right:6px;top:10px;height:18px;background:#7FB3C8;border-radius:4px}
@keyframes up{0%,8%{transform:translateY(40px)}22%{transform:translateY(-14px)}26%{transform:translateY(-14px)}40%{transform:translateY(-80px)}44%{transform:translateY(-80px)}58%{transform:translateY(-146px)}62%{transform:translateY(-146px)}76%,100%{transform:translateY(-224px)}}
'''
w_scene = '<div class="grass"></div><div class="post" style="left:330px"></div><div class="post" style="left:724px"></div><div class="beam"></div><div class="rope"></div><div class="bucket"></div><div class="well"></div><div class="hole" style="z-index:0"></div><div class="wheel"></div>'

# 3. Detyrat te tryeza e kuzhinës: fletorja, lapsi që shkruan, avulli i tenxheres
d_css = '''
body{background:#F3EDE3;color:#221F1C}
.lab{color:#3F6259}.h{color:#221F1C}.h em{color:#3F6259}
.wall{position:absolute;left:0;right:0;top:1060px;bottom:0;background:#E9DFCF}
.tiles{position:absolute;left:560px;top:1140px;width:520px;height:300px;background:repeating-linear-gradient(90deg,transparent 0 98px,#D8CCB8 98px 100px),repeating-linear-gradient(0deg,transparent 0 98px,#D8CCB8 98px 100px)}
.stove{position:absolute;left:640px;top:1440px;width:380px;height:300px;background:#DADDD9;border-radius:10px}
.pot{position:absolute;left:720px;top:1340px;width:220px;height:110px;background:#5E6A70;border-radius:10px 10px 40px 40px}
.steam{position:absolute;width:40px;height:120px;border-radius:50%;background:rgba(255,255,255,.75);filter:blur(10px);animation:steam 3s ease-out infinite}
@keyframes steam{0%{opacity:0;transform:translateY(0) scale(.6)}40%{opacity:.8}100%{opacity:0;transform:translateY(-200px) scale(1.4)}}
.table{position:absolute;left:0;top:1640px;width:620px;height:40px;background:#A07A52;border-radius:6px}
.leg{position:absolute;top:1680px;width:30px;height:240px;background:#8C6A4A}
.book{position:absolute;left:110px;top:1560px;width:380px;height:84px;background:#FBF8F1;border-radius:6px;box-shadow:0 6px 10px rgba(0,0,0,.08)}
.line{position:absolute;left:140px;height:6px;background:#3F6259;border-radius:3px;transform-origin:left;animation:write 19s linear both}
@keyframes write{0%{transform:scaleX(0)}100%{transform:scaleX(1)}}
.pencil{position:absolute;left:150px;top:1540px;width:160px;height:16px;background:#E8B96C;border-radius:3px;transform:rotate(-30deg);animation:pen 19s linear both}
@keyframes pen{0%{left:150px}100%{left:440px}}
'''
d_scene = ('<div class="wall"></div><div class="tiles"></div><div class="stove"></div><div class="pot"></div>'
           + ''.join(f'<div class="steam" style="left:{x}px;top:1240px;animation-delay:{d}s"></div>' for x, d in ((760, 0), (820, 1), (880, 2)))
           + '<div class="table"></div><div class="leg" style="left:60px"></div><div class="leg" style="left:540px"></div><div class="book"></div>'
           + '<div class="line" style="top:1586px;width:300px"></div><div class="line" style="top:1612px;width:300px;animation-delay:0s"></div><div class="pencil"></div>')

reels = {
    'specat': page('Chopin, Valsi në sol bemol maxhor, op. 70 nr. 1 (Musopen, CC0)', s_css, s_scene,
                   'Në vjeshtë', 'Gjyshja i lidhte specat në&nbsp;varg.', 'Njërin pas&nbsp;tjetrit.',
                   'I varte në diell. <em>Dhe na mbanin gjithë&nbsp;dimrin.</em>',
                   'Ruaje diçka të ngrohtë nga ditët e mira. <em>Për ditët e&nbsp;ftohta.</em>',
                   'Kur dita është e ftohtë, <em>dikush të dëgjon, pa&nbsp;emër.</em>'),
    'pusi': page('Chopin, Valsi në mi bemol maxhor, B. 46 (Musopen, CC0)', w_css, w_scene,
                 'Te pusi i gjyshit', 'Kova s’ngrihej me një&nbsp;tërheqje.', 'Dorë pas&nbsp;dore.',
                 'Gjyshi s’nxitonte. <em>Uji vinte nga&nbsp;thellë.</em>',
                 'Edhe ajo që e mban thellë <em>del, fjalë pas&nbsp;fjale.</em>',
                 'Nise me një fjalë. <em>Dikush të dëgjon, pa&nbsp;emër.</em>'),
    'detyrat': page('Chopin, Valsi në re bemol maxhor, op. 70 nr. 3 (Musopen, CC0)', d_css, d_scene,
                    'Pas shkolle', 'Detyrat i bënim te tryeza e&nbsp;kuzhinës.', 'Sepse aty ishte&nbsp;nëna.',
                    'Ajo gatuante, ne shkruanim. <em>„Hë, si po&nbsp;shkon?“</em>',
                    'S’na duhej ndihmë me detyrat. <em>Na duhej dikush&nbsp;pranë.</em>',
                    'Kur të duhet dikush pranë, <em>fol këtu, pa&nbsp;emër.</em>'),
}
for name, html in reels.items():
    open(os.path.join(OUT, f'reel-{name}.html'), 'w', encoding='utf-8').write(html)
