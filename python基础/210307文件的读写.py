#文件的读写
#使用open()函数读取文件中的内容
# filepath='d:/note1.txt'
# file1=open(filepath)  #打开d:/note1.txt  open(文件路径,读写模式)
# 读写模式默认是r(读取),也可以用w(写入),a(追加写入)
# print(file1.read())  #读取文件中的内容,返回值是字符串
# for i in range(2):
#     print(file1.readline())  #读取一行的内容
# print(file1.readlines())  #读取文件中的全部内容,返回值是列表,每一行作为列表中的一个元素
# file1.close()  #关闭文件

#如果遇到文件有乱码的情况,下检查文件的编码,改为正确的
#如果文件是正确的编码,但是仍然有乱码,那么检查pycharm的编码格式
#settings→editor→file encondings,调整文字的格式

#文件允许同时进行读取与写入,有r+,w+,a+
# filepath='d:/note210307_1.txt'
# file1=open(filepath,'w+')
# file1.write('好雨知时节,当春乃发生.随风潜入夜,润物细无声.野径云俱黑,江船火独明.晓看红湿处,花重锦官城')
# file1.seek(0)  #让光标回到文件开头,在文件同时进行读写时,通过使用seek()达到同时读写的目的
# print(file1.read())
# file1.close()

#r+ 如果文件不存在,则报错,写入时是覆盖写入
#w+ 如果文件不存在,则新建文件,写入时是清空写入
#a+ 如果文件不存在,则新建文件,写入时是追加写入

# filepath='d:/note210307_1.txt'
# file1=open(filepath)
# file1.seek(11)  #光标偏移一段距离
# print(file1.read())
# file1.close()

# with open()与open()非常类似,并且它可以同时处理多个文件,并且不需要写close()方法
# filepath1='d:/note210307_1.txt'
# filepath2='d:/note210307.txt'
# with open(filepath1) as file1,open(filepath2) as file2:
#     print(file1.read())
#     print(file2.read())

#将100以内的自然数写入到文件中
# with open('d:/自然数210307.txt','w+') as file1:
#     for i in range(1,101):
#         if i==100:
#             file1.write(str(i))  #写入时的参数,必须是字符串类型
#         else:
#             file1.write(str(i)+',')  #写入时的参数,必须是字符串类型

#课堂小结
#open()方法,read(),write(),close()
#readline(),readlines()
#r+,w+,a+
#seek()
#with open()


filepath = 'd:/note.txt'
with open(filepath) as file1:
    print(file1.read())

# file1 = open(filepath)
# file1.seek(0)
# for one in range(2):
#     print(file1.readline())
# print(file1.readlines())
# print(file1.read())

# file1 = open(filepath, 'w+')
# file1.write('窗前明月光，疑是地上霜\n')
# file1.seek(0)
# print(file1.read())
# file1.close()

# file1 = open(filepath, 'a+')
# file1.write('举头望明月，低头思故乡\n')
# file1.seek(0)
# print(file1.read())
# file1.close()

