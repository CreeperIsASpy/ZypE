from ursina import *
from pathlib import Path


def get_project_root() -> Path:
    """
    获取项目根目录 'Zype' 的绝对路径
    """
    if getattr(sys, 'frozen', False):
        return Path(sys.executable).parent.absolute()

    return Path(__file__).resolve().parent.parent


class Config:
    DEBUG = True
    SPLASH_TIME = 1
    PLAYER_COLLISION_RADIUS = 0.5
    PLAYER_COLLISION_DIRECTIONS = [ # 用于玩家碰撞检测
            Vec3(1, 0, 0),  # 右
            Vec3(1, 1, 0),  # 右上
            Vec3(1, -1, 0), # 右下
            Vec3(-1, 0, 0),  # 左
            Vec3(-1, 1, 0),  # 左上
            Vec3(-1, -1, 0),  # 左下
            Vec3(0, 1, 0),  # 上
            Vec3(0, -1, 0)  # 下
        ]
    WALKER_DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 用于随机漫步生成器
    SPEED = 5
    FOV = 15
    ROOT_DIR = get_project_root()
    pixel_art_data = [ # 用于 Home 地图的字符画彩蛋
        "###  ###",
        "  #  # #",
        "###  ###",
        "  #  # #",
        "###  ###",
    ]

    def setup(self, map):
        from src.components.loop_handlers import LoopHandlers
        from src.components.input_handlers import InputHandler
        from src.components import splash

        camera.orthographic = True
        camera.fov = self.FOV
        self.loop_handlers = LoopHandlers(player=map.player)
        self.input_handlers = InputHandler(player=map.player)
        invoke(splash.end_splash, delay=self.SPLASH_TIME)

        return self

from src.maps import map_home, map_hall, map_story

map_mapping = {
    'Home': map_home.Home,
    'Hall': map_hall.Hall,
    'Story': map_story.Story
}