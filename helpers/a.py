# up = True
# z = 1.0
# x = -251
# while x < 251:
#     y = -251
#     z = 1.0
#     while y < 251:
#         if z < 1.1:
#             up = True
#         if z > 8.9:
#             up = False
#         if up:
#             z += 2.0
#         else:
#             z -= 2.0
#         print('                        {"position":[%f, %f, %f]},' % (x, y, z))
#         y += 50.0
#     x += 50.0


current = 300.0
gap_constant = 10.0


scan_points = list()
lock_ons = list()
extras = list()

# NSJ Jumps
# y = -200.0
# gaps = [
#     (11.5, "NSJ Casual Jump. This is the biggest gap Retro expects you to cross.", False),
#     (13.0, "NSJ Casual Jump Holding L.", False),
#     (15.0, "NSJ L-Jump. Common Mistake - Releasing L too early.", False),
#     (15.5, "NSJ L-Jump Twist. Note that pressing R does nothing.", False),
#     (-4.0, None, False),
#     (18.5, "NSJ Bunny Hop. Tip - You should be sideways at the bunny hop point.", False),
#     (-6.5, None, False),
#     (22.0, "NSJ Reverse Slope Bunny Hop.", False),
# ]

# NSJ Dashes
# y = -100.0
# gaps = [
#     (32.5, "NSJ Dash. Common mistakes include holding B for too long and releasing L too early.", True),
#     (36.0, "NSJ R-Dash. Tip - Stand as far back as possible.", True),
#     (31.0, "NSJ R-Dash into Bunny Hop.", False),
#     (30.0, None, True),
# ]
# lock_ons.append('                        {"position": [%0.1f, %0.1f, 8.0]},' % (current + gap_constant/2.0 - 1.0, y))

# SJ Jumps
# y = 0.0
# gaps = [
#     (26.0, "SJ Casual Jump. This is the biggest gap Retro expects you to cross.", False),
#     (29.0, "SJ L-Jump", False),
#     (32.0, "SJ R-Jump (Easy). Most common mistake is not turning enough.", False),
#     (32.0, "SJ R-Jump around an obstacle", False),
#     (0.0, None, False),
#     (36.0, "SJ R-Jump (Hard). Most common mistake is not holding both L and R during the 2nd Jump.", False),
#     (39.5, "SJ R-Jump (Extreme). Tip - Try pressing R a few frames before the first L release. It can help prevent bleeding speed due to changing stick angles.", False),
#     (-3.0, None, False),
#     (43.0, "SJ Bunny Hop. Tip - You should be sideways at the bunny hop point.", False),
#     (45.0, "Grapple Space Jump. Use 1st jump before grappling and 2nd after grappling.", False),
# ]

# SJ Dashes
y = 100.0
gaps = [
    (61.0, "SJ Dash. Common mistakes include holding B for too long and releasing L too early.", True),
    (45.0, "SJ Dash with Momentum Cancel. Press L to prevent overshooting the target platform.", False),
    (15.0, None, True),
    (72.0, "SJ Lock-on R-Dash. Tip - Stand as far back as possible.", True),
    (72.0, "SJ L+R-Dash. Tip - Think of it like a Lock-on R-Dash where this isn't enough distance to remain locked on.", True),
    (74.0, "SJ L+R-Dash with Bending. Hold slightly up or down to accelerate more while in the air.", True),
    (70.0, "SJ Grapple Dash", True),
    (65.0, "SJ Dash around an obstacle", True),
    (33.0, "SJ Dash (Maximize Height). The most common mistake is using the 2nd jump too late.", True),
]
lock_ons.append('                        {"position": [%0.1f, %0.1f, 8.0]},' % (current + gap_constant/2.0 - 1.0, y))

