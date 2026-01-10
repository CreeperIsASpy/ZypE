from ursina import *


class Config:
    DEBUG = False
    SPLASH_TIME = 1
    WORLD_SIZE = 100
    PLAYER_COLLISION_RADIUS = 0.2
    PLAYER_COLLISION_DIRECTIONS = [
            Vec3(1, 0, 0),  # 右
            Vec3(1, 1, 0),  # 右上
            Vec3(1, -1, 0), # 右下
            Vec3(-1, 0, 0),  # 左
            Vec3(-1, 1, 0),  # 左上
            Vec3(-1, -1, 0),  # 左下
            Vec3(0, 1, 0),  # 上
            Vec3(0, -1, 0)  # 下
        ]
    SPEED = 5
    FOV = 15
    SPAWN_LIMIT = int(WORLD_SIZE / 2)

    def setup(self, player):
        from src.components.loop_handlers import LoopHandlers
        from src.components.input_handlers import InputHandler
        from src.components import splash, dialog

        camera.orthographic = True
        camera.fov = self.FOV
        self.loop_handlers = LoopHandlers(player=player)

        invoke(splash.end_splash, delay=self.SPLASH_TIME)

        dialog.toggle_dialog(False)

        self.input_handlers = InputHandler(player=player)
