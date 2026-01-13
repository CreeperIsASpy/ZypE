from ursina import *

from src.maps.map import Map
from src.components.spawner import background_displayer
from src.config import Config as conf

class Home(Map):
    is_random = True
    def __init__(self, player):
        super().__init__(player, size=(38, 9))
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
        self.pixel_art()


    def pixel_art(self):
        height = len(conf.pixel_art_data)
        px_art = Entity(position=(1, 2, 0), origin=(-0.5, -0.5),)
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

    def save(self):
        from src.components.save import Saver
        from src.components import dialog
        Saver.save(self)
        dialog.dialog_sys.trigger(self.save_point, "进度已保存。")

    def interaction(self, entity: Entity):
        from src.components import dialog
        interaction_mapping = {
            "wall": lambda: dialog.dialog_sys.trigger(entity, "这墙看起来挺厚，上面有歪歪扭扭的刻字“38号入口”。"),
            "save_point": self.save,
        }
        return interaction_mapping.get(entity.name, None)
