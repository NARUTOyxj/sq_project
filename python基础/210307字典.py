#字典
#字典永远以键值对出现,不会出现有键没值或者有值没键的情况
#字典是无序的
# dict1={'A':'apple','B':'book'}
# dict2={'B':'book','A':'apple'}
# print(dict1==dict2)
# list1=[10,20]
# list2=[20,10]
# print(list1==list2)
#字典的键能存放哪些对象?字典的值能存放哪些?
dict1={'A':'apple'}  #字典的键可以存放不可变对象,不能存放可变对象,字典的值可以存放任意对象
#字典本身算作可变对象

#可变对象,肯定可以增删改
# dict2={'A':'apple','B':'book','C':'cake','D':'duck'}
# dict2['E']='earth'  #字典中没有这个键值对,则新增
# dict2['D']='disk'  #字典中有这个键,则修改
# print(dict2)

# dict2.update({'F':'fish','A':'ace'})  #新增或修改
# print(dict2)

#删除字典中的键值对
# del dict2['A']
# dict2['MK']='apple'
# print(dict2)

#字典中的键是唯一的,不会出现重复的键
dict3={'A':'apple','A':'ace'}
# print(dict3)

#清空字典
# print(id(dict3))
# dict3.clear()  #清空字典,内存中的地址不变
# print(id(dict3))

# print(id(dict3))
# dict3={}  #相当于重新建了一个空字典,替换了旧的字典,内存中的地址发生了变化
# print(id(dict3))

#判断某个对象是否存在于字典中,根据键进行判断,而不是值
# dict_new1={'ABC':'ABCDE'}
# # print('ABCDE' in dict_new1)
# print('ABC' in dict_new1)

#遍历字典中的键值对
dict20={'A':'apple','B':'book','C':'cake','D':'duck'}
# for k,v in dict20.items():
#     print(k,v)

#遍历键
# for one in dict20.keys():
#     print(one)

#遍历值
# for one in dict20.values():
#     print(one)

# print(dict20.keys())  #类列表,可以遍历,但不能使用下标
#可以将类列表转换为真正的列表
# list20=list(dict20.keys())
# print(list20)

# list20_value=list(dict20.values())
# print(list20_value)

#json格式
str1='''{
    "aac003" : "tom",
    "tel" : "13959687639",
    "crm003" : "1",
    "crm004" : "1"
}'''
import json  #加载json模块
str1_new=json.loads(str1)  #loads()方法,将json格式转为真正的字典
# print(type(str1_new))
str2=json.dumps(str1_new)  #dumps()方法,将字典转为json格式
print(type(str2))
print(str2)

#课堂小结
#字典的概念,字典是无序的
#自定的增删改
#遍历字典中的键值对
