import os
BASE = '/home/user/Shprehu-3.5/Claude outputs/reklama/2026-11-12-tiktok-ftohti/burimi/gen.py'
OUT = os.path.dirname(os.path.abspath(__file__))
ns = {'__file__': BASE}
exec(open(BASE, encoding='utf-8').read().split('# 01:')[0], ns)
page, slide, end, D, H = ns['page'], ns['slide'], ns['end'], ns['D'], ns['H']

# 01: „Mos e zër në gojë, se e thërret!“ (rregull i pashkruar), flluskat e mbyllura me shirit hapen nga slide-i në slide
def bubble(x, y, w, h, taped, word=''):
    o = D(x, y, w, h, 'background:#FBF6EA;border-radius:40px;box-shadow:0 12px 26px rgba(60,40,20,.14)')
    o += D(x + 50, y + h - 8, 50, 50, 'background:#FBF6EA;clip-path:polygon(0 0,100% 0,0 100%)')
    if taped:
        o += D(x - 20, y + h / 2 - 30, w + 40, 60, 'background:rgba(214,190,140,.92);transform:rotate(-8deg);box-shadow:0 4px 8px rgba(60,40,20,.12)')
        o += D(x - 20, y + h / 2 - 30, w + 40, 60, 'background:rgba(214,190,140,.85);transform:rotate(9deg)')
    elif word:
        o += D(x, y, w, h, "display:flex;align-items:center;justify-content:center;font-family:Fraunces,serif;font-style:italic;font-weight:600;font-size:58px;color:#3F6259", word)
    else:
        for k in range(3):
            o += D(x + w / 2 - 60 + k * 44, y + h / 2 - 10, 20, 20, 'border-radius:50%;background:#C9BFAE')
    return o
