import json

from src.config import get_project_root

class LangFile:
    def __init__(self):
        """
        初始化语言文件加载器。
        它会加载位于 'assets/langfile/map.json' 的文件。
        """
        self.data = {}
        project_root = get_project_root()
        file_path = project_root / 'assets' / 'langfile' / 'map.json'
        with open(file_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)


    def get(self, key: str) -> str:
        """
        使用点分割的键从语言数据中获取字符串。
        """
        value = self.data
        for k in key.split('.'):
            value = value[k]

        return str(value)


langfile = LangFile()
