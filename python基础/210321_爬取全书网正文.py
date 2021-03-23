#210321_爬取全书网正文
import re
import os
import requests
import xlwt,xlrd
# url='https://www.qzguermei.com/d/1020/'
# req=requests.get(url)
# name=re.findall('<h1>(.*?)</h1>',req.text)[0]  #取得书名
# mulu=re.findall('html" title="(.*?)" target="_blank"',req.text)  #获取目录
# wangzhi=re.findall('<a href="/d/1020/(.*?).html" title="',req.text)  #获取网址
# dict1={}
# for i in range(14,len(mulu)):
#     dict1[mulu[i]]=f'{url}{wangzhi[i]}.html'


#写入文件
# excel1=xlwt.Workbook()  #实例化一个excel
# worksheet=excel1.add_sheet(f'{name}')  #新建一个sheet
# worksheet.write(0,0,'目录')  #行,列,值
# worksheet.write(0,1,'网址')  #行,列,值
# row=1
# for k,v in dict1.items():
#     worksheet.write(row,0,k)  #将目录写入到excel
#     worksheet.write(row,1,v)  #将网址写入到excel
#     row+=1
# excel1.save(f'd:/{name}.xls')

#读取excel
# data=xlrd.open_workbook(f'd:/{name}.xls')  #读取一个excel文件
# sheet1=data.sheets()[0]  #读取第一个sheet
# for i in range(1,sheet1.nrows):  #nrows 返回有效行数
#     print(sheet1.cell_value(i,0),sheet1.cell_value(i,1))

#获取正文内容
# if not os.path.exists(f'd:/{name}'):  #判断目录是否存在,如果不存在,则
#     os.mkdir(f'd:/{name}')  #新建一个以书名命名的目录
# count=1
# for k,v in dict1.items():
#     if count>=5:
#         break
#     else:
#         zhengwen=requests.get(v)  #获取正文网页的内容
#         neirong=re.findall('id="chaptercontent">(.*?)全书网手机阅读地址',zhengwen.text,re.S)[0]  #获取正文内容
#         neirong=neirong.replace('&nbsp;','').replace('<br/><br/>','\n')  #去掉多余的字符
#         with open(f'd:/{name}/{count:04}_{k}.txt','w+') as file1:
#             file1.write(neirong)
#     count+=1

#阶乘
# 6!=6*5!
# 5!=5*4*3*2*1
#
# n!=n*(n-1)!
#递归
def jiecheng(n):
    if n==1:
        return 1
    else:
        return n*jiecheng(n-1)
print(jiecheng(6))