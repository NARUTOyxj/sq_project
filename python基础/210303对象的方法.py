```python
#210303_对象的方法
#方法其实就是函数，只不过是写在类当中的
# str1='abcdefg'
# print(str1.find('c'))  #返回某个字符在字符串中的下标，找不到时返回-1
# print(str1.index('c'))  #返回某个字符在字符串中的下标，找不到时抛异常

#strip()方法，去掉字符串前后的空格或者其他指定字符
str2='       a  b    c            '
# print(str2.strip())
# str2_new='****************a  b    c****************'
# print(str2_new.strip('*'))
# print(str2.replace(' ',''))  #参数１，需要替换的字符，参数２，替换为什么字符

#starswith()  判断字符串是否以某个字符开头
#判断某个身份证是否时南京的身份证
# id_card='32010419980908070X'
# if id_card.startswith('3201'):
#     print('南京的身份证')
# else:
#     print('不是南京的身份证')
# #判断身份证的最后一位是不是X
# if id_card.endswith('X') or id_card.endswith('x'):
#     print('最后一位是X')
# else:
#     print('最后一位不是X')

#split(),切割字符串，它需要一个参数，作为切割符,将字符串切割为多个值。split()的返回值是列表
# 'abcdefg' 以ef作为切割符，['abcd','g']  #切割之后，切割符本身会消失
# str6='abcdefg'
# print(str6.split('ef'))
# str9='abcabcabcabcabcabc'
# print(str9.split('c'))

# 写一个号段筛选程序,需求如下:
# 用户从控制台输入一个手机号，判断出运营商(移动（假设号段是130-150）、
# 联通（假设是151-170）、电信（假设是171-199）),如果用户输入的位数不对，提示用户位数有误;
# 如果用户输入非数字，提示有非法字符
input1=input('请输入一个手机号：')
if not input1.isdigit():  #isdigit(),判断字符串是否是由纯数字组成，isalpha(),判断是否纯字母
    print('您输入的不是数字')
else:
    if len(input1)!=11:
        print('位数不正确，请输入11位手机号')
    else:
        num1=int(input1[0:3])  #取得输入值的前三位，并转为int型
        if 130<=num1<=150:
            print('您输入的是移动手机号')
        elif 150<num1<=170:
            print('您输入的是联通手机号')
        elif 170<num1<=199:
            print('您输入的是电信手机号')
        else:
            print('您输入的手机号不属于任何运营商')
```