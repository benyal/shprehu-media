import os
BASE = '/home/user/Shprehu-3.5/Claude outputs/reklama/2026-11-12-tiktok-ftohti/burimi/gen.py'
OUT = os.path.dirname(os.path.abspath(__file__))
ns = {'__file__': BASE}
exec(open(BASE, encoding='utf-8').read().split('# 01:')[0], ns)
page, slide, end, D, H = ns['page'], ns['slide'], ns['end'], ns['D'], ns['H']

# 04: urtësi e gjyshit: „Barra e ndarë s’peshon“, thesi që e mban një, pastaj dy
def sack(x, k):
    o = D(x, 1780, 1080, 140, 'background:#8C7A5C')
    two = k >= 3
    o += D(x + 340, 1500 + (0 if two else 60), 400, 220, 'background:#D9C29A;border-radius:110px 110px 40px 40px;box-shadow:inset 0 -20px 0 rgba(0,0,0,.08)')
    o += D(x + 500, 1470 + (0 if two else 60), 80, 50, 'background:#B89A6A;border-radius:12px')
    o += D(x + 240, 1560, 90, 220, 'background:#3F6259;border-radius:40px')
    if two:
        o += D(x + 750, 1560, 90, 220, 'background:#B04A2C;border-radius:40px')
    return o
def set4():
    W = 6480
    b = [sack(i * 1080, i) for i in range(5)]
    b.append(slide(0, 'dk', 'Gjyshi', '„Barra e ndarë <em>s’peshon.“</em>', hint=H))
    b.append(slide(1, 'dk', 'Kur bartnim thasët', 'Kush e ngrinte vetëm, <em>lodhej në gjysmë të&nbsp;rrugës.</em>'))
    b.append(slide(2, 'dk', 'Gjyshi s’e lejonte', '„Prit, <em>se e kapim&nbsp;bashkë.“</em>'))
    b.append(slide(3, 'dk', 'Ai e dinte', 'Thesi ishte i njëjti. <em>Por s’rëndonte më&nbsp;njësoj.</em>'))
    b.append(slide(4, 'dk', 'Sot', 'Edhe halli peshon më pak <em>kur e kap dikush nga ana&nbsp;tjetër.</em>', 'Kush ta kapte thesin nga ana tjetër? Shkruaje në&nbsp;koment.'))
    b.append(end(5, 'Ndaje pak nga barra. <em>Dikush të dëgjon, pa&nbsp;emër.</em>'))
    return W, page(W, 'linear-gradient(180deg,#22302B 0%,#2B3833 100%)', ''.join(b))

# 05: listë: 5 fjali që na mësuan të mos i themi kurrë, zarfet që hapen
def env(x, opened):
    o = D(x + 330, 1450, 420, 280, 'background:#FBF8F1;border-radius:10px;box-shadow:0 10px 30px rgba(0,0,0,.08)')
    if opened:
        o += D(x + 380, 1330, 320, 200, 'background:#FFFFFF;border-radius:6px;box-shadow:0 6px 14px rgba(0,0,0,.06)')
        o += D(x + 410, 1370, 220, 10, 'background:#3F6259;border-radius:5px') + D(x + 410, 1400, 160, 10, 'background:#3F6259;border-radius:5px')
    o += f'<svg class="abs" style="left:{x+330}px;top:1450px" width="420" height="280"><path d="M0 0 L210 {170 if not opened else 0} L420 0" stroke="#D8CCB8" stroke-width="6" fill="none"/></svg>'
    return o
def set5():
    W = 7560
    b = [D(0, 1760, W, 160, 'background:#D9C9AE')] + [env(i * 1080, i >= 5) for i in range(6)]
    b.append(slide(0, 'lt', 'Listë', '5 fjali që na mësuan <em>të mos i themi&nbsp;kurrë.</em>', 'E katërta na ka kushtuar më&nbsp;shumë.', hint=H))
    b.append(slide(1, 'lt', 'E para', '„Jam&nbsp;lodhur.“ <em>Se dukej&nbsp;dembeli.</em>'))
    b.append(slide(2, 'lt', 'E dyta', '„S’e&nbsp;di.“ <em>Se dukej&nbsp;dobësi.</em>'))
    b.append(slide(3, 'lt', 'E treta', '„Kam&nbsp;frikë.“ <em>Se „s’je më&nbsp;fëmijë“.</em>'))
    b.append(slide(4, 'lt', 'E katërta', '„Më duhet ndihmë.“ <em>Se ishte&nbsp;turp.</em>', 'Dhe i mbajtëm gjithçka&nbsp;vetë.'))
    b.append(slide(5, 'lt', 'E pesta', '„Të&nbsp;dua.“ <em>Se „dihet,&nbsp;s’ka&nbsp;nevojë“.</em>', 'Cilën s’e ke thënë kurrë? Shkruaj numrin në&nbsp;koment.'))
    b.append(end(6, 'Këtu mund t’i thuash të gjitha. <em>Pa emër, pa&nbsp;gjykim.</em>'))
    return W, page(W, 'linear-gradient(90deg,#F2E9DD 0%,#EEE6D8 100%)', ''.join(b))

SETS = [('04-barra', set4, 6), ('05-fjalite', set5, 7)]
if __name__ == '__main__':
    for name, fn, c in SETS:
        w, html = fn()
        open(os.path.join(OUT, f'set-{name}.html'), 'w', encoding='utf-8').write(html)
