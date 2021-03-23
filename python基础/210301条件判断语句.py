#210301_条件判断语句
#顺序执行语句,条件判断语句,循环语句
#用户在控制台输入一个数字,如果大于等于90,则打印优秀,否则如果大于等于80,则打印不错,
#否则如果大于等于60,则打印及格,否则打印不及格
# number1=int(input('请输入一个数字:'))  #input()函数的返回值,是str型
# if number1>=90:  #注意,必须是数字才能和数字进行比较
#     print('优秀')
# elif number1>=80:  #注意,必须是数字才能和数字进行比较
#     print('不错')
# elif number1>=60:
#     print('及格')
# else:
#     print('不及格')

#复合条件判断
#如果一个人的年龄大于等于60岁,并且是男性,则打印老先生
age=80
gender='male'
# if age>=60 and gender=='male':
#     print('老先生')
if age>=60:
    if gender=='male':
        print('老先生')
