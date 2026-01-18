from ursina import *

from src.maps.map import Map
from src.components.spawner import background_displayer
from src.components.langfile import langfile
from src.sprites.signboard import SignBoard
from ast import literal_eval as eval


class Hall(Map):
    is_random = True
    def __init__(self, game, player):
        super().__init__(game, player, size=(47, 46))
        self.generate_a_lot_of_walls()
        self.generate_a_lot_of_backgrounds()
        self.generate_a_lot_of_chairs()
        self.ticket_grabbed = False
        self.map_id = 'Hall'
        self.angry_chair = None
        self.setup()

    def setup(self):
        # 存档点
        self.save_point = Entity(parent=self,
                                 origin=(-0.5, -0.5),
                                 texture="assets/textures/save_point",
                                 scale=(1, 1), model="quad",
                                 x=4.5, y=0.5, z=0, collider='box', name="save_point")

        # 搞事牌
        signboard_text = eval(langfile.get("hall.interaction.signboard_entrance"))
        self.ticket = Entity(parent=self, origin=(-0.5, -0.5), texture="assets/textures/hall_ticket",
                             scale=(5, 5), model="quad",
                             x=43, y=10, z=0, collider='box', name="ticket")
            
        self.sb = SignBoard(text=signboard_text,
                                      x=9.5, y=3.5, z=0, collider="box", name="signboard_entrance", parent=self)


    def generate_a_lot_of_walls(self):
        """正如其名，生成一大堆墙"""
        self.wall_top = Entity(parent=self, position=(-1, 9, 0), origin=(-0.5, -0.5),) # 注意 y 轴放低半格
        for _ in range(1, 38):
            Entity(parent=self.wall_top, position=(_, 0, 0), origin=(-0.5, -0.5), collider='box', model='quad')

        self.wall_top.combine(analyze=True)
        self.wall_top.collider = 'box'
        self.wall_top.color = color.clear

        self.wall_topleft = Entity(parent=self, position=(37, 8, 0), origin=(-0.5, -0.5), )  # 注意 y 轴放低半格
        for _ in range(1, 38):
            Entity(parent=self.wall_topleft, position=(0, _, 0), origin=(-0.5, -0.5), collider='box', model='quad')

        self.wall_topleft.combine(analyze=True)
        self.wall_topleft.collider = 'box'
        self.wall_topleft.color = color.clear

    def generate_a_lot_of_backgrounds(self):
        """正如其名，生成一大堆背景"""
        self.background1 = background_displayer(
            size=(38, 9),
            parent=self,
            model='quad',
            texture='assets/textures/hall_tile',
        )
        self.background2 = background_displayer(
            size=(9, 46),
            parent=self,
            model='quad',
            texture='assets/textures/hall_tile',
            x=38,
            y=0,
        )

    def generate_a_lot_of_chairs(self):
        """正如其名，生成一大堆椅子"""
        self.chairs = Entity(parent=self, position=(40, 17, 0), origin=(-0.5, -0.5), )
        for x in range(3):
            for y in range(8):
                Entity(
                    parent=self.chairs,
                    position=(x, y, 0),
                    origin=(-0.5, -0.5),
                    collider='box',
                    model='quad',
                    texture='assets/textures/hall_chair',
                    name="chair",
                )

    def sit_on_the_chair(self, chair_entity: Entity):
        """你试图坐上椅子"""
        if self.ticket_grabbed:
            self.player.can_move = False
            self.player.disable()
            chair_entity.texture = 'assets/textures/hall_chair_occupied'
            camera.fov = 5
            camera.x = chair_entity.world_x
            camera.y = chair_entity.world_y
            return "椅子很高兴，决定允许你坐在它上面"
        elif not self.ticket_grabbed:
            if self.angry_chair and self.angry_chair != chair_entity:
                self.angry_chair.texture = 'assets/textures/hall_chair'

            chair_entity.texture = 'assets/textures/hall_chair_angry'
            self.angry_chair = chair_entity
            return ["椅子发现你并没有领票", "椅子尖叫着抗议", "你无法坐在它上面"]

    def grab_ticket(self):
        """领票"""
        setattr(self, "ticket_grabbed", True)
        for chair in self.chairs.children:
            chair.texture = 'assets/textures/hall_chair'
        self.angry_chair = None
        return "您已领票，感谢您的支持。请入座。"


    def _save_action(self):
        """执行存档动作并返回对话文本"""
        from src.components.save import Saver
        Saver.save(self)
        return langfile.get("hall.interaction.save_point")

    def interaction(self, entity: Entity):
        """统一处理所有交互"""
        interaction_mapping = {
            "save_point": self._save_action,
            "signboard_entrance": self.sb.trigger,
            "ticket": self.grab_ticket,
            "chair": lambda: self.sit_on_the_chair(entity)
        }

        handler = interaction_mapping.get(entity.name)

        if handler:
            return handler()

        return None
