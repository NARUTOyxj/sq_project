import yaml
def get_yaml_data(fileDir):
    #1- 在内存打开这个文件
    fo = open(fileDir,'r',encoding='utf-8')
    #2- 调用yaml读取
    res = yaml.load(fo)  # Loader=yaml.FullLoader更加安全，有警告时使用
    return res

def get_yamls_data(fileDir):
    resList = []
    #1- 在内存打开这个文件
    fo = open(fileDir,'r',encoding='utf-8')
    #2- 调用yaml读取
    res = yaml.load_all(fo)  # Loader=yaml.FullLoader更加安全，有警告时使用
    for one in res:
        resList.append(one)
    return resList

#-----------------------yaml用例读取---------------------------------------
def get_yaml_caseData(fileDir):
    #1- 在内存打开这个文件
    resList = []  # 结果数据
    fo = open(fileDir,'r',encoding='utf-8')
    #2- 调用yaml读取
    res = yaml.load(fo)  # Loader=yaml.FullLoader更加安全，有警告时使用
    baseInfo = res[0]  # 基本信息url method
    del res[0]
    for one in res:
        resList.append((one['data'],one['resp']))
    return resList

#-------------------------------------------------------------------------

"""
注意事项：
    1- 尽量少改代码
    2- pytest需要什么数据，什么类型
    [(请求数据1，期望响应数据1),(请求数据2，期望响应数据2)]
"""

from configs.config import project_path
if __name__ == '__main__':
    info = get_yaml_caseData(project_path+r'\configs\cnf.yaml')
    print(info)
    # for k,v in info.items():
    #     print(k,v)