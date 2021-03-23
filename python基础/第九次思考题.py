#210315_第9次课思考题讲解
#解题思路
#1.建立一个老虎的类
#2.建立一个羊的类
#3.建立一个房间的类
#4.把老虎或者羊放入房间
#5.写游戏相关的代码
class Tiger:
    def __init__(self):
        self.name='老虎'
        self.weight=200
    def eat(self,food):
        if food=='meat':
            print('喂食正确')
            self.weight+=10
        elif food=='grass':
            print('喂食错误')
            self.weight-=10
    def roar(self):
        print('Wow!')
        self.weight-=5

class Sheep:
    def __init__(self):
        self.name='羊'
        self.weight=100
    def eat(self,food):
        if food=='grass':
            print('喂食正确')
            self.weight+=10
        elif food=='meat':
            print('喂食错误')
            self.weight-=10
    def roar(self):
        print('mie~')
        self.weight-=5

#建立一个房间的类
class Room:
    def __init__(self,category):
        self.category=category

roomlist=[]  #定义一个列表,等下用来存放房间的实例

from random import randint
for i in range(10):
    if randint(1,2)==1:  #相当于扔硬币决定是生成老虎还是生成羊
        category=Tiger()  #实例化一个老虎
    else:
        category=Sheep()  #实例化一个羊
    rm=Room(category)  #实例化一个房间,里面有一个动物
    roomlist.append(rm)  #把房间的实例放到列表中

import time
start_time=time.time()  #记录游戏开始时间
while time.time()-start_time<=10:
    room_number=randint(0,9)  #随机选择一个数字作为房间号
    random_room=roomlist[room_number]  #选取该房间
    load1=input(f'当前访问的是{room_number+1}号房间,请问是敲门还是喂食?1/2')
    if load1=='1':
        random_room.category.roar()  #调用房间中的动物的叫的方法
    elif load1=='2':
        food=input('请输入需要喂的食物 meat/grass')
        if food=='meat' or food=='grass':
            random_room.category.eat(food)  #调用房间中的动物的吃的方法
        else:
            print('您输入的食物不正确')
    else:
        print('您输入的操作不正确')
else:
    print('游戏时间到')
    for i in range(len(roomlist)):
        print(f'{i+1}号房间的动物是{roomlist[i].category.name},体重是{roomlist[i].category.weight}')