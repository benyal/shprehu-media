import os
BASE_FILE = '/home/user/Shprehu-3.5/Claude outputs/reklama/2026-11-13-reels/gen.py'
OUT = os.path.dirname(os.path.abspath(__file__))
ns = {'__file__': BASE_FILE}
exec(open(BASE_FILE, encoding='utf-8').read().split('# 1. Qilimat')[0], ns)
page = ns['page']

# 1. Gjyshja i fliste maces: dhoma në mbrëmje, karrigia me shall, macja në prag të dritares që lëviz bishtin
m_css = '''
body{background:#F2E6D3;color:#221F1C}
.lab{color:#8C4A2F}.h{color:#221F1C}.h em{color:#8C4A2F}
.room{position:absolute;inset:0;background:linear-gradient(#F4E9D8 0%,#EFE0C8 62%,#D9BF98 63%,#CFB28A 100%)}
.win{position:absolute;left:600px;top:1040px;width:400px;height:420px;background:linear-gradient(#3C4E66,#6E6A86 70%,#C48A6A);border:18px solid #FBF6EA;box-sizing:border-box}
.win:before{content:"";position:absolute;left:50%;top:0;bottom:0;width:12px;margin-left:-6px;background:#FBF6EA}
.win:after{content:"";position:absolute;left:70px;top:60px;width:46px;height:46px;border-radius:50%;background:#F6E7B8;box-shadow:0 0 40px rgba(246,231,184,.7)}
.sill{position:absolute;left:570px;top:1450px;width:460px;height:30px;background:#FBF6EA;border-radius:6px;box-shadow:0 8px 14px rgba(60,40,20,.15)}
.cat{position:absolute;left:650px;top:1330px;width:190px;height:122px;transform:scale(1.55);transform-origin:0 100%}
.cat .body{position:absolute;left:30px;top:30px;width:160px;height:92px;background:#3A332E;border-radius:80px 80px 30px 30px}
.cat .head{position:absolute;left:0;top:10px;width:84px;height:74px;background:#3A332E;border-radius:50%}
.cat .ear{position:absolute;top:-6px;width:0;height:0;border-left:16px solid transparent;border-right:16px solid transparent;border-bottom:30px solid #3A332E}
.cat .eye{position:absolute;top:38px;width:12px;height:6px;background:#E8B96C;border-radius:6px}
.tail{position:absolute;left:170px;top:80px;width:120px;height:22px;background:#3A332E;border-radius:11px;transform-origin:0 50%;animation:tail 2.6s ease-in-out infinite}
@keyframes tail{0%,100%{transform:rotate(-6deg)}50%{transform:rotate(24deg)}}
.chair{position:absolute;left:90px;top:1180px;width:300px;height:520px}
.chair .back{position:absolute;left:20px;top:0;width:220px;height:300px;background:#8C5A3A;border-radius:110px 110px 14px 14px}
.chair .seat{position:absolute;left:0;top:280px;width:290px;height:70px;background:#7A4C30;border-radius:14px}
.chair .leg{position:absolute;top:340px;width:24px;height:180px;background:#6A4028;border-radius:6px}
.shawl{position:absolute;left:50px;top:60px;width:170px;height:250px;background:repeating-linear-gradient(135deg,#B04A2C 0 18px,#C9663F 18px 36px);border-radius:20px;transform:rotate(-6deg);opacity:.95}
.dot{position:absolute;width:14px;height:14px;border-radius:50%;background:#8C4A2F;opacity:0;animation:dot 3s ease-in-out infinite}
@keyframes dot{0%{opacity:0;transform:translate(0,0)}25%{opacity:.7}100%{opacity:0;transform:translate(260px,40px)}}
'''
m_scene = '''<div class="room"></div><div class="win"></div><div class="sill"></div>
<div class="cat"><div class="tail"></div><div class="body"></div><div class="head"><div class="ear" style="left:6px"></div><div class="ear" style="left:46px"></div><div class="eye" style="left:20px"></div><div class="eye" style="left:52px"></div></div></div>
<div class="chair"><div class="back"><div class="shawl"></div></div><div class="seat"></div><div class="leg" style="left:20px"></div><div class="leg" style="left:246px"></div></div>
''' + ''.join(f'<div class="dot" style="left:400px;top:{1290 + k * 26}px;animation-delay:{k * 0.9}s"></div>' for k in range(3))

