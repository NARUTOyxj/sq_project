from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('https://music.163.com/#/discover/toplist?id=3779629')
# 点击弹出窗广告
close_btn = driver.find_element_by_id('_qianqian_pop_cloasebtn')
# 如果弹出框存在就点击
if close_btn:
    close_btn[0].click()
ele = driver.find_element_by_id('song-list-pre-cache')
song_items = ele.find_elements_by_class_name('m-table m-table-rank')
# driver.implicitly_wait(0.5)
for item in song_items:  # 查找新歌榜所有歌曲
    # up = item.find_elements_by_class_name('up')  # 查找新歌榜
    # 取i元素的属性
    # i = item.find_element_by_class_name('status').find_element_by_tag_name('i').get_attribute('class')
    i = item.find_element_by_css_selector('.status i')
    # 判断属性是否是up
    if i == 'up':
        song_title = item.find_element_by_class_name('song-title').text  # 查找歌曲名称元素
        singer = item.find_element_by_class_name('singer').text  # 查找歌手元素
    print(f'{song_title}--------------{singer}')
driver.implicitly_wait(10)
driver.quit()
