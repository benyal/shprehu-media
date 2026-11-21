import os
BASE = '/home/user/Shprehu-3.5/Claude outputs/reklama/2026-11-12-tiktok-ftohti/burimi/gen.py'
OUT = os.path.dirname(os.path.abspath(__file__))
ns = {'__file__': BASE}
exec(open(BASE, encoding='utf-8').read().split('# 01:')[0], ns)
page, slide, end, D, H = ns['page'], ns['slide'], ns['end'], ns['D'], ns['H']

# 01: „Ku hanë dy, hanë edhe tre“ (urtësi e gjyshes), pjatat shtohen rreth tenxheres
def pot(x, n):
    o = D(x, 1760, 1080, 160, 'background:#B99A72')
    o += D(x + 100, 1600, 880, 40, 'background:#8C6A4A;border-radius:10px')
    o += D(x + 430, 1430, 220, 170, 'background:#5E6B6A;border-radius:20px 20px 60px 60px')
    o += D(x + 410, 1420, 260, 30, 'background:#4A5554;border-radius:14px')
    for k in range(n):
        o += D(x + [140, 760, 260, 650][k], 1560, 150, 36, 'background:#FAF7F1;border-radius:50%;box-shadow:0 4px 8px rgba(0,0,0,.12)')
    return o
def set1():
    W = 6480
    b = [pot(i * 1080, n) for i, n in enumerate([2, 3, 3, 4, 4])]
    b.append(slide(0, 'lt', 'Gjyshja', '„Ku hanë dy, <em>hanë edhe&nbsp;tre.“</em>', hint=H))
    b.append(slide(1, 'lt', 'Kur vinte dikush pa lajmëruar', 'S’pyeste a mjafton gjella. <em>Shtonte një&nbsp;pjatë.</em>'))
    b.append(slide(2, 'lt', 'Askush s’ngelej pa ngrënë', 'Porcionet bëheshin pak më të vogla. <em>Tryeza, më e&nbsp;madhe.</em>'))
    b.append(slide(3, 'lt', 'Ajo e dinte', 'Ku ka vend për dy, <em>ka vend edhe për hallin e&nbsp;tretit.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'Mos mendo që je barrë. <em>Ka vend edhe për&nbsp;ty.</em>', 'Kush e thoshte këtë në shtëpinë tënde? Shkruaje në&nbsp;koment.'))
    b.append(end(5, 'Edhe për fjalët e tua <em>ka vend këtu, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#F6EEDF 0%,#EFE3CE 100%)', ''.join(b))

# 02: „Mos e lër çantën në tokë, se ikin paratë!“ (rregull i pashkruar), çanta që më në fund ulet
def bag(x, down):
    o = D(x, 1780, 1080, 140, 'background:#B99A72')
    o += D(x + 600, 1500, 260, 30, 'background:#8C6A4A;border-radius:8px')
    o += D(x + 610, 1530, 22, 250, 'background:#7A5A3A')
    o += D(x + 828, 1530, 22, 250, 'background:#7A5A3A')
    bx, by = (280, 1610) if down else (640, 1330)
    o += D(x + bx, by, 190, 170, 'background:#B04A2C;border-radius:18px 18px 24px 24px')
    o += D(x + bx + 50, by - 50, 90, 60, 'border:12px solid #8C3A22;border-bottom:none;border-radius:40px 40px 0 0')
    return o
def set2():
    W = 6480
    b = [bag(i * 1080, i == 4) for i in range(5)]
    b.append(slide(0, 'lt', 'Rregull i pashkruar', '„Mos e lër çantën në tokë, <em>se ikin&nbsp;paratë!“</em>', hint=H))
    b.append(slide(1, 'lt', 'E mësuam herët', 'Çanta gjithmonë mbi karrige. <em>Kurrë&nbsp;poshtë.</em>'))
    b.append(slide(2, 'lt', 'Por brenda saj', 'Mbanim edhe gjëra që s’i lëshonim kurrë: <em>hallet, frikën, „s’kam&nbsp;kohë“.</em>'))
    b.append(slide(3, 'lt', 'E vërteta', 'Paratë s’ikin nga toka. <em>Por pesha ikën kur e&nbsp;lëshon.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'Lëshoje pak. <em>Edhe për pak&nbsp;minuta.</em>', 'E ke dëgjuar këtë rregull? Shkruaj „po“ në&nbsp;koment.'))
    b.append(end(5, 'Kur pesha rëndon, <em>lëshoje këtu, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#F6F0E6 0%,#EEE5D6 100%)', ''.join(b))

# 03: 5 fjali të nënës kur je i sëmurë (listë me boshllëk), filxhanët e çajit
def tea(x, n):
    o = D(x, 1780, 1080, 140, 'background:#8C6A4A')
    for k in range(n):
        cx = 150 + k * 170
        o += D(x + cx, 1640, 120, 120, 'background:#FAF7F1;border-radius:0 0 40px 40px')
        o += D(x + cx + 116, 1665, 36, 50, 'border:10px solid #FAF7F1;border-left:none;border-radius:0 30px 30px 0')
        o += D(x + cx + 10, 1652, 100, 22, 'background:#C98B47;border-radius:50%')
    return o
def set3():
    W = 7560
    b = [tea(i * 1080, n) for i, n in enumerate([0, 1, 2, 3, 4, 5])]
    b.append(slide(0, 'lt', 'Listë', '5 fjali të nënës shqiptare <em>kur je i&nbsp;sëmurë.</em>', 'E katërta s’e thoshte me zë.', hint=H))
    b.append(slide(1, 'lt', 'E para', '„Të kam thënë <em>të vishesh&nbsp;trashë.“</em>'))
    b.append(slide(2, 'lt', 'E dyta', '„Pije çajin, <em>sa është i&nbsp;nxehtë.“</em>'))
    b.append(slide(3, 'lt', 'E treta', '„A ke ngrënë diçka? <em>Të bëj një&nbsp;supë.“</em>'))
    b.append(slide(4, 'lt', 'E katërta', 'Ulej buzë shtratit. <em>Dhe rrinte aty pa folur.</em>', 'Kjo shëronte më shumë se çaji.'))
    b.append(slide(5, 'lt', 'E pesta', '„Fli tani. <em>Unë jam&nbsp;këtu.“</em>', 'Cilën e dëgjoje më shpesh? Shkruaj numrin në&nbsp;koment.'))
    b.append(end(6, 'Kur s’je mirë, <em>dikush rri pranë, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(90deg,#F2E9DD 0%,#EDE6EA 100%)', ''.join(b))

SETS = [('01-pjata', set1, 6), ('02-canta', set2, 6), ('03-caji', set3, 7)]
if __name__ == '__main__':
    for name, fn, c in SETS:
        w, html = fn()
        open(os.path.join(OUT, f'set-{name}.html'), 'w', encoding='utf-8').write(html)
