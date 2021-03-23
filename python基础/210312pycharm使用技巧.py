#210312_pycharm使用技巧
#settings→editor→file and code template,选择python script
#${NAME}  文件名
#${DATE}  日期

#自动补齐
# if __name__ == '__main__':  #先输入main,然后按tab键

#自动补齐一个自定义的段落
#settings→editror→live templates,在右侧点击+号,就可以新增自定义的内容
#完成之后,在下方要勾选python

#修改注释的颜色
#settings→editor→color scheme→python
#line comments

#修改函数的颜色
#settings→editor→color scheme→python

#取消语法检查,或者降低语法检查的级别
#第一种,点击右下角的小侦探图标
#inspection是最高级别检查, 回对语法和拼写规范等都进行检查
#syntax是中等级别,只检查语法错误
#None 不进行任何检查
#第二种,如果右下角没有小侦探图标,则修改以下选项
#settings→editro→inspections,选择python,去掉勾选


#设置分屏
#settings→keymap,查询split关键字,找到分屏的图标,设置快捷键

# 常见的快捷键
# 先输入main,然后ctrl+J,然后回车
# 快速换行
# shift+回车
# 快速注释
# ctrl+/ 按一次注释,再按一次取消注释
#快速缩进
#tab 按一次缩进,默认为4个空格的距离,再按一次再次缩进,shift+tab 取消缩进

#切换编码,当遇到乱码时可以通过切换编码来解决乱码的问题
#settings→editor→file encodings

#冒泡算法,给列表排序的算法
# list1=[23,-1,6,92,128,-99,50,36]
# list1.sort()  #对列表进行永久排序,这个方法只排序,没有返回值
# list1.sort(reverse=True)  #排序且倒序
# print(list1)
# print(sorted(list1))  #临时排序,返回值是排序后的结果
# print(sorted(list1,reverse=True))  #临时排序,且倒序
# print(list1[::-1])  #只翻转不排序
# str1='山西悬空寺空悬西山'
# print(str1[::-1])

#冒泡算法
# 4,3,2,1,5 每一轮比较n-1次,一共需要比较n-1轮,从第二轮开始,每一轮都可以额外少比一次
list2=[23,-1,6,92,128,-99,50,36]
for i in range(len(list2)-1):  #外层循环,控制比较的轮次数
    for j in range(len(list2)-1-i):  #内层循环,控制每轮比几次
        if list2[j]>list2[j+1]:  #如果前面的数比后面的数大
            # print(f'第{j}位和第{j+1}位的顺序不对')
            # print(f'变化之前------------------->{list2}')
            list2[j],list2[j+1]=list2[j+1],list2[j]  #两数互换
            # print(f'变化之后------------------->{list2}')
    # print(f'----------------第{i+1}轮循环结束')
print(list2)
