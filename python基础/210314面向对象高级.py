#210314_面向对象高级
#私有属性,不能被子类继承,在属性的前面加上__就变为了私有属性
#私有方法,不能被子类继承,在方法的前面加上__就变为了私有方法
#__只在前面加,后面不加,一般前后都有__的,属于类当中自带的方法或属性
class Class_test1:
    __str1='A'  #私有属性
    def __init__(self):
        pass
    def __method1(self):  #私有方法
        print('这是一个私有方法')
    def method2(self):
        print(self.__str1)  #在对外开放的方法里调用私有属性
        self.__method1()  #在对外开放的方法里调用私有方法
cls1=Class_test1()
# print(cls1.__str1)
# cls1.__method1()
# cls1.method2()
# class Class_test2(Class_test1):
#     pass
# cls2=Class_test2()
# print(cls2.__str1)
# cls2.__method1()
# cls2.method2()

#所有的类,都是object的子类,无论是否声明继承objcet,实际上都继承object
class Class1:
    '''
    人生得意须尽欢
    莫使金樽空对月
    '''
# print(Class1.__doc__)  #显示类的注释
# print(Class1.__bases__)  #显示所有父类的名称
# print(Class1.__base__)  #显示第一个父类的名称
# print(Class1.__name__)  #显示类的名称

#多继承
# class Money1:
#     def money(self):
#         print('一个亿')
# class Money2:
#     def money(self):
#         print('两个亿')
# class Human(Money1,Money2):  #继承顺序决定了碰到同名方法时继承哪一个
#     pass
# hum=Human()
# hum.money()

#多态
# class Animal:
#     def say(self):
#         pass
# class Dog(Animal):
#     def say(self):
#         print('汪汪汪')
# class Cat(Animal):
#     def say(self):
#         print('喵喵喵')
# dog=Dog()
# cat=Cat()
# def animal_say(obj):
#     obj.say()
# animal_say(dog)

# class Fanguan:
#     pass
# class Yuxiangrousi(Fanguan):
#     def caidan(self):
#         print('鱼香肉丝')
# class Gongbaojiding(Fanguan):
#     def caidan(self):
#         print('宫保鸡丁')
# class Qingjiaotudousi(Fanguan):
#     def caidan(self):
#         print('青椒土豆丝')
# guke1=Yuxiangrousi()
# guke2=Gongbaojiding()
# guke3=Qingjiaotudousi()
# def fuwuyuan(obj):
#     obj.caidan()
# fuwuyuan(guke1)

# 写一个猜数字游戏,需求如下:随机生成一个0-100之间的数字,让用户猜,如果用户猜对了,
# 提示:回答正确,游戏结束.如果猜错了给出对应的提示(您输入的值过大,您输入的值过小),最多允许猜7次.
from random import randint  #加载随机数模块
answer=randint(1,100)  #在1-100之间随机生成一个整数,包含1和100
for i in range(7):
    input1=input('请输入一个数字:')
    if not input1.isdigit():
        print('输入的不是数字,游戏结束')
        break
    else:
        input1=int(input1)
        if input1==answer:
            print('回答正确,游戏结束')
            break
        elif input1>answer:
            print('数字过大')
        elif input1<answer:
            print('数字过小')

#写一个三角形的类
class Sanjiaoxing:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def zhouchang(self):
        if self.a+self.b<=self.c or self.a+self.c<=self.b or self.b+self.c<=self.a:
            return '无法构成三角形,忽略周长'
        else:
            return self.a+self.b+self.c
    def mianji(self):
        if self.a+self.b<=self.c or self.a+self.c<=self.b or self.b+self.c<=self.a:
            return '无法构成三角形,忽略周长'
        else:
            p=(self.a+self.b+self.c)/2
            return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5