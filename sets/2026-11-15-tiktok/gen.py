import os
BASE = '/home/user/Shprehu-3.5/Claude outputs/reklama/2026-11-12-tiktok-ftohti/burimi/gen.py'
OUT = os.path.dirname(os.path.abspath(__file__))
ns = {'__file__': BASE}
exec(open(BASE, encoding='utf-8').read().split('# 01:')[0], ns)
page, slide, end, D, H = ns['page'], ns['slide'], ns['end'], ns['D'], ns['H']

# 01: „Mos lër gjë në pjatë!“ (rregull i pashkruar), pjata zbrazet dhe pastaj mbushet me „hallet“
def plate(x, y, fill):
    o = D(x, y, 420, 420, 'border-radius:50%;background:#FBF6EA;box-shadow:0 18px 30px rgba(60,40,20,.18),inset 0 0 0 26px #EFE6D6')
    if fill:
        o += D(x + 70, y + 70, 280, 280, f'border-radius:50%;background:{fill}')
    return o
def set1():
    W = 6480
    b = [D(0, 1440, W - 1080, 480, 'background:repeating-linear-gradient(45deg,#E9DCC6 0 30px,#E2D3BA 30px 60px)')]
    b.append(plate(330, 1470, 'radial-gradient(circle at 40% 40%,#E3A75C 0 40px,transparent 41px),radial-gradient(circle at 65% 60%,#9E2F2A 0 36px,transparent 37px),radial-gradient(circle at 35% 70%,#6E8B4E 0 34px,transparent 35px),#E8C68A'))
    b.append(plate(1080 + 330, 1470, 'radial-gradient(circle at 50% 50%,#E3A75C 0 30px,transparent 31px),#F1E3C7'))
    b.append(plate(2160 + 330, 1470, None))
    b.append(plate(3240 + 330, 1470, None))
    b.append(D(3240 + 400, 1540, 280, 280, "display:flex;align-items:center;justify-content:center;text-align:center;font-family:Fraunces,serif;font-style:italic;font-size:44px;line-height:1.15;color:#8C4A2F", 'gjithçka<br>deri në fund'))
    b.append(plate(4320 + 330, 1470, None))
    b.append(D(4320 + 400, 1540, 280, 280, "display:flex;align-items:center;justify-content:center;text-align:center;font-family:Fraunces,serif;font-style:italic;font-size:46px;color:#3F6259", 'pak, me&nbsp;radhë'))
    b.append(slide(0, 'lt', 'Rregull i pashkruar', '„Mos lër gjë në pjatë, <em>se është&nbsp;mëkat!“</em>', hint=H))
    b.append(slide(1, 'lt', 'Gjithmonë', 'Edhe kur ishim ngopur. <em>Edhe kur s’na&nbsp;pëlqente.</em>'))
    b.append(slide(2, 'lt', 'Mësuam', 'Të mbarojmë gjithçka që na vihet përpara. <em>Pa pyetur nëse&nbsp;mundemi.</em>'))
    b.append(slide(3, 'lt', 'Edhe me hallet', 'I mbajmë të gjitha, deri në fund. <em>Edhe kur s’kemi më&nbsp;vend.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'Mund ta lësh diçka në pjatë. <em>Mund ta ndash me dikë&nbsp;tjetër.</em>', 'Çfarë s’të lejohej të lije në pjatë? Shkruaje në&nbsp;koment.'))
    b.append(end(5, 'Ndaje pak nga ajo që mban. <em>Dikush të dëgjon, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#F5EFE4 0%,#F2EADC 74%,#E2D3BA 75%)', ''.join(b))

# 02: ora 23:50, plani për nesër (sjellje e fshehur me orë), lista e alarmeve në telefon
def alarms(x, y, rows):
    o = D(x, y, 380, 600, 'background:#0F1416;border-radius:48px;box-shadow:0 22px 50px rgba(0,0,0,.45)')
    o += D(x + 16, y + 16, 348, 568, 'background:#1B2326;border-radius:36px')
    for k, (t, on, note) in enumerate(rows):
        yy = y + 70 + k * 100
        col = '#FAF7F1' if on else 'rgba(250,247,241,.35)'
        o += D(x + 44, yy, 220, 70, f'font-family:Fraunces,serif;font-size:58px;font-weight:600;color:{col}', t)
        o += D(x + 44, yy + 62, 260, 30, 'font-size:22px;color:rgba(250,247,241,.5)', note)
        o += D(x + 270, yy + 18, 64, 36, f'border-radius:18px;background:{"#8FB8A8" if on else "rgba(250,247,241,.18)"}')
        o += D(x + (300 if on else 274), yy + 22, 28, 28, 'border-radius:50%;background:#FAF7F1')
    return o
def set2():
    W = 6480
    b = []
    plan = [('06:00', True, 'zgjohu'), ('06:15', True, 'vrapo'), ('06:45', True, 'lexo'), ('07:10', True, 'mëngjes i shëndetshëm')]
    real = [('06:00', False, 'shtyrë'), ('06:15', False, 'shtyrë'), ('06:45', False, 'shtyrë'), ('07:42', True, 'u zgjove')]
    b.append(alarms(600, 1190, plan))
    b.append(alarms(1080 + 600, 1190, plan))
    b.append(alarms(2160 + 600, 1190, real))
    b.append(alarms(3240 + 600, 1190, real))
    b.append(alarms(4320 + 600, 1190, [('07:00', True, 'mjafton kaq'), ('', False, ''), ('', False, ''), ('', False, '')]))
    b.append(slide(0, 'dk', 'Ora 23:50', 'Natën planifikon një mëngjes <em>të&nbsp;përsosur.</em>', hint=H))
    b.append(slide(1, 'dk', 'Plani', 'Zgjohu në 6. Vrapo. Lexo. <em>Bëhu tjetër njeri nga&nbsp;nesër.</em>'))
    b.append(slide(2, 'dk', 'Ora 07:42', 'Alarmin e shtyre katër herë. <em>Dhe dita nis me&nbsp;faj.</em>'))
    b.append(slide(3, 'dk', 'E vërteta', 'Plani ishte për dikë që s’lodhet kurrë. <em>Ti je njeri, jo&nbsp;listë.</em>'))
    b.append(slide(4, 'dk', 'Sot', 'Bëje planin për veten që je. <em>Një gjë e vogël mjafton.</em>', 'Sa herë e shtyn alarmin ti? Shkruaje numrin në&nbsp;koment.'))
    b.append(end(5, 'Kur faji të rëndon që në mëngjes, <em>thuaja dikujt që të dëgjon, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#1A2124 0%,#1F2A2E 70%,#171E21 100%)', ''.join(b))

# 03: vijat e gjatësisë në kornizën e derës (ritual), korniza ngjitet nëpër slide-e
def set3():
    W = 6480
    b = [D(0, 0, W - 1080, 1920, 'background:linear-gradient(90deg,transparent 0 0)')]
    for i in range(5):
        x0 = i * 1080 + 920
        b.append(D(x0, 0, 110, 1920, 'background:linear-gradient(90deg,#E9DFCC,#FBF6EA 40%,#E3D7C0);box-shadow:-6px 0 0 #D6C8AD'))
        marks = [(1760, '2001'), (1660, '2002'), (1560, '2004'), (1470, '2006'), (1390, '2009')][: i + 1] if i < 4 else []
        for y, yr in marks:
            b.append(D(x0 + 6, y, 90, 6, 'background:#3A3A3A;border-radius:3px'))
            b.append(D(x0 - 130, y - 22, 120, 40, 'font-family:Fraunces,serif;font-style:italic;font-size:36px;color:#5E4632;text-align:right', yr))
        if i == 4:
            b.append(D(x0 + 6, 1300, 90, 6, 'background:#3F6259;border-radius:3px'))
            b.append(D(x0 - 300, 1278, 290, 40, 'font-family:Fraunces,serif;font-style:italic;font-size:36px;color:#3F6259;text-align:right', 'sot, brenda'))
    b.append(slide(0, 'lt', 'Ritual', 'Nëna na matte në kornizën e&nbsp;derës. <em>Çdo vit, një vijë e&nbsp;re.</em>', hint=H))
    b.append(slide(1, 'lt', 'Me laps', 'Shpina pas murit, libri mbi kokë. <em>„Mos u ngri në&nbsp;gishta!“</em>'))
    b.append(slide(2, 'lt', 'Çdo vit', 'Vija ngjitej pak më lart. <em>Dhe ne ndiheshim më të&nbsp;mëdhenj.</em>'))
    b.append(slide(3, 'lt', 'Por', 'Askush s’e matte sa peshë mbanim. <em>Vetëm sa ishim rritur.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'Edhe rritja brenda vlen. <em>Edhe kur s’e mat&nbsp;askush.</em>', 'A kanë mbetur vijat te dera juaj? Shkruaje në&nbsp;koment.'))
    b.append(end(5, 'Fol për atë që po mban. <em>Dikush të dëgjon, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#EFE8DA 0%,#ECE3D2 100%)', ''.join(b))

# 04: 5 gjëra që të bëjnë të ndihesh në shtëpi (listë me boshllëk), kornizat në mur
def frame(x, y, inner, col):
    return D(x, y, 300, 300, f'background:#FBF6EA;border:16px solid {col};box-sizing:border-box;box-shadow:0 14px 26px rgba(60,40,20,.2)', inner)
def set4():
    W = 7560
    b = [D(0, 1420, W - 1080, 6, 'background:rgba(60,40,20,.12)')]
    icons = [
        D(70, 90, 130, 80, 'background:#D9A55B;border-radius:60px 60px 20px 20px;box-shadow:inset 0 -14px 0 #C58C42'),
        D(90, 60, 100, 140, 'border:10px solid #3F6259;border-radius:50px 50px 10px 10px;box-sizing:border-box'),
        D(60, 110, 150, 30, 'background:#C79A3C;border-radius:15px') + D(180, 90, 40, 70, 'border:10px solid #C79A3C;border-radius:50%;box-sizing:border-box'),
        "<div style=\"position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-family:Fraunces,serif;font-style:italic;font-size:42px;color:#3F6259;text-align:center\">„Si ishte<br>dita?“</div>",
        D(70, 80, 70, 110, 'background:#B04A2C;border-radius:30px 30px 14px 30px') + D(150, 80, 70, 110, 'background:#B04A2C;border-radius:30px 30px 30px 14px'),
    ]
    cols = ['#8C6A4A', '#5E4632', '#8C6A4A', '#3F6259', '#5E4632']
    for i in range(5):
        b.append(frame((i + 1) * 1080 + 640, 1480, icons[i], cols[i]))
    b.append(slide(0, 'lt', 'Listë', '5 gjëra që të bëjnë të ndihesh <em>në&nbsp;shtëpi.</em>', 'E katërta s’ka të bëjë me&nbsp;shtëpinë.', hint=H))
    b.append(slide(1, 'lt', 'E para', 'Era e bukës <em>kur hyn nga&nbsp;dera.</em>'))
    b.append(slide(2, 'lt', 'E dyta', 'Zëri i dikujt <em>në&nbsp;kuzhinë.</em>'))
    b.append(slide(3, 'lt', 'E treta', 'Çelësi që hyn <em>në bravën e&nbsp;vet.</em>'))
    b.append(slide(4, 'lt', 'E katërta', 'Dikush që të pyet „si ishte dita?“ <em>dhe pret&nbsp;përgjigjen.</em>', 'Ndonjëherë shtëpia është një&nbsp;njeri.'))
    b.append(slide(5, 'lt', 'E pesta', 'Çorapet e ngrohta <em>pas një dite të&nbsp;gjatë.</em>', 'Cila prej tyre të mungon më shumë? Shkruaj numrin në&nbsp;koment.'))
    b.append(end(6, 'Kur s’ke kush të pyet si ishte dita, <em>trego këtu, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#F4EDE2 0%,#EFE6D6 100%)', ''.join(b))

# 05: fija e shkurtër e gjyshes (urtësi), peri kalon nëpër slide-e dhe ngatërrohet kur është i gjatë
def set5():
    W = 6480
    b = []
    b.append(D(300, 1600, 200, 14, 'background:#9AA0A6;border-radius:7px;transform:rotate(-20deg)'))
    b.append(D(470, 1555, 26, 26, 'border:5px solid #9AA0A6;border-radius:50%;box-sizing:border-box'))
    b.append(D(490, 1570, 1600, 0, 'border-top:6px solid #B04A2C;border-radius:50%;transform:rotate(3deg)'))
    for k in range(9):
        b.append(D(1080 + 400 + k * 30, 1500 + (k % 3) * 40, 260, 160, 'border:6px solid #B04A2C;border-radius:50%;opacity:.85;transform:rotate(' + str(k * 23) + 'deg)'))
    b.append(D(2160 + 300, 1620, 520, 0, 'border-top:6px solid #B04A2C'))
    b.append(D(2160 + 820, 1600, 40, 40, 'border-radius:50%;background:#B04A2C'))
    b.append(D(3240 + 260, 1600, 600, 120, 'background:repeating-linear-gradient(90deg,#B04A2C 0 26px,transparent 26px 52px);height:6px;top:1620px'))
    b.append(D(3240 + 200, 1500, 720, 260, 'border:4px dashed rgba(63,98,89,.35);border-radius:20px'))
    b.append(D(4320 + 360, 1560, 360, 120, 'background:repeating-linear-gradient(90deg,#B04A2C 0 26px,transparent 26px 52px);height:6px;top:1620px'))
    b.append(slide(0, 'lt', 'Gjyshja', '„Fije e gjatë, <em>nyje&nbsp;shumë.“</em>', hint=H))
    b.append(slide(1, 'lt', 'Kur qepnim', 'Donim ta merrnim gjithë perin njëherësh. <em>Dhe ngatërrohej&nbsp;gjithmonë.</em>'))
    b.append(slide(2, 'lt', 'Ajo', 'Priste një fije të shkurtër. <em>Qepte pak, pastaj merrte&nbsp;tjetrën.</em>'))
    b.append(slide(3, 'lt', 'E vërteta', 'Edhe hallet ngatërrohen kur i merr të gjitha&nbsp;njëherësh. <em>Pak nga pak, qepen.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'Merr vetëm një hall sot. <em>Vetëm një&nbsp;fije.</em>', 'Çfarë thoshte gjyshja jote kur qepte? Shkruaje në&nbsp;koment.'))
    b.append(end(5, 'Fillo nga një fjali. <em>Dikush të dëgjon, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#F6F0E6 0%,#F1E8D9 100%)', ''.join(b))

SETS = [('01-pjata', set1), ('02-plani', set2), ('03-korniza', set3), ('04-shtepia', set4), ('05-fija', set5)]
if __name__ == '__main__':
    for name, fn in SETS:
        w, html = fn()
        open(os.path.join(OUT, f'set-{name}.html'), 'w', encoding='utf-8').write(html)
        print(name, w)
