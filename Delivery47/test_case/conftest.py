""""
def fixture(scope="function", params=None, autouse=False, ids=None, name=None):
 重点说下 scope 四组参数的意义：
- function：每个方法（函数）都会执行一次。
- class：每个类都会执行一次。类中有多个方法调用，只在第一个方法调用时执行。
- module：一个 .py 文件执行一次。一个.py 文件可能包含多个类和方法。
- package/session：多个文件调用一次，可以跨 .py 文件。

fixture运行方式：
    1- 自动调用
        自动化测试前，检查环境，访问项目，检验账号，可以自动化执行方式做
    2- 手动调用
        实际的接口的前置条件
            每一个模块的前置条件不一样！
"""
import pytest
@pytest.fixture(scope='class',autouse=True)
def start_running():
    #1- 初始化操作
    print('-----自动化测试前----初始化操作---')

    #2- 数据清除
    yield
    print('-----自动化测试完成----初始化操作---')
