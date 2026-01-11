from typing import Tuple

from ursina import *

from src.components.spawner import background_displayer
from src.sprites.player import Player


class Map(Entity):
    def __init__(self, player: Player, size: Tuple[int, int], background: str = None):
        super().__init__()
        self.size = size
        self.player = player
        if background:
            self.background = background_displayer(
                size=size,
                parent=self,
                model='quad',
                texture=background,
            )
