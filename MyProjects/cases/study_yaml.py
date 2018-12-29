#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/26 16:19
# @Author  : bbsun
# @File    : study_yaml.py
# @Software: PyCharm


import yaml, os, unittest
from ddt import ddt, data

file_path = os.getcwd().split('cases')[0] + "data\\study_data.yaml"
file = open(file_path, "r", encoding="utf-8")

yaml_data = yaml.load(file)


class TestDdt1(unittest.TestCase):
    def setUp(self):
        print(1111)

    def test_ddt(self):
        print(12333)


