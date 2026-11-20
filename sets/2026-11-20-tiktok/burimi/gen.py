import os
BASE = '/home/user/Shprehu-3.5/Claude outputs/reklama/2026-11-12-tiktok-ftohti/burimi/gen.py'
OUT = os.path.dirname(os.path.abspath(__file__))
ns = {'__file__': BASE}
exec(open(BASE, encoding='utf-8').read().split('# 01:')[0], ns)
page, slide, end, D, H = ns['page'], ns['slide'], ns['end'], ns['D'], ns['H']

# 01: „Laji duart me ujë të ftohtë“ (urtësi e gjyshes), rubineti dhe pikat që qetësohen
def tap(x, drops):
    o = D(x + 420, 1240, 60, 160, 'background:#9AA3A8;border-radius:10px')
    o += D(x + 380, 1220, 220, 50, 'background:#B7BEC2;border-radius:25px')
    for k in range(drops):
        o += D(x + 436, 1430 + k * 70, 28, 40, 'background:#8FC1D6;border-radius:50% 50% 50% 50%/60% 60% 40% 40%')
    o += D(x + 220, 1640, 480, 160, 'background:#F4F6F5;border-radius:20px 20px 120px 120px;box-shadow:0 16px 30px rgba(40,60,60,.15)')
    return o
