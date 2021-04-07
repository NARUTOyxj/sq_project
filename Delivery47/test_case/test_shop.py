from libs.login import Login
from libs.shop import Shop
import pytest,os
from tools.excelControl import get_excel_data
import allure # pip install allure-pytest
# 封装测试类

# 多个fixture在一起，离测试的方法近的先执行
# @pytest.mark.usefixtures('sq')  # 没有返回值的fixture用法
# @pytest.mark.usefixtures('sq2')  # 没有返回值的fixture用法
@pytest.mark.shop  # 标签1
@allure.epic('订餐系统') # 工程级别
@allure.feature('店铺模块')
class TestShop:
    # def setup_class(self):  # 初始化  setup_class 类级别：这个类开始的时候只执行一次
    #     """
    #     初始化--创建一个店铺实例
    #     :return:
    #     """
    #     self.token = Login().login({'username':'th0379','password':'sq123456'},getToken=True)
    #     self.shopObject = Shop(self.token)
    #     print('--------初始化操作-----------')
    #
    # def teardown_class(self):
    #     print('-------数据清除操作---------')

    # 1- 列出店铺的测试方法
    @pytest.mark.shop_list  # 标签2
    @pytest.mark.parametrize('caseTitle,inBody,expData',get_excel_data('../data/delivery47.xls', '我的商铺',
                                                                   'listshopping','标题','请求参数', '响应预期结果'))
    @allure.story('列出店铺')
    @allure.title("{caseTitle}")  # 使用{}里的变量
    def test_shop_list(self,caseTitle,inBody,expData,shop_init):
        # 调用列出接口
        res = shop_init.shop_list(inBody)
        if 'code' in res:
            assert res['code'] == expData['code']
        else:
            assert res['error'] == expData['error']

    #  2- 编辑店铺的测试方法
    @pytest.mark.shop_update  # 标签3
    @pytest.mark.parametrize('caseTitle,inBody,expData',get_excel_data('../data/delivery47.xls', '我的商铺',
                                                                       'updateshopping','标题','请求参数', '响应预期结果'))
    @allure.story('编辑店铺')
    @allure.title("{caseTitle}")
    def test_shop_update(self,caseTitle,inBody,expData,update_shop_init):
        # 调用列出接口
        res = update_shop_init[0].shop_update(inBody,update_shop_init[1],update_shop_init[2])
        assert res['code'] == expData['code']


if __name__ == '__main__':
    # try:
    #     for one in os.listdir('../report/tmp'):
    #         if '.json' in one:  # 以后有环境配置文件在里面，所以加了判断
    #             os.remove(f'../report/tmp/{one}')
    # except:
    #     print('第一次运行pytest.main()')

    pytest.main(['test_shop.py', '-s','-m','shop','--alluredir','../report/tmp'])  # -s显示打印
    os.system('allure serve ../report/tmp')