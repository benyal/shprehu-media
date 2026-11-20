import os
BASE_FILE = '/home/user/Shprehu-3.5/Claude outputs/reklama/2026-11-13-reels/gen.py'
OUT = os.path.dirname(os.path.abspath(__file__))
ns = {'__file__': BASE_FILE}
exec(open(BASE_FILE, encoding='utf-8').read().split('# 1. Qilimat')[0], ns)
page = ns['page']

# 1. Puzzle-i i dimrit: tabela me copa, një vend bosh, copa e fundit del nga poshtë divanit
p_css = '''
body{background:#EFE9DF;color:#221F1C}
.lab{color:#3F6259}.h{color:#221F1C}.h em{color:#3F6259}
.floor{position:absolute;left:0;right:0;top:1560px;bottom:0;background:#B99A72}
.table{position:absolute;left:120px;top:1150px;width:840px;height:400px;background:#8C6A4A;border-radius:14px;box-shadow:0 20px 40px rgba(40,30,20,.25)}
.pz{position:absolute;width:118px;height:88px;border-radius:10px}
.hole{position:absolute;left:672px;top:1270px;width:118px;height:88px;border-radius:10px;background:#5E4632;box-shadow:inset 0 4px 10px rgba(0,0,0,.35)}
.sofa{position:absolute;left:60px;top:1620px;width:960px;height:160px;background:#4E6A60;border-radius:30px 30px 10px 10px}
.last{position:absolute;left:672px;top:1270px;width:118px;height:88px;border-radius:10px;background:#E8B96C;animation:found 19s ease-in-out both}
@keyframes found{0%,45%{transform:translate(-300px,470px) rotate(-20deg);opacity:0}55%{transform:translate(-300px,420px) rotate(-20deg);opacity:1}70%,100%{transform:translate(0,0) rotate(0);opacity:1}}
'''
cols = ['#3F6259', '#8FB8A8', '#E8B96C', '#B04A2C', '#5B6E8C', '#C9D6D2']
pz = ''
k = 0
for r in range(3):
    for c in range(6):
        x, y = 160 + c * 128, 1180 + r * 90
        if (x, y) == (672, 1270):
            continue
        pz += f'<div class="pz" style="left:{x}px;top:{y}px;background:{cols[k % 6]}"></div>'
        k += 1
p_scene = '<div class="floor"></div><div class="table"></div>' + pz + '<div class="hole"></div><div class="sofa"></div><div class="last"></div>'

# 2. Drita e korridorit: dera gjysmë e hapur, rripi i dritës, ora 22:30
d_css = '''
body{background:#1E2427;color:#FAF7F1}
.lab{color:#8FB8A8}.h{color:#FAF7F1}.h em{color:#E8B96C}
.room{position:absolute;inset:0;background:linear-gradient(#1E2427,#232B2F)}
.door{position:absolute;left:600px;top:980px;width:300px;height:760px;background:#2C3438;border:10px solid #3A4448;border-radius:6px}
.gap{position:absolute;left:600px;top:990px;width:44px;height:740px;background:linear-gradient(90deg,#FFE2A6,#F2C66D);box-shadow:0 0 60px 20px rgba(255,214,140,.35)}
.beam{position:absolute;left:180px;top:1740px;width:470px;height:140px;background:linear-gradient(100deg,rgba(255,214,140,0),rgba(255,214,140,.45));clip-path:polygon(100% 0,100% 100%,0 100%,70% 0)}
.bed{position:absolute;left:80px;top:1480px;width:440px;height:200px;background:#3F6259;border-radius:24px}
.pillow{position:absolute;left:110px;top:1440px;width:160px;height:70px;background:#E9E2D5;border-radius:30px}
.clock{position:absolute;left:150px;top:1300px;font-family:'Courier New',monospace;font-weight:700;font-size:56px;color:#E8B96C}
'''
d_scene = '<div class="room"></div><div class="door"></div><div class="gap"></div><div class="beam"></div><div class="bed"></div><div class="pillow"></div><div class="clock">22:30</div>'

