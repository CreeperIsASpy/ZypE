from ursina import *

class SignBoard(Entity):
    def __init__(self, text, *args, **kwargs):
        super().__init__(origin=(-0.5, -0.5), *args, **kwargs)
        self.model = 'quad'
        self.scale = (1, 1)
        self.texture = "assets/textures/signboard"
        self.text = text

    def trigger(self):
        from src.components.dialog import dialog_sys
        dialog_sys.trigger(self, self.text)
