#210310_加载第三方库
#标准库 time,this,re,os,sys,math等
#第三方库 xlwt,xlrd,pytest,requests,selenium

import os  #加载操作系统模块
# os.system("calc")  #调用操作系统的计算器
# os.system("cmd")
# os.system("mstsc")

import sys  #加载系统模块
#标准路径,当导入一个包或模块时,python会按照从上到下的顺序从每一个标准路径中查看有没有符合条件的包或模块
# print(sys.path)
# for one in sys.path:
#     print(one)
#如果模块位于标准路径中,则可以导入,否则,无法导入
# sys.path.append('D:/')  #临时添加到标准路径
# for one in sys.path:
#     print(one)

# from PKG20 import QQQ  #如果这样写, 标准路径中应该有D:/
# print(QQQ.sumdata(3,6))

#永久添加路径到标准路径??
#在python目录的lib\site-packages新建一个.pth文件,文件名任意,后缀名必须是.pth
#将需要添加的路径写入到文件中,这个路径必须真实存在,否则不显示
# import QQQ  #如果这样写,那么标准路径中应该有D:/PKG20
# print(QQQ.sumdata(3,6))

#模块的命名规范,以字母开头
#当有多个标准路径中有同名模块时,按照标准路径从上到下的顺序进行导入
#所有的第三方库都安装在C:\Python38\lib\site-packages目录内

#安装第三方库的命令
#在cmd中,执行pip install 模块名

#如果安装时,速度较慢,可以考虑使用国内的镜像站进行安装
#豆瓣源
# pip install selenium -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
#清华源
#pip install selenium -i https://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn

#查看安装了哪些第三方库
#在cmd中执行pip list

#更新安装
#在cmd中执行pip install selenium -U

#卸载第三方库
#在cmd中执行pip uninstall selenium

#统计10000以内有多少个含有3的数
# count=0  #定义一个计数器
# for i in range(10001):  #在10000以内开始循环
#     if '3' in str(i):  #如果i当中含有3
#         count+=1  #计数器+1
# print(count)

#用列表推导式实现
print(len([i for i in range(10001) if '3' in str(i)]))

#课堂小结
#标准库与第三方库
#标准路径,临时添加到标准路径,永久添加到标准路径
#安装第三方库的命令
#第6节课思考题