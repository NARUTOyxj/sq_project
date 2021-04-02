import requests
from libs.login import Login
import pprint
from configs.config import HOST


class Shop:
    # 不管什么接口，都需要登录
    def __init__(self,inToken):
        # 定义一个实例属性
        self.header = {"Authorization":inToken}

    # 列出商铺
    def shop_list(self,inData):
        url = f'{HOST}/shopping/myShop'
        payload = inData
        resp = requests.get(url,params=payload,headers = self.header)
        return resp.json()

    # 图片上传接口
    def file_upload(self, fileName, fileDir, fileType):
        url = f'{HOST}/file'
        # 封装请求数据
        # {'变量名1'：文件属性}---{'变量名1'：(文件名，文件对象，文件类型)}
        # 多个文件上传{'变量名1'：文件属性}---{'变量名1'：(文件名，文件对象，文件类型),'变量名2'：(文件名，文件对象，文件类型)}
        userFile = {'file':(fileName,open(fileDir,'rb'),fileType)}  # rb二进制形式打开文件
        res = requests.post(url, files=userFile, headers=self.header)
        return res.json()

    # 编辑店铺
    """
    注意事项：
        1- 用例里店铺的id是硬编码--需要动态关联shop_list
        2- 用例里店铺的图片信息是硬编码--需要动态关联file_upload
    """
    def shop_update(self,inData,shopID,imageInfo):
        url = f'{HOST}/shopping/updatemyshop'
        # 获取动态值--更新值
        inData['id'] = shopID
        inData['image_path'] = imageInfo
        inData['image'] = f'file/getImgStream?fileName={imageInfo}'
        resp = requests.post(url,data = inData,headers = self.header)
        return resp.json()


if __name__ == '__main__':
    #1- 登录获取token
    token = Login().login({'username':'th0379','password':'sq123456'},getToken=True)

    # 实例.实例方法
    shopObject = Shop(token) # 店铺实例

    # 2- 列出店铺接口调用--获取店铺id
    # 创建实例   实例= 类名()
    shopRes = shopObject.shop_list({"page":1,"limit":10})
    print(shopRes)
    shopId = shopRes['data']['records'][0]['id']
    print(shopId)

    # 3- 文件上传接口验证--获取图片信息
    fileRes = shopObject.file_upload('商铺图片.jpg','../data/商铺图片.jpg','image/png')
    print(fileRes)
    print(fileRes['data']['realFileName'])

    # 4- 更新店铺接口
    info = { "name": "星巴克新建店",
            "address": "上海市静安区秣陵路303号",
            "id": "3269",
            "Phone": "13176876632",
            "rating": "6.0",
            "recent_order_num":100,
            "category": "快餐便当/简餐",
            "description": "满30减5，满60减8",
            "image_path": "b8be9abc-a85f-4b5b-ab13-52f48538f96c.png",
            "image": "http://121.41.14.39:8082/file/getImgStream?fileName=b8be9abc-a85f-4b5b-ab13-52f48538f96c.png"}
    resUpdate = shopObject.shop_update(info,shopId,fileRes['data']['realFileName'])
    print(resUpdate)
    # pprint.pprint(res)