print('                        {"position": [%0.1f, %0.1f, 0.0],"scale": [6.0, 50.0, 3.5]},' % (current, y))
i = 0
for (gap_length, gap_name, lock_on) in gaps:
    i += 1
    current += gap_constant + gap_length

    if gap_name is not None and gap_length > 0.01:
        scan_text = "%0.1f Units: " % gap_length
        scan_text += gap_name
        if y == -100.0 and i == 3:
            scan_string = '                        {"position": [%0.1f, %0.1f, 2.0], "isRed": false, "combatVisible": true' % (current - 3.6, y)
        elif y == 100.0 and i == 2:
            scan_string = '                        {"position": [%0.1f, %0.1f, 2.0], "isRed": false, "combatVisible": true' % (current - 2.5, y)
        else:
            scan_string = '                        {"position": [%0.1f, %0.1f, 2.0], "isRed": false, "combatVisible": true' % (current - 5.5, y)

        scan_string += ', "text": "%s"' % scan_text
        scan_string += "},"

        scan_points.append(scan_string)

    if lock_on:
        if y == 100.0 and gap_name is None:
            lock_ons.append(
                '                        {"position": [%0.1f, %0.1f, 8.0]},' % (current + gap_constant/2.0 - 1.0, y + 40.0)
            )
        elif y == 100.0 and i == 6:
            lock_ons.append(
                '                        {"position": [%0.1f, %0.1f, 12.0], "isGrapple":true},' % (current + gap_constant/2.0 - 1.0, y)
            )
        else:
            lock_ons.append(
                '                        {"position": [%0.1f, %0.1f, 8.0]},' % (current + gap_constant/2.0 - 1.0, y)
            )

    height = 0.0
    if i % 2 == 0:
        height = 0.001

    if gap_name is not None and gap_name == "SJ Dash with Momentum Cancel. Press L to prevent overshooting the target platform.":
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [1.0, 50.0, 3.5]},' % (current, y, height))
    elif gap_name is not None and gap_name == "SJ Dash (Maximize Height). The most common mistake is using the 2nd jump too late.":
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [6.0, 50.0, 12.0]},' % (current, y, height))
    elif gap_name is not None and "NSJ R-Dash into Bunny Hop." in gap_name:
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [2.0, 50.0, 3.5]},' % (current, y, height))
    elif gap_name is not None and "Grapple Space Jump" in gap_name:
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [6.0, 50.0, 12.0]},' % (current, y, height + 4.0))
        print('                        {"position": [%0.1f, %0.1f, %0.3f], "isGrapple": true},' % (current - 30.0, y, height + 20.0))
    elif y == 0.0 and i == 4:
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [6.0, 20.0, 3.5]},' % (current, y, height))

        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [1.0, 2.5, 10.0]},' % (current - 22.0, y, 5.0))
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [1.0, 2.5, 10.0]},' % (current - 22.0, y + 5, 5.0))
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [1.0, 2.5, 10.0]},' % (current - 22.0, y + 10, 5.0))
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [1.0, 2.5, 10.0]},' % (current - 22.0, y + 15, 5.0))
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [1.0, 2.5, 10.0]},' % (current - 22.0, y + 20, 5.0))
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [1.0, 2.5, 10.0]},' % (current - 22.0, y + 25, 5.0))
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [1.0, 2.5, 10.0]},' % (current - 22.0, y, 5.0))
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [1.0, 2.5, 10.0]},' % (current - 22.0, y - 5, 5.0))
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [1.0, 2.5, 10.0]},' % (current - 22.0, y - 10, 5.0))
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [1.0, 2.5, 10.0]},' % (current - 22.0, y - 15, 5.0))
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [1.0, 2.5, 10.0]},' % (current - 22.0, y - 20, 5.0))
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [1.0, 2.5, 10.0]},' % (current - 22.0, y - 25, 5.0))
    elif y == 100.0 and i == 8:
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [6.0, 25.0, 3.5]},' % (current, y, height))

        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [1.0, 2.5, 10.0]},' % (current - 40.0, y, 5.0))
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [1.0, 2.5, 10.0]},' % (current - 40.0, y + 5, 5.0))
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [1.0, 2.5, 10.0]},' % (current - 40.0, y + 10, 5.0))
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [1.0, 2.5, 10.0]},' % (current - 40.0, y + 15, 5.0))
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [1.0, 2.5, 10.0]},' % (current - 40.0, y + 20, 5.0))
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [1.0, 2.5, 10.0]},' % (current - 40.0, y + 25, 5.0))
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [1.0, 2.5, 10.0]},' % (current - 40.0, y + 30, 5.0))
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [1.0, 2.5, 10.0]},' % (current - 40.0, y, 5.0))
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [1.0, 2.5, 10.0]},' % (current - 40.0, y - 5, 5.0))
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [1.0, 2.5, 10.0]},' % (current - 40.0, y - 10, 5.0))
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [1.0, 2.5, 10.0]},' % (current - 40.0, y - 15, 5.0))
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [1.0, 2.5, 10.0]},' % (current - 40.0, y - 20, 5.0))
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [1.0, 2.5, 10.0]},' % (current - 40.0, y - 25, 5.0))
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [1.0, 2.5, 10.0]},' % (current - 40.0, y - 30, 5.0))
    else:
        print('                        {"position": [%0.1f, %0.1f, %0.3f],"scale": [6.0, 50.0, 3.5]},' % (current, y, height))

    if y == -200 and i == 7:
        extras.append('                        {"position": [%0.1f, %0.1f, 0.7], "rotation": [0.0, 23.0, 0.0], "altPlatform": true},' % (current + gap_constant - 3.0, y - 24.0))
        extras.append('                        {"position": [%0.1f, %0.1f, 0.7], "rotation": [0.0, 23.0, 0.0], "altPlatform": true},' % (current + gap_constant - 3.0, y - 16.0))
        extras.append('                        {"position": [%0.1f, %0.1f, 0.7], "rotation": [0.0, 23.0, 0.0], "altPlatform": true},' % (current + gap_constant - 3.0, y - 8.0))
        extras.append('                        {"position": [%0.1f, %0.1f, 0.7], "rotation": [0.0, 23.0, 0.0], "altPlatform": true},' % (current + gap_constant - 3.0, y))
        extras.append('                        {"position": [%0.1f, %0.1f, 0.7], "rotation": [0.0, 23.0, 0.0], "altPlatform": true},' % (current + gap_constant - 3.0, y + 8.0))
        extras.append('                        {"position": [%0.1f, %0.1f, 0.7], "rotation": [0.0, 23.0, 0.0], "altPlatform": true},' % (current + gap_constant - 3.0, y + 16.0))
        extras.append('                        {"position": [%0.1f, %0.1f, 0.7], "rotation": [0.0, 23.0, 0.0], "altPlatform": true},' % (current + gap_constant - 3.0, y + 24.0))

for scan_point in scan_points:
    print(scan_point)

for lock_on in lock_ons:
    print(lock_on)

for extra in extras:
    print(extra)
