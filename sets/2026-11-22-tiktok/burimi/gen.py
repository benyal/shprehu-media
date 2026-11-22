import os
BASE = '/home/user/Shprehu-3.5/Claude outputs/reklama/2026-11-12-tiktok-ftohti/burimi/gen.py'
OUT = os.path.dirname(os.path.abspath(__file__))
ns = {'__file__': BASE}
exec(open(BASE, encoding='utf-8').read().split('# 01:')[0], ns)
page, slide, end, D, H = ns['page'], ns['slide'], ns['end'], ns['D'], ns['H']

# 01: „Fjala e mirë hap derë të mbyllur“ (urtësi e gjyshit), dera hapet pak nga pak
def door(x, k):
    o = D(x, 1760, 1080, 160, 'background:#B99A72')
    o += D(x + 340, 1180, 400, 580, 'background:#2A2420;border-radius:8px')
    o += D(x + 360, 1200, 360, 560, 'background:linear-gradient(90deg,#F2D18A,#E8B96C);box-shadow:0 0 80px rgba(232,185,108,.5)' if k else 'background:#2A2420')
    w = [360, 290, 210, 120, 40][k]
    o += D(x + 360, 1200, w, 560, 'background:#6E4A2F;border-radius:4px')
    o += D(x + 340 + w - 10, 1470, 18, 18, 'background:#E8B96C;border-radius:50%')
    return o
