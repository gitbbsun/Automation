# coding=utf-8
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from MyProjects.common import log
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://pre.svocloud.com")

try:
    assert u"云视频" in driver.title
    log.log_message().info_log("Assertion test pass.")
except Exception as e:
    log.log_message().error_log("Assertion test fail.")

driver.close()
