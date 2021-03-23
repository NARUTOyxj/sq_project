import re
import requests
url = 'http://book.zongheng.com/showchapter/954217.html'
req = requests.get(url)
req.encoding = 'utf-8'  # 将编码转为gbk格式
book_name = re.findall('<h1>(.*?)</h1>',req.text)[0]  # 取得书名
print(book_name)
mulu = re.findall('title="(.*?)字数',req.text)  # 取得所有章节的目录
print(len(mulu))
# for i in range(1,len(mulu)):
#     print(mulu[i])
#
# wangzhi = re.findall('href="(.*?)" target=',req.text)  # 取得所有章节的正文网址
wangzhi = re.findall('/954217/(.*?).html',req.text)
print(len(wangzhi))
# for i in range(1,len(wangzhi)):
#     print(f'http://book.zongheng.com/chapter/954217/{wangzhi[i]}.html')

# dict1 = {}
# for i in range(1, len(mulu)):
#     dict1[mulu[i]] = f'https://www.xs4.cc/article{wangzhi[i]}.html'
# for k,v in dict1.items():
#     print(k, v)



