from ursina import *
from src.config import Config as conf

app = Ursina(title='ZypE', borderless=False, development_mode=conf.DEBUG)
from src.components.game import Game
game = Game()
game.start()

# 绑定到生命周期函数
def update():
    game.lc_update()

def input(key):
    game.lc_input(key)


app.run()
