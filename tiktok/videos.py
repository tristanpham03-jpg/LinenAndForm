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
V['11-blackout-curtains'] = dict(style='spot', name='Linen blend blackout curtains', end='Under $30 · on Pinterest: Linen & Form', hook='Blackout curtains that look like linen', scenes=[
    dict(img='JOYDECO_0', dur=2.8),
    dict(img='JOYDECO_2', dur=2.2, cap='Linen and polyester blend', z=1.8, fy=1.0),
    dict(img='JOYDECO_1', dur=2.2, cap='Blocks 100% of sunlight', z=1.6, fx=0.75, fy=0.45),
    dict(img='JOYDECO_0', dur=2.2, cap='Thermal insulated', z=1.5, fx=0.5, fy=0.3),
    dict(img='JOYDECO_0', dur=2.2, cap='Machine wash cold', z=1.4, fx=0.0, fy=0.5),
    dict(img='JOYDECO_0', dur=2.6, end=True, zoom='out'),
])
V['12-fall-evening'] = dict(style='list', pal=(SAND, ESP, OLIVE), hook='4 things for a slow fall night in', end_title='The whole evening, linked', end='Shop them on Pinterest: Linen & Form', items=[
    dict(img='MOFFE_0', name='A warm wood table lamp', why='Dimmable, with a built-in timer', price='Under $80'),
    dict(img='THROW_4', z=1.6, fx=0.6, fy=1.0, name='A wool blend throw', why='50 x 60, soft plush knit', price='Under $40'),
    dict(img='WAFFLE_0', name='A lighter cotton throw', why='Waffle weave for the reading chair', price='Under $25'),
    dict(img='JARLAMP_1', name='A textured jar lamp', why='Stone-look ceramic, 23 inches tall', price='Under $90'),
])
V['13-guest-room'] = dict(style='check', title='Guest room checklist before the holidays', end='Shop the list on Pinterest: Linen & Form', items=[
    dict(img='DUVET_2', line='Washed cotton duvet cover', note='Soft, lived-in look'),
    dict(img='LAMPS2_0', line='A lamp on each side of the bed', note='Ceramic, set of two'),
    dict(img='WAFFLE_4', z=1.4, fx=0.0, fy=1.0, line='A throw at the foot of the bed', note='Cotton waffle weave'),
    dict(img='YAKAMOK_0', line='Blackout curtains', note='So guests can sleep in'),
    dict(img='RUG_0', line='A washable rug by the door', note='Non-slip backing'),
])
V['14-sofa-throw'] = dict(style='spot', name='Wool blend throw blanket', end='Under $40 · on Pinterest: Linen & Form', hook='One throw and the whole sofa looks styled', scenes=[
    dict(img='THROW_4', dur=2.6, z=1.5, fx=0.7, fy=1.0),
    dict(img='THROW_5', dur=2.2, cap='Made with 10% real wool', z=1.6, fx=0.0, fy=1.0),
    dict(img='THROW_3', dur=2.2, cap='Plush, velvety texture', z=1.5, fx=0.2, fy=1.0),
    dict(img='THROW_0', dur=2.2, cap='50 x 60 inches'),
    dict(img='THROW_4', dur=2.6, end=True, zoom='out', z=1.5, fx=0.7, fy=1.0),
])
V['15-hosting'] = dict(style='list', pal=(OLIVE, CREAM, '#C9A46A'), hook='Hosting this year? 5 finds under $100', end_title='Ready for guests, linked', end='Shop them on Pinterest: Linen & Form', items=[
    dict(img='BOARD_5', name='Acacia serving board', why='17 x 13, for cutting or a cheese spread', price='Under $30'),
    dict(img='TRAY_4', fx=0.3, name='Travertine tray', why='Stone look for the coffee table', price='Under $50'),
    dict(img='RUG810_0', name='Vintage-look area rug', why='Washable, in room sizes', price='Under $100'),
    dict(img='MOFFE_1', z=1.35, fy=1.0, name='Sculptural wood lamp', why='Dimmable, with a built-in timer', price='Under $80'),
    dict(img='THROW_3', z=1.7, fx=0.3, fy=1.0, name='Wool blend throw', why='For guests on the sofa', price='Under $40'),
])
V['16-evening-lighting'] = dict(style='check', title='Your lighting checklist for darker nights', end='Shop the list on Pinterest: Linen & Form', items=[
    dict(img='MOFFE_0', line='A warm lamp at eye level', note='Dimmable solid wood base'),
    dict(img='SCONCE_1', z=1.8, fy=0.0, line='Wall sconces by the bed', note='Plug-in, no wiring'),
    dict(img='FLOOR_4', line='A floor lamp in the corner', note='Arched, linen-look shade'),
    dict(img='RIBLAMP_3', line='A small lamp on the dresser', note='Ribbed ceramic'),
    dict(img='JARLAMP_3', line='One statement table lamp', note='Textured ceramic, 23 inches'),
])
V['17-entry-rug'] = dict(style='spot', name='Washable entry rug', end='2x3 under $10 · on Pinterest: Linen & Form', hook='Muddy boot season? Get a rug you can wash', scenes=[
    dict(img='RUG_0', dur=2.6),
    dict(img='RUG_0', dur=2.2, cap='Goes in the washing machine', z=1.7, fy=0.75),
    dict(img='RUG_2', dur=2.2, cap='Spill and stain resistant', z=1.5, fx=0.6, fy=0.75),
    dict(img='RUG_2', dur=2.2, cap='Non-slip rubber backing'),
    dict(img='RUG_0', dur=2.6, end=True, zoom='out'),
])

