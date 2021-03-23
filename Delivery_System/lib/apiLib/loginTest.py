import requests
import hashlib

# md5加密


def get_md5(psw):
    md5 = hashlib.md5()  # 实例化对象
    md5.update(psw.encode('utf-8'))  # 加密操作
    return md5.hexdigest()


# print(get_md5('123456'))


def login(indata, getToken = True):
    url = 'http://121.41.14.39:8082/account/sLogin'  # 路径
    indata['password'] = get_md5(indata['password'])  # 参数
    payload = indata
    resp = requests.post(url, data=payload)
    # print(resp.text)  # 请求返回str类型
    # print(resp.headers)  # 响应头
    # 获取响应——是一个字典   resp.json()
    if getToken:
        return print(resp.json()['data']['token'])
    else:
        print(resp.json())
    # print(resp.json()['data']['token'])


login({'username': 'md0324', 'password': '36126'})


