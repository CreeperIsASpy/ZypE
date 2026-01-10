from ursina import *
from src.config import Config as conf

class LoopHandlers:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def handle_movement(self, dt):
        """处理玩家的移动输入和物理碰撞"""
        # X 轴移动逻辑
        dx = held_keys['right arrow'] - held_keys['left arrow']
        if dx != 0:  # 只有按键时才计算
            self.player.x += dx * dt * conf.SPEED
            if self.player.intersects().hit:
                self.player.x -= dx * dt * conf.SPEED

        # Y 轴移动逻辑
        dy = held_keys['up arrow'] - held_keys['down arrow']
        if dy != 0:
            self.player.y += dy * dt * conf.SPEED
            if self.player.intersects().hit:
                self.player.y -= dy * dt * conf.SPEED


    def constrain_player(self):
        """限制玩家不跑出地图边界"""
        limit_x = (conf.WORLD_SIZE / 2) - (self.player.scale_x / 2)
        limit_y = (conf.WORLD_SIZE / 2) - (self.player.scale_y / 2)

        # 修正：原代码中 player.x 用了 limit_y，这里建议对应清楚
        self.player.x = clamp(self.player.x, -limit_x, limit_x)
        self.player.y = clamp(self.player.y, -limit_y, limit_y)


    def update_camera(self):
        """相机跟随逻辑"""
        camera.x = self.player.x
        camera.y = self.player.y
