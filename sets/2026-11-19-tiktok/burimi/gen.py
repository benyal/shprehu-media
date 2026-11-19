import os
BASE = '/home/user/Shprehu-3.5/Claude outputs/reklama/2026-11-12-tiktok-ftohti/burimi/gen.py'
OUT = os.path.dirname(os.path.abspath(__file__))
ns = {'__file__': BASE}
exec(open(BASE, encoding='utf-8').read().split('# 01:')[0], ns)
page, slide, end, D, H = ns['page'], ns['slide'], ns['end'], ns['D'], ns['H']

# 01: farat në zarfe (urtësi e gjyshes), zarfi bëhet fidan që rritet
def sprout(x, n):
    o = D(x, 1640, 300, 140, 'background:#8C6A4A;border-radius:20px 20px 40px 40px')
    if n == 0:
        o += D(x + 50, 1330, 200, 260, 'background:#EADFC8;border-radius:8px;box-shadow:0 8px 16px rgba(60,40,20,.15)',
               '<div style="font-family:Fraunces,serif;font-style:italic;font-size:34px;color:#5E3A24;padding:30px 20px">Domate<br>prill</div>')
        return o
    h = 60 + n * 90
    o += D(x + 145, 1640 - h, 10, h, 'background:#4E7A4A;border-radius:5px')
    for k in range(n):
        side = -1 if k % 2 else 1
        o += D(x + 150 + (0 if side > 0 else -90), 1640 - 70 - k * 90, 90, 44, f'background:#6E9C5E;border-radius:{"0 44px" if side > 0 else "44px 0"}')
    if n >= 4:
        o += D(x + 120, 1640 - h - 50, 60, 60, 'background:#C8452C;border-radius:50%')
    return o
