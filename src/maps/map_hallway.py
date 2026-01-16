from ursina import *

from src.maps.map import Map
from src.components.spawner import background_displayer
from src.components.langfile import langfile
from src.sprites.signboard import SignBoard

class Hallway(Map):
    is_random = True
    def __init__(self, game, player):
        super().__init__(game, player, size=(38, 9))
        self.background = background_displayer(
            size=(38, 9),
            parent=self,
            model='quad',
            texture='assets/textures/hallway_tile',
        )
        self.map_id = 'Hallway'
        self.setup()

    def setup(self):
        # 存档点
        self.save_point = Entity(parent=self,
                                 origin=(-0.5, -0.5),
                                 texture="assets/textures/save_point",
                                 scale=(1, 1), model="quad",
                                 x=4.5, y=0.5, z=0, collider='box', name="save_point")

        # 搞事牌
        self.sb = SignBoard(text=langfile.get("hallway.interaction.signboard_entrance"), x=9.5, y=3.5, z=0, collider="box", name="signboard_entrance", parent=self)

    def save(self):
        from src.components.save import Saver
        from src.components import dialog
        Saver.save(self)
        dialog.dialog_sys.trigger(self.save_point, langfile.get("hallway.interaction.save_point"))

    def interaction(self, entity: Entity):
        interaction_mapping = {
            "save_point": self.save,
            "signboard_entrance": self.sb.trigger
        }
        return interaction_mapping.get(entity.name, None)
