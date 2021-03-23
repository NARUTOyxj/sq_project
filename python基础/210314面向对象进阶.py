#210314_面向对象进阶
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def permerter(self):  #只能由实例调用,称之为实例方法
        return (self.length+self.width)*2
    def area(self):
        return self.length*self.width
    @classmethod  #装饰器,声明下面的方法是类方法
    def features(cls):  #类方法,可以由实例调用,也可以由类调用
        print('两边的长相等,两边的宽也相等,长和宽的角度为90°')
    @staticmethod  #装饰器,声明下面的方法是静态方法
    def sumdata(sum1,sum2):  #静态方法,与类没有实质性的关系,只是一个写在了类里面的函数
        return sum1+sum2

# rec=Rectangle(5,3)
# print(rec.permerter())
# rec.features()  #实例可以调用类方法
# Rectangle.features()  #类也可以调用类方法
# print(Rectangle.sumdata(10,10))  #类可以调用静态方法
# print(rec.sumdata(10,10))  #实例也可以调用静态方法

#类方法还是方法,但静态方法其实是函数
#1.用type的方式证明
# print(type(Rectangle.features))  #method
# print(type(Rectangle.sumdata))  #function

#2.使用inspect模块进行判断
import inspect  #python的自检模块,可以判断某个对象是否是某种类型,返回值是布尔型
# print(inspect.ismethod(Rectangle.features))
# print(inspect.isfunction(Rectangle.features))
# print(inspect.ismethod(Rectangle.sumdata))
# print(inspect.isfunction(Rectangle.sumdata))

#继承
#1.完全继承
# class Square(Rectangle):
#     pass
# squ=Square(6,6)
# print(squ.permerter())
# print(squ.area())

#2.部分继承,改写一些方法
# class Square(Rectangle):
#     def __init__(self,side):  #重写了__init__方法,覆盖了父类的同名方法
#         self.length=side
#         self.width=side
# squ=Square(6)
# print(squ.permerter())
# print(squ.area())

#3.对父类的方法进行扩展
class Square(Rectangle):
    def __init__(self,side):
        self.length=side
        self.width=side
    @classmethod
    def features(cls):
        super().features()  #声明继承父类的同名方法的代码
        print('长和宽也相等')
squ=Square(6)
squ.features()

#课堂小结
#实例方法,类方法,静态方法
#实例方法,可以由实例调用
#类方法,可以由实例和类调用,本质上还是方法
#静态方法,可以由实例和类调用,本质上是函数,与类没有实际的关系,只是写在了类里面
#type的方式,以及使用inspect模块,判断是函数还是方法
#完全继承,部分继承,父类方法的扩展