# 2. Kutia me kartolina: kutia e këpucëve e hapur, kartolinat në radhë, një kartolinë ngrihet dhe lexohet
k_css = '''
body{background:#EEF0EC;color:#221F1C}
.lab{color:#3F6259}.h{color:#221F1C}.h em{color:#3F6259}
.table{position:absolute;inset:0;background:linear-gradient(#EEF0EC 0%,#E8E6DD 60%,#C9B497 61%,#B99F7E 100%)}
.box{position:absolute;left:140px;top:1440px;width:800px;height:330px;background:#C9A57A;border-radius:10px;box-shadow:0 18px 30px rgba(60,40,20,.25)}
.box:after{content:"";position:absolute;left:0;right:0;top:0;height:40px;background:rgba(0,0,0,.08)}
.lid{position:absolute;left:600px;top:1300px;width:420px;height:90px;background:#D9B78C;border-radius:10px;transform:rotate(-14deg);box-shadow:0 10px 20px rgba(60,40,20,.2)}
.card{position:absolute;top:1330px;width:300px;height:190px;border-radius:8px;box-shadow:0 6px 12px rgba(60,40,20,.15)}
.lift{position:absolute;left:330px;top:1330px;width:420px;height:270px;background:#FBF6EA;border-radius:10px;box-shadow:0 20px 40px rgba(60,40,20,.25);animation:lift 19s ease-in-out both;padding:34px 36px;box-sizing:border-box}
@keyframes lift{0%,20%{transform:translateY(80px) rotate(0)}36%,100%{transform:translateY(-150px) rotate(-4deg)}}
.lift .st{position:absolute;right:28px;top:26px;width:70px;height:86px;background:#8FB8A8;border:5px dashed #FBF6EA;outline:2px solid #8FB8A8}
.lift .w{font-family:'Fraunces',serif;font-style:italic;font-size:46px;color:#2E4A43;line-height:1.2}
.lift .ln{height:4px;background:rgba(46,74,67,.25);margin-top:26px;width:62%}
'''
cards = ''.join(f'<div class="card" style="left:{170 + i * 120}px;background:{c};transform:rotate({r}deg)"></div>'
                for i, (c, r) in enumerate([('#E7D3B1', -6), ('#D6E2DA', 4), ('#F1D9CF', -2), ('#E3DCC9', 6), ('#DCE3EA', -4), ('#EAD7B9', 3)]))
k_scene = f'''<div class="table"></div>{cards}<div class="box"></div><div class="lid"></div>
<div class="lift"><div class="st"></div><div class="w">Gëzuar 1998!</div><div class="ln"></div><div class="ln" style="width:48%"></div></div>'''

reels = {
    'macja': page('Chopin, Souvenir de Paganini, B. 37 (CC0)', m_css, m_scene,
                  'Te gjyshja', 'Gjyshja i tregonte maces të gjitha&nbsp;hallet.', 'Çdo&nbsp;mbrëmje.',
                  'Macja s’jepte këshilla. <em>Vetëm rrinte&nbsp;aty.</em>',
                  'Dhe gjyshja ngrihej më e lehtë. <em>Ndonjëherë mjafton ta thuash me&nbsp;zë.</em>',
                  'Thuaje me zë. <em>Dikush rri dhe të dëgjon, pa&nbsp;emër.</em>'),
    'kartolinat': page('Chopin, Nocturne në fa minor, op. 55 nr. 1 (CC0)', k_css, k_scene,
                       'Në dollap', 'Nëna kishte një kuti këpucësh plot&nbsp;kartolina.', '„Gëzuar&nbsp;1998!“',
                       'Nga njerëz që s’i kishim parë prej vitesh. <em>Dy rreshta, dhe ajo i ruante të&nbsp;gjitha.</em>',
                       'Dy rreshta mjaftonin. <em>Sot një „si je?“ e vërtetë mjafton&nbsp;njësoj.</em>',
                       'Shkruaje atë që ke në zemër. <em>Dikush e lexon, pa&nbsp;emër.</em>')
}
for name, html in reels.items():
    open(os.path.join(OUT, f'reel-{name}.html'), 'w', encoding='utf-8').write(html)
    print(name)
