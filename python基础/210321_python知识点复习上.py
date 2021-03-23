#单引号,双引号,三引号
# str1="It's OK"
# print(str1)
# str2='He said:"Are you OK?"'
# print(str2)
# str3="""He said:"Are you OK?",It's OK"""
# print(str3)
# str3_new='''空山不见人
# 但闻人语响
# 返景入深林
# 复照青苔上'''
# print(str3_new)

#字符串的拼接
# print('A'+'B')
# print('1'+'6')
# print('1'*'6')  #报错
# print('1'*6)

#字符串的转换  int(),float(),str()
# num1=3.6
# num1_1='3.6'
# print(int(num1))
# print(int(float(num1_1)))  #直接转'3.6'会报错,可以先转为float型的3.6,再转为int型

#转义符
# path1='d:\note1.txt'
# path1='d:\\note1.txt'  #再加一个\去掉转义符的特殊含义
# path1=r'd:\note1.txt'  #字符串前面加一个r,表示后面的字符串不进行转义
# path1='d:/note1.txt'  #路径可以使用/代替\

#字符串的下标
str6='nybtevrc'
# print(str6[5])
# print(str6[-3])
# str6[5]='c'  #报错,字符串是不可变对象

#字符串的切片  [起始值:终止值:步长]  包含起始值,不包含终止值,步长默认为1
#字符串的切片是生成了新对象,与原对象无关
# print(str6[3:6])
# print(str6[-5:-2])

# print(str6[5:2:-1])  #vet
# print(str6[-3:-6:-1])  #vet

#翻转字符串
# print(str6[::-1])

#列表可以存放哪些对象?任意对象
#列表是可变对象,可以增删改
#增  append,insert,extend
#改  通过下标就可以改
#删  pop,remove,del
#1,1,2,3,5,8,13,21,34  斐波那契数列
# list1=[]
# for i in range(20):
#     if i<=1:
#         list1.append(1)
#     else:
#         list1.append(list1[-2]+list1[-1])
# print(list1)

#列表的切片,也是生成一个新的对象,原理与字符串的切片一样
# print(list1[:])  #生成一个完整的切片,原列表的一个复制

#元组  元组也可以使用下标和切片,但是元组是不可变对象
# tuple1=(10,)  #元组中只有一个值时,后面加一个逗号
# print(type(tuple1))
# tuple2=(10,20,30)
# print(tuple2[:2])

#浅拷贝,深拷贝
list9=[10,20,30,[40,50]]
# list9_new=list9  #此处实际上只是建立了list9的一个快捷方式
# list9[0]=200
# print(list9)
# print(list9_new)

import copy
# list9_new=copy.copy(list9)  #浅拷贝 列表是不同的对象,子列表仍然是相同的对象
# list9[0]=200
# list9[-1][0]=360  #对子列表修改,两者仍然指向的是同一个子列表
# print(list9)
# print(list9_new)
#浅拷贝等价于切片list9_new=copy.copy(list9),也可以写成list9_new=list9[:]

# list9_new=copy.deepcopy(list9)  #深拷贝,列表和子列表都是不同的对象
# list9[-1][0]=360
# print(list9)
# print(list9_new)

#list()函数,将对象转为列表,tuple()函数,将对象转为元组

#布尔表达式
#and 一假为假,全真为真
#or  一真为真,全假为假