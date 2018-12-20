from MyProjects.common import util
from MyProjects.page.Login_Page import *
from selenium import webdriver
import unittest
import os

path = os.getcwd()
case_path = path + '\\data\\case.xlsx'
case_datas = util.get_case_data(case_path, 0)


# TODO 1 截图将浏览器console中内容截图下来
# TODO  log 所有用例一个log
# TODO 优化代码   元素定位
# TODO ddt读取数据修改

class Test_Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.login_fun = Login_test(self.driver)

    def login_verify(self, name, pwd, assert_value):
        self.re_data = self.login_fun.login(name, pwd)
        if (self.re_data == "账号或密码有误"):
            log_message().error_log("账号或密码有误")
        else:
            self.re_data = "登录成功"
            log_message().error_log("登录成功")
        self.driver.get_screenshot_as_file(path + '\\resultpang\\%s.png' % self.name)
        self.assertEqual(self.re_data, assert_value)

    def test_loginA(self):
        """1：正确用户名、密码，登录成功"""
        self.name = case_datas[0]['username']
        self.pwd = case_datas[0]['pwd']
        self.assert_value = case_datas[0]['assert']
        self.login_verify(self.name, self.pwd, self.assert_value)

    def test_loginB(self):
        """2：错误用户名，正确密码，登录失败"""
        self.name = case_datas[1]['username']
        self.pwd = case_datas[1]['pwd']
        self.assert_value = case_datas[1]['assert']
        self.login_verify(self.name, self.pwd, self.assert_value)

    def test_loginC(self):
        """3：正确用户名，错误密码，登录失败"""
        self.name = case_datas[2]['username']
        self.pwd = case_datas[2]['pwd']
        self.assert_value = case_datas[2]['assert']
        self.login_verify(self.name, self.pwd, self.assert_value)

    def tearDown(self):
        self.driver.quit()
