current_x = 300.0
x_spacing = 30.0

# scale
pillar_x_scale = 4.0
pillar_y_scale = 4.0
pillar_z_scale = 10.0

pillar_height_offset = -8.5

blocks = list()
scans = list()
camera_hints = list()
platforms = list()
liquids = list()

y = 200.0
pillars = [
    (3.3, "NSJ Single Bomb Jump (Intended)"),
    (6.5, "NSJ Double Bomb Jump (Intended)"),
    (7.8, "NSJ Double Bomb Jump"),
    (3.0, None),
    (9.8, "NSJ Laddered Double Bomb Jump"),
    (8.1, "NSJ Triple Bomb Jump"),
    (9.0, "NSJ HBJ"),
    (10.0, "NSJ UBJ"),
    (6.8, "NSJ BSJ"),
    (7.4, "NSJ 3BSJ"),
    (4.3, "NSJ Shallow Water Bomb Jump"),
    (3.5, "NSJ Deep Water Bomb Jump"),
    (6.6, "NSJ Boost IUJ"),
]

# y = 300.0
# pillars = [
#     (3.4, "NSJ Jump)"),
#     (4.7, "NSJ Slope Jump"),
#     (5.1, "NSJ Reverse Slope Jump"),
#     (7.4, "NSJ Ledge Clip Jump"),
# ]
# pillar_y_scale = 6.0

i = 0
for (pillar_height, pillar_name) in pillars:
    i += 1

    if y == 200.0 and i == 13:
        current_x += x_spacing

    if pillar_name is not None:
        blocks.append('                        {"position": [%0.1f, %0.1f, %0.1f], "scale": [%0.1f, %0.1f, %0.1f]},' % (current_x, y, pillar_height + pillar_height_offset, pillar_x_scale, pillar_y_scale, pillar_z_scale))
    else:
        blocks.append('                        {"position": [%0.1f, %0.1f, %0.1f], "scale": [%0.1f, %0.1f, %0.1f]},' % (current_x + x_spacing - 14.6, y, pillar_height + pillar_height_offset, pillar_x_scale, pillar_y_scale, pillar_z_scale))

    if pillar_name is not None:        
        if "BSJ" in pillar_name:
            blocks.append('                        {"position": [%0.1f, %0.1f, %0.1f], "scale": [%0.1f, %0.1f, %0.1f]},' % (current_x - 3.0, y + 3.5, (-1*pillar_height_offset) - 5.0, pillar_x_scale*1.3, 0.3, pillar_z_scale))
            blocks.append('                        {"position": [%0.1f, %0.1f, %0.1f], "scale": [%0.1f, %0.1f, %0.1f]},' % (current_x - 3.0, y - 3.5, (-1*pillar_height_offset) - 5.0, pillar_x_scale*1.3, 0.3, pillar_z_scale))
            camera_hints.append('                        {"triggerPos": [%0.1f, %0.1f, %0.1f], "triggerScale": [7.0, 7.0, 15.0], "cameraPos": [209.6516, -121.3058, 23.9048], "cameraRot": [-13.0, 0.0, 0.0], "behavior": 5},' % (current_x - 3.45, y, 2.0))

        pillar_text = ""
        if pillar_height is not None:
            pillar_text += "%0.1f Units: " % pillar_height
        pillar_text += pillar_name
        x = current_x - 3.45
        if y == 300.0 and i == 4:
            x -= 5.3
        scans.append( '                        {"position": [%0.2f, %0.2f, %0.2f], "combatVisible": true, "text": "%s"},' % (x, y, 2.5, pillar_text))

    if y == 300.0:
        if i == 2:
            platforms.append('                        {"position": [%0.1f, %0.1f, -0.1], "rotation": [0.0, -30.0, 0.0], "altPlatform": true},' % (current_x - 3.0, y))
        if i == 3:
            platforms.append('                        {"position": [%0.1f, %0.1f, -0.9], "rotation": [0.0, 40.0, 0.0], "altPlatform": false},' % (current_x - 9.5, y))
            blocks.append('                        {"position": [%0.1f, %0.1f, %0.1f], "scale": [%0.1f, %0.1f, %0.1f]},' % (current_x - (9.5 + 3.0), y, 9.0 + pillar_height_offset, 1.0, pillar_y_scale, pillar_z_scale))
        if i == 4:
            blocks.append('                        {"position": [%0.1f, %0.1f, %0.1f], "scale": [%0.1f, %0.1f, %0.1f]},' % (current_x - 5.0, y, 3.4 + pillar_height_offset, pillar_x_scale, pillar_y_scale - 1.0, pillar_z_scale))

    if y == 200.0:
        if i == 11:
            liquids.append(
                '                        {"type":"WATER", "position": [%0.1f, %0.1f, %0.1f], "scale": [%0.1f, %0.1f, %0.1f]},' %
                (current_x - 4.0, y, 1.4, pillar_x_scale - 2.0, pillar_y_scale, 2.5)
            )
        elif i == 12:
            liquids.append(
                '                        {"type":"WATER", "position": [%0.1f, %0.1f, %0.1f], "scale": [%0.1f, %0.1f, %0.1f]},' %
                (current_x - 4.0, y, 3.0, pillar_x_scale - 2.0, pillar_y_scale, 4.0)
            )
        elif i == 13:
            platforms.append(   '                        {"position": [%0.1f, %0.1f, -0.7], "rotation": [0.0, -28.0, 0.0], "altPlatform": false},' % (current_x - 14.0, y))
            camera_hints.append('                        {"triggerPos": [%0.1f, %0.1f, %0.1f], "triggerScale": [7.0, 7.0, 15.0], "cameraPos": [209.6516, -121.3058, 23.9048], "cameraRot": [-13.0, 0.0, 0.0], "behavior": 5},' % (current_x - 3.45, y, 2.0))

    current_x += x_spacing

for block in blocks:
    print(block)

for scan in scans:
    print(scan)

for ch in camera_hints:
    print(ch)

for p in platforms:
    print(p)

for l in liquids:
    print(l)
