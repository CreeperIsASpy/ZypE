from typing import Tuple

from ursina import *

from src.components.langfile import langfile
from src.components.spawner import background_displayer
from src.sprites.player import Player


class Map(Entity):
    def __init__(self, game, player: Player, size: Tuple[int, int], background: str = None):
        super().__init__()
        self.game = game
        self.size = size
        self.player = player
        if background:
            self.background = background_displayer(
                size=size,
                parent=self,
                model='quad',
                texture=background,
            )

    def setup(self):
        """初始化地图"""
        pass


    def interaction(self, entity: Entity):
        """统一处理所有交互"""
        pass

    def _save_action(self):
        """执行存档动作并返回对话文本"""
        from src.components.save import Saver
        Saver.save(self)
        return langfile.get(f"{self.name}.interaction.save_point")
