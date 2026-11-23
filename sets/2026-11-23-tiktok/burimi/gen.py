import os
BASE = '/home/user/Shprehu-3.5/Claude outputs/reklama/2026-11-12-tiktok-ftohti/burimi/gen.py'
OUT = os.path.dirname(os.path.abspath(__file__))
ns = {'__file__': BASE}
exec(open(BASE, encoding='utf-8').read().split('# 01:')[0], ns)
page, slide, end, D, H = ns['page'], ns['slide'], ns['end'], ns['D'], ns['H']

# 01: „Mos e mat tjetrin me pashën tënd“ (urtësi e gjyshes), metrat e rrobaqepëses me gjatësi të ndryshme
def tapes(x, k):
    o = D(x, 1780, 1080, 140, 'background:#B99A72')
    lens = [[560, 560, 560], [560, 420, 300], [300, 640, 460], [460, 300, 620], [380, 520, 700]][k]
    for i, L in enumerate(lens):
        y = 1380 + i * 120
        o += D(x + 300, y, L, 56, 'background:repeating-linear-gradient(90deg,#F2D18A 0 34px,#E8B96C 34px 36px);border-radius:6px')
        o += D(x + 300, y + 4, 8, 48, 'background:#B04A2C')
    return o
def set1():
    W = 6480
    b = [tapes(i * 1080, i) for i in range(5)]
    b.append(slide(0, 'lt', 'Gjyshja, kur qepte', '„Mos e mat tjetrin <em>me pashën&nbsp;tënd.“</em>', hint=H))
    b.append(slide(1, 'lt', 'Çdo rrobë', 'Kishte masën e vet. <em>Askush s’ishte&nbsp;njësoj.</em>'))
    b.append(slide(2, 'lt', 'Ajo e dinte', 'Ajo që ty të rri mirë <em>dikujt tjetër i&nbsp;shtrëngon.</em>'))
    b.append(slide(3, 'lt', 'Dhe anasjelltas', 'As veten mos e mat <em>me pashën e&nbsp;tjetrit.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'Ke masën tënde. <em>Dhe ajo mjafton.</em>', 'Çfarë thoshte gjyshja jote kur qepte? Shkruaje në&nbsp;koment.'))
    b.append(end(5, 'Me masën tënde, <em>dikush të dëgjon, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#F6EEDF 0%,#EFE3CE 100%)', ''.join(b))

# 02: „Mos fishkëllo natën, se thërret të liga!“ (rregull i pashkruar), notat që shfaqen
def notes(x, n):
    o = D(x, 1780, 1080, 140, 'background:#2C3438')
    for k in range(5):
        o += D(x + 120, 1300 + k * 50, 840, 4, 'background:rgba(250,247,241,.35)')
    for k in range(n):
        nx, ny = 200 + k * 170, 1330 + (k * 37 % 4) * 50
        o += D(x + nx, ny, 56, 44, 'background:#E8B96C;border-radius:50%;transform:rotate(-20deg)')
        o += D(x + nx + 48, ny - 140, 8, 160, 'background:#E8B96C')
    return o
def set2():
    W = 6480
    b = [notes(i * 1080, n) for i, n in enumerate([0, 0, 1, 2, 5])]
    b.append(slide(0, 'dk', 'Rregull i pashkruar', '„Mos fishkëllo natën, <em>se thërret të&nbsp;liga!“</em>', hint=H))
    b.append(slide(1, 'dk', 'E mësuam herët', 'Heshtnim. <em>Edhe kur na vinte të&nbsp;këndonim.</em>'))
    b.append(slide(2, 'dk', 'Pastaj', 'Heshtëm edhe këngën <em>që kishim&nbsp;brenda.</em>'))
    b.append(slide(3, 'dk', 'E vërteta', 'Të ligat s’vijnë nga një këngë. <em>Vijnë kur mbajmë gjithçka&nbsp;brenda.</em>'))
    b.append(slide(4, 'dk', 'Sot', 'Këndo pak. <em>Edhe vetëm, edhe me zë të&nbsp;ulët.</em>', 'E ke dëgjuar këtë rregull? Shkruaj „po“ në&nbsp;koment.'))
    b.append(end(5, 'Ajo që mban brenda <em>mund ta thuash këtu, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#1C2329 0%,#252E34 100%)', ''.join(b))

# 03: 5 zakone të mëngjesit të nënës shqiptare (listë me boshllëk), dritarja që hapet
def window(x, k):
    o = D(x + 340, 1200, 560, 560, 'background:#8C6A4A;border-radius:8px')
    o += D(x + 370, 1230, 500, 500, 'background:linear-gradient(#F6D9A0,#F2E6CF)')
    w = [250, 200, 140, 80, 40, 20][k]
    o += D(x + 370, 1230, w, 500, 'background:#C9D6DE;border:6px solid #6E4A2F;box-sizing:border-box')
    o += D(x + 870 - w, 1230, w, 500, 'background:#C9D6DE;border:6px solid #6E4A2F;box-sizing:border-box')
    return o
def set3():
    W = 7560
    b = [window(i * 1080, i) for i in range(6)]
    b.append(slide(0, 'lt', 'Listë', '5 zakone të mëngjesit <em>të nënës&nbsp;shqiptare.</em>', 'E katërta e bën edhe sot.', hint=H))
    b.append(slide(1, 'lt', 'E para', 'Hap dritaret. <em>Edhe në&nbsp;janar.</em>'))
    b.append(slide(2, 'lt', 'E dyta', 'Ndez lajmet <em>„vetëm sa të dëgjoj&nbsp;motin“.</em>'))
    b.append(slide(3, 'lt', 'E treta', '„Hajde, se u ftoh <em>mëngjesi!“</em>'))
    b.append(slide(4, 'lt', 'E katërta', 'Të shikon nga dritarja <em>derisa të humbësh nga&nbsp;sytë.</em>', 'Edhe kur je i&nbsp;rritur.'))
    b.append(slide(5, 'lt', 'E pesta', '„Merre një xhaketë, <em>se ndryshon&nbsp;koha.“</em>', 'Cilën e bën nëna jote? Shkruaj numrin në&nbsp;koment.'))
    b.append(end(6, 'Dikush të ndjek me sy. <em>Edhe këtu dikush të dëgjon, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(90deg,#F6EEDF 0%,#E9EEF0 100%)', ''.join(b))

SETS = [('01-masa', set1, 6), ('02-fishkellima', set2, 6), ('03-mengjesi', set3, 7)]
if __name__ == '__main__':
    for name, fn, c in SETS:
        w, html = fn()
        open(os.path.join(OUT, f'set-{name}.html'), 'w', encoding='utf-8').write(html)
