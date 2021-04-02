from libs.login import Login
from libs.shop import Shop
import pytest,os
from tools.excelControl import get_excel_data
class TestShop:
    def setup_class(self):  # 初始化  setup_class 类级别：这个类开始的时候只执行一次
        """
        初始化--创建一个店铺实例
        :return:
        """
        self.token = Login().login({'username':'th0379','password':'sq123456'},getToken=True)
        self.shopObject = Shop(self.token)
        print('--------初始化操作-----------')
    # 列出店铺的测试方法
    @pytest.mark.parametrize('inBody,expData',('../data/delivery47.xls', '我的商铺','listshopping','用例编号', 'URL'))
    def test_shop_list(self,inBody,expData):
        # 调用列出接口
        res = self.shopObject.shop_list()
        if 'code' in res:
            assert res['code'] == expData['code']
        else:
            assert res['msg'] == expData['msg']

    def teardown_class(self):
        print('-------数据清除操作---------')

if __name__ == '__main__':
    try:
        for one in os.listdir('../report/tmp'):
            if '.json' in one:  # 以后有环境配置文件在里面，所以加了判断
                os.remove(f'../report/tmp/{one}')
    except:
        print('第一次运行pytest.main()')

    pytest.main(['test_login.py', '-s','--alluredir','../report/tmp'])  # -s显示打印
    os.system('allure serve ../report/tmp')