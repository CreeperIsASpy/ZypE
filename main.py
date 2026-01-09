from ursina import *
from random import randint, choice

app = Ursina(development_mode=False, icon='assets/zype.ico', borderless=False)
window.fullscreen = True

import dialog
camera.orthographic = True
camera.fov = 15

world_size = 100
global flash

background = Entity(
    model='quad',
    texture='textures/home_tile',
    scale=(world_size, world_size),
    texture_scale=(world_size, world_size),

    z=1
)

splash = True
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

def spawn_player_safely(limit):
    for i in range(100):
        rx = randint(-limit, limit)
        ry = randint(-limit, limit)

        player.position = (rx, ry)

        hit_info = player.intersects(ignore=[player,])
        if not hit_info.hit:
            return

    raise RuntimeError("Cannot Spawn Player")


def end_splash():
    global splash
    splash_bg.animate_color(color.clear, duration=1.5)
    splash_logo.animate_color(color.clear, duration=1)

    destroy(splash_bg, delay=1.5)
    destroy(splash_logo, delay=1)
    splash = False


invoke(end_splash, delay=3)

limit = int(world_size / 2)
walker_x = randint(-limit, limit)
walker_y = randint(-limit, limit)


for i in range(10):
    for _ in range(100):
        # 造墙
        wall = Entity(
            model='quad',
            texture='textures/home_brick_wall',
            scale=(1, 1),
            x=walker_x,
            y=walker_y,
            z=0,
            collider='box',
            name='wall'
        )
        wall.collider = BoxCollider(wall, center=(0,0,0), size=(1, 1, 5))


        direction = choice([(0, 1), (0, -1), (1, 0), (-1, 0)])

        walker_x += direction[0]
        walker_y += direction[1]

        walker_x = clamp(walker_x, 0, world_size - 1)
        walker_y = clamp(walker_y, 0, world_size - 1)

player = Entity(model='quad', texture='textures/me', scale=(256 / 318 * 1.19, 1 * 1.19), collider='box')
spawn_player_safely(limit)
dialog.toggle_dialog(False)


def update():
    global splash
    if not splash:
        speed = 5
        dt = time.dt

        dx = held_keys['right arrow'] - held_keys['left arrow']
        player.x += dx * dt * speed


        hit_info = player.intersects()

        if hit_info.hit:
            player.x -= dx * dt * speed

        dy = held_keys['up arrow'] - held_keys['down arrow']
        player.y += dy * dt * speed

        hit_info = player.intersects()
        if hit_info.hit:
            player.y -= dy * dt * speed

        limit_x = (world_size / 2) - (player.scale_x / 2)
        limit_y = (world_size / 2) - (player.scale_y / 2)


        player.x = clamp(player.x, -limit_x, limit_y)
        player.y = clamp(player.y, -limit_x, limit_y)

        camera.x = player.x
        camera.y = player.y
    else:
        return


def input(key):
    if key == 'h':
        dialog.toggle_dialog(text="Hello World")
    if key == 'enter':
        found_wall = False
        directions = [
            Vec3(1, 0, 0),  # 右
            Vec3(1, 1, 0),  # 右上
            Vec3(1, -1, 0), # 右下
            Vec3(-1, 0, 0),  # 左
            Vec3(-1, 1, 0),  # 左上
            Vec3(-1, -1, 0),  # 左下
            Vec3(0, 1, 0),  # 上
            Vec3(0, -1, 0)  # 下
        ]

        for d in directions:
            hit_info = raycast(
                origin=player.position,
                direction=d,
                distance=1,
                ignore=[player,],
                debug=True,
            )

            # 如果射到了东西
            if hit_info.hit:
                found_wall = True
                break

        if found_wall:
            dialog.toggle_dialog(text="This wall is really thick.")
    if key == 'escape':
        quit()

app.run()