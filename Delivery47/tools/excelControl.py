"""
需求：定义一个excel用例读取函数
常规功能：
    1、读取指定列数据
    2、具备自动化识别无效用例
优化功能：v1.2
    1- 在前一个版本的时候，是指定读取列，不合理，如果需要根据用户需要去读取对应的列
    方案：定义参数的时候，可以数量不定——可变数量参数  *args
    用户习惯传递什么标识
    1- 列编号
    2- 列名称
        问题1：用户输入的是列名称，但是代码去获取单元格数据是通过cell(行编号，列编号)
具体的操作流程：
    1、先把磁盘的excel用例打开到内存里
    2- 使用excel第三库去操作  xlrd(.xls)   pyopenxl(.xlxs) pandas(处理大数据 .csv)
"""
import xlrd
import json


# def get_excel_data(excelDir, sheetName, caseName, *args):
#
#     resList = []  # 存放结果
#     # 1- 定义excel的路径
#     # 2- 打开excel
#     # formatting_info = True 保持样式
#     workBook = xlrd.open_workbook(excelDir,formatting_info=True)  # workbook  是一个xx.xl文件对象
#     # 3- 具体操作excel文件里哪一个sheet,通过sheet名，获取表对象
#     # workSheet = workBook.sheet_names()
#     workSheet = workBook.sheet_by_name(sheetName)
#     # 4- 读取一行数据
#     # print(workSheet.row_values(0))
#     # 4- 读取一列数据
#     # print(workSheet.col_values(0))
#     # 5- 筛选用例
#     idx = 0  # 行的初始值
#     for one in workSheet.col_values(0): # 对第一列数据进行遍历
#         if caseName in one:  # 说明这里用例是符合要求的
#             # 读取对应的数据
#             # workSheet.cell(行号，列号).value
#             reqBody = workSheet.cell(idx, 9).value  # 读取请求体
#             expData = workSheet.cell(idx, 11).value
#             resList.append((reqBody, expData))
#         idx += 1  # 行编号变化
#     return resList
#     # print(workSheet)


# #—————————————————————扩展版本代码———————————————————————————————————
# def get_excel_data(excelDir, sheetName, caseName, *args):
#
#     resList = []  # 存放结果
#     # 1- 定义excel的路径
#     # 2- 打开excel
#     # formatting_info = True 保持样式
#     workBook = xlrd.open_workbook(excelDir,formatting_info=True)  # workbook  是一个xx.xl文件对象
#     # 3- 具体操作excel文件里哪一个sheet,通过sheet名，获取表对象
#     # workSheet = workBook.sheet_names()
#     workSheet = workBook.sheet_by_name(sheetName)
#     # 4- 读取一行数据
#     # print(workSheet.row_values(0))
#     # 4- 读取一列数据
#     # print(workSheet.col_values(0))
#     colIdex = []  # 存放用户需要获取列名对应的列编号
#
#     # —————————————————把用户输入列表转化成列编号————————————————————————————————
#     for i in args: # 遍历元组
#         # 列明在sheet第0行数据
#         colIdex.append(workSheet.row_values(0).index(i))  # 获取列表对应的下标
#     # —————————————————————----------———————————————————————————————————---
#     # print("列名对应的下标>>> ",colIdex)
#
#     # 5- 筛选用例
#     idx = 0  # 行的初始值
#     for one in workSheet.col_values(0): # 对第一列数据进行遍历
#         if caseName in one:  # 说明这个用例是符合要求的
#             getColData = []  # 这行代码必须要，每一次需要初始化
#             # 读取对应的数据
#             # workSheet.cell(行号，列号).value
#             for num in colIdex:
#                 res = json.loads(workSheet.cell(idx,num).value)  # 获取单元格数据
#                 getColData.append(res)  # 把用户需要读取的列数据，append到一个列表
#             resList.append(getColData)  # 获取所有符合要求的用例数据
#         idx += 1  # 行编号变化
#     return resList
# #————————————————————————————————————————————————————————



#—————————————————————代码优化-v1.2———————————————————————————————————
"""
优化需求：
    1- 如果我们需要获取不是json 格式的列数据---代码会报错！
           json.loads(workSheet.cell(idx, num).value)
    2- 数据驱动的时候：
        一个登录的接口用例sheet  全表读取？
        需求点：能不能我只执行某几条用例  连续的用例编码，也可以单个不连续的
        方案：
            1- pytest数据驱动是靠一个@pytest.mark.parametrize
            2- 只需要把我们需挑选的用例读取出来就可以！
            3-  分类：
                1- all 所有用例
                2- 001-004  连续一段
                3- 001,003,005
                复杂的 场景  ['001','005-008','010']
"""


#判定是否是json
def is_json(str1):
    try:
        json.loads(str1)  # 字符串转化成字典
    except ValueError:
        return False  # 不是json
    return True  # 是json

def get_excel_data(excelDir, sheetName, caseName, *args,runCase = ['all']):
    """

    :param excelDir:
    :param sheetName:
    :param caseName:
    :param args:
    :param runCase: 挑选运行用例，默认是all
    :return:
    """

    resList = []  # 存放结果
    workBook = xlrd.open_workbook(excelDir,formatting_info=True)  # workbook  是一个xx.xl文件对象
    workSheet = workBook.sheet_by_name(sheetName)
    colIdex = []  # 存放用户需要获取列名对应的列编号
    for i in args: # 遍历元组
        colIdex.append(workSheet.row_values(0).index(i))  # 获取列表对应的下标
    # 5- 筛选用例

    runList = []  # 最后的运行列表
    if runCase[0] == 'all':  # 全部运行！
        runList = workSheet.col_values(0)  # 第一列所有的数据
    else:  # 如果不是all
        # 连续的 001-003
        # 不连续 001,005
        for one in runCase:  # ['001','004-008']
            if '-' in one:  # for 004 005 006 007 008
                start,end = one.split('-')  # 获取连续用例编号的头尾
                for i in range(int(start),int(end)+1):
                    runList.append(caseName+f'{i:0>3}')
            else:
                runList.append(caseName+f'{one:0>3}')  # Login001

    idx = 0  # 行的初始值
    for one in workSheet.col_values(0): # 对第一列数据进行遍历
        if caseName in one and one in runList:  # 说明这个用例是符合要求的
            getColData = []  # 这行代码必须要，每一次需要初始化
            # 读取对应的数据
            for num in colIdex:
                # workSheet.cell(行号，列号).value  前提是json
                # 如果是json字符串，就传话成字典，不是就不操作
                res = workSheet.cell(idx,num).value
                # if res[0] == '{' and res[-1] == '}':
                if is_json(res):  # 判断是不是json
                    res = json.loads(res)  # 获取单元格数据
                getColData.append(res)  # 把用户需要读取的列数据，append到一个列表
            resList.append(getColData)  # 获取所有符合要求的用例数据
        idx += 1  # 行编号变化
    return resList
#————————————————————————————————————————————————————————


if __name__ == '__main__':
    res = get_excel_data('../data/delivery47.xls', '登录模块','Login','用例编号', 'URL',runCase=['001','003-005'])
    # print(res)
    for one in res:
        print(one)