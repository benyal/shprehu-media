import os
BASE = '/home/user/Shprehu-3.5/Claude outputs/reklama/2026-11-12-tiktok-ftohti/burimi/gen.py'
OUT = os.path.dirname(os.path.abspath(__file__))
ns = {'__file__': BASE}
exec(open(BASE, encoding='utf-8').read().split('# 01:')[0], ns)
page, slide, end, D, H = ns['page'], ns['slide'], ns['end'], ns['D'], ns['H']

# 01: stoli i gjyshit nën hardhi (urtësi), stoli i gjatë kalon nëpër të gjitha slide-et
def leaf(x, y, r, rot):
    return D(x, y, r, r, f'background:#6E8B4E;border-radius:0 60% 0 60%;transform:rotate({rot}deg);opacity:.92')
def grapes(x, y):
    o = ''
    for row, n in enumerate([4, 3, 2, 1]):
        for k in range(n):
            o += D(x + k * 34 + row * 17, y + row * 30, 36, 36, 'border-radius:50%;background:radial-gradient(circle at 35% 30%,#9C6BB0,#5E3570 75%)')
    return o
def set1():
    W = 6480
    b = [D(0, 0, W, 34, 'background:#7A5A3A')]
    for k in range(0, W, 150):
        b.append(leaf(k + 20, 20, 120, (k * 7) % 90))
        b.append(leaf(k + 90, 70, 90, (k * 11) % 90 + 20))
    for x in [700, 1900, 3400, 4700]:
        b.append(grapes(x, 120))
    b.append(D(0, 1650, W - 1080, 46, 'background:#9C7A52;border-radius:10px;box-shadow:0 12px 20px rgba(60,40,20,.2)'))
    b.append(D(0, 1700, W - 1080, 18, 'background:#7A5A3A'))
    for x in range(120, W - 1080, 900):
        b.append(D(x, 1718, 34, 200, 'background:#7A5A3A'))
    b.append(D(380, 1590, 170, 64, 'background:#3A3A3A;border-radius:80px 80px 10px 10px'))
    b.append(D(360, 1638, 210, 18, 'background:#2A2A2A;border-radius:9px'))
    b.append(D(1500, 1570, 90, 80, 'background:#FBF6EA;border-radius:0 0 30px 30px;box-shadow:inset 0 -14px 0 #E8DCC4'))
    b.append(D(1585, 1590, 30, 36, 'border:8px solid #FBF6EA;border-left:0;border-radius:0 20px 20px 0'))
    b.append(D(2700, 1600, 260, 50, 'background:#E8DCC4;transform:rotate(-3deg);border-radius:4px;box-shadow:0 4px 0 #D3C6AA'))
    b.append(D(3900, 1490, 380, 160, 'border:6px dashed rgba(63,98,89,.45);border-radius:24px'))
    b.append(slide(0, 'lt', 'Gjyshi', 'Gjyshi kishte një stol nën hardhi. <em>Gjithmonë me një vend&nbsp;bosh.</em>', hint=H))
    b.append(slide(1, 'lt', 'S’pyeste', 'S’të pyeste „çfarë ke?“. <em>Vetëm shtyhej pak&nbsp;mënjanë.</em>'))
    b.append(slide(2, 'lt', 'Pastaj', 'Uleshe pranë tij. <em>Dhe pas pak, fillonte të flisje&nbsp;ti.</em>', 'Ai shikonte rrushin. Ti e nxirrje&nbsp;hallin.'))
    b.append(slide(3, 'lt', 'Ai e dinte', 'Njerëzit s’hapen kur i pyet. <em>Hapen kur u bën&nbsp;vend.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'Lëre një vend bosh pranë teje. <em>Dikush mund të ketë nevojë për&nbsp;të.</em>'))
    b.append(end(5, 'Edhe për ty ka një vend bosh. <em>Ulu dhe fol, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#EEF0E2 0%,#F5F0E2 70%,#E3D5B5 86%,#D9C7A3 100%)', ''.join(b))

# 02: ora 19:00, vrapon derisa mendja të heshtë; shiriti i distancës mbushet nga slide-i në slide
def set2():
    W = 6480
    b = [D(0, 1560, W - 1080, 14, 'background:rgba(250,247,241,.12);border-radius:7px')]
    b.append(D(0, 1560, 3240 + 540, 14, 'background:linear-gradient(90deg,#8FB8A8,#E8B96C);border-radius:7px'))
    for i, (km, t) in enumerate([('0.4', '19:02'), ('2.1', '19:14'), ('5.0', '19:38'), ('5.0', '19:45'), ('5.0', '19:45')]):
        x = i * 1080 + 96
        b.append(D(x, 1610, 600, 150, 'font-family:Fraunces,serif;font-size:130px;font-weight:600;color:#FAF7F1;line-height:1', f'{km}<span style="font-size:52px;color:#8FB8A8"> km</span>'))
        b.append(D(x + 4, 1770, 400, 50, 'font-size:38px;font-weight:600;color:rgba(250,247,241,.6);letter-spacing:.08em', t))
    for i in range(3):
        x = i * 1080 + 760
        b.append(D(x, 1640, 18, 120 - i * 10, 'background:#E8B96C;border-radius:9px;opacity:.75'))
        b.append(D(x + 34, 1600 + i * 12, 18, 160 - i * 30, 'background:#E8B96C;border-radius:9px;opacity:.55'))
        b.append(D(x + 68, 1660, 18, 100 + i * 20, 'background:#E8B96C;border-radius:9px;opacity:.4'))
    b.append(D(3240 + 560, 1580, 300, 220, 'border:5px solid rgba(250,247,241,.35);border-radius:10px 10px 0 0'))
    b.append(D(3240 + 690, 1680, 16, 16, 'border-radius:50%;background:#E8B96C'))
    b.append(slide(0, 'dk', 'Ora 19:00', 'Vrapon derisa mendja <em>të&nbsp;heshtë.</em>', hint=H))
    b.append(slide(1, 'dk', 'Kilometri i dytë', 'Muzika fort, sytë te numrat. <em>Asnjë mendim s’të&nbsp;arrin.</em>'))
    b.append(slide(2, 'dk', 'Kilometri i pestë', 'Trupi lodhet. <em>Mendja, për pak, pushon.</em>'))
    b.append(slide(3, 'dk', 'Ora 19:45', 'Pastaj del nga palestra. <em>Mendimet të presin te&nbsp;dera.</em>'))
    b.append(slide(4, 'dk', 'E vërteta', 'Vrapi të bën mirë, mos e lër. <em>Por disa gjëra s’dalin me djersë. Duan të&nbsp;thuhen.</em>'))
    b.append(end(5, 'Pas vrapit, <em>thuaja dikujt që të dëgjon, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#1E2B2E 0%,#22343A 70%,#1A2629 100%)', ''.join(b))

# 03: „Për hajër!“ (ritual), sende të reja me fjongo, dhe në fund një flluskë bisede me fjongo
def bow(x, y, c='#C0392B'):
    return (D(x - 46, y - 24, 52, 48, f'background:{c};border-radius:50% 10% 10% 50%')
            + D(x + 2, y - 24, 52, 48, f'background:{c};border-radius:10% 50% 50% 10%')
            + D(x - 8, y - 14, 20, 28, f'background:{c};filter:brightness(.8);border-radius:6px'))
def set3():
    W = 6480
    b = [D(0, 1800, W - 1080, 120, 'background:#E6D9C2')]
    b.append(D(240, 1560, 520, 180, 'background:#3F6259;border-radius:90px 120px 30px 30px'))
    b.append(D(300, 1700, 110, 110, 'border-radius:50%;background:#2A2A2A;box-shadow:inset 0 0 0 26px #555'))
    b.append(D(590, 1700, 110, 110, 'border-radius:50%;background:#2A2A2A;box-shadow:inset 0 0 0 26px #555'))
    b.append(D(360, 1590, 140, 60, 'background:#BFD6CE;border-radius:40px 10px 0 0'))
    b.append(bow(500, 1560))
    b.append(D(1080 + 160, 1660, 260, 120, 'background:#B04A2C;border-radius:80px 30px 20px 20px'))
    b.append(D(1080 + 160, 1770, 300, 26, 'background:#F3EBDD;border-radius:13px'))
    b.append(bow(1080 + 300, 1650))
    b.append(D(1080 + 620, 1520, 150, 270, 'background:#2E2A26;border-radius:26px;box-shadow:inset 0 0 0 10px #444'))
    b.append(D(1080 + 640, 1550, 110, 200, 'background:#8FB8A8;border-radius:12px'))
    b.append(bow(1080 + 695, 1515))
    b.append(D(2160 + 300, 1560, 460, 230, 'border:6px dashed rgba(63,98,89,.45);border-radius:30px'))
    b.append(D(3240 + 260, 1500, 560, 260, 'background:#FBF6EA;border-radius:40px;box-shadow:0 14px 30px rgba(60,40,20,.15)'))
    b.append(D(3240 + 330, 1740, 80, 80, 'background:#FBF6EA;clip-path:polygon(0 0,100% 0,0 100%)'))
    for k in range(3):
        b.append(D(3240 + 330, 1560 + k * 56, 420 - k * 90, 22, 'background:#D8CCB4;border-radius:11px'))
    b.append(bow(3240 + 790, 1500))
    b.append(slide(0, 'lt', 'Ritual', 'Makinë e re? <em>„Për hajër!“</em>', 'Flokë të prera? Shtëpi e re? „Për&nbsp;hajër!“', hint=H))
    b.append(slide(1, 'lt', 'Gjithmonë', 'Për çdo gjë të re kemi një urim. <em>Këpucë, telefon, punë, shtëpi.</em>'))
    b.append(slide(2, 'lt', 'Por', 'Kur dikush thotë „kam nisur të flas për hallet e mia“, <em>s’dimë çfarë të&nbsp;themi.</em>'))
    b.append(slide(3, 'lt', 'E vërteta', 'Edhe ky është fillim i ri. <em>Ndoshta më i rëndësishmi nga të&nbsp;gjithë.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'Kur dikush hapet me ty, thuaji: <em>„Për hajër, mirë që e&nbsp;the.“</em>'))
    b.append(end(5, 'Nise edhe ti fillimin tënd. <em>Dikush të dëgjon, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(90deg,#F7EFE6,#F3E9DC)', ''.join(b))

# 04: 5 gjëra që na thanë si fëmijë dhe i besuam (listë me boshllëk), fletorja me vija dhe vija e kuqe e kufirit
def set4():
    W = 7560
    b = []
    for i in range(7):
        b.append(D(i * 1080 + 70, 0, 4, 1920, 'background:rgba(192,57,43,.45)'))
    b.append(D(1080 + 640, 1560, 300, 200, 'background:#3E8E4E;border-radius:0 0 150px 150px'))
    b.append(D(1080 + 660, 1560, 260, 170, 'background:#E8574A;border-radius:0 0 130px 130px'))
    for k, (dx, dy) in enumerate([(60, 30), (130, 60), (200, 30), (100, 100), (170, 100)]):
        b.append(D(1080 + 660 + dx, 1560 + dy, 16, 24, 'background:#2A2A2A;border-radius:50%'))
    b.append(D(2160 + 680, 1560, 220, 220, 'border-radius:50%;background:#F2C14E'))
    b.append(D(2160 + 740, 1630, 26, 26, 'border-radius:50%;background:#2A2A2A'))
    b.append(D(2160 + 810, 1650, 26, 14, 'border-radius:50%;background:#2A2A2A'))
    b.append(D(2160 + 740, 1700, 120, 30, 'border-bottom:10px solid #2A2A2A;border-radius:0 0 50% 50%;transform:rotate(12deg)'))
    b.append(D(3240 + 640, 1600, 300, 170, 'background:#D9A55B;border-radius:120px 120px 40px 40px;box-shadow:inset 0 -24px 0 #C58C42'))
    b.append(D(3240 + 700, 1620, 180, 20, 'background:#E7BE7C;border-radius:10px;transform:rotate(-8deg)'))
    b.append(D(4320 + 560, 1480, 440, 300, 'background:#FBF6EA;border:4px solid #2E2A26;border-radius:10px;transform:rotate(-3deg)'))
    b.append(D(4320 + 600, 1520, 360, 26, 'background:#2E2A26;opacity:.85;transform:rotate(-3deg)'))
    b.append(D(4320 + 600, 1580, 300, 26, 'background:#2E2A26;opacity:.85;transform:rotate(-3deg)'))
    b.append(D(4320 + 600, 1640, 340, 26, 'background:#2E2A26;opacity:.85;transform:rotate(-3deg)'))
    b.append(D(4320 + 600, 1700, 220, 26, 'background:#2E2A26;opacity:.85;transform:rotate(-3deg)'))
    b.append(D(5400 + 700, 1520, 200, 200, 'border-radius:50%;box-shadow:-40px 10px 0 0 #E8B96C'))
    b.append(slide(0, 'lt', 'Listë', '5 gjëra që na thanë si fëmijë <em>dhe i&nbsp;besuam.</em>', 'E katërta e besojmë&nbsp;ende.', hint=H))
    b.append(slide(1, 'lt', 'E para', '„Po e gëlltite farën, <em>të mbin shalqi në&nbsp;bark.“</em>'))
    b.append(slide(2, 'lt', 'E dyta', '„Mos bëj fytyrë të shtrembër, <em>se të mbetet&nbsp;ashtu.“</em>'))
    b.append(slide(3, 'lt', 'E treta', '„Po s’e hëngre bukën, <em>s’rritesh.“</em>'))
    b.append(slide(4, 'lt', 'E katërta', '„Mos fol për hallet, <em>se ikin&nbsp;vetë.“</em>', 'Nuk ikin. Vetëm fshihen më&nbsp;thellë.'))
    b.append(slide(5, 'lt', 'E pesta', '„Fli shpejt, <em>se vjen&nbsp;gogoli.“</em>', 'Gogoli s’erdhi kurrë. Hallet që s’i thamë,&nbsp;po.'))
    b.append(end(6, 'Hallet lehtësohen kur i thua. <em>Thuaji këtu, pa&nbsp;emër.</em>'))
    bg = '#FBF8F1;background-image:repeating-linear-gradient(180deg,transparent 0 78px,rgba(63,98,89,.16) 78px 80px)'
    return W, page(W, bg, ''.join(b))

# 05: mysafiri përcillet deri te porta (rregull i pashkruar), shtegu i oborrit me gjurmë nga dera te porta
def set5():
    W = 6480
    b = [D(0, 1500, W - 1080, 420, 'background:#C9D3B0')]
    b.append(D(0, 1640, W - 1080, 150, 'background:#E6DCC6;border-radius:75px'))
    for k in range(0, W - 1300, 160):
        y = 1665 + (40 if (k // 160) % 2 else 0)
        b.append(D(k + 40, y, 34, 52, 'background:rgba(90,70,50,.35);border-radius:50% 50% 45% 45%'))
        b.append(D(k + 100, y + 6, 30, 46, 'background:rgba(90,70,50,.22);border-radius:50% 50% 45% 45%'))
    b.append(D(60, 1180, 300, 470, 'background:#7A5338;border-radius:8px 8px 0 0;box-shadow:inset 0 0 0 14px #5E3E28'))
    b.append(D(300, 1420, 22, 22, 'border-radius:50%;background:#E8B96C'))
    b.append(D(40, 1100, 340, 90, 'background:#FFD79A;opacity:.45;border-radius:50%;filter:blur(18px)'))
    gx = 4320 + 300
    for k in range(9):
        b.append(D(gx + k * 52, 1320 + (k % 2) * 20, 22, 330 - (k % 2) * 20, 'background:#3A3A3A;border-radius:11px 11px 0 0'))
    b.append(D(gx - 10, 1430, 480, 18, 'background:#3A3A3A'))
    b.append(D(gx - 10, 1580, 480, 18, 'background:#3A3A3A'))
    b.append(D(gx - 70, 1260, 60, 400, 'background:#BFB3A0;border-radius:6px'))
    b.append(D(gx + 470, 1260, 60, 400, 'background:#BFB3A0;border-radius:6px'))
    b.append(D(gx + 200, 1080, 80, 80, 'border-radius:50%;background:radial-gradient(circle,#FFE7B0,rgba(255,231,176,0) 70%)'))
    b.append(slide(0, 'lt', 'Rregull i pashkruar', 'Mysafiri përcillet deri te&nbsp;porta. <em>Kurrë vetëm deri te&nbsp;dera.</em>', hint=H))
    b.append(slide(1, 'lt', 'Rruga', 'Dhjetë hapa nëpër oborr. <em>Dhe biseda nis&nbsp;vërtet.</em>'))
    b.append(slide(2, 'lt', 'Te porta', 'Aty thuhej ajo që s’u tha gjithë mbrëmjen. <em>„Po, desha të të&nbsp;them…“</em>'))
    b.append(slide(3, 'lt', 'Pse?', 'Sepse te porta s’ka kohë për turp. <em>Vetëm për të&nbsp;vërtetën.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'Mos e prit portën. <em>Thuaje kur je ende&nbsp;ulur.</em>'))
    b.append(end(5, 'Ke diçka që s’e the gjithë mbrëmjen? <em>Thuaje këtu, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#E9EEF2 0%,#F3F1EA 60%,#E6E2D2 78%,#C9D3B0 100%)', ''.join(b))

SETS = [('01-stoli', set1), ('02-vrapi', set2), ('03-perhajer', set3), ('04-sifemije', set4), ('05-porta', set5)]
if __name__ == '__main__':
    for name, fn in SETS:
        w, html = fn()
        open(os.path.join(OUT, f'set-{name}.html'), 'w', encoding='utf-8').write(html)
        print(name, w)
