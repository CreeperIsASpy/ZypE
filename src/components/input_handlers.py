from ursina import *
from src.config import Config as conf


class InputHandler:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.hit_entity = None

    def collision(self, player):
        hit_info = boxcast(
            origin=player.position + Vec3(player.scale_x / 2, player.scale_y / 2, 0),
            thickness=(player.scale_x + conf.PLAYER_COLLISION_RADIUS, player.scale_y + conf.PLAYER_COLLISION_RADIUS),
            ignore=[player],
            direction=player.forward,
        )
        return hit_info

    def handle_interaction(self, player):
        """
        整个交互系统的逻辑：
        interaction_mapping 在 map 中定义，其中的键为 entity.name，值为函数返回值（字符串、列表或 None）
        这个函数中执行了被调用时需要执行的操作，并返回一个值。
        返回值是 None 则不会打开对话框
        是字符串或列表则分别显示单个或连续对话框
        """
        from src.components.dialog import dialog_sys
        hit_info = self.collision(player)

        if hit_info.entity:
            dialog_content = player.map.interaction(hit_info.entity)
            dialog_sys.trigger(hit_info.entity, dialog_content)
        else:
            dialog_sys.trigger(None)
