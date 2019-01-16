import time

from appium import webdriver

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
