
#循环语句与注释
#打印1-10的数字
# for i in range(1,11):  #range(起始值,终止值,步长)  包含起始值,不包含终止值,步长默认为1
#     print(i)

# i=1
# while i<=10:
#     print(i)
#     i+=1  #i每次自增长1  等价于i=i+1
#如果有明确的循环次数,建议用for循环,如果循环次数不确定,建议用while循环
#两者可以互相替换

#打印100以内的奇数
# for i in range(1,100,2):
#     print(i)
# for i in range(1,100):
#     if i%2==1:
#         print(i)

#for循环的起始值也是可以省略的,当不写起始值时,缺省为0
# for i in range(11):
#     print(i)

#使用for循环遍历列表
# list1=['星矢','冰河','紫龙','舜','一辉']
#第一种,下标方式进行遍历
# for i in range(len(list1)):
#     print(list1[i])
#第二种,直接遍历
# for one in list1:
#     print(one)

#break 终止循环,continue 跳出当次循环
# for i in range(1,11):
#     if i==5:
#         # break
#         continue
#         # pass  #站位符,防止语法错误
#     print(i)
# else:  #循环语句,可以有一个else语句,当循环成功地执行完毕时,会执行一次else中的语句
#     print('循环运行完毕')

#写一个倒计时小程序
# import time  #导入时间模块
# for i in range(10,0,-1):
#     print(f'\r倒计时{i}秒',end='')  #\r让光标回到行首
#     time.sleep(1)  #让程序等待1秒
# else:
#     print('\r倒计时结束')

#课堂小结
#for循环,while循环
#for循环中的,起始值,终止值,步长
#for循环遍历列表
#break,continue
#倒计时程序

#可以使用三引号在函数或类的方法中进行注释
def fun1():
    '''
    tntybrtevfdcnthbrg
    untbrgvf
    munthrgvfnthgf
    :return:
    '''
print(fun1.__doc__)  #打印函数中的注释
