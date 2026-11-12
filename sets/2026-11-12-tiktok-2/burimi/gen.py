import os, sys, random
sys.path.insert(0, '/home/user/Shprehu-3.5/Claude outputs/reklama/2026-11-12-tiktok-ftohti/burimi')
import importlib.util
spec = importlib.util.spec_from_file_location('baza', '/home/user/Shprehu-3.5/Claude outputs/reklama/2026-11-12-tiktok-ftohti/burimi/gen.py')
OUT = os.path.dirname(os.path.abspath(__file__))
src = open(spec.origin, encoding='utf-8').read().split('# 01:')[0]
ns = {'__file__': spec.origin}
exec(src, ns)
page, slide, end, D, H = ns['page'], ns['slide'], ns['end'], ns['D'], ns['H']

# 01: gjyshja dhe fshesa (urtësi), oborri fshihet nga slide-i në slide
def set1():
    W = 6480
    b = []
    random.seed(7)
    for k in range(140):
        x = random.randint(0, W - 1080); y = random.randint(1500, 1880)
        clean = x > 1080 * (1 + (y - 1500) / 400 * 0.2) + 900 * (x // 1080)
        if x // 1080 >= 3:
            continue
        r = random.randint(14, 30)
        col = random.choice(['#C98B4A', '#B5652F', '#D9A55B', '#9C7A3C'])
        b.append(D(x, y, r * 2, r, f'background:{col};border-radius:50% 0 50% 0;transform:rotate({random.randint(0,180)}deg);opacity:.85'))
    for i in range(1, 5):
        for j in range(5):
            x0 = i * 1080 - 200 + j * 60
            b.append(D(x0, 1520 + j * 70, 560, 70, 'border-top:5px solid rgba(120,90,50,.22);border-radius:50% 50% 0 0'))
    b.append(D(5160, 1250, 26, 520, 'background:linear-gradient(90deg,#9C7A3C,#C9A46A,#9C7A3C);border-radius:13px;transform:rotate(14deg)'))
    b.append(D(5070, 1700, 210, 170, 'background:repeating-linear-gradient(90deg,#D9B26A 0 10px,#C29A52 10px 16px);border-radius:20px 20px 60px 60px;transform:rotate(14deg)'))
    b.append(slide(0, 'lt', 'Gjyshja', 'Kur zemërohej, gjyshja s’bërtiste. <em>Merrte&nbsp;fshesën.</em>', hint=H))
    b.append(slide(1, 'lt', 'Oborri', 'Fshinte nga porta deri te shtëpia. <em>Ngadalë, pa folur me&nbsp;askënd.</em>'))
    b.append(slide(2, 'lt', 'Në fund', 'Kur mbaronte oborri, <em>mbaronte edhe&nbsp;zemërimi.</em>', 'Pastaj ulej, dhe fliste&nbsp;qetë.'))
    b.append(slide(3, 'lt', 'Ajo e dinte', 'Zemërimit i duhet një rrugë nga të dalë. <em>Jo një njeri ku të&nbsp;bjerë.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'S’ke oborr? Ec një xhiro. <em>Ose thuaja dikujt që s’të&nbsp;gjykon.</em>'))
    b.append(end(5, 'Kur s’di ku ta çosh, <em>fol me dikë që të dëgjon, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#F5EEE1 0%,#F5EEE1 74%,#E6D6B8 78%,#DCC9A6 100%)', ''.join(b))

# 02: „Te askush s’shkohet me duar bosh“ (rregull i pashkruar), dhuratat zhduken deri te dera e hapur
def box(x, y):
    return (D(x, y, 300, 190, 'background:#B5443A;border-radius:12px;box-shadow:0 14px 24px rgba(60,30,20,.2)')
            + D(x + 135, y, 30, 190, 'background:#E8B96C') + D(x, y + 80, 300, 30, 'background:#E8B96C')
            + D(x + 100, y - 46, 100, 60, 'border:12px solid #E8B96C;border-radius:50% 50% 10px 10px'))
def bag(x, y):
    o = ''.join(D(x + 30 + (k % 3) * 80, y - 20 + (k // 3) * 60, 86, 86, 'border-radius:50%;background:radial-gradient(circle at 35% 30%,#FFB45C,#E97A1C 70%)') for k in range(5))
    return o + D(x, y + 70, 300, 170, 'background:rgba(240,240,236,.88);border-radius:10px 10px 30px 30px;box-shadow:0 14px 24px rgba(60,30,20,.15)')
def coffee(x, y):
    return D(x, y, 210, 270, 'background:linear-gradient(#5A3A26,#3E2618);border-radius:10px 10px 6px 6px;box-shadow:0 14px 24px rgba(60,30,20,.25)', D(30, 90, 150, 70, 'background:#E8B96C;border-radius:6px;font-weight:800;color:#3E2618;font-size:34px;display:flex;align-items:center;justify-content:center', 'KAFE'))
def door(x, y):
    return (D(x, y, 420, 560, 'background:#3A2A20;border-radius:10px 10px 0 0')
            + D(x + 20, y + 20, 380, 540, 'background:linear-gradient(90deg,#FFD79A,#F2B866)')
            + D(x + 20, y + 20, 230, 540, 'background:#8C6A4A;transform:perspective(900px) rotateY(-38deg);transform-origin:0 50%;box-shadow:inset -10px 0 0 rgba(0,0,0,.12)'))
def set2():
    W = 6480
    b = [D(0, 1760, W, 160, 'background:#D9CBB1')]
    b.append(bag(390, 1520))
    b.append(box(1080 + 200, 1570))
    b.append(coffee(1080 + 600, 1490))
    b.append(D(2160 + 330, 1500, 420, 260, 'border:6px dashed rgba(63,98,89,.4);border-radius:30px'))
    b.append(door(3240 + 330, 1200))
    b.append(door(4320 + 330, 1200))
    b.append(D(4320 + 360, 1760, 360, 40, 'background:#B5443A;border-radius:8px'))
    b.append(slide(0, 'lt', 'Rregull i pashkruar', 'Te askush s’shkohet me duar&nbsp;bosh. <em>E mësuam që&nbsp;fëmijë.</em>', hint=H))
    b.append(slide(1, 'lt', 'Gjithmonë', 'Një kuti çokollata, pak portokalle, një pako&nbsp;kafe. <em>Pa to, as që&nbsp;trokisnim.</em>'))
    b.append(slide(2, 'lt', 'E vërteta', 'Prandaj, kur jemi bosh brenda, <em>s’shkojmë te&nbsp;askush.</em>'))
    b.append(slide(3, 'lt', 'Por', 'Ata që të duan s’të presin për atë që sjell. <em>Të presin&nbsp;ty.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'Shko edhe kur s’ke asgjë për të sjellë. <em>Mjafton që&nbsp;vjen.</em>'))
    b.append(end(5, 'Edhe kur s’ke asgjë të bukur për të thënë, <em>ka dikë që të dëgjon, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(90deg,#F6F0E4,#F1E8D8)', ''.join(b))

for name, fn in [('01-fshesa', set1), ('02-duarbosh', set2)]:
    w, html = fn()
    open(os.path.join(OUT, f'set-{name}.html'), 'w', encoding='utf-8').write(html)
    print(name, w)
