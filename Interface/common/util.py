#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 17:01
# @Author  : bbsun
# @File    : util.py
# @Software: PyCharm

import json, xlrd, request
import openpyxl
from openpyxl import load_workbook


def send_requests(s, testdata):
    method = testdata["method"]
    url = testdata["url"]
    # url后面的参数
    try:
        params = eval(testdata["params"])
    except:
        params = None
    try:
        # 头部信息
        headers = eval(testdata["headers"])
        print(f"打印头部信息:{headers}")
    except:
        headers = None
    # post请求body类型
    type = testdata["type"]
    test_num = testdata["id"]
    print(f"正在执行的用例:{test_num},请求方式：{method},请求url：{url},请求参数：{params}")
    # 判断body内容
    try:
        bodydata = eval(testdata["body"])
    except:
        bodydata = {}
    # 判断传的data数据还是json
    if type == "data":
        body = bodydata
    else:
        body = json.dumps(bodydata)
    verify = False
    res = {}
    if method == "post":
        try:
            r = s.request(method=method,
                          url=url,
                          params=params,
                          headers=headers,
                          data=body,
                          verify=verify)
            res['id'] = testdata['id']
            res['rowNum'] = testdata['rowNum']
            res['statuscode'] = str(r.status_code)
            res['text'] = r.content.decode("utf-8")
            res["times"] = str(r.elapsed.total_seconds())
            if res["statuscode"] != "200":
                res["error"] = res["text"]
            else:
                res["error"] = ""
            res["msg"] = ""
            if testdata["checkpoint"] in res["text"]:
                res["result"] = "pass"
            else:
                res["result"] = "fail"
            return res
        except Exception as msg:
            res["msg"] = str(msg)
            return res


# xlrd读取excel测试数据，返回字典格式
class ExcelUtil():
    def __init__(self, excelPath, sheetName="Sheet1"):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为总行数
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("无数据")
        else:
            r = []
            j = 1
            for i in list(range(self.rowNum - 1)):
                s = {}
                # 从第二行获取对应values的值
                # s["rowNum"] = i + 2
                values = self.table.row_values(j)
                for x in list(range(self.colNum)):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
                print(f"打印excel数据:{r}")
            return r


def copy_excel(data_path, report_path):
    report = openpyxl.Workbook()
    report.save(report_path)
    # 读取数据
    data = openpyxl.load_workbook(data_path)
    report = openpyxl.load_workbook(report_path)
    sheets1 = data.sheetnames
    sheets2 = report.sheetnames
    sheet1 = data[sheets1[0]]
    sheet2 = report[sheets2[0]]
    max_row = sheet1.max_row
    max_column = sheet1.max_column
    for m in list(range(1, max_row + 1)):
        for n in list(range(97, 97 + max_column)):  # chr(97)=='a'
            n = chr(n)
            i = f"{n}{m}"  # 单元格编号
            cell1 = sheet1[i].value  # 获取data单元格数据
            sheet2[i].value = cell1  # 赋值到test单元格
    report.save(report_path)
    data.close()
    report.close()


class Write_excel(object):
    def __init__(self, filename):
        self.filename = filename
        self.wb = load_workbook(self.filename)
        self.ws = self.wb.active  # 激活sheet

    def write(self, row_n, col_m, value):
        self.ws.cell(row_n, col_m).value = value
        self.wb.save(self.filename)
