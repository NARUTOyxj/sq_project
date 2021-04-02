import requests

HOST = 'HTTP://120.55.190.222:7080'  # 前端访问路径 http://120.55.190.222:7080/mgr/login/login.html


def login():
    url = f'{HOST}/api/mgr/loginReq'
    payload = {"username":"auto", "password":"sdfsdfsdf"}  # 请求体
    resp = requests.post(url,data=payload)
    # 打印下相应里面的cookies—————原则上在响应头里面
    # print(resp.headers)  # 响应头，字典类型
    # 原生态的cookies
    print(resp.cookies)
    # 方案一：
    # return resp.cookies

    # 方案二：有时cookies需要测试人员二次封装，以前只有 sessionid ，项目接口需要增加另一个身份 token联合校验（先登录vip系统，获取到token后，再登录测试系统）
    return resp.cookies['sessionid']  # 返回cookie对象

# 关联接口,需要关联的接口
# 方案一：
# def add_lesson(userCookie):
#     url = f'{HOST}/api/mgr/sq_mgr'
#     resp = requests.post(url,cookies = userCookie)  # 不需要关注data，不做校验，只用来练习的
#     # 可以把cookies封装到请求头 headers
#     # resp = requests.post(url, headers = {"cookie"}userCookie) # 需要拆开再组合，使用上面一种方法比较好
#     print(resp.request.headers)  # 查看请求头的cookies


# 方案二：
def add_lesson(inData):
    url = f'{HOST}/api/mgr/sq_mgr'
    cookies_test = {"sessionid":inData,"token":"123456"}
    resp = requests.post(url,cookies = cookies_test)  # 不需要关注data，不做校验，只用来练习的
    # 可以把cookies封装到请求头 headers
    # resp = requests.post(url, headers = {"cookie"}userCookie) # 需要拆开再组合，使用上面一种方法比较好
    # print(resp.request.headers)  # 查看请求头的cookies


if __name__ == '__main__':
    res = login()
    print(res)
    add_lesson(res)