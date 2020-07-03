# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 14:24
# @Author  : suk
# @FileName: exec_case.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/
from pages.basepage import BasePage
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ExecCase(BasePage):

    # 查询用例
    def query_case(self, loc_type, attr_name, caseNo):
        self.refresh()
        self.find_element(eval(loc_type), attr_name).clear()
        self.find_element(eval(loc_type), attr_name).send_keys(caseNo)
        self.find_element(eval(loc_type), attr_name).send_keys(Keys.ENTER)

    # 进入执行用例页面
    def enter_exec_page(self, loc_type, attr_name):
        # self.refresh()
        self.find_element(eval(loc_type), attr_name).click()

    # 执行用例
    def exec_case(self, loc_type, attr_name):
        self.find_element(eval(loc_type), attr_name).click()
        sleep(2)

    # 阻塞页面返回
    def back_from_block(self, loc_type, attr_name):
        self.refresh()
        self.find_element(eval(loc_type), attr_name).click()

    # 缺陷填报页面返回
    def back_from_issue(self, loc_type, attr_name):
        self.refresh()
        self.find_element(eval(loc_type), attr_name).click()

    def next_page(self, loc_type, attr_name):
        # self.refresh()
        self.find_element(eval(loc_type), attr_name).click()

    def get_expect(self, loc_type, attr_name):
        self.find_element(eval(loc_type), attr_name).click()


