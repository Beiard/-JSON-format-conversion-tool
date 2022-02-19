import json


class Transformation:
    """将json文件改写成人类能看的格式"""

    def __init__(self, name='1'):
        """初始化路径"""
        self.info = None
        self.file_name = name
        self.file_address = f"{name}.json"

    def read(self):
        """完成读取功能"""
        try:
            print(f"打开文件:{self.file_address}")
            with open(self.file_address) as f:
                self.info = json.load(f)
            return True
        except Exception as err:
            print(f"读取失败,错误代码{err}")

    def dump(self):
        """完成写入功能"""
        try:
            print(f'写入文件:{self.file_name}'+'_1.json')
            with open(self.file_name + "_1.json", "w") as f:
                json.dump(self.info, f, indent=4)
        except Exception as err:
            print(f"写入失败,错误代码{err}")

    def main(self):
        """主程序"""
        if self.read():
            self.dump()


if __name__ == '__main__':
    filename = input('请输入文件名称，默认为:1')
    if filename == '':
        trans = Transformation()
    else:
        trans = Transformation(filename)
    print('开始运行')
    trans.main()
