import pytest
@pytest.fixture(scope='class')  #装饰器,相当于setup_method
# 缺省级别为function级,可以使用scope='class'更改级别
#scope='module'
#scope='session' 选择这个级别时,将fixture的内容写到conftest.py中,目录下的所有文件共用这个配置
def some_data():
    print('开始')
    yield  #这句话以下的内容,视为teardown_method
    print('结束')
def test_some_data(some_data):
    print('test')
if __name__ == '__main__':
    pytest.main(['test_example1.py','-s'])

#将九九乘法表写入文件
with open ('d:/九九乘法表_210319.txt','w+') as file1:
    for i in range(1,10):
        for j in range(1,i+1):
            file1.write(f'{j}*{i}={i*j}\t')
        file1.write('\n')
