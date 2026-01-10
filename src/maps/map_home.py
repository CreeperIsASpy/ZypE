from src.maps.map import Map
from src.components.spawner import random_entities_spawner
from src.config import Config as conf

class Home(Map):
    def __init__(self, player):
        super().__init__(player, background='assets/textures/home_tile')
        random_entities_spawner(conf.SPAWN_LIMIT,
                                model="quad",
                                texture="assets/textures/home_brick_wall",
                                scale=(1, 1),
                                z=0,
                                collider='box',
                                )

