import requests
import hashlib

from configs.config import HOST
# 加密方式：规则加密（md65, base64 aes）,自定义加密（开发自定义--跟开发确认规则）


def get_md5(psw):
    md5 = hashlib.md5()
    md5.update(psw.encode('utf-8'))
    return md5.hexdigest()


class Login:
    def login(self,indata,getToken = False):
        # 1- url
        url = f'{HOST}/account/sLogin'
        # 2- 参数
        indata['password'] = get_md5(indata['password'])
        payload = indata
        # 3- 发请求
        resp = requests.post(url, data=payload)

        #---------------------------------------------------------
        # 打印url
        # print('登录接口的请求url>>>', resp.request.url)
        # # 打印请求体
        # print('登录接口的请求体>>>',resp.request.body)
        # # 在接口的关联，一般的鉴权token，封装在headers(headers数据格式，一般是字典格式)
        # # 打印请求头
        # print('登录接口的请求头>>>', resp.request.headers)
        # # 响应头
        # print('登录接口的响应头>>>', resp.headers)
        # '''
        # data:默认表单格式
        # json:默认json格式
        # params:参数放到url?后面的
        # files:文件上传接口
        #
        # 在pycharm的控制台输出时，
        # 字典一定是单引号，json是双引号
        # '''
        #----------------------------------------------------------

        # 4- 查看响应结果
        # print(resp.text)  # 返回是json格式，是字符串
        # print(resp.json())  # 返回是字典

        '''
        接口问题解决思路：
        
        '''
        if getToken:
            return resp.json()['data']['token']
        else:
            return resp.json()  # 返回是字典---------前提是这个响应体必须是json格式


if __name__ == '__main__':
    res = Login().login({'username':'th0379','password':'sq123456'},getToken=True)
    print(res)