# 3. Radioja: doreza rrotullohet, vija e stacioneve, zhurma bëhet zë
r_css = '''
body{background:#F1EBE1;color:#221F1C}
.lab{color:#B04A2C}.h{color:#221F1C}.h em{color:#B04A2C}
.shelf{position:absolute;left:0;right:0;top:1600px;bottom:0;background:#A88560}
.radio{position:absolute;left:150px;top:1170px;width:780px;height:430px;background:#8C4A2F;border-radius:40px;box-shadow:0 24px 40px rgba(40,30,20,.3)}
.grill{position:absolute;left:200px;top:1220px;width:380px;height:330px;border-radius:24px;background:repeating-linear-gradient(0deg,#5E3A24 0 10px,#7A4A2F 10px 20px)}
.dial{position:absolute;left:620px;top:1240px;width:260px;height:70px;background:#F3E6C8;border-radius:10px}
.needle{position:absolute;left:630px;top:1236px;width:6px;height:78px;background:#B04A2C;animation:tune 19s ease-in-out both}
@keyframes tune{0%{transform:translateX(0)}20%{transform:translateX(60px)}30%{transform:translateX(30px)}50%{transform:translateX(150px)}60%,100%{transform:translateX(120px)}}
.knob{position:absolute;left:690px;top:1380px;width:130px;height:130px;border-radius:50%;background:#2E2A26;animation:turn 19s ease-in-out both}
.knob:after{content:"";position:absolute;left:60px;top:10px;width:10px;height:40px;background:#F3E6C8;border-radius:5px}
@keyframes turn{0%{transform:rotate(0)}20%{transform:rotate(90deg)}30%{transform:rotate(45deg)}50%{transform:rotate(220deg)}60%,100%{transform:rotate(180deg)}}
.noise{position:absolute;left:230px;top:1040px;width:320px;height:80px;background:repeating-linear-gradient(90deg,#B04A2C 0 4px,transparent 4px 12px);opacity:.5;animation:quiet 19s linear both}
@keyframes quiet{0%,45%{opacity:.55}60%,100%{opacity:0}}
.wave{position:absolute;left:230px;top:1060px;width:320px;height:40px;border-bottom:6px solid #3F6259;border-radius:0 0 50% 50%;opacity:0;animation:clear 19s linear both}
@keyframes clear{0%,55%{opacity:0}65%,100%{opacity:1}}
.clock{position:absolute;left:640px;top:1060px;font-family:'Courier New',monospace;font-weight:700;font-size:52px;color:#B04A2C}
'''
r_scene = '<div class="shelf"></div><div class="radio"></div><div class="grill"></div><div class="dial"></div><div class="needle"></div><div class="knob"></div><div class="noise"></div><div class="wave"></div><div class="clock">21:30</div>'

reels = {
    'puzzle': page('Chopin, Nocturne në mi bemol maxhor, op. 9 nr. 2 (Musopen, CC0)', p_css, p_scene,
                   'Dimrit, në dhomën e ndenjes', 'Puzzle-i me njëmijë copa zgjaste gjithë&nbsp;dimrin.', 'Gjithmonë mungonte një&nbsp;copë.',
                   'E gjenim në fund, <em>poshtë&nbsp;divanit.</em>',
                   'Edhe copa jote që mungon <em>nuk ka humbur. Pret të&nbsp;gjendet.</em>',
                   'Kërkoje bashkë me dikë. <em>Fol këtu, pa&nbsp;emër.</em>'),
    'korridori': page('Chopin, Preludi në re bemol maxhor, op. 28 nr. 15 (Musopen, CC0)', d_css, d_scene,
                      'Ora 22:30', 'Kur kishim frikë nga errësira, nëna e linte derën&nbsp;hapur.', 'Dhe dritën e korridorit&nbsp;ndezur.',
                      'Një rrip drite mjaftonte <em>që të flinim të&nbsp;qetë.</em>',
                      'Edhe sot, nuk duhet gjithë drita. <em>Mjafton një derë&nbsp;hapur.</em>',
                      'Kur nata rëndon, <em>dikush të dëgjon, pa&nbsp;emër.</em>'),
    'radioja': page('Chopin, Balada nr. 4 në fa minor, op. 52 (hyrja, CC0)', r_css, r_scene,
                    'Ora 21:30', 'Gjyshi e rrotullonte dorezën e radios&nbsp;ngadalë.', 'Fillimisht vetëm&nbsp;zhurmë.',
                    'Pastaj, një zë <em>i&nbsp;qartë.</em>',
                    'Edhe mendimet kanë zhurmë <em>derisa gjen stacionin&nbsp;tënd.</em>',
                    'Fol, derisa të dëgjosh veten qartë. <em>Pa&nbsp;emër.</em>'),
}
for name, html in reels.items():
    open(os.path.join(OUT, f'reel-{name}.html'), 'w', encoding='utf-8').write(html)
    print(name)
