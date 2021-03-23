#字符串
#字符串可以用单引号,双引号,三引号表示
# str1="It's OK"  #当句子本身含有单引号时,外面需要用双引号表示
#如果在运行时,遇到invalid syntax,表示语法有问题
# str2='He said:"Nice to see you"'

#三引号,可以跨行表示字符串,它会记录所有的换行符,空格,制表符等
# str3="""第一种三引号"""
# str3_new='''第二种三引号'''

# str6="""今天天气不错
# 挺风和日丽的"""
# print(str6)

#\n表示换行符,\t表示制表符
# str6_new='今天\t天气不错\n挺风和日丽的'
# print(str6_new)

#字符串的拼接
# print(1+1)
# print('1'+'1')
# a=1
# print('1'+str(a))  #前面是字符串str类型,后面是整数int类型,两者不能进行拼接
#str()转为str型,int()转为int型,float()转为float型
#type()函数,返回对象的类型
# print(type(2))

# str9='1.2'
# print(int(float(str9)))
# '1.2'→1.2→1

#字符串的拼接中的 *
# print('1'*'1')  #报错,两个字符串不能相乘
# print('1'*6)  #这么写语法是OK的,相当于将字符串打印n次

#字符串中的转义符
# filepath='d:\note1.txt'  #这么写,有换行符,打印的结果不符合预期
# filepath='d:\\note1.txt'  #方案一,在前面多加一个\
# filepath=r'd:\note1.txt'  #方案二,在字符串的外面加一个r,表示整个字符串中的转义符都不生效
# filepath='d:/note1.txt'  #方案三,改为/
# print(filepath)

#字符串的下标
# str10='abcdefg'
# print(str10[2])  #字符串的下标从0开始,所以是第二位
# print(str10[-2])  #负下标从-1开始,所以倒数第二位是f
# print(str10[7])  #下标越界 index out of range
# str10[0]='q'  #字符串是不可变对象,不可以修改其中的某个值

#字符串的切片
str10='abcdefg'
#打印abc
# print(str10[0:3])  #起始值,终止值,步长 包含起始值,不包含终止值,步长默认为1
# print(str10[2:4])  #cd
# print(str10[-5:-3]) #cd
#打印dc?
# print(str10[3:1:-1])  #当步长为负数时,起始值必须大于终止值
# print(str10[-4:-6:-1])  #当步长为负数时,起始值必须大于终止值
