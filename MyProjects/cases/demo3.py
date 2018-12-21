#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 10:51
# @Author  : bbsun
# @File    : demo3.py
# @Software: PyCharm
import unittest

from ddt import ddt, data
from MyProjects.common import util
from MyProjects.page.Login_Page import *
from selenium import webdriver
import unittest, os

path = os.getcwd().split('cases')[0]
case_path = path + '\\data\\case.xlsx'
case_datas = util.get_case_data(case_path, 0)


class Test_Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://pre.svocloud.com")


    def test_login1(self):
        """1：正确用户名、密码，登录成功"""
        self.driver.find_element_by_xpath("//input[@type='text']").clear()
        self.driver.find_element_by_xpath("//input[@type='text']").send_keys("12508781@qq.com")
        self.driver.find_element_by_xpath("//input[@type='password']").click()
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys("1112333")
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(3)

        self.driver.get_screenshot_as_file(path + '\\resultpang\\测试.png')
        self.driver.quit()

    # def tearDown(self):
    #     self.driver.quit()
