import re    # 加载正则表达式
# re.findall(参数1，参数2)    # 参数1表示用什么规则进行提取，参数2表示从哪个字符串进行提取
# 参数3 一般有re.I  表示不区分大小写，re.S  匹配多行中，符合条件的值
# str1 = 'abcdeafg'

# . 通配符，匹配某个字符前面或后面一个字符
# print(re.findall('a.',str1))  # 提取a后面的一个字符,返回值是列表，包括条件a也返回
# print(re.findall('a(.)',str1))  # 提提取a后面的一个字符,返回值是列表，不包括条件a

# *  通配符，匹配某个字符后面的若干个字符，若干也包括0个的情况
# str1_1 = 'abcdabeafg'
# print(re.findall('ab*', str1_1))  # a后面有若干个b的字符找出来，包括0个b的情况

# ? 通配符，匹配某个字符串后面的0-1个字符
# str1_2 = 'abacabbbbbd'
# print(re.findall('ab?', str1_2))

# + 通配符，匹配某个字符串后面有一个或多个字符，不包括0个的情况
# print(re.findall('ab+', str1_2))

# .*?  提取字符串两端之间的内容   A(.*?)B
load1 = '一二三四五六七八九'
# print(re.findall('三(.*?)六',load1))

# 如果只有一段给出了条件，值会怎么取？
# print(re.findall('三(.*?)',load1))  # 懒惰匹配，在符合查询要求的情况下，尽可能少的匹配
# print(re.findall('(.*?)六',load1))  # 需要匹配的字符串后面是’六‘，无法偷懒

# 只给出一端的条件时，如果希望获取后面全部的结果，则应当使用贪婪匹配
# print(re.findall('三(.*)',load1))  # 贪婪匹配

# 当有多个满足条件的值时，两者的结果并不相同
load1 = '一二六三四五六三七八九六'
# print(re.findall('三(.*?)六',load1))  # 懒惰匹配
# print(re.findall('三(.*)六',load1))  # 贪婪匹配

# 如果没有满足条件的查询，返回空列表
# print(re.findall('九(.*?)一',load1))  # 懒惰匹配
# print(re.findall('九(.*)一',load1))  # 贪婪匹配

# \w{n}  匹配字母，数字，下划线,n表示连续满足条件的位数
# str3 = 'as&deg'
# print(re.findall('\w{3}',str3))

# \W  匹配\w的补集
# str3_new = 'as&#$deg'
# print(re.findall('\W{3}',str3_new))

# \s  匹配空格，换行符\n，制表符\t
# str6 = '''床前明月光，
# 疑是地上   霜。
# 举头望明   月，
# 低头思故   乡。
# '''
# print(re.findall('\s',str6))

# \S  \s的补集
# print(re.findall('\S',str6))

# ^匹配开头，$匹配结尾
# list1 = ['abcde','deabc','fabcf']
# for one in list1:
#     if re.findall('^abc',one):  # 匹配以abc开头的字符串
#         print(one, '以abc开头')
#     elif re.findall('abc$',one):  # 匹配以abc结尾的字符串
#         print(one, '以abc结尾')

# re.I  不区分大小写
# req = 'AbcabcABcaBCabCABC'
# print(re.findall('abc',req,re.I))

# re.S  匹配多行中，符合条件的值
# req2 = '''helloadfjhksdalds
# ,imujsdhfsla
# 68,jkfhdsfak,afsworld'''
# print(re.findall('hello(.*?)world',req2,re.S))
# print(re.findall('(.*?)world',req2))  # 匹配最后一行

# 课堂小结
# 正则表达式通配符 . * ? +
# 加()和不加()的区别
# .*? 懒惰匹配   .* 贪婪匹配

