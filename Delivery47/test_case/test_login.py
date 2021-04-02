"""
需要自动化执行excel用例
流程：
    1- 从excel用例获取对应的接口数据---优化
    2- 数据结合接口代码进行自动化执行---接口代码需要什么就传递什么
    3- 判定结果是否符合预期
"""
# 1- 从excel用例获取对应的接口数据
# from tools.excelControl import get_excel_data
# from libs.login import Login
# resList = get_excel_data('../data/Delivery47.xls', '登录模块','Login','请求参数', '响应预期结果')
# # print(resList)
#
# for one in resList:
#     # print(one)  # [请求替数据，期望结果响应数据]
#     # 2- 数据结合接口代码进行自动化执行
#     # 封装的业务代码indata--字典
#     res = Login().login(one[0])  # 接口实际返回的响应数据
#     print(res)
#     if res['msg'] == one[1]['msg']:
#         print('--pass--')
#     else:
#         print('--fail--')



#-------------------------------------------------------
#测试代码
import pytest
import allure
from tools.excelControl import get_excel_data
from libs.login import Login
import os
class TestLogin:
    # 测试方法
    # 数据驱动--参数化--读取用例数据
    # @pytest.mark.parametrize('参数的变量名',实际需要传入的参数)
    # @pytest.mark.parametrize('a,b,c',[(1,2,3),(4,5,6)])
    @pytest.mark.parametrize('inBody,expData',get_excel_data('../data/delivery47.xls', '登录模块','Login','请求参数', '响应预期结果'))
    def test_login(self,inBody,expData):
        # 调用接口代码
        res = Login().login(inBody)  # 请求体传入--调用登录接口
        # 断言
        print('--用例执行--')
        assert res['msg'] == expData['msg']
        #多个标识需要断言的操作
        # assert res['msg'] == expData['msg'] and \
        #        res['code'] == expData['code']

if __name__ == '__main__':
    # 删除已存在的报告
    try:
        for one in os.listdir('../report/tmp'):
            if '.json' in one:  # 以后有环境配置文件在里面，所以加了判断
                os.remove(f'../report/tmp/{one}')
    except:
        print('第一次运行pytest.main()')

    # '--alluredir', '..report/tmp'  报告需要的文件存放路径
    pytest.main(['test_login.py', '-s','--alluredir','../report/tmp'])  # -s显示打印
    # 转化成可视化报告  allure 指令
    # allure serve 把报告起一个服务
    # 需要把谷歌或火狐设为默认浏览器
    os.system('allure serve ../report/tmp')
    """
    allure工作流程
        1- 生成报告需要的源数据：pytest运行测试用例  pytest.main()------一定有数据，后面报告源数据
        2- 有了源数据-需要工具去转化源数据得到  allure，可视化报告
        
    """