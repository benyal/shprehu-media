import os
BASE_FILE = '/home/user/Shprehu-3.5/Claude outputs/reklama/2026-11-13-reels/gen.py'
OUT = os.path.dirname(os.path.abspath(__file__))
ns = {'__file__': BASE_FILE}
exec(open(BASE_FILE, encoding='utf-8').read().split('# 1. Qilimat')[0], ns)
page = ns['page']

# 1. Xhupi i vëllait të madh: dollapi i hapur, xhupi i madh në varëse me mëngët e palosura
x_css = '''
body{background:#E8EEF0;color:#221F1C}
.lab{color:#3F6259}.h{color:#221F1C}.h em{color:#3F6259}
.wall{position:absolute;inset:0;background:linear-gradient(#EAF0F1 0%,#E4EBEC 62%,#C9B497 63%,#BFA785 100%)}
.ward{position:absolute;left:150px;top:1000px;width:780px;height:760px;background:#8C6A4A;border-radius:12px;box-shadow:0 20px 40px rgba(60,40,20,.25)}
.ward .in{position:absolute;left:30px;top:30px;right:30px;bottom:30px;background:#5E4632;border-radius:6px}
.rod{position:absolute;left:180px;top:1080px;width:720px;height:12px;background:#C9C3B6;border-radius:6px}
.hanger{position:absolute;top:1060px;width:4px;height:40px;background:#C9C3B6}
.jacket{position:absolute;left:300px;top:1110px;width:460px;height:560px;animation:sw 4s ease-in-out infinite alternate;transform-origin:50% 0}
@keyframes sw{0%{transform:rotate(-1.2deg)}100%{transform:rotate(1.2deg)}}
.jacket .b{position:absolute;left:80px;top:0;width:300px;height:520px;background:#3F6259;border-radius:60px 60px 24px 24px}
.jacket .z{position:absolute;left:228px;top:40px;width:6px;height:470px;background:#2E4A43}
.jacket .s{position:absolute;top:20px;width:110px;height:470px;background:#36574E;border-radius:50px 50px 20px 20px}
.jacket .cuff{position:absolute;bottom:0;left:0;right:0;height:70px;background:repeating-linear-gradient(180deg,#2E4A43 0 14px,#3F6259 14px 24px);border-radius:0 0 20px 20px}
.small{position:absolute;left:620px;top:1140px;width:120px;height:200px;background:#E8B96C;border-radius:30px 30px 12px 12px;opacity:.9}
'''
x_scene = '''<div class="wall"></div><div class="ward"><div class="in"></div></div><div class="rod"></div>
<div class="hanger" style="left:528px"></div>
<div class="jacket"><div class="s" style="left:0"><div class="cuff"></div></div><div class="s" style="right:0"><div class="cuff"></div></div><div class="b"></div><div class="z"></div></div>'''

# 2. Bastuni i gjyshit: hyrja e shtëpisë, varësja me plisin dhe bastuni që mbështetet te karrigia
b_css = '''
body{background:#F1E9DC;color:#221F1C}
.lab{color:#8C4A2F}.h{color:#221F1C}.h em{color:#8C4A2F}
.wall{position:absolute;inset:0;background:linear-gradient(#F3ECE0 0%,#EEE4D3 64%,#B99F7E 65%,#AE9670 100%)}
.door{position:absolute;left:620px;top:960px;width:380px;height:800px;background:#7A5338;border-radius:8px 8px 0 0;box-shadow:inset 0 0 0 16px #5E3E28}
.door b{position:absolute;left:40px;top:420px;width:26px;height:26px;border-radius:50%;background:#E8B96C}
.rack{position:absolute;left:150px;top:1030px;width:340px;height:30px;background:#8C6A4A;border-radius:8px}
.peg{position:absolute;top:1058px;width:16px;height:40px;background:#6A4A32;border-radius:6px}
.plis{position:absolute;left:190px;top:1080px;width:130px;height:90px;background:#FBF6EA;border-radius:65px 65px 10px 10px;box-shadow:inset 0 -12px 0 #E8DCC4}
.coat{position:absolute;left:330px;top:1080px;width:130px;height:380px;background:#5B5248;border-radius:40px 40px 14px 14px}
.chair{position:absolute;left:140px;top:1440px;width:300px;height:330px}
.chair .seat{position:absolute;left:0;top:120px;width:300px;height:44px;background:#7A4C30;border-radius:10px}
.chair .back{position:absolute;left:10px;top:-100px;width:40px;height:230px;background:#6A4028;border-radius:10px}
.chair .leg{position:absolute;top:160px;width:26px;height:170px;background:#6A4028;border-radius:6px}
.cane{position:absolute;left:470px;top:1290px;width:22px;height:480px;background:linear-gradient(90deg,#8C5A3A,#B98A5E,#8C5A3A);border-radius:11px;transform-origin:50% 100%;transform:rotate(-9deg)}
.cane:before{content:"";position:absolute;left:-60px;top:-28px;width:82px;height:60px;border:20px solid #9C6A44;border-bottom:0;border-right:0;border-radius:60px 0 0 0;box-sizing:border-box}
.light{position:absolute;left:560px;top:880px;width:500px;height:500px;border-radius:50%;background:radial-gradient(circle,rgba(255,226,160,.45),rgba(255,226,160,0) 65%);animation:glow 6s ease-in-out infinite alternate}
@keyframes glow{0%{opacity:.6}100%{opacity:1}}
'''
b_scene = '''<div class="wall"></div><div class="light"></div><div class="door"><b></b></div>
<div class="rack"></div><div class="peg" style="left:240px"></div><div class="peg" style="left:390px"></div>
<div class="plis"></div><div class="coat"></div>
<div class="chair"><div class="back"></div><div class="seat"></div><div class="leg" style="left:20px"></div><div class="leg" style="left:254px"></div></div>
<div class="cane"></div>'''

