from selenium import webdriver
import time
import pprint
driver = webdriver.Chrome()
# driver.implicitly_wait(10)  # 隐式等待最大10s,全局设置

driver.get('https://www.baidu.com/')
ele = driver.find_element_by_id('kw')
ele.send_keys('chromedriver')
btn = driver.find_element_by_id('su')
btn.click()

# 等加载网页
time.sleep(1)
# 获取搜索页第一个结果
res = driver.find_element_by_id('1')

# 通过父元素找子元素
h3 = res.find_element_by_tag_name('h3')

if 'ChromeDriver Mirror' in h3.text:
    print('pass')
    print(h3.text)
else:
    print('fail')
    print(h3.text)

# 耗时操作，需要30s
driver.implicitly_wait(30)
# 耗时操作

# 改回原来的隐式等待时间
driver.implicitly_wait(10)
# 退出浏览器
driver.quit()
