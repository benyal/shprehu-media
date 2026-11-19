import os
BASE_FILE = '/home/user/Shprehu-3.5/Claude outputs/reklama/2026-11-13-reels/gen.py'
OUT = os.path.dirname(os.path.abspath(__file__))
ns = {'__file__': BASE_FILE}
exec(open(BASE_FILE, encoding='utf-8').read().split('# 1. Qilimat')[0], ns)
page = ns['page']

# 1. Sapuni i gjyshes: copat e vogla ngjiten te sapuni i ri
s_css = '''
body{background:#EEF1EE;color:#221F1C}
.lab{color:#3F6259}.h{color:#221F1C}.h em{color:#3F6259}
.tiles{position:absolute;inset:0;background:#EEF1EE;background-image:linear-gradient(#DDE4E0 2px,transparent 2px),linear-gradient(90deg,#DDE4E0 2px,transparent 2px);background-size:120px 120px}
.sink{position:absolute;left:140px;top:1420px;width:800px;height:300px;background:#FBFBF8;border-radius:30px 30px 160px 160px;box-shadow:0 20px 40px rgba(40,60,60,.18)}
.dish{position:absolute;left:330px;top:1340px;width:420px;height:70px;background:#C9D6D2;border-radius:0 0 40px 40px}
.soap{position:absolute;left:390px;top:1240px;width:300px;height:110px;background:#F1E3C4;border-radius:40px;box-shadow:inset 0 -12px 0 rgba(0,0,0,.06)}
.chip{position:absolute;height:44px;border-radius:22px;box-shadow:inset 0 -6px 0 rgba(0,0,0,.08)}
.c1{left:150px;top:1120px;width:120px;background:#E3B9C5;animation:j1 19s ease-in-out both}
.c2{left:820px;top:1090px;width:100px;background:#BFD7C4;animation:j2 19s ease-in-out both}
.c3{left:500px;top:1020px;width:90px;background:#F2D18A;animation:j3 19s ease-in-out both}
@keyframes j1{0%,30%{transform:translate(0,0)}45%,100%{transform:translate(270px,150px)}}
@keyframes j2{0%,40%{transform:translate(0,0)}55%,100%{transform:translate(-170px,180px)}}
@keyframes j3{0%,50%{transform:translate(0,0)}65%,100%{transform:translate(20px,176px)}}
'''
s_scene = '<div class="tiles"></div><div class="sink"></div><div class="dish"></div><div class="soap"></div><div class="chip c1"></div><div class="chip c2"></div><div class="chip c3"></div>'

# 2. Kutia e kopsave: kuti biskotash plot kopsa, një kops qepet te xhaketa
k_css = '''
body{background:#F4EEE4;color:#221F1C}
.lab{color:#B04A2C}.h{color:#221F1C}.h em{color:#B04A2C}
.table{position:absolute;left:0;right:0;top:1500px;bottom:0;background:#C9A77E}
.tin{position:absolute;left:170px;top:1240px;width:520px;height:330px;border-radius:50%/30%;background:#2F5D7C;box-shadow:0 22px 40px rgba(40,30,20,.3)}
.tin:before{content:"";position:absolute;inset:26px;border-radius:50%/30%;background:#F2EBDD}
.btn{position:absolute;border-radius:50%;box-shadow:inset 0 -5px 0 rgba(0,0,0,.15)}
.btn:after{content:"";position:absolute;left:30%;top:30%;width:40%;height:40%;background:radial-gradient(circle,rgba(0,0,0,.35) 0 18%,transparent 20%) 0 0/50% 50%}
.cloth{position:absolute;left:720px;top:1060px;width:300px;height:520px;background:#5E6E4E;border-radius:24px 24px 8px 8px}
.slot{position:absolute;left:850px;width:44px;height:44px;border-radius:50%}
.new{left:850px;top:1360px;width:44px;height:44px;background:#E8B96C;opacity:0;animation:sew 19s ease-out both}
@keyframes sew{0%,48%{opacity:0;transform:translate(-300px,120px)}62%,100%{opacity:1;transform:translate(0,0)}}
'''
import random
random.seed(7)
cols = ['#E8B96C', '#B04A2C', '#FAF7F1', '#3F6259', '#8C6A4A', '#221F1C', '#C9D6D2']
btns = ''.join(f'<div class="btn" style="left:{230+random.randint(0,380)}px;top:{1300+random.randint(0,190)}px;width:{w}px;height:{w}px;background:{random.choice(cols)}"></div>'
               for w in [random.randint(30, 60) for _ in range(26)])
k_scene = ('<div class="table"></div><div class="tin"></div>' + btns + '<div class="cloth"></div>'
           + ''.join(f'<div class="btn slot" style="top:{t}px;background:#E8B96C"></div>' for t in (1130, 1250, 1470))
           + '<div class="btn new"></div>')

