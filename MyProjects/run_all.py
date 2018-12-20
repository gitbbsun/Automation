#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 10:55
# @Author  : bbsun
# @File    : run_all.py
# @Software: PyCharm

import unittest, os, time
import HTMLTestReportCN
from MyProjects.common.util import send_email


def create_suite(case_dir):  # 生成测试套件
    test_cases = unittest.TestSuite()
    # 使用discover找出用例文件夹下test_开头的cases的所有用例
    discover = unittest.defaultTestLoader.discover(case_dir, pattern="*test.py",
                                                   top_level_dir=None)  # top_level_dir：测试模块的顶层目录，即测试用例不是放在多级目录下，设置为none
    # 使用for循环出suite,再循环出case
    for test_suite in discover:
        for test_case in test_suite:
            test_cases.addTests(test_case)
    return test_cases


case_path = os.path.join(os.getcwd(), "cases")  # 指明要自动查找的py文件所在文件夹路径
case = create_suite(case_dir=case_path)  # 找到cases文件夹下所有的cases

now = time.strftime("%Y%m%d%H", time.localtime(time.time()))
filename = os.getcwd() + "\\report\\" + now + "_UC_UI_TestReport.html"
fp = open(filename, 'wb')
runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title=u'UI测试报告', description=u'用例测试结果',tester='bbsun')
runner.run(case)
fp.close()
send_email(filename)
