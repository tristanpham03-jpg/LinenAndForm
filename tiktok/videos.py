from gen3 import *

V = {}
V['01-moffe-lamp'] = dict(style='spot', name='Sculptural wood table lamp', end='Shop it on Pinterest: Linen & Form', hook='This lamp looks good even switched off', scenes=[
    dict(img='MOFFE_0', dur=2.6),
    dict(img='MOFFE_3', dur=2.2, cap='Solid wood base', z=1.4, fy=1.0),
    dict(img='MOFFE_0', dur=2.2, cap='One-piece woven shade', z=1.6, fy=0.25),
    dict(img='MOFFE_1', dur=2.2, cap='Dimmable + built-in timer', z=1.35, fy=1.0),
    dict(img='MOFFE_5', dur=2.2, cap='Bulb included', z=1.4, fy=0.8),
    dict(img='MOFFE_0', dur=2.6, end=True, zoom='out'),
])
V['02-lamps-roundup'] = dict(style='list', hook='5 lamps that make a room look finished', end_title='Every light, linked', end='Shop them on Pinterest: Linen & Form', items=[
    dict(img='RIBLAMP_2', name='Ribbed ceramic lamp', why='Linen shade, warm glow, looks handmade', price='Under $50'),
    dict(img='MOFFE_0', name='Sculptural wood lamp', why='Solid wood base, dimmable, timer', price='Under $80'),
    dict(img='JARLAMP_1', name='Textured jar lamp', why='23 inches of quiet, stone-look ceramic', price='Under $90'),
    dict(img='SCONCE_1', z=1.8, fy=0.0, name='Plug-in wall sconces', why='No electrician. Set of two', price='Under $30'),
    dict(img='FLOOR_0', name='Linen-shade floor lamp', why='Arched reading light for any corner', price='Under $30'),
])
V['03-wool-throw'] = dict(style='spot', name='Wool blend knit throw', end='Under $40 · on Pinterest: Linen & Form', hook='The throw doing all the work on this sofa', scenes=[
    dict(img='THROW_3', dur=2.6, z=1.4, fx=0.3, fy=1.0),
    dict(img='THROW_2', dur=2.2, cap='Wool blend, soft knit', z=1.4, fx=0.2, fy=1.0),
    dict(img='THROW_4', dur=2.2, cap='Brown and cream geometric', z=1.35, fy=1.0),
    dict(img='THROW_0', dur=2.2, cap='50 x 60 inches'),
    dict(img='THROW_3', dur=2.6, end=True, zoom='out', z=1.4, fx=0.3, fy=1.0),
])
V['04-washable-rug'] = dict(style='spot', name='Washable floral rug', end='Shop it on Pinterest: Linen & Form', hook='Pet owners: this rug goes in the washer', scenes=[
    dict(img='RUG_7', dur=2.6, fy=0.6),
    dict(img='RUG_7', dur=2.2, cap='Kid and pet friendly', z=1.7, fx=0.95, fy=0.75),
    dict(img='RUG_1', dur=2.2, cap='Machine washable'),
    dict(img='RUG_0', dur=2.2, cap='Low pile, non-slip backing', z=1.5, fy=0.7),
    dict(img='RUG_7', dur=2.6, end=True, zoom='out', fy=0.6),
])
V['05-blackout-curtains'] = dict(style='spot', name='Linen-look blackout curtains', end='Shop it on Pinterest: Linen & Form', hook='Hang curtains high and wide. Trust me.', scenes=[
    dict(img='JOYDECO_0', dur=2.8),
    dict(img='JOY_5', dur=2.2, cap='Mount the rod near the ceiling'),
    dict(img='JOY_1', dur=2.2, cap='Linen-look texture', z=1.45, fx=1.0, fy=1.0),
    dict(img='JOY_6', dur=2.2, cap='100% blackout, thermal lined'),
    dict(img='JOYDECO_0', dur=2.6, end=True, zoom='out'),
])
V['06-bedroom-refresh'] = dict(style='list', pal=(OLIVE, CREAM, '#C9A46A'), hook='Bedroom refresh, nothing over $70', end_title='The whole bedroom, linked', end='Shop them on Pinterest: Linen & Form', items=[
    dict(img='DUVET_0', name='Washed cotton duvet cover', why='The lived-in, hotel-soft look', price='Under $70'),
    dict(img='LAMPS2_3', name='Ceramic bedside lamps', why='A matching pair for each side', price='Under $60 for 2'),
    dict(img='WAFFLE_0', name='Cotton waffle throw', why='Texture at the foot of the bed', price='Under $30'),
    dict(img='JOYDECO_0', name='Linen-look blackout curtains', why='Sleep in, even at noon', price='Under $30'),
    dict(img='THROW_3', z=1.7, fx=0.3, fy=1.0, name='Wool blend throw', why='For the reading chair', price='Under $40'),
])
V['07-looks-expensive'] = dict(style='list', pal=(ESP, CREAM, CLAY), hook='Looks expensive. Isn’t.', end_title='Quiet luxury, linked', end='Shop them on Pinterest: Linen & Form', items=[
    dict(img='TRAY_1', name='Travertine tray', why='Real stone look for the vanity or coffee table', price='Under $50'),
    dict(img='JARLAMP_3', name='Textured jar lamp', why='Reads like a designer piece', price='Under $90'),
    dict(img='YAKAMOK_0', name='Linen-textured curtains', why='Blackout, but they look like linen', price='Under $25'),
    dict(img='RUG810_0', name='Soft vintage-look rug', why='Washable, in room sizes', price='Under $100'),
    dict(img='LAMPS2_4', name='Ribbed ceramic lamps', why='A set of two', price='Under $60'),
])
V['08-renter-upgrades'] = dict(style='check', title='Renter-friendly upgrades, no electrician needed', end='Shop the list on Pinterest: Linen & Form', items=[
    dict(img='SCONCE_1', z=1.8, fy=0.0, line='Plug-in wall sconces', note='Plugs in, no wiring'),
    dict(img='SINK_4', line='Expandable under-sink shelf', note='Fits around the pipes'),
    dict(img='RUG_7', line='Washable rug', note='Machine washable', fy=0.6),
    dict(img='JOYDECO_0', line='Blackout curtains', note='Hang high for taller windows'),
    dict(img='FLOOR_0', line='Floor lamp for the dark corner', note='No overhead light needed'),
])
V['09-cozy-corner'] = dict(style='list', pal=(CREAM, ESP, CLAY), hook='How to build a cozy reading corner', end_title='Your corner, linked', end='Shop them on Pinterest: Linen & Form', items=[
    dict(img='FLOOR_3', name='An arched floor lamp', why='Light from above, not the ceiling', price='Under $30'),
    dict(img='THROW_3', z=1.7, fx=0.3, fy=1.0, name='A heavy knit throw', why='Wool blend, over the arm of the chair', price='Under $40'),
    dict(img='MOFFE_1', z=1.35, fy=1.0, name='A warm side lamp', why='Dimmable, with a sleep timer', price='Under $80'),
    dict(img='WAFFLE_0', name='A second, lighter throw', why='Cotton waffle for warmer nights', price='Under $30'),
])
V['10-small-space'] = dict(style='check', title='Small-space organizing that doesn’t look cheap', end='Shop the list on Pinterest: Linen & Form', items=[
    dict(img='MAKEUP_4', line='Clear stacking makeup drawers', note='Everything visible'),
    dict(img='SINK_0', line='Two-tier under-sink shelf', note='Adjustable width'),
    dict(img='TRAY_1', line='Stone tray to corral the counter', note='Travertine look'),
    dict(img='BOARD_4', line='Acacia board that stays out', note='Cutting + serving'),
])

if __name__ == '__main__':
    import sys
    name = sys.argv[1]
    v = V[name]
    os.makedirs(D + 'out', exist_ok=True)
    if len(sys.argv) > 2:  # preview frames at given seconds
        secs = [float(s) for s in sys.argv[2].split(',')]
        shots = STYLES[v['style']](v, None, only=[int(s * FPS) for s in secs])
        sheet = Image.new('RGB', (len(shots) * 360, 640))
        for n, s in enumerate(shots):
            sheet.paste(s.resize((360, 640)), (n * 360, 0))
        sheet.save(D + f'prev_{name}.jpg', quality=85)
    else:
        STYLES[v['style']](v, D + f'out/{name}.mp4')
