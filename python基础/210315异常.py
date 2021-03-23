#210315_异常处理
#一个标准的try except语句,至少要有一个except,也可以有多个except,也可以加一个else语句,以及finally语句
# try:
#     int1=int(input('请输入一个整数'))
#     print(1/int1)
# except ZeroDivisionError:
#     print('0不能作为分母')
# except ValueError:
#     print('您输入的不是整数')
# except:  #以上的异常没有捕捉到的情况下,此处起到兜底的作用
#     print('程序有问题')
# else:  #程序未出现异常,则执行else中的语句
#     print('没有出现异常')
# finally:  #无论程序是否出现异常,都会执行
#     print('程序运行完毕')

#常见的异常
# NameError  #未定义的变量
# print(num1)
# IndexError
# list1=[10,20]
# print(list1[2])
# IOError  #输入输出异常
# FileNotFoundError
# with open('D:/中国足球勇夺世界杯冠军.txt') as file1:
#     file1.read()

#所有的异常,都是Exception的子类或者子类的子类
# print(NameError.__bases__)
# print(IndexError.__bases__)
# print(LookupError.__bases__)
#Exception也有一个父类,BaseException
# print(Exception.__bases__)
# print(BaseException.__bases__)

#手动抛出异常
# try:
#     raise IOError  #假装这里有异常
# except:
#     print('文件读写错误')

#日志模块
import time  #加载时间模块
import logging  #加载日志模块
import traceback  #加载配合日志的异常模块
logging.basicConfig(level='DEBUG',filename='D:/log_210315.log',filemode='a+')
# logging.debug('这是debug级信息')
# logging.info('这是info级信息')
# logging.warning('这是warning级信息')
# logging.error('这是error级信息')
# logging.critical('这是critical级信息')
try:
    int1=int(input('请输入一个整数'))
    print(1/int1)
except ZeroDivisionError:
    logging.error(time.strftime('%y-%m-%d %H:%M:%S')+traceback.format_exc())
except ValueError:
    logging.error(time.strftime('%y-%m-%d %H:%M:%S')+traceback.format_exc())
except:  #以上的异常没有捕捉到的情况下,此处起到兜底的作用
    print('程序有问题')
else:  #程序未出现异常,则执行else中的语句
    logging.info('服务器未出现异常')
finally:  #无论程序是否出现异常,都会执行
    print('程序运行完毕')

#课堂小结
#try,excpet,else,finally
#常见的异常
#所有的异常都是Exception的子类
#手动抛出异常 raise
#将异常写入日志