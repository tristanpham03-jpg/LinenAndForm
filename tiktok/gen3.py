import math, subprocess, sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
W, H, FPS = 1080, 1920, 30
SER = '/home/claude/fonts/CormorantGaramond%5Bwght%5D.ttf'
SANS = '/home/claude/fonts/Jost%5Bwght%5D.ttf'
D = os.environ.get('TT_DIR', '/home/claude/media/v3/')
OLIVE, CREAM, CLAY, ESP, SAND = '#343F32', '#F3EDE3', '#B98466', '#2D2521', '#CDBFA8'
_fc = {}


def F(p, s, w=500):
    k = (p, s, w)
    if k not in _fc:
        f = ImageFont.truetype(p, s)
        try:
            f.set_variation_by_axes([w])
        except Exception:
            pass
        _fc[k] = f
    return _fc[k]


def ease(t):
    t = max(0, min(1, t))
    return 1 - (1 - t) ** 3


def wrap(d, t, f, mw):
    L, c = [], ''
    for x in t.split():
        y = (c + ' ' + x).strip()
        if d.textlength(y, font=f) <= mw:
            c = y
        else:
            L.append(c)
            c = x
    L.append(c)
    return L


_ic = {}


def load(name):
    if name not in _ic:
        p = D + 'hr/' + name + '.jpg'
        if not os.path.exists(p):
            p = D + 'img/' + name + '.jpg'
        _ic[name] = Image.open(p).convert('RGB')
    return _ic[name]


def cover(img, w, h, z=1.0, fx=0.5, fy=0.5):
    s = max(w / img.width, h / img.height) * z
    nw, nh = img.width * s, img.height * s
    x0 = (nw - w) * fx
    y0 = (nh - h) * fy
    box = (x0 / s, y0 / s, (x0 + w) / s, (y0 + h) / s)
    return img.resize((w, h), Image.BILINEAR, box=box)


_bg = {}


def fullbleed(name, z, fx=0.5, fy=0.5):
    """Portrait-ish images fill the screen; wider ones sit on a blurred copy of themselves."""
    img = load(name)
    if img.width / img.height <= 1.2:
        return cover(img, W, H, z, fx, fy)
    if name not in _bg:
        b = cover(img, W // 4, H // 4).filter(ImageFilter.GaussianBlur(14)).resize((W, H))
        _bg[name] = ImageEnhance.Brightness(b).enhance(0.75)
    im = _bg[name].copy()
    fw = W
    fh = int(img.height * fw / img.width)
    fh = min(fh, 1300)
    im.paste(cover(img, fw, fh, z, fx, fy), (0, (H - fh) // 2 - 40))
    return im


def shadow_text(lines, font, fill='white', spacing=1.15, align='left', maxw=W):
    """Pre-render a block of text with a soft shadow, returns RGBA."""
    tmp = ImageDraw.Draw(Image.new('L', (1, 1)))
    lh = int(font.size * spacing)
    w = int(max(tmp.textlength(l, font=font) for l in lines)) + 60
    h = lh * len(lines) + 60
    sh = Image.new('L', (w, h), 0)
    ds = ImageDraw.Draw(sh)
    txt = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    dt = ImageDraw.Draw(txt)
    for i, l in enumerate(lines):
        x = 30 if align == 'left' else (w - tmp.textlength(l, font=font)) / 2
        ds.text((x, 30 + i * lh), l, font=font, fill=200)
        dt.text((x, 30 + i * lh), l, font=font, fill=fill)
    sh = sh.filter(ImageFilter.GaussianBlur(12))
    out = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    out.putalpha(sh)
    out = Image.alpha_composite(Image.new('RGBA', (w, h), (20, 15, 12, 0)), out)
    return Image.alpha_composite(out, txt)


def pill(text, font, bg=CREAM, fg=ESP, pad=(34, 18)):
    tmp = ImageDraw.Draw(Image.new('L', (1, 1)))
    tw = int(tmp.textlength(text, font=font))
    w, h = tw + pad[0] * 2, font.size + pad[1] * 2 + 8
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, w - 1, h - 1), radius=h // 2, fill=bg)
    d.text((pad[0], pad[1]), text, font=font, fill=fg)
    return im


def paste_a(im, layer, xy, alpha=1.0):
    if alpha <= 0:
        return
    if alpha < 1:
        layer = layer.copy()
        a = layer.split()[3].point(lambda v: int(v * alpha))
        layer.putalpha(a)
    im.paste(layer, (int(xy[0]), int(xy[1])), layer)


def rounded(img, r):
    m = Image.new('L', img.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, img.width - 1, img.height - 1), radius=r, fill=255)
    return m


class Writer:
    def __init__(self, out):
        self.tmp = out[:-4] + '.part.mp4'
        self.out = out
        self.p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24',
                                   '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-f', 'lavfi', '-i',
                                   'anullsrc=r=44100:cl=stereo', '-shortest', '-c:v', 'libx264', '-preset', 'medium',
                                   '-crf', '20', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-movflags', '+faststart',
                                   self.tmp], stdin=subprocess.PIPE)

    def add(self, im):
        self.p.stdin.write(im.convert('RGB').tobytes())

    def close(self):
        self.p.stdin.close()
        if self.p.wait() == 0:
            os.replace(self.tmp, self.out)
        else:
            raise SystemExit('ffmpeg failed ' + self.out)


