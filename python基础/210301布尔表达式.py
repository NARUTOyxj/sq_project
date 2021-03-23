#210301_布尔表达式
#布尔类型 True真 False假
# a=9  #赋值
# print(9==9)  #两个等于表示判断恒等
# print('A'<'a')  #字符串之间比较时,根据ASCII码来比较 a=97 A=65
# print('Aa'<='aA')  #字符串比较时,只比较第一位,除非第一位相同,才会向后比较
#True和False,哪个大?
# print(True>False)  #可以把True看作1,False看作0
# print(3*(True+True))  #布尔型可以直接参与算术运算

#in,not in
# list1=[10,[20]]
# print(10 in list1)  #True
# print(20 in list1)  #False
# print(10 not in list1)  #布尔型的结果,非假即真,非真即假 not True为False,not False 为 True
# print(20 not in list1)

#and 与,or 或
# print(5>3 and 9>8 and 100>99 and 8>7 and 3>6)  #一假为假,全真为真
# print(5>3 or 3>6)  #一真为真,全假为假
# print(1>2 and 1>2 or 3>2)  #逻辑运算符not,and,or的优先级 not>and>or
# print(1>2 and (1>2 or 3>2))  #括号可以改变优先级

# print(isinstance(100,int))  #判断某个对象是否属于某个类,返回值是布尔型

# print(1!=2)

#浅拷贝,深拷贝
list_old=[10,20,30,40,[50,60]]
# list_new=list_old  #普通的赋值,相当于添加了一个快捷方式,两者指向的是同一个列表
# list_old[0]=98
# print(list_old)
# print(list_new)

import copy  #加载拷贝模块
# list_new=copy.copy(list_old)  #浅拷贝,会生成新的对象,但是子列表仍然是同一个对象
# list_new=list_old[:]  #切片,等价于浅拷贝
# list_old[0]=98
# print(list_old)
# print(list_new)

#对子列表中的值进行修改,需要用到深拷贝
list_new = copy.deepcopy(list_old)  #深拷贝的列表和子列表都是不同的对象
list_old[-1][0]=100
print(list_old)
print(list_new)
