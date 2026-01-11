from ursina import *

from random import randint, choice

from src.config import Config as conf
from src.sprites.player import Player

player = None

def player_spawner(map, limit, is_random=True, *position):
    global player
    player = Player(map)
    if is_random:
        for _ in range(100):
            rx = randint(-limit, limit)
            ry = randint(-limit, limit)

            player.position = (rx, ry)

            hit_info = player.intersects(ignore=[player, ])
            if not hit_info.hit:
                return player
    else:
        player.position = position
        return player

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
                ent = Entity(x=walker_x, y=walker_y, *args, **kwargs)

                visited_positions.add(current_pos)
                cubes.append(ent)

            direction = choice(conf.WALKER_DIRECTIONS)
            walker_x += direction[0]
            walker_y += direction[1]

            walker_x = clamp(walker_x, -limit, limit)
            walker_y = clamp(walker_y, -limit, limit)

def background_displayer(size, *args, **kwargs) -> Entity:
    background = Entity(
        origin=(-0.5, -0.5),
        scale=(size[0], size[1]),
        texture_scale=(size[0], size[1]),
        z=1,
        *args, **kwargs
    )
    return background
