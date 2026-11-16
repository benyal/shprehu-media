import os
BASE = '/home/user/Shprehu-3.5/Claude outputs/reklama/2026-11-12-tiktok-ftohti/burimi/gen.py'
OUT = os.path.dirname(os.path.abspath(__file__))
ns = {'__file__': BASE}
exec(open(BASE, encoding='utf-8').read().split('# 01:')[0], ns)
page, slide, end, D, H = ns['page'], ns['slide'], ns['end'], ns['D'], ns['H']

# 01: „Fike dritën, se rryma s’është falas!“ (rregull i pashkruar), llamba fiket dhe në fund ndizet sërish
def bulb(x, y, on):
    glow = D(x - 110, y - 110, 380, 380, 'border-radius:50%;background:radial-gradient(circle,rgba(255,214,120,.55),rgba(255,214,120,0) 65%)') if on else ''
    return (glow + D(x + 76, y - 200, 8, 210, 'background:#3A3A3A')
            + D(x, y, 160, 180, f'border-radius:50% 50% 45% 45%;background:{"#FFE29A" if on else "#D9D3C7"};box-shadow:inset 0 -10px 0 rgba(0,0,0,.06)')
            + D(x + 40, y + 170, 80, 50, 'background:#9A948A;border-radius:6px'))
def switch(x, y, on):
    return (D(x, y, 120, 180, 'background:#FBF6EA;border-radius:16px;box-shadow:0 8px 16px rgba(60,40,20,.15)')
            + D(x + 35, y + (30 if on else 90), 50, 60, 'background:#C9C3B6;border-radius:10px'))