# 3. Ditari me dry: ditari mbi tavolinë, kapësja e flokëve që e hap drynin
d_css = '''
body{background:#F4EEF0;color:#221F1C}
.lab{color:#3F6259}.h{color:#221F1C}.h em{color:#3F6259}
.desk{position:absolute;inset:0;background:linear-gradient(#F4EEF0 0%,#EFE7EA 60%,#C9A57A 61%,#B99068 100%)}
.diary{position:absolute;left:250px;top:1230px;width:520px;height:400px;background:#C9707A;border-radius:14px 22px 22px 14px;box-shadow:0 22px 40px rgba(60,30,30,.28)}
.diary:before{content:"";position:absolute;left:0;top:0;bottom:0;width:46px;background:#A9555F;border-radius:14px 0 0 14px}
.diary .pages{position:absolute;right:-12px;top:14px;bottom:14px;width:16px;background:repeating-linear-gradient(180deg,#FBF6EA 0 4px,#E8DCC4 4px 6px);border-radius:0 6px 6px 0}
.diary .t{position:absolute;left:110px;top:120px;font-family:'Fraunces',serif;font-style:italic;font-size:64px;color:#FBF6EA}
.strap{position:absolute;left:700px;top:1370px;width:110px;height:120px;background:#A9555F;border-radius:12px}
.lock{position:absolute;left:730px;top:1395px;width:66px;height:70px;background:linear-gradient(#E8C67A,#C79A3C);border-radius:12px;box-shadow:0 4px 8px rgba(0,0,0,.2)}
.lock:before{content:"";position:absolute;left:12px;top:-34px;width:42px;height:44px;border:9px solid #C79A3C;border-bottom:0;border-radius:24px 24px 0 0;box-sizing:border-box;animation:open 19s ease-in-out both}
@keyframes open{0%,30%{transform:none}36%,100%{transform:translate(14px,-14px) rotate(20deg)}}
.lock:after{content:"";position:absolute;left:28px;top:28px;width:10px;height:18px;background:#5E4632;border-radius:5px}
.pin{position:absolute;left:850px;top:1500px;width:150px;height:12px;background:#3A3A3A;border-radius:6px;transform-origin:0 50%;animation:pin 19s ease-in-out both}
@keyframes pin{0%,18%{transform:translate(0,0) rotate(0)}30%,100%{transform:translate(-78px,-62px) rotate(-14deg)}}
.pin:after{content:"";position:absolute;left:10px;top:-14px;width:120px;height:10px;background:#3A3A3A;border-radius:6px}
.pencil{position:absolute;left:180px;top:1680px;width:420px;height:24px;background:linear-gradient(90deg,#E8B96C 0 88%,#F1D9CF 88% 94%,#3A3A3A 94%);border-radius:4px;transform:rotate(-4deg)}
'''
d_scene = '''<div class="desk"></div><div class="diary"><div class="pages"></div><div class="t">Ditari</div></div>
<div class="strap"></div><div class="lock"></div><div class="pin"></div><div class="pencil"></div>'''

reels = {
    'xhupi': page('Chopin, Valsi në si minor, op. 69 nr. 2 (Musopen, CC0)', x_css, x_scene,
                  'Në dollap', 'Xhupi i vëllait të madh më vinte gjithmonë i&nbsp;gjerë.', '„Do rritesh në&nbsp;të.“',
                  'Mëngët i palosnim dy herë. <em>Dhe e mbanim me&nbsp;krenari.</em>',
                  'Por s’ke pse rritesh në rrobat e dikujt tjetër. <em>As në pritjet e&nbsp;tyre.</em>',
                  'Thuaje si je ti, me masën tënde. <em>Dikush të dëgjon, pa&nbsp;emër.</em>'),
    'bastuni': page('Beethoven, Sonata nr. 13 op. 27 nr. 1, Andante, Daniel Veesey (CC0)', b_css, b_scene,
                    'Gjyshi', 'Gjyshi s’kishte turp nga&nbsp;bastuni.', '„Edhe këmbët e forta&nbsp;lodhen.“',
                    'Mbështetej pa e fshehur. <em>Dhe ecte më larg se të&nbsp;gjithë.</em>',
                    'Të mbështetesh s’do të thotë që je i dobët. <em>Do të thotë që do të&nbsp;vazhdosh.</em>',
                    'Mbështetu pak sot. <em>Dikush të dëgjon, pa&nbsp;emër.</em>'),
    'ditari': page('Chopin, Nocturne në mi minor, op. 72 nr. 1 (Musopen, CC0)', d_css, d_scene,
                   'Në sirtar', 'Ditari i shkollës kishte një dry të&nbsp;vogël.', 'Hapej me një kapëse&nbsp;flokësh.',
                   'Aty shkruanim atë që s’ia thoshim askujt. <em>Faqe pas&nbsp;faqeje.</em>',
                   'Na duhej një vend vetëm për ne. <em>Na duhet edhe&nbsp;sot.</em>',
                   'Ditari te Shprehu është vetëm për ty. <em>Shkruaj sot një&nbsp;faqe.</em>')
}
for name, html in reels.items():
    open(os.path.join(OUT, f'reel-{name}.html'), 'w', encoding='utf-8').write(html)
    print(name)
