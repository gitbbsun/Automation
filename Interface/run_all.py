#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 9:32
# @Author  : bbsun
# @File    : run_all.py
# @Software: PyCharm

import unittest, os, time, HTMLTestReportCN


def create_suite(path):
    test_cases = unittest.TestSuite()  # 测试用例存放套件

    discover = unittest.defaultTestLoader.discover(path, pattern='test*.py')  # 遍历所有的测试文件
    for test_suite in discover:
        for test_case in test_suite:
            test_cases.addTest(test_case)
    return test_cases  # 返回所有的cases


case_path = os.path.join(os.getcwd(), "cases")  # 查到case的路径
cases = create_suite(case_path)
now = time.strftime("%Y%m%d%H", time.localtime(time.time()))
filename = os.getcwd() + "\\report\\" + now + "_Intserface_TestReport.html"
fp = open(filename, 'wb')
runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title=u'UI测试报告', description=u'用例测试结果', tester='bbsun')
runner.run(cases)
fp.close()
