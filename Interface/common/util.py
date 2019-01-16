#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 17:01
# @Author  : bbsun
# @File    : util.py
# @Software: PyCharm


def getSize(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


def swipeLeft(driver):
    l = getSize(driver=driver)
    x1 = int(l[0] * 0.9)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.1)
    driver.swipe(x1, y1, x2, y1)
