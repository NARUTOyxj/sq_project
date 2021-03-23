
# 面向对象基础
# 类和实例
# 新建一个长方形的类
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def permerter(self):
        return (self.length + self.width) * 2

    def area(self):
        return self.length * self.width


# 类不能直接被使用,需要先实例化,再使用
rec = Rectangle(5, 4)  # 实例化一个长为5,宽为4的长方形
print(rec.permerter())
print(rec.area())
