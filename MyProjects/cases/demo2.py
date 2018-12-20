#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 10:50
# @Author  : bbsun
# @File    : demo2.py
# @Software: PyCharm

import unittest
from selenium import webdriver

class Test_Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()



    def test_login1(self):
        """1：正确用户名、密码，登录成功"""
        self.driver.get("https://pre.svocloud.com")

    def tearDown(self):
        self.driver.quit()