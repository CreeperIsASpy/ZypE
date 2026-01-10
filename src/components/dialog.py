from ursina import *

dialog_border = Entity(
    parent=camera.ui,
    model='quad',
    color=color.white,
    
    scale=(1.32, 0.22),
    
    position=(0, -0.35),
    z=1  
)


dialog_bg = Entity(
    parent=camera.ui,
    model='quad',
    color=color.black,
    
    scale=(1.3, 0.2),
    position=(0, -0.35),
    z=0  
)


dialog_text = Text(
    parent=camera.ui,
    text='...',
    font='assets/fonts/5_Minecraft AE.ttf',
    
    position=(-0.6, -0.28),
    
    origin=(-0.5, 0.5),
    color=color.white,
    scale=1.5, 
    z=-1 
)

def toggle_dialog(enabled = None, text = None):
    if enabled is None:
        dialog_bg.enabled = not dialog_bg.enabled
        dialog_border.enabled = not dialog_border.enabled
        dialog_text.enabled = not dialog_text.enabled
    else:
        dialog_bg.enabled = enabled
        dialog_border.enabled = enabled
        dialog_text.enabled = enabled

    if text is not None:
        dialog_text.text = text
