from ursina import *

from src.components import splash, save, spawner


class Game:
    def __init__(self):
        self.map = None
        self.player = None
        self.conf = None

    def _spawn_player(self):
        """Spawns a player entity, hiding it if the current map is 'Story'."""
        self.player = spawner.player_spawner(self.map, self.map.size, False, (self.map.map_id == 'Story'), 0, 0)
        self.map.player = self.player

    def start(self):
        from src.config import Config as conf
        from src.components import save

        self.map_type = save.Saver.load()
        self.map = self.map_type(self, self.player)
        self.conf = conf.setup(conf, self.map)
        self._spawn_player()

    def lc_update(self):
        if not splash.splashed:
            return


        self.conf.loop_handlers.handle_movement(self.player)
        self.conf.loop_handlers.constrain_player(self.player)
        self.conf.loop_handlers.update_camera(self.player)

    def lc_input(self, key):
        if key == 'escape':
            quit()
        elif key == 'enter':
            self.conf.input_handlers.handle_interaction(self.player)

    def switch_map(self, map):
        from src.config import Config as conf
        if self.player:
            destroy(self.player)
        if self.map:
            destroy(self.map)
        self.map_type = map
        self.map = self.map_type(self, None)
        self._spawn_player()
        self.conf = conf.setup(conf, self.map)
