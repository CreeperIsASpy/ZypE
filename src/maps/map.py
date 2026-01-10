from ursina import *

from src.components.spawner import background_displayer


class Map:
    def __init__(self, player, background):
        self.player = player
        self.background = background_displayer(
            model='quad',
            texture=background,
        )

