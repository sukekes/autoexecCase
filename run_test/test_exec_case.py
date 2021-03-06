# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 17:06
# @Author  : suk
# @FileName: test_exec_case.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/
import pytest
from selenium import webdriver
from testcase.execcase.exec_case import exec_case


@pytest.mark.tasks
def test_exec_case():
    driver = webdriver.Chrome()
    anticipation = exec_case(driver, "execc", "execc")
    assert anticipation
    driver.quit()

