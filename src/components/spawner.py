from ursina import *

from random import randint, choice

from src.config import Config as conf

player = None

def player_spawner(limit):
    global player
    player = Entity(model='quad', texture='textures/me', scale=(256 / 318 * 1.19, 1 * 1.19), collider='box')
    for _ in range(100):
        rx = randint(-limit, limit)
        ry = randint(-limit, limit)

        player.position = (rx, ry)

        hit_info = player.intersects(ignore=[player,])
        if not hit_info.hit:
            return

    raise RuntimeError("Cannot Spawn Player")

def random_entities_spawner(limit, times=10, steps=100,  *args, **kwargs):
    visited_positions = set()
    cubes = []
    for i in range(times):
        walker_x = randint(-limit, limit)
        walker_y = randint(-limit, limit)
        for _ in range(steps):
            current_pos = (int(walker_x), int(walker_y))

            if current_pos not in visited_positions:
                wall = Entity(x=walker_x, y=walker_y, *args, **kwargs)

                visited_positions.add(current_pos)
                cubes.append(wall)

            direction = choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
            walker_x += direction[0]
            walker_y += direction[1]

            walker_x = clamp(walker_x, -limit, limit)
            walker_y = clamp(walker_y, -limit, limit)

def background_displayer(*args, **kwargs) -> Entity:
    background = Entity(
        scale=(conf.WORLD_SIZE, conf.WORLD_SIZE),
        texture_scale=(conf.WORLD_SIZE, conf.WORLD_SIZE),
        z=1,
        *args, **kwargs
    )
    return background