V['18-gift-guide'] = dict(style='list', pal=(ESP, CREAM, '#C9A46A'), hook='Gifts for friends with great taste', end_title='Every gift, linked', end='Shop them on Pinterest: Linen & Form', items=[
    dict(img='MOFFE_0', name='Solid wood table lamp', why='Dimmable, with a built-in timer', price='Under $80'),
    dict(img='THROW_3', z=1.7, fx=0.3, fy=1.0, name='Wool blend throw', why='Soft knit, 50 x 60 inches', price='Under $40'),
    dict(img='TRAY_1', name='Travertine tray', why='For the vanity or the coffee table', price='Under $50'),
    dict(img='BOARD_4', name='Acacia serving board', why='17 x 13, for cutting and serving', price='Under $30'),
    dict(img='WAFFLE_5', name='Cotton waffle throw', why='100% cotton, lightweight', price='Under $30'),
])
V['19-winter-bedroom'] = dict(style='check', title='Winter bedroom checklist', end='Shop the list on Pinterest: Linen & Form', items=[
    dict(img='JOYDECO_1', line='Thermal blackout curtains', note='Linen blend, floor length'),
    dict(img='DUVET_1', line='A washed cotton duvet cover', note='Hidden zipper, corner ties'),
    dict(img='THROW_4', z=1.6, fx=0.6, fy=1.0, line='A wool blend throw', note='Soft knit, 50 x 60'),
    dict(img='MOFFE_1', z=1.35, fy=1.0, line='A bedside lamp with a timer', note='Dims down for reading'),
    dict(img='RUG_0', line='A soft rug where your feet land', note='Washable, non-slip backing'),
])
V['20-wood-lamp'] = dict(style='spot', name='Solid wood table lamp', end='Under $80 · on Pinterest: Linen & Form', hook='Turn off the overhead light. Use this.', scenes=[
    dict(img='MOFFE_0', dur=2.6),
    dict(img='MOFFE_0', dur=2.2, cap='Real solid wood base', z=1.7, fy=1.0),
    dict(img='MOFFE_0', dur=2.2, cap='Lacing you can re-lace', z=1.6, fy=0.25),
    dict(img='MOFFE_4', dur=2.2, cap='Dimmable, with a timer', z=1.5, fy=1.0),
    dict(img='MOFFE_1', dur=2.2, cap='Warm 2700K bulb included', z=1.35, fy=1.0),
    dict(img='MOFFE_0', dur=2.6, end=True, zoom='out'),
])
V['21-under-40'] = dict(style='list', pal=(CLAY, CREAM, ESP), hook='Cozy upgrades, all under $40', end_title='All five, linked', end='Shop them on Pinterest: Linen & Form', items=[
    dict(img='THROW_4', z=1.6, fx=0.6, fy=1.0, name='Wool blend throw', why='Brown and cream knit', price='Under $40'),
    dict(img='JOYDECO_0', name='Linen blend blackout curtains', why='Thermal insulated', price='Under $35'),
    dict(img='SCONCE_1', z=1.8, fy=0.0, name='Plug-in wall sconces', why='Set of two, no wiring', price='Under $35'),
    dict(img='FLOOR_3', name='Arched floor lamp', why='Linen-look shade', price='Under $30'),
    dict(img='RUG_0', name='Washable entry rug', why='2x3, non-slip backing', price='Under $10'),
])
V['22-calm-living-room'] = dict(style='check', title='Small swaps for a calmer living room', end='Shop the list on Pinterest: Linen & Form', items=[
    dict(img='TRAY_4', fx=0.3, line='A stone tray for the clutter', note='Travertine, 15 x 10'),
    dict(img='JARLAMP_1', line='Lamps instead of the ceiling light', note='Ceramic, 3-way switch'),
    dict(img='WAFFLE_4', z=1.4, fx=0.0, fy=1.0, line='A light cotton throw', note='100% cotton waffle'),
    dict(img='JOYDECO_1', line='Curtains that soften the window', note='Linen blend, floor length'),
    dict(img='RUG_0', line='A rug you can actually wash', note='Non-slip backing'),
])
V['23-jar-lamp'] = dict(style='spot', name='Ceramic jar table lamp', end='Under $90 · on Pinterest: Linen & Form', hook='One big lamp beats three small ones', scenes=[
    dict(img='JARLAMP_3', dur=2.6),
    dict(img='JARLAMP_0', dur=2.2, cap='23 inches tall'),
    dict(img='JARLAMP_4', dur=2.2, cap='Distressed cream ceramic'),
    dict(img='JARLAMP_1', dur=2.2, cap='3-way switch, ivory shade'),
    dict(img='JARLAMP_3', dur=2.6, end=True, zoom='out'),
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
