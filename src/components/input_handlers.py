from ursina import *
from src.config import Config as conf
from src.components import dialog

class InputHandler:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def collision(self):
        """
        我们有全世界最好的物理引擎：盒体扫掠检测 (BoxCast)
        """
        hit_info = boxcast(
            origin=self.player.position,
            thickness=(self.player.scale_x + conf.PLAYER_COLLISION_RADIUS, self.player.scale_y + conf.PLAYER_COLLISION_RADIUS),
            ignore=[self.player, ],
            debug=conf.DEBUG,
        )

        if hit_info.hit:
            return True


    def handle_interaction(self):
        if self.collision():
            dialog.toggle_dialog()
