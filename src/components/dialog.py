from ursina import *


class DialogManager:
    def __init__(self):
        self.current_speaker = None
        self.is_open = False
        self.dialog_list = []
        self.dialog_index = 0

        self.dialog_border = Entity(
            parent=camera.ui,
            model='quad',
            color=color.white,
            scale=(1.32, 0.22),
            position=(0, -0.35),
            z=1,
            enabled=False
        )

        self.dialog_bg = Entity(
            parent=camera.ui,
            model='quad',
            color=color.black,
            scale=(1.3, 0.2),
            position=(0, -0.35),
            z=0,
            enabled=False
        )

        self.dialog_text = Text(
            parent=camera.ui,
            text='...',
            font='assets/fonts/5_Minecraft AE.ttf',
            position=(-0.6, -0.28),
            origin=(-0.5, 0.5),
            color=color.white,
            scale=1.5,
            z=-1,
            enabled=False
        )

    def show(self, entity, content=None):
        self.current_speaker = entity
        self.is_open = True

        self.dialog_border.enabled = True
        self.dialog_bg.enabled = True
        self.dialog_text.enabled = True

        if content:
            if isinstance(content, list):
                self.dialog_list = content
                self.dialog_index = 0
                self.dialog_text.text = self.dialog_list[self.dialog_index]
            else:
                self.dialog_list = [content]
                self.dialog_index = 0
                self.dialog_text.text = content
        else:
            self.dialog_list = ["..."]
            self.dialog_index = 0
            self.dialog_text.text = "..."

    def hide(self):
        self.current_speaker = None
        self.is_open = False

        self.dialog_border.enabled = False
        self.dialog_bg.enabled = False
        self.dialog_text.enabled = False

        self.dialog_list = []
        self.dialog_index = 0

    def trigger(self, target, text=None):
        if target is None or text is None:
            if self.is_open:
                self.hide()
            return
        else:
            if not self.is_open:
                self.show(target, text)
            else:
                if self.current_speaker.name == target.name:
                    if self.dialog_index < len(self.dialog_list) - 1:
                        self.dialog_index += 1
                        self.dialog_text.text = self.dialog_list[self.dialog_index]
                    else:
                        self.hide()
                else:
                    self.hide()
                    self.show(target, text)


dialog_sys = DialogManager()
