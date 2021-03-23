# 第二次思考题
# number = input('请输入手机号：\n')
# while not number.isdigit():
#     number = input('有非法字符，请重新输入手机号：\n')
# length = len(number)
# while length != 11:
#     number = input('位数错误，请输入11位手机号：\n')
# start = int(number[0:3])
# if 130 <= start <= 150:     # 或者 start >= 130 and start <= 150
#     print('运营商是移动')
# elif 151 <= start <= 170:
#     print('运营商是联通')
# elif 171 <= start <= 199:
#     print('运营商是电信')
# else:
#     print('是其他运营商')



# 第三次思考题
# def getName(srcStr):
#     return srcStr.split('the name is')[1].split(',')[0]
# print(getName('A old lady come in, the name is Mary, level 94454'))

# 第四次思考题1
# Jack Green ,   21  ;  Mike Mos, 9;
# str = input('请输入姓名及年龄：')
# stuInfoList = str.split(';')
# for one in stuInfoList:
#     if one != '':
#         stuInfo = one.strip()
#         name = stuInfo.split(',')[0].strip()
#         age = stuInfo.split(',')[1].strip()
#         # print('{:<20}:{:>02}'.format(name,age))
#         print(f'{name:<20}:{age:>02}')



# 第四次思考题2
log = '''
f20180111014341/i_51a7hC3W.jpeg	169472	FrITJxleSP7wUD-MWw-phL_KP6Eu	15156063244230469	image/jpeg	0
f20180111014341/j_R0Hpl4EG.json	1036	ForGzwzV3e-uR3_UzvppJs1VgfQG	15156064773253144	application/json	0
f20180111020739/i_0TDKs0rD.jpeg	169472	FrITJxleSP7wUD-MWw-phL_KP6Eu	15156076847077556	image/jpeg	0
f20180111020739/j_JFO6xiir.json	1040	FmUhTchdLOd7LBoE8OXzPLDKcW60	15156077904192983	application/json	0
f20180111090619/i_1BwNksbL.jpg	49634	FtXBGmipcDha-67WQgGQR5shEBu2	15156329458714950	image/jpeg	0
'''
# dict1 = {}
# line_list = log.strip().split('\n')
# for one in line_list:
#     if one != '':
#         one1 = one.split('\t')[0]
#         file_type = one1.split('.')[1]
#         file_size = int(one.split('\t')[1])
#         if file_type not in dict1:
#             dict1[file_type] = file_size
#         else:
#             dict1[file_type] += file_size
# print(dict1)

# 第五次思考题

# filePath = 'd:/sqfile/signInLog.txt'
# def putInfoToDict(filePath):
#     dict1 = {}
#     dict2 = {}
#     with open(filePath) as file1:
#         list1 = file1.read().splitlines()
#         for one in list1:
#             one1 = one.replace('(', '').replace(')', '').replace("'", '').replace('\t', '').strip(',').strip(';')
#             checkintime, lessonid, studentid = one1.split(',')
#             checkintime = checkintime.strip()
#             lessonid = lessonid.strip()
#             studentid = int(studentid.strip())
#             dict2 = {'lessonid':lessonid,'checkintime':checkintime}
#             if studentid not in dict1:
#                 dict1[studentid] = []
#             dict1[studentid].append(dict2)
#     return dict1
#
# import pprint
# pprint.pprint(putInfoToDict(filePath))

# filepath = 'd:/sqfile/file1.txt'
# filepath2 = 'd:/sqfile/file2.txt'
# with open(filepath) as file1,open(filepath2, 'w+') as file2:
#     file_lines = file1.read().splitlines()
#     for one in file_lines:
#         one1,one2 = one.split(';')
#         name = one1.split(':')[1].strip()
#         salary = int(one2.split(':')[1].strip())
#         file2.write(f'name:{name:<7} ;    salary:{salary:>7} ;    tax:{int(salary*0.1):>7} ;    income:{int(salary*0.9):>7}\n')


# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def perimeter(self):
#         return self.a + self.b + self.c
#
#     def area(self):
#         p = (self.a + self.b + self.c) * 0.5
#         return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
#
#
# tri = Triangle(6, 4, 5)
# print(tri.perimeter())
# print(tri.area())


# 第九次思考题
# from random import randint
# import time
# class Tiger:
#     classname = 'tiger'
#     def __init__(self,weight = 200):
#         self.weight = weight
#
#     def say(self):
#         print('Wow !!')
#         self.weight -= 5
#         print('体重 -5')
#
#     def feed(self, food):
#         if food == 'meat':
#             self.weight += 10
#             print('体重 +10')
#         else:
#             self.weight -= 10
#             print('体重 -10')
#
#
# class Sheep:
#     classname = 'sheep'
#     def __init__(self,weight =100):
#         self.weight = weight
#
#     def say(self):
#         print('mie~~')
#         self.weight -= 5
#         print('体重 -5')
#
#     def feed(self, food):
#         if food == 'grass':
#             self.weight += 10
#             print('体重 +10')
#         else:
#             self.weight -= 10
#             print('体重 -10')
#
# class Room:
#     def __init__(self, num, animal):
#         self.num = num
#         self.animal = animal
#
# rooms = []
# for no in range(10):
#     if randint(0, 1):
#         animal = Tiger(200)
#     else:
#         animal = Sheep(100)
#     room = Room(no,animal)
#     rooms.append(room)
#
# startTime = time.time()
# while True:
#     curTime = time.time()
#     if (curTime - startTime) >120:
#         print('\n\n游戏结束')
#         for idx,room in enumerate(rooms):
#             print('房间：%s '% (idx+1),room.animal.classname,room.animal.weight)
#         break
#     roomno = randint(1,10)
#     room = rooms[roomno-1]
#     choose = input('房间号%s,要敲门吗？[y/n]'% roomno)
#     if choose == 'y':
#         room.animal.say()
#     food = input('请给房间里的动物喂食：meat还是grass?')
#     room.animal.feed(food.strip())


# 第十一次课思考题

# def fun(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * fun(n-1)
#
#
# n = int(input('请输入一个正整数：'))
# print(fun(n))

import re
str1='<html>a="as1d32as1d654as54d65asd465asd4"</html>'
print(re.findall('<html>a="(.+?)"</html>',str1))

# dict = {'a':'apple','c':'cookie'}
# print(dict.count())
