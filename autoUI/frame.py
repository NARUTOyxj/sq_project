from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
# 访问排行榜
driver.get('https://music.163.com/#/discover/toplist?id=3779629')

# 切到frame里面
driver.switch_to.frame(0)  # 可以通过frame的id, name和索引查找
# driver.switch_to.default_content()   # 切到最外层frame
driver.switch_to.parent_frame()  # 切到上一层frame

# 抓取元素信息
ele = driver.find_element_by_id('song-list-pre-cache')
print(ele)

driver.quit()
