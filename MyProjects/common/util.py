import xlrd

from MyProjects.common import log

logs = log.log_message()


def get_case_data(filepath, index):
    try:
        file = xlrd.open_workbook(filepath)
        case_data = file.sheets()[index]
        nrows = case_data.nrows
        list_data = []
        for i in range(1, nrows):
            dict_param = {}
            dict_param['id'] = case_data.cell(i, 0).value
            dict_param.update(eval(case_data.cell(i, 2).value))
            dict_param.update(eval(case_data.cell(i, 3).value))
            list_data.append(dict_param)
        return list_data
    except Exception as e:
        logs.error_log(e)
