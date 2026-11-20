import os
BASE = '/home/user/Shprehu-3.5/Claude outputs/reklama/2026-11-12-tiktok-ftohti/burimi/gen.py'
OUT = os.path.dirname(os.path.abspath(__file__))
ns = {'__file__': BASE}
exec(open(BASE, encoding='utf-8').read().split('# 01:')[0], ns)
page, slide, end, D, H = ns['page'], ns['slide'], ns['end'], ns['D'], ns['H']
import random

# 01: „Kur s’fle dot, numëro të mirat“ (urtësi e gjyshes), yjet shtohen mbi verandë
def sky(x, n, seed):
    r = random.Random(seed)
    o = D(x, 1640, 1080, 280, 'background:#2A2420')
    o += D(x + 140, 1560, 800, 24, 'background:#5E4632;border-radius:6px')
    for k in range(n):
        sx, sy, w = r.randint(60, 1000), r.randint(1100, 1500), r.choice([8, 10, 14])
        o += D(x + sx, sy, w, w, 'background:#F2D18A;border-radius:50%;box-shadow:0 0 14px rgba(242,209,138,.8)')
    return o
def set1():
    W = 6480
    b = [sky(i * 1080, n, i) for i, n in enumerate([2, 6, 12, 20, 30])]
    b.append(slide(0, 'dk', 'Gjyshja', 'Kur s’na zinte gjumi, <em>na nxirrte në&nbsp;verandë.</em>', hint=H))
    b.append(slide(1, 'dk', 'Me zë të ulët', '„Numëro të mirat e ditës. <em>Një për çdo&nbsp;yll.“</em>'))
    b.append(slide(2, 'dk', 'Ne qeshnim', 'Fillonim me një. <em>Pastaj nuk&nbsp;ndaleshim.</em>'))
    b.append(slide(3, 'dk', 'Ajo e dinte', 'Mendja që numëron të mirat <em>s’ka kohë të&nbsp;frikësohet.</em>'))
    b.append(slide(4, 'dk', 'Sonte', 'Para gjumit, gjej tri. <em>Edhe të&nbsp;vogla.</em>', 'Cila është një e mirë e sotme? Shkruaje në&nbsp;koment.'))
    b.append(end(5, 'Kur s’të zë gjumi, <em>dikush të dëgjon, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#141B26 0%,#1E2735 100%)', ''.join(b))

# 02: „Mos thuaj që je lodhur, se të marrin për dembel!“ (rregull i pashkruar), karrigia ku s’ulemi
def chair(x, sit):
    o = D(x, 1700, 1080, 220, 'background:#B99A72')
    o += D(x + 420, 1420, 240, 30, 'background:#8C6A4A;border-radius:8px')
    o += D(x + 420, 1240, 30, 200, 'background:#8C6A4A;border-radius:6px')
    o += D(x + 435, 1450, 20, 250, 'background:#7A5A3A')
    o += D(x + 625, 1450, 20, 250, 'background:#7A5A3A')
    if sit:
        o += D(x + 470, 1300, 160, 120, 'background:#3F6259;border-radius:60px 60px 20px 20px')
        o += D(x + 500, 1200, 100, 100, 'background:#E9D3BE;border-radius:50%')
    return o
def set2():
    W = 6480
    b = [chair(i * 1080, i == 4) for i in range(5)]
    b.append(slide(0, 'lt', 'Rregull i pashkruar', '„Mos thuaj që je lodhur, <em>se të marrin për&nbsp;dembel!“</em>', hint=H))
    b.append(slide(1, 'lt', 'E mësuam herët', 'Karrigia ishte aty. <em>Por ne s’uleshim.</em>'))
    b.append(slide(2, 'lt', 'Pastaj', 'Punonim edhe kur s’mundnim më. <em>Dhe thoshim „mirë jam“.</em>'))
    b.append(slide(3, 'lt', 'E vërteta', 'S’ishim dembelë. <em>Ishim të&nbsp;lodhur.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'Ulu pak. <em>Pushimi s’është&nbsp;turp.</em>', 'E ke dëgjuar këtë rregull? Shkruaj „po“ në&nbsp;koment.'))
    b.append(end(5, 'Thuaje sa je lodhur. <em>Këtu askush s’të gjykon, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#F6F0E6 0%,#EEE5D6 100%)', ''.join(b))

# 03: 5 gjëra që bëjmë kur na vjen „duhet të flasim“ (listë me boshllëk), flluska e mesazhit
def msg(x, dots):
    o = D(x + 260, 1260, 560, 520, 'background:#20292D;border-radius:46px')
    o += D(x + 300, 1320, 380, 70, 'background:#3F6259;border-radius:24px;color:#FAF7F1;font-size:30px;display:flex;align-items:center;justify-content:center', '„Duhet të flasim.“')
    for k in range(dots):
        o += D(x + 310 + k * 36, 1430, 22, 22, 'background:#8FB8A8;border-radius:50%')
    return o
def set3():
    W = 7560
    b = [msg(i * 1080, n) for i, n in enumerate([0, 1, 2, 3, 3, 3])]
    b.append(slide(0, 'lt', 'Listë', '5 gjëra që bëjmë kur na vjen <em>„duhet të&nbsp;flasim“.</em>', 'E katërta s’e pranon askush.', hint=H))
    b.append(slide(1, 'lt', 'E para', 'E lexojmë dhjetë herë. <em>Sikur do të&nbsp;ndryshojë.</em>'))
    b.append(slide(2, 'lt', 'E dyta', 'Shkruajmë „për çfarë?“ <em>dhe e&nbsp;fshijmë.</em>'))
    b.append(slide(3, 'lt', 'E treta', 'Kontrollojmë kur ishte online <em>për herë të&nbsp;fundit.</em>'))
    b.append(slide(4, 'lt', 'E katërta', 'Rishkruajmë në kokë <em>gjithë gabimet e&nbsp;vitit.</em>', 'Zakonisht ishte diçka e&nbsp;vogël.'))
    b.append(slide(5, 'lt', 'E pesta', '„Mirë, kur?“ <em>Dhe zemra rreh&nbsp;fort.</em>', 'Cilën e ke bërë? Shkruaj numrin në&nbsp;koment.'))
    b.append(end(6, 'Kur mendja vrapon, <em>fol me dikë, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(90deg,#E9EEF0 0%,#F2EDE4 100%)', ''.join(b))

SETS = [('01-yjet', set1), ('02-karrigia', set2), ('03-mesazhi', set3)]
if __name__ == '__main__':
    for name, fn in SETS:
        w, html = fn()
        open(os.path.join(OUT, f'set-{name}.html'), 'w', encoding='utf-8').write(html)
        print(name, w)
