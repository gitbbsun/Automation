from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib, os, logging, xlrd
from email.header import Header


# 写入日志
def set_log(str):
    logger = logging.getLogger("UI_test")

    if not logger.handlers:
        # 1：创建日志级别：logging 有6个日志级别  NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL
        # 创建日志级别为INFO，那么低于INFO级别的日志都会被忽略
        logger.setLevel(logging.INFO)
        path = os.getcwd().split('cases')[0] + "\\Log\\UI_autotest.log"

        # 2：创建文件handler，用于写入日志文件并设置文件日志级别
        fh = logging.FileHandler(path)
        fh.setLevel(logging.INFO)

        # 3：创建控制端输出handler，用于输出到控制端并设置输出日志级别
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 4：在控制端handler添加过滤器，将含有chat或者gui的handler信息输出    或者在日志文件添加过滤器
        filter = logging.Filter("hello")
        ch.addFilter(filter)

        formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d]-%(funcName)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)
    logger.info(str)


# 获取excel用例数据
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
            dict_param.update(eval(case_data.cell(i, 4).value))
            dict_param.update(eval(case_data.cell(i, 5).value))
            list_data.append(dict_param)
        return list_data
    except Exception as e:
        set_log(e)


# 发送测试报告
def send_email(newfile):
    # 打开文件
    f = open(newfile, 'rb')
    # 读取文件内容
    mail_body = f.read()
    # 调试使用
    #    print u'打印'
    #    print mail_body
    # 关闭文件
    f.close()

    # 发送邮箱服务器
    smtpserver = 'smtp.qq.com'
    # 发送邮箱用户名/密码
    user = '1250878171@qq.com'
    password = 'nnqwdkmbdiuabaff'
    # 发送邮箱
    sender = '1250878171@qq.com'
    # 多个接收邮箱，单个收件人的话，直接是receiver='XXX@126.com'
    receiver = ['sunbb@svocloud.com', '1979857657@qq.com']
    # receiver = ['sunbb@svocloud.com', 'goujb@svocloud.com','lixy@svocloud.com','gaojing@svocloud.com','houwj@svocloud.com']
    # 发送邮件主题
    subject = '自动化测试报告'

    # 编写 HTML类型的邮件正文
    # MIMEText这个效果和下方用MIMEMultipart效果是一致的，已通过。
    #    msg = MIMEText(mail_body,'html','utf-8')

    msg = MIMEMultipart('mixed')

    # 注意：由于msg_html在msg_plain后面，所以msg_html以附件的形式出现
    #    text = "Dear all!\nThe attachment is new testreport.\nPlease check it."
    # 中文测试ok
    #    text = "Dear all!\n附件是最新的测试报告。\n麻烦下载下来看，用火狐浏览器打开查看。\n请知悉，谢谢。"
    #    msg_plain = MIMEText(text,'plain', 'utf-8')
    #    msg.attach(msg_plain)

    msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msg_html1)

    msg_html = MIMEText(mail_body, 'html', 'utf-8')
    msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    msg.attach(msg_html)

    # 以附件的方式发送：但是会报554，倍163退信。--此路不通。
    #    msg_html = MIMEText(mail_body,'base64','utf-8')
    #    msg_html["Content-Type"] = 'application/octet-stream'
    #    msg_html.add_header('Content-Disposition', 'attachment', filename='testreport.html')
    #    msg.attach(msg_html)

    # 要加上msg['From']这句话，否则会报554的错误。
    # 要在163有限设置授权码（即客户端的密码），否则会报535
    msg['From'] = '1250878171@qq.com <1250878171@qq.com>'
    #    msg['To'] = 'XXX@doov.com.cn'
    # 多个收件人
    msg['To'] = ";".join(receiver)
    msg['Subject'] = Header(subject, 'utf-8')

    # 连接发送邮件
    smtp = smtplib.SMTP_SSL("SMTP.qq.com", 465)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