def set1():
    W = 6480
    b = []
    b.append(bubble(300, 1520, 460, 200, True))
    b.append(bubble(1080 + 200, 1480, 380, 170, True))
    b.append(bubble(1080 + 560, 1620, 300, 150, True))
    b.append(bubble(2160 + 280, 1500, 460, 200, True))
    b.append(bubble(3240 + 280, 1500, 460, 200, False))
    b.append(bubble(4320 + 260, 1500, 500, 210, False, 'ankth'))
    b.append(slide(0, 'lt', 'Rregull i pashkruar', '„Mos e zër në gojë, <em>se e&nbsp;thërret!“</em>', hint=H))
    b.append(slide(1, 'lt', 'E dëgjuam', 'Për sëmundjet, për hallet, për frikën. <em>Më mirë mos i&nbsp;përmend.</em>'))
    b.append(slide(2, 'lt', 'Kështu', 'Mësuam t’i mbajmë pa emër. <em>Dhe pa emër, s’ikën&nbsp;askund.</em>'))
    b.append(slide(3, 'lt', 'E vërteta', 'Një hall me emër mund të ndahet. <em>Një hall pa emër mbetet vetëm&nbsp;yti.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'Zëre në gojë. <em>Me dikë që s’të&nbsp;gjykon.</em>', 'S’e gjen fjalën? Fjalori i ndjenjave te shprehu.cc të&nbsp;ndihmon.'))
    b.append(end(5, 'Thuaje me emrin e vet. <em>Dikush të dëgjon, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#F1EADF 0%,#EFE6D6 70%,#E4D6BE 100%)', ''.join(b))

# 02: ora 23:30, video pastrimi (sjellje e fshehur me orë), telefoni në dorë dhe rafti në ekran që rregullohet nga slide-i në slide
def phone(x, y, step, t):
    o = D(x, y, 340, 560, 'background:#14191B;border-radius:46px;box-shadow:0 20px 50px rgba(0,0,0,.45)')
    o += D(x + 16, y + 16, 308, 528, 'background:#EDE7DA;border-radius:34px;overflow:hidden')
    cols = ['#B04A2C', '#3F6259', '#E8B96C', '#8FB8A8', '#C9663F', '#5B6E8C']
    for row in range(3):
        o += D(x + 36, y + 160 + row * 120, 268, 10, 'background:#B99F7E;border-radius:4px')
        for k in range(5):
            tidy = step > row
            h = 70 if tidy else 40 + ((k * 23 + row * 11) % 45)
            rot = 0 if tidy else ((k * 37 + row * 19) % 30) - 15
            o += D(x + 46 + k * 50, y + 160 + row * 120 - h, 38, h, f'background:{cols[(k + row) % 6]};border-radius:6px;transform:rotate({rot}deg);transform-origin:50% 100%')
    o += D(x + 16, y + 470, 308, 8, 'background:rgba(0,0,0,.08)')
    o += D(x + 16, y + 470, 77 * (step + 1), 8, 'background:#E8B96C')
    o += D(x + 40, y + 34, 200, 40, 'font-size:26px;font-weight:700;color:#2E2A26', t)
    return o
def set2():
    W = 6480
    b = []
    for i, (st, t) in enumerate([(0, '23:30'), (1, '23:52'), (2, '00:40'), (3, '00:41'), (3, '00:41')]):
        b.append(phone(i * 1080 + 620, 1260, st, t))
    b.append(slide(0, 'dk', 'Ora 23:30', 'Shikon video me njerëz që pastrojnë. <em>Dhe të&nbsp;qetëson.</em>', hint=H))
    b.append(slide(1, 'dk', 'Ora 23:52', 'Një raft i rregulluar. Një dollap i palosur. <em>Edhe një, edhe&nbsp;një.</em>'))
    b.append(slide(2, 'dk', 'Ora 00:40', 'Gjithçka në ekran po bëhet në rregull. <em>Brenda teje, jo&nbsp;ende.</em>'))
    b.append(slide(3, 'dk', 'Pse?', 'Kur brenda ka rrëmujë, <em>mendja kërkon pak rregull&nbsp;diku.</em>'))
    b.append(slide(4, 'dk', 'Sot', 'Fillo nga një raft i vogël brenda vetes. <em>Thuaje një gjë që të&nbsp;rëndon.</em>'))
    b.append(end(5, 'Rrëmuja brenda s’pastrohet duke parë. <em>Fol me dikë që të dëgjon, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#1B2326 0%,#202C30 70%,#182024 100%)', ''.join(b))

# 03: 5 shenja që je mërzitur edhe kur thua „jam mirë“ (listë me boshllëk), kartat me pineska në tabelë tapë
def card(x, y, n, rot, col):
    return (D(x, y, 300, 220, f'background:{col};border-radius:6px;transform:rotate({rot}deg);box-shadow:0 12px 22px rgba(60,40,20,.22)',
              D(30, 40, 240, 150, "font-family:Fraunces,serif;font-weight:600;font-size:150px;line-height:1;color:rgba(46,42,38,.82)", str(n)))
            + D(x + 135, y - 10, 30, 30, 'border-radius:50%;background:radial-gradient(circle at 35% 30%,#E8574A,#9E2F2A 70%);box-shadow:0 4px 6px rgba(0,0,0,.25)'))
def set3():
    W = 7560
    b = [D(0, 1510, W - 1080, 410, 'background:#C49A6C;background-image:radial-gradient(rgba(90,60,30,.25) 2px,transparent 2.5px);background-size:22px 22px;box-shadow:inset 0 12px 0 #8C6A4A')]
    cols = ['#FBF6EA', '#F2E3C6', '#E3EDE7', '#F6DCD2', '#E6E3F0']
    for i in range(1, 6):
        b.append(card(i * 1080 + 600, 1620, i, [-5, 4, -3, 6, -4][i - 1], cols[i - 1]))
    b.append(D(300, 1620, 300, 220, 'background:#FBF6EA;border-radius:6px;transform:rotate(-4deg);box-shadow:0 12px 22px rgba(60,40,20,.22)',
               D(30, 70, 240, 80, "font-family:Fraunces,serif;font-style:italic;font-size:44px;color:#3F6259;white-space:nowrap", '„jam mirë“')))
    b.append(D(435, 1610, 30, 30, 'border-radius:50%;background:radial-gradient(circle at 35% 30%,#E8574A,#9E2F2A 70%)'))
    b.append(slide(0, 'lt', 'Listë', '5 shenja që je mërzitur, <em>edhe kur thua „jam&nbsp;mirë“.</em>', 'E katërta s’e vë re&nbsp;askush.', hint=H))
    b.append(slide(1, 'lt', 'E para', 'Dëgjon të njëjtën këngë <em>tridhjetë&nbsp;herë.</em>'))
    b.append(slide(2, 'lt', 'E dyta', 'I lë mesazhet pa hapur, <em>edhe ato të&nbsp;mirat.</em>'))
    b.append(slide(3, 'lt', 'E treta', 'Fle shumë, <em>ose s’fle&nbsp;fare.</em>'))
    b.append(slide(4, 'lt', 'E katërta', 'Qesh më shumë se kurrë, <em>kur je me të&nbsp;tjerët.</em>', 'Askush s’e pyet atë që qesh më&nbsp;shumë.'))
    b.append(slide(5, 'lt', 'E pesta', 'Thua „jam mirë“ <em>para se të të&nbsp;pyesin.</em>'))
    b.append(end(6, 'Nëse e njohe veten, <em>thuaje këtu, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#F4EEE4 0%,#F1E9DB 78%,#C49A6C 79%)', ''.join(b))

SETS = [('01-zeregojes', set1), ('02-videopastrimi', set2), ('03-jammire', set3)]
if __name__ == '__main__':
    for name, fn in SETS:
        w, html = fn()
        open(os.path.join(OUT, f'set-{name}.html'), 'w', encoding='utf-8').write(html)
        print(name, w)
