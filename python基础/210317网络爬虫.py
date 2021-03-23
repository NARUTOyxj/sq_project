import re
import requests
url = 'https://www.xs4.cc/chapter/?870.html'
req = requests.get(url)
req.encoding = 'gbk'  # 将编码转为gbk格式
book_name = re.findall('<h1>(.*?)</h1>',req.text)[0]  # 取得书名
mulu = re.findall('title="(第.*?)">第',req.text)  # 取得所有章节的目录
# for i in range(1,len(mulu)):
#     print(mulu[i])

wangzhi = re.findall('<a href="article(.*?).html"',req.text)  # 取得所有章节的正文网址
# for i in range(1,len(wangzhi)):
#     print(f'https://www.xs4.cc/article{wangzhi[i]}.html')

dict1 = {}
for i in range(1, len(mulu)):
    dict1[mulu[i]] = f'https://www.xs4.cc/article{wangzhi[i]}.html'
for k,v in dict1.items():
    print(k, v)



