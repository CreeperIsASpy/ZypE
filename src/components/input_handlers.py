from ursina import *
from src.config import Config as conf
from src.components import dialog
from src.components.save import Saver

class InputHandler:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.hit_entity = None

    def collision(self, player, entity_name=None):
        """
        我们有全世界最好的物理引擎：盒体扫掠检测 (BoxCast)
        """
        hit_info = boxcast(
            origin=player.position + Vec3(player.scale_x / 2, player.scale_y / 2, 0),
            thickness=(player.scale_x + conf.PLAYER_COLLISION_RADIUS, player.scale_y + conf.PLAYER_COLLISION_RADIUS),
            ignore=[player, ],
            debug=conf.DEBUG,
        )

        if hit_info.hit:
            if entity_name:
                self.hit_entity = hit_info.entity
                return entity_name == hit_info.entity.name
            else:
                return True

        return False


    def handle_interaction(self, player):
        if self.collision(player, "wall"):
            dialog.toggle_dialog(text="这墙看起来挺厚，上面有歪歪扭扭的刻字“38号入口”。")
        if self.collision(player, "save_point"):
            Saver.save(player.map)
            dialog.toggle_dialog(text="saved")
