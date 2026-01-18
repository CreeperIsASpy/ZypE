from ursina import *

from src.components.langfile import langfile
from src.maps.map import Map
from src.components.spawner import background_displayer
from src.config import Config as conf

class Home(Map):
    is_random = True
    def __init__(self, game, player):
        super().__init__(game, player, size=(38, 9))
        self.background = background_displayer(
            size=(38, 9),
            parent=self,
            model='quad',
            texture='assets/textures/home_tile',
        )
        self.map_id = 'Home'
        self.setup()

    def setup(self):
        # 存档点
        self.save_point = Entity(parent=self,
                                 origin=(-0.5, -0.5),
                                 texture="assets/textures/save_point",
                                 scale=(1, 1), model="quad",
                                 x=4.5, y=0.5, z=0, collider='box', name="save_point", tag=self)

        self.hallway = Entity(parent=self,
                              origin=(-0.5, -0.5),
                              texture="assets/textures/save_point",
                              scale=(1, 1), model="quad",
                              x=37.5, y=4.5, z=0, collider='box', name="hall", tag=self)

        self.pixel_art()


    def pixel_art(self):
        height = len(conf.pixel_art_data)
        px_art = Entity(parent=self, position=(1, 2, 0), origin=(-0.5, -0.5),)
        for y, line in enumerate(conf.pixel_art_data):
            for x, char in enumerate(line):
                if char == '#':
                    Entity(
                        parent=px_art,
                        origin=(-0.5, -0.5),
                        model='quad',
                        texture='assets/textures/home_brick_wall',
                        scale=(1, 1),
                        position=(
                            x,
                            height - 1 - y,
                            0
                        ),
                        collider='box',
                        name="wall"
                    )

    def _save_action(self):
        """执行存档动作并返回对话文本"""
        from src.components.save import Saver
        Saver.save(self)
        return langfile.get("home.interaction.save_point")

    def interaction(self, entity: Entity | None):
        from src.maps.map_hall import Hall
        if not entity:
            return None

        interaction_mapping = {
            "wall": lambda: langfile.get("home.interaction.wall"),
            "save_point": self._save_action,
            "hall": lambda: self.game.switch_map(Hall),
        }
        
        handler = interaction_mapping.get(entity.name)

        if handler:
            return handler()

        return None