def timeline(scenes):
    starts, t = [], 0
    for s in scenes:
        starts.append(t)
        t += s['dur']
    return starts, t


# ---------------- SPOTLIGHT: one product, full-bleed photos, hook + feature pills ----------------
def spotlight(v, out, only=None):
    scenes = v['scenes']
    starts, total = timeline(scenes)
    hook_f = F(SANS, 86, 650)
    pill_f = F(SANS, 50, 500)
    d0 = ImageDraw.Draw(Image.new('L', (1, 1)))
    hook_lines = wrap(d0, v['hook'], hook_f, 960)
    hook_words = []  # per-word layers for pop-in
    y = 0
    for L in hook_lines:
        x = 0
        for wd in L.split():
            hook_words.append((shadow_text([wd], hook_f), x, y))
            x += d0.textlength(wd + ' ', font=hook_f)
        y += int(hook_f.size * 1.12)
    pills = [pill(s.get('cap', ''), pill_f) if s.get('cap') else None for s in scenes]
    end_name = shadow_text(wrap(d0, v['name'], F(SER, 96, 600), 900), F(SER, 96, 600), align='center')
    end_sub = pill(v['end'], F(SANS, 46, 500), bg=CLAY, fg='white')
    tag = shadow_text(['#ad'], F(SANS, 34, 400))
    XF = 0.35

    def scene_img(k, lt):
        s = scenes[k]
        z0 = s.get('z', 1.0)
        z = z0 * ((1.0 + 0.07 * (lt / s['dur'])) if s.get('zoom', 'in') == 'in' else (1.07 - 0.07 * (lt / s['dur'])))
        return fullbleed(s['img'], z, s.get('fx', 0.5), s.get('fy', 0.5))

    frames = range(int(total * FPS)) if only is None else only
    w = None if only is not None else Writer(out)
    shots = []
    for i in frames:
        t = i / FPS
        k = max(j for j in range(len(scenes)) if starts[j] <= t)
        lt = t - starts[k]
        im = scene_img(k, lt)
        if k + 1 < len(scenes) and lt > scenes[k]['dur'] - XF:
            a = (lt - (scenes[k]['dur'] - XF)) / XF
            im = Image.blend(im, scene_img(k + 1, 0), a)
        if k == 0:  # hook words pop
            ga = 1 - ease((lt - (scenes[0]['dur'] - 0.4)) / 0.3)
            im = Image.composite(Image.new('RGB', (W, H), (22, 17, 14)), im, GRAD.point(lambda v: int(v * ga)))
            for n, (lay, x, y) in enumerate(hook_words):
                p = ease((lt - 0.12 * n) / 0.22)
                fade = 1 - ease((lt - (scenes[0]['dur'] - 0.4)) / 0.3)
                paste_a(im, lay, (60 + x - 30, 210 + y - 30 + 30 * (1 - p)), p * fade)
        elif scenes[k].get('end'):
            p = ease(lt / 0.5)
            dim = Image.new('RGB', (W, H), (25, 20, 16))
            im = Image.blend(im, dim, 0.45 * p)
            paste_a(im, end_name, ((W - end_name.width) / 2, 700 + 40 * (1 - p)), p)
            q = ease((lt - 0.4) / 0.4)
            paste_a(im, end_sub, ((W - end_sub.width) / 2, 720 + end_name.height + 20), q)
        if pills[k] is not None:
            p = ease((lt - 0.15) / 0.35)
            fade = 1 - ease((lt - (scenes[k]['dur'] - 0.35)) / 0.25) if k + 1 < len(scenes) else 1
            paste_a(im, pills[k], ((W - pills[k].width) / 2, 1480 + 50 * (1 - p)), p * fade)
        paste_a(im, tag, (40, 1780))
        if w:
            w.add(im)
        else:
            shots.append(im)
    if w:
        w.close()
    return shots


