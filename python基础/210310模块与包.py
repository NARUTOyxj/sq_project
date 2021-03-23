#210310_模块与包
#一个python文件就是一个模块
#存放py文件的目录,我们称之为包,或者文件夹
#如果文件夹中有一个__init__.py,那么就称之为包
#如果是包,必定会有__init__.py,如果没有,则是一个普通的文件夹
#当加载一个包时,会自动执行一次__init__.py中的内容
# import AUTO47

# import time  #加载时间模块
# time.sleep(1)

#标准库,不需要安装,加载就能使用
# import this  #python之禅

#第三方库,需要安装后才可以使用
# import requests  #网络爬虫
# import xlwt,xlrd  #读写excel

#导入模块的几种方式
#import 模块名
# import Sumdata_210310
# print(Sumdata_210310.fun1(3,6))  #模块名.函数名

#from 包 import 模块
# from AUTO47 import Sumdata_210310
# print(Sumdata_210310.fun1(3,6))  #模块名.函数名

#from 包.模块 import 函数
# from AUTO47.Sumdata_210310 import fun1,fun2  #导入多个函数时,中间用逗号隔开
# print(fun1(3,6))  #函数名
# print(fun2(3,6))

#from 模块 import 函数
# from Sumdata_210310 import fun1
# print(fun1(3,6))  #函数名

#from 模块 import *  #加载模块下的所有内容,不推荐这种写法
# from Sumdata_210310 import *
# print(fun1(3,6))
# print(fun2(3,6))

#不同的模块当中,有相同的函数名,可以使用别名对函数进行区分
# from AUTO47.Sumdata_210310 import fun1 as f1
# from AUTO47.Sumdata2_210310 import fun1 as f2
# print(f1(3,6))
# print(f2(3,6))

# if __name__ == '__main__': 这句话表示,以下的代码,只在本模块内执行
#如果被别的模块调用,则不执行以下的代码

#课堂小结
#导入模块的几种方式
#import 模块名
#from 包 import 模块
#from 包.模块 import 函数
#from 模块 import 函数

#导入模块时,如果出现红色波浪线,可以右键文件夹,选择Mark Directory as,选择Sources Root
#就可以将这个目录加入到标准路径中
# if __name__ == '__main__': 的用处