from ursina import *
from src.config import Config as conf

app = Ursina(title='Zype', borderless=False, development=conf.DEBUG)
window.icon = 'assets/zype.ico'
window.fullscreen = False

from src.components import splash, spawner
from src.maps import map_home

spawner.player_spawner(conf.SPAWN_LIMIT)
conf.setup(conf, spawner.player)

map = map_home.Home(spawner.player)

def update():
    if not splash.splashed:
        return

    dt = time.dt

    conf.loop_handlers.handle_movement(dt)
    conf.loop_handlers.constrain_player()
    conf.loop_handlers.update_camera()


def input(key):
    if key == 'escape':
        quit()
    elif key == 'enter':
        conf.input_handlers.handle_interaction()

app.run()