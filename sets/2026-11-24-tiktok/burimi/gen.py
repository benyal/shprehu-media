import os
BASE = '/home/user/Shprehu-3.5/Claude outputs/reklama/2026-11-12-tiktok-ftohti/burimi/gen.py'
OUT = os.path.dirname(os.path.abspath(__file__))
ns = {'__file__': BASE}
exec(open(BASE, encoding='utf-8').read().split('# 01:')[0], ns)
page, slide, end, D, H = ns['page'], ns['slide'], ns['end'], ns['D'], ns['H']

# 01: „Zjarri i madh ndizet ngadalë“ (urtësi e gjyshes), flaka rritet nëpër slide-e
def fire(x, k):
    o = D(x, 1780, 1080, 140, 'background:#5E4632')
    o += D(x + 380, 1640, 320, 40, 'background:#8C6A4A;border-radius:20px;transform:rotate(-8deg)')
    o += D(x + 380, 1640, 320, 40, 'background:#7A5A3A;border-radius:20px;transform:rotate(8deg)')
    h = [40, 90, 160, 250, 340][k]
    w = [60, 110, 160, 210, 250][k]
    o += D(x + 540 - w // 2, 1650 - h, w, h, 'background:radial-gradient(ellipse at 50% 85%,#FFE2A6 0%,#F2A23A 45%,#D9572A 80%,rgba(217,87,42,0) 100%);border-radius:50% 50% 45% 45%;filter:blur(1px)')
    return o
def set1():
    W = 6480
    b = [fire(i * 1080, i) for i in range(5)]
    b.append(slide(0, 'dk', 'Gjyshja', '„Zjarri i madh <em>ndizet&nbsp;ngadalë.“</em>', hint=H))
    b.append(slide(1, 'dk', 'Te soba, çdo mëngjes', 'Fillimisht vinte shkarpat. <em>Pastaj drutë e&nbsp;mëdha.</em>'))
    b.append(slide(2, 'dk', 'Kur nxitonim', '„Mos e mbyt me dru, <em>se të shuhet.“</em>'))
    b.append(slide(3, 'dk', 'Ajo e dinte', 'As njeriu s’ndizet me nxitim. <em>Ka nevojë për&nbsp;kohë.</em>'))
    b.append(slide(4, 'dk', 'Sot', 'Mos i kërko vetes shumë menjëherë. <em>Pak nga&nbsp;pak.</em>', 'Kush e ndizte sobën në shtëpinë tënde? Shkruaje në&nbsp;koment.'))
    b.append(end(5, 'Pak nga pak, <em>dikush të dëgjon, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#1E1A17 0%,#2A221D 100%)', ''.join(b))

# 02: „Mos e fshi shtëpinë natën, se e nxjerr fatin jashtë!“ (rregull i pashkruar), fshesa dhe pluhuri
def broom(x, k):
    o = D(x, 1760, 1080, 160, 'background:#C9B08A')
    o += D(x + 640, 1250, 18, 420, 'background:#8C6A4A;border-radius:9px;transform:rotate(18deg)')
    o += D(x + 560, 1640, 170, 90, 'background:#D9B24C;border-radius:10px 10px 40px 40px;transform:rotate(18deg)')
    dust = [6, 6, 6, 3, 0][k]
    for j in range(dust):
        o += D(x + 180 + j * 55, 1700 - (j % 3) * 18, 30, 30, 'background:rgba(110,90,60,.35);border-radius:50%')
    return o
def set2():
    W = 6480
    b = [broom(i * 1080, i) for i in range(5)]
    b.append(slide(0, 'lt', 'Rregull i pashkruar', '„Mos e fshi shtëpinë natën, <em>se e nxjerr fatin&nbsp;jashtë!“</em>', hint=H))
    b.append(slide(1, 'lt', 'E linim për mëngjes', 'Pluhuri priste <em>te&nbsp;dera.</em>'))
    b.append(slide(2, 'lt', 'Por', 'Askush s’na tha si ta pastrojmë <em>rrëmujën&nbsp;brenda.</em>'))
    b.append(slide(3, 'lt', 'E vërteta', 'Fati s’ikën me pluhurin. <em>Ikën kur mbajmë gjithçka&nbsp;brenda.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'Nxirre pak nga ajo që të rëndon. <em>Edhe&nbsp;natën.</em>', 'E ke dëgjuar këtë rregull? Shkruaj „po“ në&nbsp;koment.'))
    b.append(end(5, 'Ajo që të rëndon <em>mund ta thuash këtu, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#F6F0E6 0%,#EEE5D6 100%)', ''.join(b))

# 03: 5 gjëra kur na bie telefoni nga nëna në mes të ditës (listë me boshllëk), valët e ziles
def phone(x, n):
    o = D(x + 410, 1240, 260, 470, 'background:#20292D;border-radius:40px')
    o += D(x + 430, 1270, 220, 410, 'background:#3F6259;border-radius:26px')
    o += D(x + 470, 1360, 140, 140, 'background:#F3E6C8;border-radius:50%;color:#3F6259;font:700 44px/140px Fraunces,serif;text-align:center', 'Ma')
    for k in range(n):
        o += D(x + 540 - (180 + k * 60), 1475 - (180 + k * 60), 2 * (180 + k * 60), 2 * (180 + k * 60), 'border:6px solid rgba(232,185,108,%.2f);border-radius:50%%' % (0.6 - k * 0.1))
    return o
def set3():
    W = 7560
    b = [phone(i * 1080, n) for i, n in enumerate([1, 1, 2, 3, 4, 4])]
    b.append(slide(0, 'lt', 'Listë', '5 gjëra kur na bie telefoni <em>nga nëna në mes të&nbsp;ditës.</em>', 'E katërta e bëjmë të gjithë.', hint=H))
    b.append(slide(1, 'lt', 'E para', 'Na ngrin zemra <em>për një&nbsp;sekondë.</em>'))
    b.append(slide(2, 'lt', 'E dyta', '„Alo, ma, çka ka?“ <em>Para se të thotë&nbsp;asgjë.</em>'))
    b.append(slide(3, 'lt', 'E treta', '„Asgjë, thjesht të dëgjoj.“ <em>Dhe na kthehet&nbsp;fryma.</em>'))
    b.append(slide(4, 'lt', 'E katërta', 'Themi „jam në punë, ma“. <em>Dhe e mbyllim shpejt.</em>', 'Pastaj na vjen keq gjithë&nbsp;ditën.'))
    b.append(slide(5, 'lt', 'E pesta', 'Në mbrëmje e marrim ne. <em>„Çka bëre sot, ma?“</em>', 'Cilën e bën ti? Shkruaj numrin në&nbsp;koment.'))
    b.append(end(6, 'Edhe ty dikush do të të dëgjojë. <em>Këtu, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(90deg,#F2E9DD 0%,#E9EEF0 100%)', ''.join(b))

SETS = [('01-zjarri', set1, 6), ('02-fshesa', set2, 6), ('03-telefoni', set3, 7)]
if __name__ == '__main__':
    for name, fn, c in SETS:
        w, html = fn()
        open(os.path.join(OUT, f'set-{name}.html'), 'w', encoding='utf-8').write(html)
