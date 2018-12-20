# coding=utf-8
import os, time, logging


class log_message():
    def __init__(self):
        '''
        1：指定保存日志文件路径
        2：日志级别
        3：将日志文件存到指定的文件中
        '''
        time_str = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        logname = time_str + "_autotest.log"

        parentdir_path = os.getcwd().split('cases')[0]  # 获取上级目录
        os.chdir(parentdir_path)  # 修改目录

        log_filedir = 'Log'
        if not os.path.isdir(log_filedir):
            os.mkdir('Log')
        file = os.path.join(parentdir_path + '\\Log', logname)
        # 1：创建日志级别：logging 有6个日志级别  NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL
        self.logger = logging.Logger("自动化测试")
        self.logger.setLevel(logging.INFO)  # 创建日志级别为INFO，那么低于INFO级别的日志都会被忽略

        # 2：创建文件handler，用于写入日志文件并设置文件日志级别
        self.logfile = logging.FileHandler(file)
        self.logfile.setLevel(logging.INFO)

        # 3：创建控制端输出handler，用于输出到控制端并设置输出日志级别
        self.control = logging.StreamHandler()
        self.control.setLevel(logging.INFO)  # cmd窗口显示

        # 在控制端handler添加过滤器，将含有chat或者gui的handler信息输出
        filter = logging.Filter("hello")
        self.control.addFilter(filter)

        self.formater = logging.Formatter('%(asctime)s - %(filename)s - [line:%(lineno)d] - %(levelname)s - %(message)s')

        self.logfile.setFormatter(self.formater)
        self.control.setFormatter(self.formater)

        self.logger.addHandler(self.logfile)
        self.logger.addHandler(self.control)

    def debug_log(self, message):
        self.logger.debug(message)

    def info_log(self, message):
        self.logger.info(message)

    def warning_log(self, message):
        self.logger.warning(message)

    def error_log(self, message):
        self.logger.error(message)
