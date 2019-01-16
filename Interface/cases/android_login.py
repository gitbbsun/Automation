import time

from appium import webdriver


#TODO 查看demo
#TODO 断言添加
#TODO 编写登录、注册、发起会议、加入会议功能脚本
#TODO 查看appium文档 了解appium、selenium的底层关系
#TODO 学习monkey、monkeyrunner工具

#TODO 移动端自动化脚本框架


desired_caps = {}
desired_caps['platformName'] = "Android"
desired_caps['platformVersion'] = "5.1"
desired_caps['deviceName'] = "CYSBBBE752606037"
desired_caps['unid'] = "CYSBBBE752606037"
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# desired_caps['platformVersion'] = "8.0.0"
# desired_caps['deviceName'] = "KWG5T16405002250"
desired_caps['appPackage'] = "com.svocloud.vcs"
desired_caps['appActivity'] = ".modules.other.SplashActivity"
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(5)

# 登录

driver.find_element_by_id("com.svocloud.vcs:id/btn_login").click()

driver.find_element_by_id("com.svocloud.vcs:id/activity_login_etPhone").clear()

driver.find_element_by_id("com.svocloud.vcs:id/activity_login_etPhone").send_keys("sunbb@svocloud.com")

driver.find_element_by_id("com.svocloud.vcs:id/activity_login_etPwd").clear()

driver.find_element_by_id("com.svocloud.vcs:id/activity_login_etPwd").send_keys("123456")

driver.find_element_by_id("com.svocloud.vcs:id/btn_login").clear()

time.sleep(5)
