import os
BASE = '/home/user/Shprehu-3.5/Claude outputs/reklama/2026-11-12-tiktok-ftohti/burimi/gen.py'
OUT = os.path.dirname(os.path.abspath(__file__))
ns = {'__file__': BASE}
exec(open(BASE, encoding='utf-8').read().split('# 01:')[0], ns)
page, slide, end, D, H = ns['page'], ns['slide'], ns['end'], ns['D'], ns['H']

# 01: „Fjalën e rëndë mos e thuaj në vapë“ (urtësi e gjyshes: lulet ujiten në mbrëmje), dielli ulet nëpër slide-e
def garden(x, k):
    sy = 1150 + k * 120
    o = D(x + 760, sy, 160, 160, f'background:{"#E8B96C" if k < 4 else "#D98C5F"};border-radius:50%;box-shadow:0 0 60px rgba(232,185,108,.6)')
    o += D(x, 1700, 1080, 220, 'background:#6E8F5E')
    for j in range(5):
        o += D(x + 120 + j * 180, 1580, 14, 130, 'background:#3F6259')
        o += D(x + 96 + j * 180, 1540, 60, 60, f'background:{["#D95A6A","#E8B96C","#B04A2C","#D95A6A","#F2D18A"][j]};border-radius:50%')
    return o
def set1():
    W = 6480
    b = [garden(i * 1080, i) for i in range(5)]
    b.append(slide(0, 'lt', 'Gjyshja', 'Lulet nuk i ujiste kurrë <em>në&nbsp;mesditë.</em>', hint=H))
    b.append(slide(1, 'lt', '„Në vapë digjen“', 'Priste sa të ulej dielli. <em>Pastaj merrte&nbsp;ujin.</em>'))
    b.append(slide(2, 'lt', 'Njësoj me fjalët', 'Edhe fjala e rëndë, e thënë në vapë, <em>djeg më&nbsp;shumë.</em>'))
    b.append(slide(3, 'lt', 'Ajo e dinte', 'Prit sa të ftohet dita. <em>Pastaj&nbsp;fol.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'Kur je i nxehur, shkruaje diku. <em>Thuaje kur të&nbsp;qetësohesh.</em>', 'E ke pasur një gjyshe që e thoshte këtë? Shkruaje në&nbsp;koment.'))
    b.append(end(5, 'Kur s’di si ta thuash, <em>provoje këtu, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#F6EEDF 0%,#F2DFC6 100%)', ''.join(b))

# 02: „Mos u ul në cep të tryezës, se s’martohesh!“ (rregull i pashkruar), tryeza dhe karrigia në cep
def table(x, cep):
    o = D(x, 1800, 1080, 120, 'background:#B99A72')
    o += D(x + 140, 1520, 800, 40, 'background:#8C6A4A;border-radius:10px')
    o += D(x + 180, 1560, 24, 240, 'background:#7A5A3A')
    o += D(x + 876, 1560, 24, 240, 'background:#7A5A3A')
    for j in range(4):
        o += D(x + 230 + j * 170, 1480, 110, 40, 'background:#FAF7F1;border-radius:50%')
    if cep:
        o += D(x + 860, 1620, 120, 24, 'background:#3F6259;border-radius:6px')
        o += D(x + 950, 1500, 24, 140, 'background:#3F6259;border-radius:6px')
    return o
def set2():
    W = 6480
    b = [table(i * 1080, i in (0, 1, 2)) for i in range(5)]
    b.append(slide(0, 'lt', 'Rregull i pashkruar', '„Mos u ul në cep të tryezës, <em>se&nbsp;s’martohesh!“</em>', hint=H))
    b.append(slide(1, 'lt', 'E dëgjuam qindra herë', 'Rregulla për fatin kishim <em>me&nbsp;dhjetëra.</em>'))
    b.append(slide(2, 'lt', 'Por', 'Askush s’na tha ku të ulemi <em>kur ndihemi&nbsp;vetëm.</em>'))
    b.append(slide(3, 'lt', 'E vërteta', 'Karrigia në cep s’të sjell fat të keq. <em>Të sjell pak&nbsp;vetmi.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'Afroje karrigen. <em>Ka vend edhe për&nbsp;ty.</em>', 'Cilin rregull të tryezës e dëgjoje ti? Shkruaje në&nbsp;koment.'))
    b.append(end(5, 'Edhe kur ndihesh në cep, <em>dikush të dëgjon, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#F6F0E6 0%,#EEE5D6 100%)', ''.join(b))

# 03: 5 gjëra që i mbajmë në telefon dhe s’i fshijmë kurrë (listë me boshllëk), dosjet
def phone(x, n):
    o = D(x + 300, 1180, 480, 640, 'background:#20292D;border-radius:56px')
    o += D(x + 330, 1220, 420, 560, 'background:#F2EDE4;border-radius:34px')
    for k in range(n):
        o += D(x + 360, 1260 + k * 100, 360, 76, 'background:#FAF7F1;border-radius:14px;box-shadow:0 4px 10px rgba(0,0,0,.08)')
        o += D(x + 380, 1280 + k * 100, 36, 36, f'background:{["#3F6259","#8FB8A8","#E8B96C","#B04A2C","#5B6E8C"][k]};border-radius:10px')
    return o
def set3():
    W = 7560
    b = [phone(i * 1080, n) for i, n in enumerate([0, 1, 2, 3, 4, 5])]
    b.append(slide(0, 'lt', 'Listë', '5 gjëra që i mbajmë në telefon <em>dhe s’i fshijmë&nbsp;kurrë.</em>', 'E katërta s’e tregojmë askujt.', hint=H))
    b.append(slide(1, 'lt', 'E para', 'Një foto e turbullt <em>nga një natë e&nbsp;mirë.</em>'))
    b.append(slide(2, 'lt', 'E dyta', 'Biseda e parë <em>me një shok të&nbsp;vjetër.</em>'))
    b.append(slide(3, 'lt', 'E treta', 'Një shënim me ide <em>që s’i bëmë&nbsp;kurrë.</em>'))
    b.append(slide(4, 'lt', 'E katërta', 'Një mesazh zanor i nënës. <em>E dëgjojmë kur s’jemi&nbsp;mirë.</em>', 'Zëri i saj na qetëson edhe&nbsp;sot.'))
    b.append(slide(5, 'lt', 'E pesta', 'Një screenshot <em>me fjalë që na&nbsp;ndihmuan.</em>', 'Cilën e ke ti? Shkruaj numrin në&nbsp;koment.'))
    b.append(end(6, 'Edhe fjalët që s’i fshin, <em>mund t’i thuash këtu, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(90deg,#E9EEF0 0%,#F2EDE4 100%)', ''.join(b))

SETS = [('01-lulet', set1), ('02-cepi', set2), ('03-telefoni', set3)]
if __name__ == '__main__':
    for name, fn in SETS:
        w, html = fn()
        open(os.path.join(OUT, f'set-{name}.html'), 'w', encoding='utf-8').write(html)
        print(name, w)
