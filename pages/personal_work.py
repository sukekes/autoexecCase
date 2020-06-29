# -*- coding: utf-8 -*-
# @Time    : 2020-5-26 18:24
# @Author  : suk
# @FileName: personal_work.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/
from pages.basepage import BasePage
from pages.loginpage import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PersonalWork(BasePage):
    # def __init__(self):
    #     LoginPage.__init__()
    # 点击我的任务
    def click_menu(self, loc_type, attr_name):
        self.find_element(eval(loc_type), attr_name).click()

    # 查询我的项目
    def query_project(self, loc_type, attr_name, input_params):
        self.find_element(eval(loc_type), attr_name).sendkeys(input_params)
        self.find_element(eval(loc_type), attr_name).sendkeys(Keys.ENTER)

    # 点击项目名称
    def click_project(self, loc_type, attr_name):
        self.find_element(eval(loc_type), attr_name).click()

    # 点击我的用例
    def click_my_case(self, loc_type, attr_name):
        self.find_element(eval(loc_type), attr_name).click()