# ---------------- LIST: numbered roundup on cream, product photo cards ----------------
def roundup(v, out, only=None):
    items = v['items']
    HOOK, ITEM, END = v.get('hook_dur', 2.4), v.get('item_dur', 2.6), 2.4
    total = HOOK + ITEM * len(items) + END
    bg, fg, acc = v.get('pal', (CREAM, ESP, CLAY))
    d0 = ImageDraw.Draw(Image.new('L', (1, 1)))
    hf = F(SER, 124, 600)
    hook_lines = wrap(d0, v['hook'], hf, 920)
    nf, tf, sf, cf = F(SANS, 64, 600), F(SER, 84, 600), F(SANS, 44, 400), F(SANS, 40, 600)
    CW, CH, CY = 960, 1160, 270
    cards = []
    for it in items:
        cards.append(load(it['img']))
    masks = rounded(Image.new('L', (CW, CH)), 36)
    thumbs = [cover(load(it['img']), 300, 380, it.get('z', 1.0), it.get('fx', .5), it.get('fy', .5)) for it in items]

    def base():
        im = Image.new('RGB', (W, H), bg)
        return im, ImageDraw.Draw(im)

    frames = range(int(total * FPS)) if only is None else only
    w = None if only is not None else Writer(out)
    shots = []
    for i in frames:
        t = i / FPS
        im, d = base()
        if t < HOOK:
            lt = t
            y = 420
            for n, L in enumerate(hook_lines):
                p = ease((lt - 0.12 * n) / 0.4)
                fill = fg
                d.text((80 + 60 * (1 - p), y), L, font=hf, fill=fill if p > 0.02 else bg)
                y += 132
            # thumbnail strip teaser
            for n, th in enumerate(thumbs[:3]):
                p = ease((lt - 0.5 - 0.15 * n) / 0.4)
                if p > 0:
                    x = 80 + n * 320
                    im.paste(th, (x, int(y + 140 + 80 * (1 - p))), rounded(th, 24))
            d.rectangle((80, y + 40, 80 + int(300 * ease(lt / 0.8)), y + 48), fill=acc)
        elif t < HOOK + ITEM * len(items):
            k = int((t - HOOK) // ITEM)
            lt = t - HOOK - k * ITEM
            it = items[k]
            p = ease(lt / 0.4)
            z = 1.0 + 0.05 * lt / ITEM
            card = cover(cards[k], CW, CH, z * it.get('z', 1.0), it.get('fx', .5), it.get('fy', .5))
            x = (W - CW) / 2 + 300 * (1 - p)
            im.paste(card, (int(x), CY), masks)
            # number badge
            d.ellipse((x + 30, CY + 30, x + 150, CY + 150), fill=acc)
            num = str(k + 1)
            d.text((x + 90 - d.textlength(num, font=nf) / 2, CY + 45), num, font=nf, fill='white')
            y = CY + CH + 50
            q = ease((lt - 0.15) / 0.35)
            for L in wrap(d, it['name'], tf, 920):
                d.text((70 + 40 * (1 - q), y), L, font=tf, fill=fg if q > 0.02 else bg)
                y += 92
            q2 = ease((lt - 0.35) / 0.35)
            if q2 > 0:
                for L in wrap(d, it['why'], sf, 920):
                    d.text((72, y + 10), L, font=sf, fill=fg)
                    y += 56
                if it.get('price'):
                    ch = pill(it['price'], cf, bg=acc, fg='white', pad=(26, 12))
                    paste_a(im, ch, (72, y + 34), q2)
            # progress dots
            for n in range(len(items)):
                cx = W / 2 + (n - (len(items) - 1) / 2) * 34
                d.ellipse((cx - 7, 220, cx + 7, 234), fill=acc if n <= k else SAND)
        else:
            lt = t - HOOK - ITEM * len(items)
            p = ease(lt / 0.5)
            y = 560
            for L in wrap(d, v['end_title'], F(SER, 110, 600), 920):
                d.text(((W - d.textlength(L, font=F(SER, 110, 600))) / 2, y + 40 * (1 - p)), L,
                       font=F(SER, 110, 600), fill=fg if p > 0.02 else bg)
                y += 120
            ch = pill(v['end'], F(SANS, 46, 500), bg=acc, fg='white')
            paste_a(im, ch, ((W - ch.width) / 2, y + 60), ease((lt - 0.3) / 0.4))
            for n, th in enumerate(thumbs[:3]):
                im.paste(th, (int(80 + n * 320), int(y + 220)), rounded(th, 24))
        d.text((44, 1830), '#ad', font=F(SANS, 34, 400), fill=fg)
        if w:
            w.add(im)
        else:
            shots.append(im)
    if w:
        w.close()
    return shots


# ---------------- CHECKLIST: notes-app list that ticks off, photo for each item ----------------
def checklist(v, out, only=None):
    items = v['items']
    HOOK, ITEM, END = 1.0, 2.4, 2.0
    total = HOOK + ITEM * len(items) + END
    tf, itf, smf = F(SANS, 70, 650), F(SANS, 48, 500), F(SANS, 36, 400)
    PW, PH, PY = 980, 1000, 790
    frames = range(int(total * FPS)) if only is None else only
    w = None if only is not None else Writer(out)
    shots = []
    pm = rounded(Image.new('L', (PW, PH)), 30)
    for i in frames:
        t = i / FPS
        im = Image.new('RGB', (W, H), '#FBFAF7')
        d = ImageDraw.Draw(im)
        d.text((50, 70), '‹ Notes', font=F(SANS, 40, 500), fill='#C8962E')
        y = 170
        tl = wrap(d, v['title'], tf, 960)
        for L in tl:
            d.text((50, y), L, font=tf, fill='#1E1E1E')
            y += 84
        y += 20
        k_now = int((t - HOOK) // ITEM) if t >= HOOK else -1
        k_now = min(k_now, len(items) - 1)
        for n, it in enumerate(items):
            st = HOOK + n * ITEM
            if t < st:
                break
            lt = t - st
            p = ease(lt / 0.3)
            d.ellipse((50, y + 6, 96, y + 52), outline='#C8962E', width=4)
            if lt > 0.9 or t >= HOOK + ITEM * len(items):
                d.ellipse((50, y + 6, 96, y + 52), fill='#C8962E')
                d.line((61, y + 30, 70, y + 40), fill='white', width=5)
                d.line((70, y + 40, 86, y + 18), fill='white', width=5)
            d.text((120 + 30 * (1 - p), y), it['line'], font=itf, fill='#1E1E1E')
            y += 74
        # photo area
        if HOOK <= t < HOOK + ITEM * len(items):
            k = k_now
            lt = t - HOOK - k * ITEM
            it = items[k]
            p = ease(lt / 0.35)
            ph = cover(load(it['img']), PW, PH, it.get('z', 1.0) * (1.0 + 0.05 * lt / ITEM), it.get('fx', .5), it.get('fy', .5))
            yy = max(y + 40, PY)
            hh = min(PH, H - yy - 120)
            ph = ph.crop((0, (PH - hh) // 2, PW, (PH - hh) // 2 + hh))
            m = rounded(ph, 30)
            im.paste(ph, (50, int(yy + 60 * (1 - p))), m)
            if it.get('note'):
                c = pill(it['note'], smf, bg='white', fg='#1E1E1E', pad=(24, 12))
                paste_a(im, c, (80, int(yy + hh - c.height - 30)), ease((lt - 0.3) / 0.3))
        elif t >= HOOK + ITEM * len(items):
            lt = t - HOOK - ITEM * len(items)
            c = pill(v['end'], F(SANS, 48, 500), bg='#C8962E', fg='white')
            paste_a(im, c, ((W - c.width) / 2, y + 80 + 30 * (1 - ease(lt / .4))), ease(lt / .4))
            n = min(len(items), 4)
            tw = (W - 100 - 20 * (n - 1)) // n
            for j, it in enumerate(items[:n]):
                th = cover(load(it['img']), tw, int(tw * 1.3), it.get('z', 1.0), it.get('fx', .5), it.get('fy', .5))
                q = ease((lt - 0.2 - 0.1 * j) / 0.4)
                if q > 0:
                    im.paste(th, (50 + j * (tw + 20), int(y + 240 + 60 * (1 - q))), rounded(th, 24))
        d.text((50, 1840), '#ad', font=F(SANS, 34, 400), fill='#777')
        if w:
            w.add(im)
        else:
            shots.append(im)
    if w:
        w.close()
    return shots


GRAD = Image.linear_gradient('L').rotate(180).resize((W, H)).point(lambda v: max(0, int((v - 110) * 1.6)))
STYLES = {'spot': spotlight, 'list': roundup, 'check': checklist}
