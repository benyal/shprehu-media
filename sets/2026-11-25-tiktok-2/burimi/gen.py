import os
BASE = '/home/user/Shprehu-3.5/Claude outputs/reklama/2026-11-12-tiktok-ftohti/burimi/gen.py'
OUT = os.path.dirname(os.path.abspath(__file__))
ns = {'__file__': BASE}
exec(open(BASE, encoding='utf-8').read().split('# 01:')[0], ns)
page, slide, end, D, H = ns['page'], ns['slide'], ns['end'], ns['D'], ns['H']

# 01: sjellje e fshehur: rregullon fytyrën në xhamin e derës para se të hyjë te nëna
def door(x, k):
    o = D(x + 300, 1150, 480, 770, 'background:#7A5A3A;border-radius:10px 10px 0 0')
    o += D(x + 380, 1220, 320, 300, 'background:linear-gradient(135deg,#BFD3DA,#8FAEB8);border-radius:8px')
    o += D(x + 690, 1560, 50, 20, 'background:#D6A24C;border-radius:10px')
    mouth = ['M10 30 Q50 10 90 30', 'M10 25 Q50 25 90 25', 'M10 20 Q50 40 90 20', 'M10 15 Q50 50 90 15', 'M10 15 Q50 50 90 15'][k]
    o += (f'<svg class="abs" style="left:{x+470}px;top:1300px" width="140" height="160" viewBox="0 0 100 110">'
          '<circle cx="50" cy="40" r="38" fill="rgba(255,255,255,.35)"/><circle cx="35" cy="34" r="4" fill="#2E4A43"/><circle cx="65" cy="34" r="4" fill="#2E4A43"/>'
          f'<path d="{mouth}" transform="translate(0,25) scale(1,.8)" stroke="#2E4A43" stroke-width="4" fill="none"/></svg>')
    return o
def set1():
    W = 6480
    b = [D(0, 1840, W, 80, 'background:#5E4632')] + [door(i * 1080, i) for i in range(5)]
    b.append(slide(0, 'lt', 'Te dera e shtëpisë', 'Para se të hysh, <em>shikon xhamin e&nbsp;derës.</em>', hint=H))
    b.append(slide(1, 'lt', 'Jo për flokët', 'Për fytyrën. <em>Që të mos duket&nbsp;dita.</em>'))
    b.append(slide(2, 'lt', 'Një buzëqeshje', 'E provon dy herë. <em>Derisa të duket e&nbsp;vërtetë.</em>'))
    b.append(slide(3, 'lt', 'Sepse brenda është nëna', 'Dhe nëna <em>e kupton nga&nbsp;pragu.</em>'))
    b.append(slide(4, 'lt', 'Por', 'Ndoshta s’ka nevojë për buzëqeshje. <em>Ka nevojë për&nbsp;ty.</em>', 'E ke bërë këtë? Shkruaj „po“ në&nbsp;koment.'))
    b.append(end(5, 'Kur s’të del buzëqeshja, <em>dikush të dëgjon, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(90deg,#F1EADF 0%,#EDE5D8 100%)', ''.join(b))

# 02: urtësi e gjyshes: „eja, më ndihmo pak“, fasulet që qërohen në tabaka
def tray(x, k):
    o = D(x + 260, 1560, 560, 140, 'background:#C9A26A;border-radius:70px/24px')
    o += D(x + 290, 1580, 500, 90, 'background:#B8894E;border-radius:60px/20px')
    for j in range(3 + k * 2):
        o += D(x + 320 + (j * 47) % 440, 1600 + (j % 3) * 18, 34, 20, 'background:#F1E7D2;border-radius:50%')
    for j in range(6 - k):
        o += D(x + 330 + j * 70, 1500 - (j % 2) * 20, 70, 22, 'background:#6E8B4E;border-radius:11px;transform:rotate(%ddeg)' % (j * 14 - 30))
    return o
def set2():
    W = 6480
    b = [tray(i * 1080, i) for i in range(5)]
    b.append(slide(0, 'dk', 'Gjyshja', 'S’pyeste „çfarë ke?“. <em>Thoshte: „Eja, më ndihmo&nbsp;pak.“</em>', hint=H))
    b.append(slide(1, 'dk', 'Te tabakaja', 'Na jepte fasule <em>për t’i&nbsp;qëruar.</em>'))
    b.append(slide(2, 'dk', 'Duart punonin', 'Dhe pa e kuptuar, <em>goja nisi të&nbsp;flasë.</em>'))
    b.append(slide(3, 'dk', 'Ajo e dinte', 'Disa gjëra s’thuhen ballë për ballë. <em>Thuhen krah për&nbsp;krah.</em>'))
    b.append(slide(4, 'dk', 'Sot', 'S’ke pse e thua menjëherë. <em>Nise si të vjen.</em>', 'Çfarë të jepte gjyshja për të bërë? Shkruaje në&nbsp;koment.'))
    b.append(end(5, 'Krah për krah, <em>dikush të dëgjon, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#24302C 0%,#2C3833 100%)', ''.join(b))

# 03: listë: 5 gjëra që ua fshehim prindërve edhe në 30 vjeç, kutia që mbyllet
def box(x, n):
    o = D(x + 340, 1500, 400, 260, 'background:#B8894E;border-radius:10px')
    o += D(x + 320, 1460, 440, 60, 'background:#A07A44;border-radius:10px;transform:rotate(%ddeg);transform-origin:left' % (-8 + n * 2))
    for j in range(n):
        o += D(x + 370 + j * 70, 1420 - j * 8, 52, 70, 'background:#FBF8F1;border-radius:6px;transform:rotate(%ddeg)' % (j * 8 - 12))
    return o
def set3():
    W = 7560
    b = [D(0, 1760, W, 160, 'background:#D9C9AE')] + [box(i * 1080, n) for i, n in enumerate([0, 1, 2, 3, 4, 5])]
    b.append(slide(0, 'lt', 'Listë', '5 gjëra që ua fshehim prindërve <em>edhe në 30&nbsp;vjeç.</em>', 'E katërta është më e&nbsp;rënda.', hint=H))
    b.append(slide(1, 'lt', 'E para', 'Sa e paguam <em>diçka që&nbsp;blemë.</em>'))
    b.append(slide(2, 'lt', 'E dyta', 'Që s’kemi ngrënë <em>gjithë&nbsp;ditën.</em>'))
    b.append(slide(3, 'lt', 'E treta', 'Që jemi të sëmurë. <em>„Pak u ftoha, ma.“</em>'))
    b.append(slide(4, 'lt', 'E katërta', 'Që jemi mërzitur. <em>„Mirë jam, mos ki&nbsp;merak.“</em>', 'Sepse s’duam t’u shtojmë&nbsp;hallin.'))
    b.append(slide(5, 'lt', 'E pesta', 'Sa shumë <em>na&nbsp;mungojnë.</em>', 'Cilën e fsheh ti? Shkruaj numrin në&nbsp;koment.'))
    b.append(end(6, 'Atë që s’ua thua dot atyre, <em>thuaje këtu, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(90deg,#F2E9DD 0%,#EFE7DA 100%)', ''.join(b))

SETS = [('01-xhami', set1, 6), ('02-fasulet', set2, 6), ('03-fshehim', set3, 7)]
if __name__ == '__main__':
    for name, fn, c in SETS:
        w, html = fn()
        open(os.path.join(OUT, f'set-{name}.html'), 'w', encoding='utf-8').write(html)
