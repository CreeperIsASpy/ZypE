from ursina import *


class DialogManager:
    def __init__(self):
        # --- 1. 状态变量 ---
        self.current_speaker = None  # 记录当前正在跟谁说话
        self.is_open = False  # 记录当前 UI 是否开着

        # --- 2. UI 实体 (初始化时创建，但先隐藏) ---
        self.dialog_border = Entity(
            parent=camera.ui,
            model='quad',
            color=color.white,
            scale=(1.32, 0.22),
            position=(0, -0.35),
            z=1,
            enabled=False  # 默认隐藏
        )

        self.dialog_bg = Entity(
            parent=camera.ui,
            model='quad',
            color=color.black,
            scale=(1.3, 0.2),
            position=(0, -0.35),
            z=0,
            enabled=False  # 默认隐藏
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
            enabled=False  # 默认隐藏
        )

    # --- 3. 明确的“打开”函数 ---
    def show(self, entity, content=None):
        """
        entity: 是谁在说话 (用来判断是否需要关闭)
        content: 说话的内容
        """
        self.current_speaker = entity
        self.is_open = True

        # 启用 UI
        self.dialog_border.enabled = True
        self.dialog_bg.enabled = True
        self.dialog_text.enabled = True

        # 更新文字
        if content:
            self.dialog_text.text = content
        else:
            self.dialog_text.text = "..."

    # --- 4. 明确的“关闭”函数 ---
    def hide(self):
        self.current_speaker = None
        self.is_open = False

        # 禁用 UI
        self.dialog_border.enabled = False
        self.dialog_bg.enabled = False
        self.dialog_text.enabled = False

    def trigger(self, target, text=None):
        self.current_speaker = target
        if target is None: # 对空气按下了交互键，且对话框打开 -> 意图为关闭对话框
            if self.is_open:
                self.hide()
            return # 对空气按下了交互键，且对话框关着 -> 啥也不干
        else: # 对有效交互目标按下了交互键
            if not self.is_open: # 对话框关着 -> 啥也不干
                self.show(target, text)
            else: # 对话框开着
                if self.current_speaker == target: # 是同一个人 -> 关闭对话框
                    self.hide()
                else:
                    self.hide()
                    self.show(target, text) # 不是是同一个人 -> 直接展示新对象的内容



# 实例化一个全局管理器供后续调用
dialog_sys = DialogManager()