# 3. Ora 21:40, hekurosja: hekuri lëviz, avulli, rrudhat zhduken
h_css = '''
body{background:#22292D;color:#FAF7F1}
.lab{color:#8FB8A8}.h{color:#FAF7F1}.h em{color:#E8B96C}
.room{position:absolute;inset:0;background:linear-gradient(#22292D 0%,#262F33 100%)}
.lamp{position:absolute;left:520px;top:900px;width:700px;height:700px;border-radius:50%;background:radial-gradient(circle,rgba(255,214,150,.22),rgba(255,214,150,0) 65%)}
.board{position:absolute;left:110px;top:1430px;width:860px;height:70px;background:#D8D2C6;border-radius:35px 10px 10px 35px}
.leg1,.leg2{position:absolute;top:1500px;width:14px;height:330px;background:#7C8287}
.leg1{left:340px;transform:rotate(18deg)}.leg2{left:700px;transform:rotate(-18deg)}
.shirt{position:absolute;left:220px;top:1370px;width:640px;height:70px;background:#FAF7F1;border-radius:14px}
.wr{position:absolute;top:1385px;height:8px;width:90px;background:rgba(0,0,0,.18);border-radius:4px;animation:flat 19s linear both}
@keyframes flat{0%,25%{opacity:1}70%,100%{opacity:0}}
.iron{position:absolute;left:250px;top:1260px;width:220px;height:110px;background:#4C6E8C;border-radius:110px 20px 10px 10px;animation:glide 3.2s ease-in-out infinite alternate}
.iron:after{content:"";position:absolute;left:60px;top:-40px;width:120px;height:40px;border:12px solid #2E3A44;border-bottom:0;border-radius:40px 40px 0 0}
@keyframes glide{0%{transform:translateX(0)}100%{transform:translateX(360px)}}
.st{position:absolute;top:1180px;width:40px;height:80px;border-radius:50%;background:rgba(255,255,255,.35);filter:blur(6px);animation:steam 3.2s ease-out infinite}
@keyframes steam{0%{opacity:0;transform:translateY(0)}30%{opacity:.8}100%{opacity:0;transform:translateY(-140px)}}
.clock{position:absolute;left:820px;top:980px;font-family:'Courier New',monospace;font-weight:700;font-size:56px;color:#E8B96C}
'''
h_scene = ('<div class="room"></div><div class="lamp"></div><div class="board"></div><div class="leg1"></div><div class="leg2"></div><div class="shirt"></div>'
           + ''.join(f'<div class="wr" style="left:{x}px"></div>' for x in (290, 430, 580, 720))
           + '<div class="iron"></div>' + ''.join(f'<div class="st" style="left:{x}px;animation-delay:{d}s"></div>' for x, d in ((330, 0), (420, 1.1), (520, 2.1)))
           + '<div class="clock">21:40</div>')

reels = {
    'sapuni': page('Chopin, Nocturne në fa maxhor, op. 15 nr. 1 (Musopen, CC0)', s_css, s_scene,
                   'Në banjë', 'Gjyshja s’e hidhte kurrë copën e vogël të&nbsp;sapunit.', 'E ngjiste te i&nbsp;riu.',
                   'Copë pas cope, <em>bëhej një sapun i&nbsp;ri.</em>',
                   'Edhe copat e vogla të vetes vlejnë. <em>Mos i hidh.</em>',
                   'Mblidhe veten pak nga pak. <em>Dikush të dëgjon, pa&nbsp;emër.</em>'),
    'kopsat': page('Chopin, Polonaza në si bemol maxhor, op. 71 nr. 2 (CC0)', k_css, k_scene,
                   'Kutia e biskotave', 'Te nëna, kutia e biskotave s’kishte kurrë&nbsp;biskota.', 'Kishte&nbsp;kopsa.',
                   'S’hidhte asnjë. <em>„Një ditë do të&nbsp;duhet.“</em>',
                   'Edhe një kopsë e vogël <em>mban gjithë xhaketën&nbsp;bashkë.</em>',
                   'Edhe ti mban më shumë se sa mendon. <em>Fol pa emër, kur të&nbsp;duash.</em>'),
    'hekuri': page('Chopin, Nocturne në la bemol maxhor, op. 32 nr. 2 (Musopen, CC0)', h_css, h_scene,
                   'Ora 21:40', 'Nëna hekuroste natën rrobat për&nbsp;nesër.', 'Rrudhë pas&nbsp;rrudhe.',
                   'Ngadalë, me durim, <em>derisa këmisha bëhej si e&nbsp;re.</em>',
                   'Disa rrudha s’hiqen me hekur. <em>Hiqen me një&nbsp;bisedë.</em>',
                   'Ato të brendshmet, thuaji këtu. <em>Dikush të dëgjon, pa&nbsp;emër.</em>'),
}
for name, html in reels.items():
    open(os.path.join(OUT, f'reel-{name}.html'), 'w', encoding='utf-8').write(html)
    print(name)
