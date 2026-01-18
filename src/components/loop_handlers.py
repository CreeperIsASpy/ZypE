from ursina import *
from src.config import Config as conf

class LoopHandlers:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def handle_movement(self, player):
        """处理玩家的移动输入和物理碰撞"""
        if not player.can_move:
            return

        # X 轴移动逻辑
        dx = held_keys['right arrow'] - held_keys['left arrow']
        if dx != 0:  # 只有按键时才计算
            player.x += dx * time.dt * conf.SPEED
            if player.intersects().hit:
                player.x -= dx * time.dt * conf.SPEED

        # Y 轴移动逻辑
        dy = held_keys['up arrow'] - held_keys['down arrow']
        if dy != 0:
            player.y += dy * time.dt * conf.SPEED
            if player.intersects().hit:
                player.y -= dy * time.dt * conf.SPEED

    def constrain_player(self, player):
        """限制玩家不跑出地图边界 (左下角对齐)"""

        map_origin_x = player.map.x
        map_origin_y = player.map.y

        map_w = player.map.size[0]
        map_h = player.map.size[1]

        min_x = map_origin_x
        max_x = map_origin_x + map_w - player.scale_x

        min_y = map_origin_y
        max_y = map_origin_y + map_h - player.scale_y

        # 执行限制
        player.x = clamp(player.x, min_x, max_x)
        player.y = clamp(player.y, min_y, max_y)


    def update_camera(self, player):
        """相机跟随逻辑"""
        if not player.can_move:
            return

        camera.x = player.x
        camera.y = player.y
