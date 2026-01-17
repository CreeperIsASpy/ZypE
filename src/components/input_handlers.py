from ursina import *
from src.config import Config as conf

class InputHandler:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.hit_entity = None

    def collision(self, player):
        """
        我们有全世界最好的物理引擎：盒体扫掠检测 (BoxCast)
        """
        hit_info = boxcast(
            origin=player.position + Vec3(player.scale_x / 2, player.scale_y / 2, 0),
            thickness=(player.scale_x + conf.PLAYER_COLLISION_RADIUS, player.scale_y + conf.PLAYER_COLLISION_RADIUS),
            ignore=[player],
            # debug=conf.DEBUG,
            direction=player.forward,
        )

        return hit_info


    def handle_interaction(self, player):
        from src.components.dialog import dialog_sys
        hit_info = self.collision(player)
        if hit_info.entity:
            action = player.map.interaction(hit_info.entity)

            if action:
                action()

        else:
            dialog_sys.trigger(hit_info.entity)
