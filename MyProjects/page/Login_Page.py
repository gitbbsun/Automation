import yaml, os, time
from MyProjects.common.util import set_log

path = os.getcwd().split('cases')[0]  # 获取当前目录


class Login_test():
    def __init__(self, driver):
        self.driver = driver
        self.file = open(path + "\\data\\page_data.yaml", "r", encoding="utf-8")
        self.page_data = yaml.load(self.file)
        self.file.close()
        self.login_url = self.page_data['login'].get('url')
        self.login_title = self.page_data['login'].get('login_title')
        self.user_name = self.page_data['login'].get('username')
        self.pwd = self.page_data['login'].get('password')
        self.login_btn = self.page_data['login'].get('login_btn')
        self.error = self.page_data['login'].get('login_err')
        self.driver.get(self.login_url)

    def login(self, username, pwd):
        try:
            self.driver.find_element_by_xpath(self.user_name).clear()
            self.driver.find_element_by_xpath(self.user_name).send_keys(username)
            self.driver.find_element_by_xpath(self.pwd).click()
            self.driver.find_element_by_xpath(self.pwd).send_keys(pwd)
            time.sleep(3)
            self.driver.find_element_by_xpath(self.login_btn).click()
            return self.driver.find_element_by_xpath(self.error).text
        except BaseException as e:
            set_log(e)
