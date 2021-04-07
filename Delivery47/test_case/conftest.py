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
import pytest,os
from libs.login import Login
from libs.shop import Shop
@pytest.fixture(scope='session',autouse=True)
def start_running():
    #1- 初始化操作
    print('-----自动化测试前----初始化操作---')
    try:
        for one in os.listdir('../report/tmp'):
            if '.json' in one:  # 以后有环境配置文件在里面，所以加了判断
                os.remove(f'../report/tmp/{one}')
    except:
        print('第一次运行pytest.main()')
    #2- 数据清除
    yield
    print('-----自动化测试完成----初始化操作---')


# 项目中的很多业务模块都需要登录
# 1- 登录操作——初始化，获取token——需要手动调用fixture
@pytest.fixture(scope='class')
def login_init():
    token = Login().login({'username':'th0379','password':'sq123456'},getToken=True)
    print('-----1-登录初始化-----')
    return token


# 2- 创建店铺——创建店铺实例
@pytest.fixture(scope='class')
def shop_init(login_init):  # (写前置的fixture名字)用来引入前置fixture的返回值，多个值用下标
    shopObject = Shop(login_init)
    print('-----2-创建店铺实例-----')
    return shopObject

# 3- 店铺更新接口初始化
"""
更新店铺前置条件：
  1- shopID  从列出店铺——需要登录——店铺实例——列出店铺
  2- imageInfo  要登录——店铺实力——上传接口
"""
@pytest.fixture(scope='function')  # 只有店铺更新接口需要
def update_shop_init(shop_init):  # (写前置的fixture名字)用来引入前置fixture的返回值，多个值用下标
    # 获取店铺id
    shopID = shop_init.shop_list({"page":1,"limit":10})['data']['records'][0]['id']
    #
    imageInfo = shop_init.file_upload('商铺图片.jpg','../data/商铺图片.jpg','image/png')['data']['realFileName']
    print('-----3-店铺更新-----')
    return shop_init,shopID,imageInfo  # 返回类型为元组


@pytest.fixture(scope='class')  # 没有返回值的用法，直接使用usefixture就可以
def sq():
    print('-----fixture test-----')

@pytest.fixture(scope='class')  # 没有返回值的用法，直接使用usefixture就可以
def sq2():
    print('-----fixture test-----')