def set1():
    W = 6480
    b = [sprout(i * 1080 + 640, n) for i, n in enumerate([0, 1, 2, 3, 4])]
    b.append(slide(0, 'lt', 'Gjyshja', 'Gjyshja i ruante farat <em>në zarfe&nbsp;letre.</em>', hint=H))
    b.append(slide(1, 'lt', 'Mbi çdo zarf', 'Shkruante emrin dhe muajin. <em>Domate, prill.</em>'))
    b.append(slide(2, 'lt', 'Kur nxitonim', '„Çdo farë ka stinën e vet. <em>S’e mbjell borën në&nbsp;korrik.“</em>'))
    b.append(slide(3, 'lt', 'E vërteta', 'Edhe ti nuk je vonë. <em>Je në stinën&nbsp;tënde.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'Mos e krahaso kopshtin tënd <em>me atë të&nbsp;fqinjit.</em>', 'Çfarë mbillte gjyshja jote? Shkruaje në&nbsp;koment.'))
    b.append(end(5, 'Ndonjëherë rritja nis me një fjalë. <em>Thuaje këtu, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#F3EFE4 0%,#EEE8D8 100%)', ''.join(b))

# 02: „Ul zërin, se dëgjojnë fqinjtë!“ (rregull i pashkruar), dritaret e pallatit
def block(x, lit):
    o = D(x + 260, 1180, 560, 700, 'background:#3A3F44;border-radius:8px 8px 0 0')
    for r in range(3):
        for c in range(3):
            on = (r * 3 + c) in lit
            o += D(x + 300 + c * 170, 1230 + r * 200, 120, 140, f'background:{"#F2C66D" if on else "#22272B"};border-radius:6px')
    return o
def set2():
    W = 6480
    lits = [{0, 1, 2, 3, 5, 6, 7, 8}, {0, 2, 3, 5, 6, 8}, {4}, {4}, {1, 4, 7}]
    b = [block(i * 1080, l) for i, l in enumerate(lits)]
    b.append(slide(0, 'dk', 'Rregull i pashkruar', '„Ul zërin, <em>se dëgjojnë&nbsp;fqinjtë!“</em>', hint=H))
    b.append(slide(1, 'dk', 'E mësuam herët', 'Edhe kur qeshnim. <em>Edhe kur&nbsp;grindeshim.</em>'))
    b.append(slide(2, 'dk', 'Pastaj', 'E ulëm zërin edhe për atë që na dhembte. <em>Aq sa s’e dëgjonim as&nbsp;vetë.</em>'))
    b.append(slide(3, 'dk', 'E vërteta', 'Muret janë të holla. <em>Por ti ke të drejtë të&nbsp;flasësh.</em>'))
    b.append(slide(4, 'dk', 'Sot', 'Diku, dikush e dëgjon zërin tënd <em>dhe s’të&nbsp;gjykon.</em>', 'Çfarë thuhej në shtëpinë tënde „që të mos dëgjojnë“? Shkruaje në&nbsp;koment.'))
    b.append(end(5, 'Këtu s’ka fqinjë. <em>Fol me zë, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#1B2228 0%,#232C33 100%)', ''.join(b))

# 03: ora 20:15, në dyqan (sjellje e fshehur), shalli që merret dhe kthehet në raft
def shelf(x, taken):
    o = D(x + 120, 1400, 840, 20, 'background:#8C6A4A;border-radius:6px')
    o += D(x + 120, 1700, 840, 20, 'background:#8C6A4A;border-radius:6px')
    for k, c in enumerate(['#5B6E8C', '#B04A2C', '#3F6259', '#E8B96C']):
        if k == 2 and taken:
            continue
        o += D(x + 160 + k * 200, 1290, 160, 110, f'background:{c};border-radius:12px;box-shadow:inset 0 -14px 0 rgba(0,0,0,.12)')
    for k in range(4):
        o += D(x + 180 + k * 200, 1590, 130, 110, 'background:#CFC6B4;border-radius:10px')
    if taken:
        o += D(x + 460, 1470, 170, 110, 'background:#3F6259;border-radius:12px;transform:rotate(-8deg);box-shadow:0 12px 20px rgba(0,0,0,.2)')
    return o
def set3():
    W = 6480
    b = [shelf(i * 1080, t) for i, t in enumerate([False, True, True, False, True])]
    b.append(slide(0, 'lt', 'Ora 20:15, në dyqan', 'E merr në dorë diçka për vete. <em>Pastaj e kthen në&nbsp;raft.</em>', hint=H))
    b.append(slide(1, 'lt', 'Ora 20:16', 'E prek pak. <em>E sheh çmimin dy&nbsp;herë.</em>'))
    b.append(slide(2, 'lt', 'Ora 20:17', '„S’më duhet.“ <em>Për të tjerët s’e mendove&nbsp;kurrë.</em>'))
    b.append(slide(3, 'lt', 'E vërteta', 'Nuk ishte çmimi. <em>Ishte ndjesia që s’e&nbsp;meriton.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'Edhe ti je në listën e njerëzve <em>për të cilët&nbsp;kujdesesh.</em>', 'E ke bërë ndonjëherë? Shkruaj „po“ në&nbsp;koment.'))
    b.append(end(5, 'Fillo me pak kohë për veten. <em>Fol këtu, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#F6F1E8 0%,#EDE6D8 100%)', ''.join(b))

# 04: 5 gjëra që bën nëna kur e kupton që je mërzitur (listë me boshllëk), dritaret e shtëpisë ndizen një nga një
def house(x, n):
    o = D(x + 300, 1330, 480, 420, 'background:#E8DCC6;border-radius:10px')
    o += D(x + 270, 1200, 540, 150, 'background:#B04A2C;clip-path:polygon(50% 0,100% 100%,0 100%)')
    for k in range(4):
        on = k < n
        o += D(x + 340 + (k % 2) * 240, 1390 + (k // 2) * 170, 160, 120, f'background:{"#F2C66D" if on else "#5E6A70"};border-radius:6px')
    return o
def set4():
    W = 7560
    b = [house(i * 1080, n) for i, n in enumerate([0, 1, 2, 3, 4, 4])]
    b.append(slide(0, 'lt', 'Listë', '5 gjëra që bën nëna kur e kupton <em>që je&nbsp;mërzitur.</em>', 'Pa i thënë asgjë. E katërta të&nbsp;prek.', hint=H))
    b.append(slide(1, 'lt', 'E para', 'Të gatuan <em>gjellën që të&nbsp;pëlqen.</em>'))
    b.append(slide(2, 'lt', 'E dyta', 'Të pyet „a ke ngrohtë?“ <em>tri herë në një&nbsp;orë.</em>'))
    b.append(slide(3, 'lt', 'E treta', 'Të thërret për diçka të vogël. <em>Vetëm që të të&nbsp;shohë.</em>'))
    b.append(slide(4, 'lt', 'E katërta', 'S’të pyet asgjë. <em>Vetëm ulet&nbsp;pranë.</em>', 'Ndonjëherë kjo flet më shumë se çdo&nbsp;fjalë.'))
    b.append(slide(5, 'lt', 'E pesta', 'Para gjumit të thotë <em>„hajt, natën e&nbsp;mirë“.</em>', 'Cila prej tyre e bënte nëna jote? Shkruaj numrin në&nbsp;koment.'))
    b.append(end(6, 'Kur s’ke kush të ulet pranë, <em>dikush të dëgjon, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(90deg,#D9DCE0 0%,#E9E2D6 50%,#F6E6CC 100%)', ''.join(b))

# 05: rrjepja e misrit (ritual), grumbulli i kallinjve zvogëlohet dhe del vargu i artë
def corn(x, pile, braid):
    o = ''
    for k in range(pile):
        o += D(x + 260 + (k % 5) * 110, 1700 - (k // 5) * 70, 120, 56, f'background:#C9B98A;border-radius:28px;transform:rotate({(k * 37) % 40 - 20}deg)')
    for k in range(braid):
        o += D(x + 780, 1180 + k * 70, 60, 100, 'background:#E8B96C;border-radius:30px;box-shadow:inset 0 -10px 0 rgba(140,90,30,.25)')
    return o
def set5():
    W = 6480
    b = [corn(i * 1080, p, br) for i, (p, br) in enumerate([(15, 0), (12, 2), (8, 4), (4, 6), (0, 8)])]
    b.append(slide(0, 'lt', 'Ritual', 'Në vjeshtë, fqinjët mblidheshin <em>për të rrjepur&nbsp;misrin.</em>', hint=H))
    b.append(slide(1, 'lt', 'Deri vonë', 'Grumbulli ishte i madh. <em>Askush s’e numëronte.</em>'))
    b.append(slide(2, 'lt', 'Gjatë punës', 'Tregonin histori, qeshnin, <em>e thoshin edhe hallin.</em>'))
    b.append(slide(3, 'lt', 'E vërteta', 'Puna e rëndë bëhej e lehtë. <em>Sepse s’ishe&nbsp;vetëm.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'Edhe halli yt s’ka pse të rrjepet <em>i&nbsp;vetëm.</em>', 'A e ke bërë ndonjëherë? Shkruaje në&nbsp;koment.'))
    b.append(end(5, 'Ndaje pak nga grumbulli. <em>Dikush të dëgjon, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#F4ECDD 0%,#EADFC8 100%)', ''.join(b))

SETS = [('01-farat', set1), ('02-zeri', set2), ('03-dyqani', set3), ('04-nena', set4), ('05-misri', set5)]
if __name__ == '__main__':
    for name, fn in SETS:
        w, html = fn()
        open(os.path.join(OUT, f'set-{name}.html'), 'w', encoding='utf-8').write(html)
        print(name, w)