def set1():
    W = 6480
    b = [door(i * 1080, i) for i in range(5)]
    b.append(slide(0, 'lt', 'Gjyshi', '„Fjala e mirë <em>hap derë të&nbsp;mbyllur.“</em>', hint=H))
    b.append(slide(1, 'lt', 'Kur dikush mërzitej', 'Nuk bërtiste. <em>Nuk shtynte.</em>'))
    b.append(slide(2, 'lt', 'Trokiste butë', '„Hajde, se të pres.“ <em>Dhe priste.</em>'))
    b.append(slide(3, 'lt', 'Ai e dinte', 'Dera s’hapet me forcë. <em>Hapet nga&nbsp;brenda.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'Thuaji dikujt një fjalë të mirë. <em>Edhe vetes.</em>', 'Kush ta ka hapur derën me një fjalë? Shkruaje në&nbsp;koment.'))
    b.append(end(5, 'Kur dera rri mbyllur, <em>një fjalë e butë të pret këtu, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#F6EEDF 0%,#EFE3CE 100%)', ''.join(b))

# 02: „Mos rri mbi prag, se sjell grindje!“ (rregull i pashkruar), këmbët mbi prag
def sill(x, inside):
    o = D(x, 1760, 1080, 160, 'background:#B99A72')
    o += D(x + 300, 1100, 480, 660, 'border:24px solid #8C6A4A;border-bottom:none;border-radius:6px')
    o += D(x + 280, 1740, 520, 26, 'background:#6E4A2F;border-radius:6px')
    o += D(x + 324, 1124, 432, 616, 'background:#F2E2C4' if inside else 'background:#DCE5E8')
    fx = 470 if not inside else 470
    fy = 1700 if not inside else 1660
    o += D(x + fx, fy, 60, 40, 'background:#3F6259;border-radius:20px 20px 8px 8px')
    o += D(x + fx + 80, fy, 60, 40, 'background:#3F6259;border-radius:20px 20px 8px 8px')
    return o
def set2():
    W = 6480
    b = [sill(i * 1080, i == 4) for i in range(5)]
    b.append(slide(0, 'lt', 'Rregull i pashkruar', '„Mos rri mbi prag, <em>se sjell&nbsp;grindje!“</em>', hint=H))
    b.append(slide(1, 'lt', 'E dëgjuam me qindra herë', 'Ose hyr, ose dil. <em>Mbi prag jo.</em>'))
    b.append(slide(2, 'lt', 'Por shumë prej nesh', 'Jetojmë pikërisht aty. <em>As brenda, as&nbsp;jashtë.</em>'))
    b.append(slide(3, 'lt', 'E vërteta', 'Pragu s’sjell grindje. <em>Pritja e gjatë po.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'Bëj një hap. <em>Hyr te ajo që do të&nbsp;thuash.</em>', 'E ke dëgjuar këtë rregull? Shkruaj „po“ në&nbsp;koment.'))
    b.append(end(5, 'Kur s’di a të hysh, <em>bëje hapin e parë këtu, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#F6F0E6 0%,#EEE5D6 100%)', ''.join(b))

# 03: 5 gjëra që na i mësoi gjyshi pa i thënë kurrë (listë me boshllëk), veglat në mur
def tools(x, n):
    o = D(x + 300, 1240, 700, 520, 'background:#A88560;border-radius:10px')
    for k in range(n):
        tx = 330 + k * 130
        o += D(x + tx + 50, 1270, 20, 20, 'background:#3A2A1E;border-radius:50%')
        o += D(x + tx + 54, 1290, 12, 300, 'background:#6E4A2F;border-radius:6px')
        o += D(x + tx + 10, 1560 - (k % 2) * 40, 100, 60, f'background:{["#5E6B6A","#B04A2C","#3F6259","#E8B96C","#5B6E8C"][k]};border-radius:10px')
    return o
def set3():
    W = 7560
    b = [tools(i * 1080, n) for i, n in enumerate([0, 1, 2, 3, 4, 5])]
    b.append(slide(0, 'lt', 'Listë', '5 gjëra që na i mësoi gjyshi <em>pa i thënë&nbsp;kurrë.</em>', 'E katërta na duhet edhe sot.', hint=H))
    b.append(slide(1, 'lt', 'E para', 'Që gjërat e prishura <em>ndreqen, s’hidhen.</em>'))
    b.append(slide(2, 'lt', 'E dyta', 'Që puna e mirë <em>bëhet pa&nbsp;ngut.</em>'))
    b.append(slide(3, 'lt', 'E treta', 'Që fjala e dhënë <em>mbahet.</em>'))
    b.append(slide(4, 'lt', 'E katërta', 'Si të rrish pranë dikujt <em>në heshtje, pa e bërë të&nbsp;rëndë.</em>', 'Mjaftonte që ishte&nbsp;aty.'))
    b.append(slide(5, 'lt', 'E pesta', 'Që një „bravo“ e vogël <em>vlen më shumë se një&nbsp;dhuratë.</em>', 'Cilën ta mësoi i yti? Shkruaj numrin në&nbsp;koment.'))
    b.append(end(6, 'Edhe sot dikush rri pranë, <em>në heshtje ose me fjalë, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(90deg,#EFE7DA 0%,#E9EEF0 100%)', ''.join(b))

# 04: Drutë e dimrit (ritual), stiva zvogëlohet, hyn në kasolle
def wood(x, k):
    o = D(x, 1760, 1080, 160, 'background:#9C8A6A')
    o += D(x + 640, 1300, 340, 460, 'background:#6E4A2F;border-radius:10px 10px 0 0')
    o += D(x + 680, 1380, 260, 380, 'background:#3A2A1E')
    rows = [5, 4, 3, 2, 0][k]
    for r in range(rows):
        for c in range(3):
            o += D(x + 300 + c * 105, 1670 - r * 90, 100, 90, 'background:#C98B47;border-radius:50%;border:8px solid #8C5A2F;box-sizing:border-box')
    filled = [0, 1, 2, 3, 4][k]
    for r in range(filled):
        o += D(x + 690, 1680 - r * 70, 240, 64, 'background:#C98B47;border-radius:30px')
    return o
def set4():
    W = 6480
    b = [wood(i * 1080, i) for i in range(5)]
    b.append(slide(0, 'lt', 'Çdo vjeshtë', 'Kur vinin drutë e dimrit, <em>dilte gjithë&nbsp;lagjja.</em>', hint=H))
    b.append(slide(1, 'lt', 'Askush s’thërriste', 'Fqinji shihte stivën <em>dhe vinte me&nbsp;doreza.</em>'))
    b.append(slide(2, 'lt', 'Dorë më dorë', 'Ajo që një njeriu i merrte ditë, <em>bëhej në një&nbsp;orë.</em>'))
    b.append(slide(3, 'lt', 'E dinim', 'Drutë s’futeshin <em>kurrë vetëm.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'As pesha jote s’ka pse <em>të mbahet&nbsp;vetëm.</em>', 'Kush vinte të ndihmonte te ju? Shkruaje në&nbsp;koment.'))
    b.append(end(5, 'Kur pesha është shumë, <em>ndaje këtu, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#EDE6DA 0%,#E2DACB 100%)', ''.join(b))

SETS = [('01-dera', set1, 6), ('02-pragu', set2, 6), ('03-gjyshi', set3, 7), ('04-drute', set4, 6)]
if __name__ == '__main__':
    for name, fn, c in SETS:
        w, html = fn()
        open(os.path.join(OUT, f'set-{name}.html'), 'w', encoding='utf-8').write(html)
