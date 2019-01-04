#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/30 17:35
# @Author  : bbsun
# @File    : study_os.py
# @Software: PyCharm

import os

# 检验权限模式
a = os.access("data.xlsx", os.F_OK)  # 测试path是否存在

b = os.access("data.xlsx", os.W_OK)  # 测试此文件是否可写

c = os.access("data.xlsx", os.X_OK)  # 测试文件是否可执行

# 修改路径

print(a)
print(b)
print(c)
