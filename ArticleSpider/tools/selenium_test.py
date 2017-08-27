from selenium import webdriver
import time

from selenium import webdriver
import time

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("permissions.default.stylesheet", 2)  # 禁用样式表文件
firefox_profile.set_preference("permissions.default.image", 2)  # 不加载图片
firefox_profile.set_preference("javascript.enabled", False)  # 禁止JS
firefox_profile.update_preferences()  # 更新设置
firefox = webdriver.Firefox(firefox_profile, executable_path="/Users/yons/webdriver/geckodriver")

url = 'https://www.zhihu.com'
print("开始加载")
t_start = time.time()
firefox.get(url)
t_end = time.time()
print("加载时间是：", t_end - t_start)
time.sleep(10)
firefox.quit()




#
# 模拟登陆微博
# browser.get("http://www.weibo.com/")
#
# # 等待10秒，等待页面全部加载完成
# time.sleep(10)
#
# browser.find_element_by_css_selector("#loginname").send_keys("13419516267")
# browser.find_element_by_css_selector(".info_list.password input[name='password']").clear().send_keys("ssjusher123")
# browser.find_element_by_css_selector(".info_list.login_btn a[node-type='submitBtn']").clear().click()

# 模拟鼠标下拉
# browser.get("https://www.oschina.net/blog")
# time.sleep(5)
# for i in range(3):
#     # 执行js代码模拟下拉动作
#     browser.execute_script(
#         "window.scrollTo(0, document.body.scrollHeight); var lenofPage=document.body.scrollHeight; return lenofPage")
#     time.sleep(3)
#
# browser.quit()
