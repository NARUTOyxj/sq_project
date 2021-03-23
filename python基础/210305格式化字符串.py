```python
#格式化字符串
# a=7
# b=8
# print(str(a)+'+'+str(b)+'='+str(a+b))
# print('%d+%d=%d'%(a,b,a+b))  #格式化字符串,%d表示一个数字类型的占位符  %s str型  %f float型

#格式化字符串方案一
# info1='我叫%s,你叫%s,他叫%s,今年是%d年'%('天乐','德华','青云',2021)
# print(info1)
#如果前面的占位符比后面的参数多,则报错
# info1='我叫%s,你叫%s,他叫%s,今年是%d年'%('天乐','德华','青云',2021)
# print(info1)
#如果前面的占位符比后面的参数少,也报错
# info1='我叫%s,你叫%s,他叫%s,今年是2021年'%('天乐','德华','青云',2021)
# print(info1)
#前面是%d,后面的参数是字符串,则报错;前面是%s,后面参数是数字,则不报错
# info1='我叫%d'%('天乐')
# print(info1)

#补齐 %ns n是任意自然数,不足n位时,补齐到n位
# info1='我叫%6s,你叫%s,他叫%s,今年是%d年'%('天乐','德华','青云',2021)
# print(info1)
#超过n位时,正常显示所有位数
# info1='我叫%6s,你叫%s,他叫%s,今年是%d年'%('高手名字不能太长','德华','青云',2021)
# print(info1)
#数字的补齐,与字符串一样,都是右对齐
# info1='我叫%6s,你叫%s,他叫%s,今年是%6d年'%('天乐','德华','青云',1)
# print(info1)
#数字的补齐,可以在左侧补0
# info1='我叫%6s,你叫%s,他叫%s,今年是%06d年'%('天乐','德华','青云',1)
# print(info1)
#如果想把右对齐改为左对齐,怎么办?
# info1='我叫%-6s,你叫%s,他叫%s,今年是%-6d年'%('天乐','德华','青云',1)
# print(info1)

#%f 浮点型,默认保留6位小数
# number1='您输入的数字是%f'%(3.6)
# print(number1)

#改为保留两位小数
# number1='您输入的数字是%.2f'%(3.6)
# print(number1)

#补齐到10位,保留两位小数
# number1='您输入的数字是%10.2f'%(3.6)
# print(number1)

#方案二 .format
# str1='My name is {},Your name is {},age is {}.'.format('Clark','Ralf',23)
# print(str1)
#前面的占位符比后面的参数多会报错
# str1='My name is {},Your name is {},age is {}.'.format('Clark','Ralf')
# print(str1)

#前面的占位符比后面的参数少则不报错
# str1='My name is {},Your name is {}.'.format('Clark','Ralf',23)
# print(str1)

#补齐 {:n},不足n位,则补空格.字符串默认左对齐,空格在右侧,数字默认右对齐,空格在左侧
# str1='My name is {:10},Your name is {:10},age is {:10}.'.format('Clark','Ralf',23)
# print(str1)
#可以改变默认的对齐方式  > 右对齐 < 左对齐  ^ 居中对齐
# str1='My name is {:>10},Your name is {:^10},age is {:<10}.'.format('Clark','Ralf',23)
# print(str1)

#数字补0
# str1='My name is {:>10},Your name is {:^10},age is {:>010}.'.format('Clark','Ralf',23)
# print(str1)

#方案二中,除了可以使用顺序取值法,也可以使用下标取值法
# str1='My name is {2},Your name is {1},age is {0}.'.format('Clark','Ralf',23)
# print(str1)

#顺序取值法与下标取值法不能混用
# str1='My name is {1},Your name is {1},age is {1}.'.format('Clark','Ralf',23)
# print(str1)
#在python3.6以后的版本中,可以使用f'字符串'的写法
x='天乐'
y='青云'
str2=f'My name is {x:>10},Your name is {y}'
print(str2)

#课堂小结
#格式化字符串,方案一
#1补齐 2对齐 3前后参数个数要保持一致
#方案二
#1补齐 2对齐 3前面的参数个数要小于等于后面的 4顺序取值法与下标取值法 5顺序取值与下标取值不可以混用
#方案二的新写法 f'字符串'
```