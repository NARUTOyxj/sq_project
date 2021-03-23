#210321_python知识点复习下
# import time
# for i in range(10,0,-1):
#     print(f'\r倒计时{i}秒',end='')  #\r让光标回到行首
#     time.sleep(1)  #让程序等1秒
# else:  #循环正常结束时,执行一次else中的语句
#     print(f'\r倒计时结束')

# for i in range(1,11):
#     if i==5:
#         # break  #终止循环
#         continue  #跳出一次循环
#     else:
#         print(i)

#使用while循环时,注意设置终止条件,如果while后面的布尔表达式始终为真,则会变为死循环
# i=0
# while i<=5:
#     print('12345')
#     i+=1

#文件读写
# with open('d:/210321.txt','w+') as file1:
#     file1.write('庆历四年春,滕子京谪守巴陵郡.')
#     file1.seek(0)
#     print(file1.read())

#字典
#字典是可变对象
#字典的键可以存放不可变对象
#字典的值可以存放任何对象
#字典以键值对的形式进行存放
#字典是无序的
dict1={'A':'apple','B':'book'}
dict2={'B':'book','A':'apple'}
# print(dict1==dict2)

for k,v in dict1.items():
    print(k,v)

#json格式
str1='''{
    "aac003" : "tom",
    "tel" : "13959687639",
    "crm003" : "1",
    "crm004" : "1"
}'''
import json  #加载json模块
str1_new=json.loads(str1)  #loads()方法,将json格式转为真正的字典
# print(type(str1_new))
str2=json.dumps(str1_new)  #dumps()方法,将字典转为json格式
print(type(str2))
print(str2)