from ursina import *
from src.maps.map import Map
from src.components.langfile import langfile
from src.maps.map_home import Home

class Story(Map):
    def __init__(self, game, player):
        super().__init__(game=game, player=player, size=(10, 10))
        self.map_id = "Story"

        self.total_slides = 6
        self.current_slide = 1
        
        self.setup()
        self.update_slide()

        # 添加背景音乐
        self.background_music = Audio(
            'assets/audio/story.ogg',
            loop=True,
            autoplay=True
        )

        # 自动切换幻灯片
        self.slide_switcher = Sequence(
            Wait(9.38),
            Func(self.switch_slide),
            loop=True
        )
        self.slide_switcher.start()

    def setup(self):
        self.presentation = Entity(
            parent=camera.ui,
            model='quad',
            scale=(16 / 9, 1),
            y=0.1,
        )

        self.text_area = Entity(
            parent=camera.ui,
            model='quad',
            color=color.black,
            scale=(1.5, 0.2),
            y=-0.38,
            origin=(0, 0)
        )

        self.story_text = Text(
            parent=camera.ui,
            text="",
            scale=1.5,
            origin=(0, 0),
            position=(0, -0.4),
            font='assets/fonts/5_Minecraft AE.ttf',
            color=color.white
        )

        self.page_number = Text(
            parent=camera.ui,
            text="",
            scale=1.5,
            origin=(0.5, 0.5),
            position=(0.85, 0.45),
            font='assets/fonts/5_Minecraft AE.ttf',
            color=color.white
        )

    def update_slide(self):
        """根据当前幻灯片编号更新图片和文字"""
        if self.current_slide > self.total_slides:
            # 幻灯片播放完毕，切换到主地图
            self.background_music.fade_out(duration=3)
            self.slide_switcher.pause()
            destroy(self.presentation)
            destroy(self.text_area)
            destroy(self.story_text)
            destroy(self.page_number)
            self.game.switch_map(Home)
            return

        texture_path = f'assets/textures/story/{self.current_slide}.png'
        self.presentation.texture = texture_path

        lang_key = f'story.content.{self.current_slide}'
        self.story_text.text = langfile.get(lang_key)
        self.page_number.text = f"{self.current_slide}/{self.total_slides}"

    def switch_slide(self):
        self.current_slide += 1
        self.update_slide()
