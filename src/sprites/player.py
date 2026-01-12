from ursina import *


class Player(Entity):
    def __init__(self, map):
        super().__init__(model='quad', texture='textures/me',
                         scale=(256 / 318 * 1.19, 1 * 1.19),
                         collider='box', x=0, y=0, z=0,  origin=(-0.5, -0.5))
        self.map = map
