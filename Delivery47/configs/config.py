HOST = 'http://121.41.14.39:8082'

"""
在一些代码里使用相对路径会报文件找不到
../data/xxx
解决方案：
    通过代码自动获取当前运行项目的路径：
"""
import os  # os.path 相当于python解释器的环境变量 path--import查找的路径
# 工程路径
project_path = os.path.split(os.path.realpath(__file__))[0].split('configs')[0]
# print(__file__)  # 当前运行文件所在路径
# print(project_path)