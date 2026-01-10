from ursina import *

splashed = False
splash_bg = Entity(
    parent=camera.ui,
    model='quad',
    scale=(2, 2),
    color=color.black,
    z=-254
)
splash_logo = Entity(
    parent=camera.ui,
    model='quad',
    texture='textures/splash',
    scale=(16 / 9, 1),
    z=-255
)

def end_splash():
    global splashed
    splash_bg.animate_color(color.clear, duration=1.5)
    splash_logo.animate_color(color.clear, duration=1)

    destroy(splash_bg, delay=1.5)
    destroy(splash_logo, delay=1)
    splashed = True