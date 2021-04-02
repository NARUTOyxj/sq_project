import requests

# HOST = 'HTTP://120.55.190.222:7080'  # 前端访问路径 http://120.55.190.222:7080/mgr/login/login.html
#
#
# def login():
#     url = f'{HOST}/api/mgr/loginReq'
#     payload = {"username":"auto", "password":"sdfsdfsdf"}  # 请求体
#     resp = requests.post(url,data=payload)
#     return resp.text
#
# if __name__ == '__main__':
#     res = login()
#     print(res)

# 关联接口,需要关联的接口
# 方案一：
# def add_lesson(userCookie):
#     url = f'{HOST}/api/mgr/sq_mgr'
#     resp = requests.post(url,cookies = userCookie)  # 不需要关注data，不做校验，只用来练习的
#     # 可以把cookies封装到请求头 headers
#     # resp = requests.post(url, headers = {"cookie"}userCookie) # 需要拆开再组合，使用上面一种方法比较好
#     print(resp.request.headers)  # 查看请求头的cookies

# https协议
HOST = 'https://120.55.190.222'
# 屏蔽https警告
requests.packages.urllib3.disable_warnings()


def login():
    url = f'{HOST}/api/mgr/loginReq'
    payload = {'username':'auto','password':'sdfsdfsdf'}
    resp = requests.post(url,data=payload,verify = False)
    return resp.text


if __name__ == '__main__':
    res = login()
    print(res)
