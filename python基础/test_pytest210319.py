#test_pytest210319
#pytest是一种自动化测试框架,是python的第三方单元测试框架,向下兼容unittest
#预期结果,实际结果
#pip install pytest,或者使用豆瓣源,清华源等进行安装

#pytest命名规范
#文件名应当以test_开头,或者以_test结尾
#类应当以Test开头,且类当中不能有__init__方法
#方法或函数应当以test_开头
#断言必须使用assert  结果为真,断言不做事情,结果为假,断言生效,抛出异常AssertionError

# assert 1==2  #判断等式两边是否相等
# assert 200  #判断某个语句是否为真
# assert 10 in [10,20]  #判断某个值是否属于某个对象
# assert 1!=2  #判断某个值是否不等于另一个值
# assert not False

import pytest
import allure
import os  #加载系统模块
# def test_01():
#     print('HelloWorld')
#     assert 1==1  #判断预期结果和实际结果是否一致
# def test_02():
#     assert 1==2

# class Test1:
#     def teardown_method(self):  #④
#         print('这是最后执行的方法')
#     def test_c01(self):  #②
#         assert 10==100
#     def test_c02(self):  # ③
#         assert 1 == 1
#     def setup_method(self):  #①
#         print('这是最先执行的方法')
#method级别 ①②④①③④

# class Test1:
#     def teardown_class(self):  #④
#         print('这是最后执行的方法')
#     def test_c01(self):  #②
#         assert 10==100
#     def test_c02(self):  # ③
#         assert 1 == 1
#     def setup_class(self):  #①
#         print('这是最先执行的方法')
#class级别  ①②③④

# class Test10:
#     @pytest.mark.parametrize('result,real_result',[[3,6],[6,9],[18,18]])  #数据驱动,参数化
#     def test_10(self,result,real_result):
#         assert result==real_result

@allure.feature('层级1')
@allure.story('层级2')
@allure.title('层级3')
class Test20:
    def test_20(self):
        assert 3+6==9
#pytest框架,测试通过,显示".",测试不通过,显示F
if __name__ == '__main__':
    pytest.main(['test_pytest210319.py','-s','--alluredir','./report'])  #test_pytest210319.py 文件名 -s展示打印的语句
    os.system('allure generate ./report -o ./report/report --clean')

#课堂小结
#pytest框架的概念,命名规范
#assert断言
#pytest的写法
#setup,teardown,@pytest.fixture(scope='class')
#数据驱动 @pytest.mark.parametrize

#allure环境搭建
# 1、下载allure.zip
# 2、解压allure.zip到一个文件目录中
# 3、将allure报告安装目录\bin所在的路径添加环境变量path中
# 4、pip install  allure-pytest
# 5、验证