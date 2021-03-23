#210303_函数
#函数其实就是封装一段代码,在需要的时候调用
# def fun1():
#     print('HelloWorld')  #这是一个没有返回值的函数,因此它的返回值是None
# fun1()

# def fun2():
#     return 'HelloWorld'
# print(fun2())

#写一个函数,可以求两个数的和
# def sumdata(a,b):  #a,b形式参数,简称形参
#     return a+b
# print(sumdata(6,9))  #实际参数,简称实参

#函数的缺省值，当用户未输入参数时，使用缺省值，当用户输入参数时，使用用户的值
def sumdata(a=100,b=200):
    return a+b
# print(sumdata(6))  #a使用用户输入的值,b使用缺省值
# print(sumdata(b=6))  #指定b=6,则python认可此处是b的值为6
#缺省值的几种写法
# print(sumdata(36,72))  #简略写法
# print(sumdata(36,b=72))  #前面简略写法,后面完整写法
# print(sumdata(a=36,b=72))  #完整写法
# print(sumdata(a=36,72))  #前面完整写法,后面简略写法,不可以这么写

#函数中可以有多个return语句
#写一个函数，返回某数的绝对值
# def jueduizhi(n):
#     if n>=0:
#         return n
#         return '今天天气不错'  #第一个return之后，实际已经退出了函数，后面的语句称之为不可达语句
#     else:
#         return -n
# print(jueduizhi(67890))

#函数可以return多个值,当有多个值时，会以元组形式返回
# def sumdata2(a,b):
#     return a+b,a-b,a*b,a**b
# print(sumdata2(2,10))

# def sumdata2_new(a,b):
#     return [a+b,a-b,a*b,a**b]  #列表是一个对象，返回时不需要加上元组
# print(sumdata2_new(2,10))

# print(1,2,3,4,5)
#*args  可变长度参数，允许用户输入任意个实参
#sep=' ',间隔符，在每个参数之间填充的值
#end='\n',换行符，在打印的结尾自动补一个值

def fun6(a=1,*args):
    return a,*args  #解包，这样写可以少一层元组，这种写法适合较新版本的python
    # return a,args  #这种写法会多一层元组
    # return (a,*args)  #这种写法适合较低版本的python
print(fun6(100,200,300,400))

#关键字参数  **kwargs  允许用户输入任意个参数，必须是x=y的形式，返回值是字典形式
# def fun9(a=1,**kwargs):
#     return a,kwargs
# print(fun9(100,A='apple',B='book',C='cake'))
