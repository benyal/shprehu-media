import os
BASE = '/home/user/Shprehu-3.5/Claude outputs/reklama/2026-11-12-tiktok-ftohti/burimi/gen.py'
OUT = os.path.dirname(os.path.abspath(__file__))
ns = {'__file__': BASE}
exec(open(BASE, encoding='utf-8').read().split('# 01:')[0], ns)
page, slide, end, D, H = ns['page'], ns['slide'], ns['end'], ns['D'], ns['H']

# 01: „Pema me shumë fryte e ul degën“ (urtësi e gjyshit), dega përkulet, pastaj mbështetet
def tree(x, k):
    o = D(x, 1780, 1080, 140, 'background:#8FA77E')
    o += D(x + 760, 1180, 60, 600, 'background:#6E4A2F;border-radius:20px')
    ang = [-4, 4, 10, 16, 8][k]
    o += f'<div style="position:absolute;left:{x+300}px;top:1250px;width:480px;height:22px;background:#6E4A2F;border-radius:11px;transform-origin:right center;transform:rotate({ang}deg)">'
    for j in range(min(k + 1, 4) * 2):
        o += f'<div style="position:absolute;left:{20+j*55}px;top:20px;width:44px;height:44px;border-radius:50%;background:#D9A441"></div>'
    o += '</div>'
    if k == 4:
        o += D(x + 330, 1290, 18, 490, 'background:#8C6A4A;border-radius:6px')
    return o
def set1():
    W = 6480
    b = [tree(i * 1080, i) for i in range(5)]
    b.append(slide(0, 'lt', 'Gjyshi', '„Pema me shumë fryte <em>e ul&nbsp;degën.“</em>', hint=H))
    b.append(slide(1, 'lt', 'Ai e thoshte për ata', 'Që japin shumë <em>dhe s’mburren&nbsp;kurrë.</em>'))
    b.append(slide(2, 'lt', 'Por', 'Dega që mban shumë <em>lodhet edhe&nbsp;ajo.</em>'))
    b.append(slide(3, 'lt', 'Ai e dinte', 'Prandaj në vjeshtë <em>i vinte një shkop&nbsp;poshtë.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'Nëse jep shumë, <em>gjej edhe ti një&nbsp;mbështetje.</em>', 'Kush është „pema me shumë fryte“ në familjen tënde? Shkruaje në&nbsp;koment.'))
    b.append(end(5, 'Edhe ti mund të mbështetesh. <em>Dikush të dëgjon, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#F3EEDF 0%,#EAE6D2 100%)', ''.join(b))

# 02: „Mos e lër gërshërën hapur, se sjell grindje!“ (rregull i pashkruar), gërshëra mbyllet
def scissors(x, k):
    o = D(x + 300, 1420, 640, 300, 'background:#E9DFCF;border-radius:16px')
    a = [28, 24, 18, 10, 2][k]
    for s, c in ((1, '#5E6B6A'), (-1, '#6F7C7B')):
        o += f'<div style="position:absolute;left:{x+500}px;top:1560px;width:340px;height:22px;background:{c};border-radius:0 11px 11px 0;transform-origin:left center;transform:rotate({s*a}deg)"></div>'
        o += f'<div style="position:absolute;left:{x+410}px;top:{1520 + (40 if s<0 else -10)}px;width:90px;height:60px;border:14px solid #B04A2C;border-radius:50%;box-sizing:border-box"></div>'
    return o
def set2():
    W = 6480
    b = [scissors(i * 1080, i) for i in range(5)]
    b.append(slide(0, 'lt', 'Rregull i pashkruar', '„Mos e lër gërshërën hapur, <em>se sjell&nbsp;grindje!“</em>', hint=H))
    b.append(slide(1, 'lt', 'E mbyllnim me nxitim', 'Sikur grindja <em>të priste te&nbsp;tavolina.</em>'))
    b.append(slide(2, 'lt', 'Por grindjet', 'Nuk vinin nga gërshëra. <em>Vinin nga fjalët e&nbsp;pathëna.</em>'))
    b.append(slide(3, 'lt', 'E vërteta', 'Gërshëra e hapur s’pret asgjë. <em>Heshtja e gjatë&nbsp;po.</em>'))
    b.append(slide(4, 'lt', 'Sot', 'Mbylle gërshërën. <em>Dhe hape&nbsp;bisedën.</em>', 'E ke dëgjuar këtë rregull? Shkruaj „po“ në&nbsp;koment.'))
    b.append(end(5, 'Fjalët e pathëna <em>mund t’i thuash këtu, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#F6F0E6 0%,#EEE5D6 100%)', ''.join(b))

# 03: 5 gjëra që bëjmë kur na pyesin „kur do martohesh?“ (listë me boshllëk), flluskat rreth tryezës
def table(x, n):
    o = D(x, 1800, 1080, 120, 'background:#B99A72')
    o += D(x + 160, 1620, 760, 34, 'background:#8C6A4A;border-radius:10px')
    o += D(x + 470, 1520, 140, 100, 'background:#3F6259;border-radius:60px 60px 10px 10px')
    o += D(x + 500, 1430, 80, 80, 'background:#E9D3BE;border-radius:50%')
    pos = [(170, 1260), (720, 1220), (200, 1380), (760, 1360), (440, 1180)]
    for k in range(n):
        px, py = pos[k]
        o += D(x + px, py, 160, 70, 'background:#FAF7F1;border-radius:24px;box-shadow:0 6px 12px rgba(0,0,0,.08);font:700 40px/70px Fraunces,serif;color:#B04A2C;text-align:center', '?')
    return o
def set3():
    W = 7560
    b = [table(i * 1080, n) for i, n in enumerate([1, 2, 3, 4, 5, 5])]
    b.append(slide(0, 'lt', 'Listë', '5 gjëra që bëjmë kur na pyesin <em>„kur do&nbsp;martohesh?“</em>', 'E katërta s’e pranon askush.', hint=H))
    b.append(slide(1, 'lt', 'E para', 'Qeshim. <em>„Hë, kur të vijë&nbsp;koha.“</em>'))
    b.append(slide(2, 'lt', 'E dyta', 'Ndërrojmë temën <em>te gatimi i&nbsp;tezes.</em>'))
    b.append(slide(3, 'lt', 'E treta', 'Gjejmë një punë urgjente <em>në&nbsp;kuzhinë.</em>'))
    b.append(slide(4, 'lt', 'E katërta', 'Pastaj, në shtëpi, <em>na rri në mendje gjithë&nbsp;natën.</em>', 'Edhe kur bëjmë sikur s’na&nbsp;intereson.'))
    b.append(slide(5, 'lt', 'E pesta', 'Mësojmë të themi: <em>„Jam mirë kështu, faleminderit.“</em>', 'Cilën e bën ti? Shkruaj numrin në&nbsp;koment.'))
    b.append(end(6, 'Ajo që të rri në mendje <em>mund ta thuash këtu, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(90deg,#F4ECE4 0%,#ECE7EE 100%)', ''.join(b))

SETS = [('01-pema', set1, 6), ('02-gershera', set2, 6), ('03-martesa', set3, 7)]
if __name__ == '__main__':
    for name, fn, c in SETS:
        w, html = fn()
        open(os.path.join(OUT, f'set-{name}.html'), 'w', encoding='utf-8').write(html)
