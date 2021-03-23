import xlrd
import json
from xlutils.copy import copy

def get_excelData(SheetName, caseName):
    resList = []
    excelDir = '../data/Delivery_System_excel-V1.5.xls'
    workBook = xlrd.open_workbook(excelDir,formatting_info = True)
    workSheet = workBook.sheet_by_name(SheetName)
    idx = 0  #开始的下标
    for one in workSheet.col_values(0):
        if caseName in one:
            reqBodyData = workSheet.cell(idx, 9).value
            respData = workSheet.cell(idx, 12).value
            resList.append((reqBodyData, respData))
        idx += 1
    return resList

    # for one in range(startRow-1, endRow):
    #     reqBodyData = workSheet.cell(one, 9).value
    #     respData = workSheet.cell(one, 12).value
    #     resList.append((reqBodyData, respData))
    # return resList

def set_excelData():
    excelDir = '../data/外卖系统接口测试用例.xls'
    workBook = xlrd.open_workbook(excelDir, formatting_info=True)
    workBookNew = copy(workBook)  #复制一个新excel文件对象
    workSheetNew = workBookNew.get_sheet(0)
    return workBookNew,workSheetNew

if __name__ == '__main__':
    # print(get_excelData('登录模块', 'Login'))
    for one in get_excelData('登录模块', 'Login'):
        print(one)