def set1():
    W = 6480
    b = [tap(i * 1080, n) for i, n in enumerate([3, 3, 2, 1, 1])]
    b.append(slide(0, 'lt', 'Gjyshja', 'Kur nxeheshim, gjyshja s’na qortonte. <em>Na çonte te&nbsp;rubineti.</em>', hint=H))
    b.append(slide(1, 'lt', 'Me zë të ulët', '„Laji duart me ujë të ftohtë. <em>Pastaj&nbsp;fol.“</em>'))
    b.append(slide(2, 'lt', 'Na dukej e kotë', 'Një minutë ujë. <em>Dhe zemërimi ulej&nbsp;pak.</em>'))
    b.append(slide(3, 'lt', 'Ajo e dinte', 'Fjala që thua në vapë <em>s’është ajo që mendon.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'Para se ta thuash, merr një minutë. <em>Pastaj&nbsp;fol.</em>', 'Çfarë bënte gjyshja jote kur zemëroheshe? Shkruaje në&nbsp;koment.'))
    b.append(end(5, 'Kur të duhet ta nxjerrësh, <em>thuaje këtu, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#EEF2F1 0%,#E5ECEA 100%)', ''.join(b))

# 02: „Mos e shiko në sy kur të qorton!“ (rregull i pashkruar), pllakat e dyshemesë dhe këpucët
def floor(x, up):
    o = D(x, 1300, 1080, 620, 'background:repeating-linear-gradient(90deg,#D8CDB8 0 180px,#CFC3AC 180px 360px)')
    o += D(x + 380, 1620, 140, 70, 'background:#3A3F44;border-radius:40px 40px 10px 10px')
    o += D(x + 560, 1620, 140, 70, 'background:#3A3F44;border-radius:40px 40px 10px 10px')
    if up:
        o += D(x + 440, 1100, 200, 140, 'border-radius:50%;background:radial-gradient(circle,rgba(232,185,108,.5),rgba(232,185,108,0) 70%)')
    return o
def set2():
    W = 6480
    b = [floor(i * 1080, i == 4) for i in range(5)]
    b.append(slide(0, 'lt', 'Rregull i pashkruar', '„Mos e shiko në sy <em>kur të&nbsp;qorton!“</em>', hint=H))
    b.append(slide(1, 'lt', 'E mësuam herët', 'Sytë poshtë, te pllakat. <em>Edhe kur kishim&nbsp;të&nbsp;drejtë.</em>'))
    b.append(slide(2, 'lt', 'Pastaj', 'Shikonim poshtë edhe kur na lëndonin. <em>Edhe kur duhej të&nbsp;flisnim.</em>'))
    b.append(slide(3, 'lt', 'E vërteta', 'Respekti s’do të thotë të heshtësh. <em>As të mos e ngresh&nbsp;kokën.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'Ngrije kokën. <em>Ke të drejtë të thuash si&nbsp;ndihesh.</em>', 'E ke dëgjuar këtë rregull? Shkruaj „po“ në&nbsp;koment.'))
    b.append(end(5, 'Këtu askush s’të qorton. <em>Fol lirshëm, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#F5EFE6 0%,#EFE7DA 100%)', ''.join(b))

# 03: ora 23:10, „natën e mirë“ (sjellje e fshehur), telefoni në errësirë, ora ecën
def phone(x, t):
    o = D(x + 330, 1150, 420, 700, 'background:#111517;border-radius:50px;box-shadow:0 0 120px rgba(143,184,168,.25)')
    o += D(x + 352, 1172, 376, 656, 'background:#1E2A2E;border-radius:40px')
    o += D(x + 400, 1260, 280, 64, 'background:#3F6259;border-radius:20px;color:#FAF7F1;font-size:28px;display:flex;align-items:center;justify-content:center', 'Natën e mirë')
    o += D(x + 352, 1700, 376, 60, 'color:#8FB8A8;font-family:Courier New,monospace;font-weight:700;font-size:40px;text-align:center', t)
    return o
def set3():
    W = 6480
    b = [phone(i * 1080, t) for i, t in enumerate(['23:10', '23:40', '00:15', '00:50', '00:50'])]
    b.append(slide(0, 'dk', 'Ora 23:10', 'Ia shkruan të gjithëve „natën e mirë“. <em>Pastaj rri edhe një orë&nbsp;zgjuar.</em>', hint=H))
    b.append(slide(1, 'dk', 'Ora 23:40', 'Video pas videoje. <em>S’po shikon asgjë.</em>'))
    b.append(slide(2, 'dk', 'Ora 00:15', 'Nuk do të flesh. <em>Do që dita të mos&nbsp;mbarojë&nbsp;ende.</em>'))
    b.append(slide(3, 'dk', 'E vërteta', 'Ajo orë është e vetmja vetëm për ty. <em>Prandaj s’e lëshon.</em>'))
    b.append(slide(4, 'dk', 'Sot', 'Merre atë kohë gjatë ditës. <em>Edhe pak&nbsp;minuta.</em>', 'Në çfarë ore e fik telefonin ti? Shkruaje në&nbsp;koment.'))
    b.append(end(5, 'Kur s’të zë gjumi, <em>dikush të dëgjon, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#14191B 0%,#1C2326 100%)', ''.join(b))

# 04: 5 gjëra që thoshte gjyshja kur e vizitoje (listë me boshllëk), tasi me ëmbëlsira mbushet
def bowl(x, n):
    o = D(x + 340, 1560, 400, 160, 'background:#E9E2D5;border-radius:0 0 200px 200px;box-shadow:0 14px 26px rgba(40,30,20,.15)')
    for k in range(n):
        o += D(x + 370 + (k % 4) * 85, 1520 - (k // 4) * 50, 70, 60, f'background:{["#E8B96C","#B04A2C","#3F6259","#8FB8A8"][k % 4]};border-radius:30px')
    return o
def set4():
    W = 7560
    b = [bowl(i * 1080, n) for i, n in enumerate([0, 2, 4, 6, 8, 8])]
    b.append(slide(0, 'lt', 'Listë', '5 gjëra që thoshte gjyshja kur e <em>vizitoje.</em>', 'E katërta ishte gjithmonë e fundit.', hint=H))
    b.append(slide(1, 'lt', 'E para', '„Hajde, hajde, <em>sa u rrite!“</em>'))
    b.append(slide(2, 'lt', 'E dyta', '„Ha diçka, <em>je dobësuar.“</em>'))
    b.append(slide(3, 'lt', 'E treta', '„Si ia kalojnë <em>të&nbsp;tutë?“</em>'))
    b.append(slide(4, 'lt', 'E katërta', '„Ulu edhe pak, <em>mos ik&nbsp;akoma.“</em>', 'Sot e kuptojmë: s’donte të mbetej&nbsp;vetëm.'))
    b.append(slide(5, 'lt', 'E pesta', '„Eja <em>prapë.“</em>', 'Cila prej tyre të kujtohet më shumë? Shkruaj numrin në&nbsp;koment.'))
    b.append(end(6, 'Ulu edhe pak me veten. <em>Fol këtu, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(90deg,#F6EEE3 0%,#F2E6D6 100%)', ''.join(b))

# 05: lyerja me gëlqere (ritual), muri bëhet i bardhë nga slide-i në slide
def wall(x, pct):
    o = D(x + 160, 1180, 760, 560, 'background:#C9BBA0;border-radius:8px')
    o += D(x + 160, 1180, int(760 * pct), 560, 'background:#FBFAF6;border-radius:8px')
    o += D(x + 160 + int(760 * pct) - 30, 1420, 60, 220, 'background:#8C6A4A;border-radius:10px') if 0 < pct < 1 else ''
    return o
def set5():
    W = 6480
    b = [wall(i * 1080, p) for i, p in enumerate([0, .3, .6, .9, 1])]
    b.append(slide(0, 'lt', 'Ritual', 'Një herë në vit, shtëpia <em>lyhej me&nbsp;gëlqere.</em>', hint=H))
    b.append(slide(1, 'lt', 'Të gjithë ndihmonin', 'Mobiljet në mes, gazeta në dysheme. <em>Era e gëlqeres&nbsp;kudo.</em>'))
    b.append(slide(2, 'lt', 'Në fund', 'Dhoma dukej si e re. <em>Edhe më e&nbsp;madhe.</em>'))
    b.append(slide(3, 'lt', 'E vërteta', 'Edhe muret e brendshme <em>duan pak dritë herë pas&nbsp;here.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'Mos prit një vit. <em>Fillo me një&nbsp;mur.</em>', 'A e ke bërë ndonjëherë? Shkruaje në&nbsp;koment.'))
    b.append(end(5, 'Fillo me një fjalë. <em>Dikush të dëgjon, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#F3EEE4 0%,#EAE3D6 100%)', ''.join(b))

SETS = [('01-uji', set1), ('02-syte', set2), ('03-natenemire', set3), ('04-gjyshja', set4), ('05-gelqerja', set5)]
if __name__ == '__main__':
    for name, fn in SETS:
        w, html = fn()
        open(os.path.join(OUT, f'set-{name}.html'), 'w', encoding='utf-8').write(html)
        print(name, w)
