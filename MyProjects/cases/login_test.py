from MyProjects.common import util
from MyProjects.page.Login_Page import *
from selenium import webdriver
import unittest
import ddt
import os

path = os.getcwd()
case_path = path + '\\data\\case.xlsx'
case_datas = util.get_case_data(case_path, 0)


#TODO  log 所有用例一个log
#TODO 生成报告并且以邮件的形式发送
#TODO 优化代码

@ddt.ddt
class Test_Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.login_fun = Login_test(self.driver)

    def login_verify(self, name, pwd, assert_value):
        self.re_data = self.login_fun.login(name, pwd)
        self.driver.get_screenshot_as_file(path + '\\resultpang\\%s.png' % self.name)
        self.assertEqual(self.re_data, assert_value)

    @ddt.data(case_datas)
    def test_login1(self, case_datas):
        self.name = case_datas[0]['username']
        self.pwd = case_datas[0]['pwd']
        self.assert_value = case_datas[0]['assert']
        self.login_verify(self.name, self.pwd, self.assert_value)

    @ddt.data(case_datas)
    def test_login2(self, case_datas):
        self.name = case_datas[1]['username']
        self.pwd = case_datas[1]['pwd']
        self.assert_value = case_datas[1]['assert']
        self.login_verify(self.name, self.pwd, self.assert_value)

    @ddt.data(case_datas)
    def test_login3(self, case_datas):
        self.name = case_datas[2]['username']
        self.pwd = case_datas[2]['pwd']
        self.assert_value = case_datas[2]['assert']
        self.login_verify(self.name, self.pwd, self.assert_value)

    def tearDown(self):
        self.driver.quit()