def set1():
    W = 6480
    b = []
    states = [True, False, False, False, True]
    for i, on in enumerate(states):
        b.append(bulb(i * 1080 + 460, 1500, on))
        b.append(switch(i * 1080 + 820, 1560, on))
    b.append(slide(0, 'lt', 'Rregull i pashkruar', '„Fike dritën, <em>se rryma s’është&nbsp;falas!“</em>', hint=H))
    b.append(slide(1, 'lt', 'Gjithmonë', 'Dilje nga dhoma dhe dikush e fikte pas teje. <em>Klik.</em>'))
    b.append(slide(2, 'lt', 'Mësuam', 'Të kursejmë dritën. <em>Edhe atë brenda&nbsp;nesh.</em>'))
    b.append(slide(3, 'lt', 'E vërteta', 'U bëmë të qetë, të vegjël, që të mos „harxhojmë“. <em>Por drita jote s’është&nbsp;luks.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'Ndize pak dritën tënde. <em>Edhe nëse dikush e&nbsp;sheh.</em>', 'Cila fjali e shtëpisë të kujtohet më shumë? Shkruaje në&nbsp;koment.'))
    b.append(end(5, 'Fol pa e ulur zërin. <em>Dikush të dëgjon, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(90deg,#F4EEE2 0%,#E4DED2 20%,#D9D2C4 60%,#F4EEE2 100%)', ''.join(b))

# 02: ora 21:00, video-thirrja (sjellje e fshehur me orë), korniza e kamerës tregon vetëm cepin e rregulluar
def room(x, mess):
    o = D(x + 200, 1300, 760, 520, 'background:#EDE6D8;border-radius:12px')
    o += D(x + 520, 1380, 300, 220, 'background:#C9D3B0;border-radius:8px;box-shadow:inset 0 0 0 12px #FBF6EA')
    o += D(x + 560, 1640, 220, 120, 'background:#8C6A4A;border-radius:6px')
    if mess:
        for k, (dx, dy, w, h, c, r) in enumerate([(230, 1660, 200, 60, '#5B6E8C', -12), (270, 1720, 160, 70, '#B04A2C', 18), (240, 1560, 120, 120, '#E8B96C', 30), (330, 1600, 140, 50, '#3F6259', -25), (880, 1700, 70, 100, '#9A948A', 8)]):
            o += D(x + dx, dy, w, h, f'background:{c};border-radius:10px;transform:rotate({r}deg)')
    o += D(x + 480, 1340, 380, 460, 'border:6px solid #E8B96C;border-radius:16px')
    o += D(x + 500, 1350, 60, 30, 'background:#B04A2C;border-radius:6px;font-size:18px;font-weight:700;color:#fff;display:flex;align-items:center;justify-content:center', 'LIVE')
    return o
def set2():
    W = 6480
    b = []
    for i in range(5):
        b.append(room(i * 1080, i < 4))
    b.append(slide(0, 'dk', 'Ora 21:00', 'Para video-thirrjes, <em>rregullon vetëm cepin që del në&nbsp;kamerë.</em>', hint=H))
    b.append(slide(1, 'dk', 'Ora 21:02', 'Rrobat te karrigia, enët në tavolinë. <em>Jashtë kornizës, s’ekzistojnë.</em>'))
    b.append(slide(2, 'dk', 'Ora 21:05', '„Si je?“ „Mirë, shumë mirë.“ <em>Edhe kjo jashtë&nbsp;kornizës.</em>'))
    b.append(slide(3, 'dk', 'E vërteta', 'Të gjithë tregojmë vetëm cepin e rregulluar. <em>Rrëmuja s’të bën më pak.</em>'))
    b.append(slide(4, 'dk', 'Sot', 'Diku ke të drejtë ta tregosh gjithë dhomën. <em>Edhe rrëmujën.</em>', 'Çfarë fsheh ti jashtë kamerës? Shkruaje në koment, pa&nbsp;turp.'))
    b.append(end(5, 'Këtu s’ka kamerë. <em>Fol si je vërtet, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#1E2629 0%,#232D31 62%,#1B2326 100%)', ''.join(b))

# 03: gërshetat e mëngjesit (ritual), gërsheta rritet nga slide-i në slide
def braid(x, n):
    o = ''
    for k in range(n):
        side = -1 if k % 2 else 1
        o += D(x + side * 18, 1300 + k * 70, 70, 90, f'background:#5E3A24;border-radius:50%;transform:rotate({side * 30}deg);box-shadow:inset 0 -10px 0 rgba(0,0,0,.18)')
    o += D(x - 10, 1300 + n * 70 + 20, 90, 24, 'background:#B04A2C;border-radius:12px')
    return o
def set3():
    W = 6480
    b = []
    for i, n in enumerate([2, 3, 4, 5, 6]):
        b.append(D(i * 1080 + 740, 1180, 220, 160, 'background:#5E3A24;border-radius:110px 110px 30px 30px'))
        b.append(braid(i * 1080 + 815, n))
    b.append(slide(0, 'lt', 'Ritual', 'Çdo mëngjes, para shkollës, <em>nëna na bënte&nbsp;gërsheta.</em>', hint=H))
    b.append(slide(1, 'lt', 'Pak shtrënguar', '„Rri pa lëvizur!“ <em>Dhe ne rrinim, me sytë&nbsp;mbyllur.</em>'))
    b.append(slide(2, 'lt', 'Gjatë asaj kohe', 'Ajo pyeste për mësimet, për shoqet, <em>për gjithçka.</em>'))
    b.append(slide(3, 'lt', 'E vërteta', 'Dhjetë minuta të njëjtat çdo ditë. <em>Ishin biseda, jo&nbsp;vetëm&nbsp;flokë.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'Gjej një ritual të vogël me dikë. <em>Dhjetë minuta mjaftojnë.</em>', 'Kush t’i bënte gërshetat ty? Shkruaje në&nbsp;koment.'))
    b.append(end(5, 'Kur s’ke kush të pyet për ditën, <em>trego këtu, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#F6EEE6 0%,#F1E6DC 100%)', ''.join(b))

# 04: 5 shenja të vogla që po bëhesh më mirë (listë me boshllëk), dielli lind nga slide-i në slide
def set4():
    W = 7560
    b = []
    for i in range(7):
        y = 1700 - i * 60
        b.append(D(i * 1080 + 640, y, 220, 220, f'border-radius:50%;background:radial-gradient(circle,#FFD58A,#E8B96C 70%);opacity:{0.35 + i * 0.1:.2f}'))
    b.append(D(0, 1780, W - 1080, 140, 'background:#3F6259'))
    b.append(slide(0, 'lt', 'Listë', '5 shenja të vogla që po bëhesh <em>më&nbsp;mirë.</em>', 'E katërta është më e rëndësishmja.', hint=H))
    b.append(slide(1, 'lt', 'E para', 'E hap dritaren <em>në&nbsp;mëngjes.</em>'))
    b.append(slide(2, 'lt', 'E dyta', 'U përgjigjesh mesazheve <em>pa i shtyrë.</em>'))
    b.append(slide(3, 'lt', 'E treta', 'Kafja <em>të shijon&nbsp;sërish.</em>'))
    b.append(slide(4, 'lt', 'E katërta', 'Flet për atë që ndodhi <em>pa ju dridhur&nbsp;zëri.</em>', 'Kjo s’vjen vetë. Vjen pasi e ke thënë disa&nbsp;herë.'))
    b.append(slide(5, 'lt', 'E pesta', 'Bën plane <em>për javën&nbsp;tjetër.</em>', 'Sa prej këtyre i ke këtë javë? Shkruaj numrin në&nbsp;koment.'))
    b.append(end(6, 'Hapi i katërt nis me fjalinë e parë. <em>Thuaje këtu, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(90deg,#E4E6EA 0%,#EFE6DA 45%,#F8E8CF 100%)', ''.join(b))

# 05: „Pika-pika bëhet lumë“ (urtësi e gjyshërve), pikat mbushin gotën dhe në fund dalin si lumë
def glass(x, level):
    o = D(x, 1380, 260, 380, 'border:8px solid rgba(63,98,89,.45);border-top:0;border-radius:0 0 40px 40px;box-sizing:border-box')
    if level:
        o += D(x + 8, 1380 + 372 - level, 244, level, 'background:linear-gradient(#9CC3D6,#6FA3BE);border-radius:0 0 32px 32px')
    o += D(x + 115, 1240, 30, 44, 'background:#6FA3BE;border-radius:50% 50% 50% 50%/60% 60% 40% 40%')
    return o
def set5():
    W = 6480
    b = []
    for i, lv in enumerate([20, 90, 180, 300]):
        b.append(glass(i * 1080 + 620, lv))
    b.append(D(4320, 1640, 1080, 120, 'background:linear-gradient(90deg,#9CC3D6,#6FA3BE);border-radius:60px 0 0 60px'))
    b.append(D(4320 + 200, 1600, 860, 40, 'background:repeating-linear-gradient(90deg,rgba(255,255,255,.6) 0 40px,transparent 40px 90px);border-radius:20px'))
    b.append(slide(0, 'lt', 'Gjyshja', '„Pika-pika <em>bëhet&nbsp;lumë.“</em>', hint=H))
    b.append(slide(1, 'lt', 'Kur ishim të vegjël', 'Na dukej se s’ndryshonte asgjë. <em>Një pikë, pastaj&nbsp;tjetra.</em>'))
    b.append(slide(2, 'lt', 'Ajo e dinte', 'Edhe gota mbushet pa e parë kur. <em>Mjafton të mos&nbsp;ndalesh.</em>'))
    b.append(slide(3, 'lt', 'Edhe sot', 'Një fjali në ditë, një frymë e thellë, një bisedë. <em>Pika të&nbsp;vogla.</em>'))
    b.append(slide(4, 'lt', 'Pastaj', 'Një ditë, kthehesh pas dhe e sheh. <em>Ishte&nbsp;lumë.</em>', 'Çfarë thënie të gjyshes e mban mend? Shkruaje në&nbsp;koment.'))
    b.append(end(5, 'Fillo me një pikë sot. <em>Dikush të dëgjon, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#F1F3EF 0%,#ECEEE8 100%)', ''.join(b))

SETS = [('01-drita', set1), ('02-kamera', set2), ('03-gershetat', set3), ('04-shenjat', set4), ('05-pikapika', set5)]
if __name__ == '__main__':
    for name, fn in SETS:
        w, html = fn()
        open(os.path.join(OUT, f'set-{name}.html'), 'w', encoding='utf-8').write(html)
        print(name, w)
