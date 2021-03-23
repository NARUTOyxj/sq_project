#列表与元组
#列表,类似于java中的数组,但是它比数组更加强大,可以存放任意对象
# list1=[1,'abc',[10],(20,30),{'A':'apple'}]
# print(list1)
#列表是可变对象,可以修改其中的元素的值
list2=[10,20,30]
# list2[0]=90
# print(list2)

#添加列表中的元素
# list2.append(985)  #添加一个元素到列表末尾
# print(list2)
# list2.insert(1,666)  #参数1表示插入的位置,参数2表示插入的值
# print(list2)
# list2.extend([700,800,900])
# list2.extend('abc')  #'abc'→['a','b','c']
# list2.extend(123)  #int型不可以使用extend进行拼接
# print(list2)

#删除列表中的元素
# list3=[11,22,33,44,55,33,66]
# list3.pop()  #默认删除列表中的最后一位
# list3.pop(0)  #pop可以指定下标进行删除
# print(list3)

# list3.remove(33)  #根据值进行删除,这种删除方式效率相对较低,每次remove只会删除它遇到的第一个符合条件的值
# print(list3)

# del list3[0]
# print(list3)

# list3_new=[10,20,30,40,50]
# print(list3_new[0:3])
# print(list3_new[-5:-2])
#30,20,10
# print(list3_new[-3::-1])

#元组 元组和列表一样,可以使用下标和切片,但是元组属于不可变对象,不能增删改其中的元素
# tuple1=(10,20,30,40,50)
# tuple1_new=tuple1[0:2]
# print(tuple1_new)
# print(tuple1)  #切片是一个新的对象,所以不会影响原来的对象
#如果元组中有一个子列表,请问,子列表中的值可以修改
# tuple2=(100,200,[300,400])
# tuple2[2][0]=87  #第一个下标指的是子列表[300,400],第二个下标指的是子列表中的300
# print(tuple2)

#如果元组中只有一个元素,需要加一个逗号
tuple3=(10000,)
print(type(tuple3))
