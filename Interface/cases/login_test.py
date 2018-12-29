import unittest
from Interface.common import util

if __name__ == '__main__':
    filepath = "data.xlsx"
    data = util.ExcelUtil(filepath)
    print(data.dict_data())

    util.copy_excel("data.xlsx", "testreport.xlsx")
    wt = util.Write_excel("testreport.xlsx")
    wt.write(4, 5, "hello")
    wt.write(4, 6, "hello")
