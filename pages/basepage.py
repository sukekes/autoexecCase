# -*- coding: utf-8 -*-
# @Time    : 2020-5-22 17:35
# @Author  : suk
# @FileName: basepage.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/

from common.log import logging
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import WebDriverException, NoSuchWindowException, NoSuchElementException


class BasePage(object):
    def __init__(self, driver):
        self.element = None
        self.elements = None
        self.pre_case = False
        self.base_url = "http://10.215.142.114/LightTower/login"
        self.driver = driver
        self.timeout = 10

    # protected mthod
    def _open(self):
        try:
            self.driver.get(self.base_url)
            self.driver.implicitly_wait(self.timeout)
            self.driver.maximize_window()
        except (WebDriverException, NoSuchWindowException, NoSuchElementException) as error:
            logging.error(error)

    def open(self):
        self._open()

    def find_element(self, *loc):
        try:
            # self.driver.switch_to.window(now_handle)
            self.driver.implicitly_wait(self.timeout)
            self.element = self.driver.find_element(*loc)
            sleep(1)
            logging.info("find the element %s success." % str(loc))
            return self.element
        except NoSuchElementException as error:
            logging.error(error)

    def find_elements(self, *loc):
        try:
            # self.driver.switch_to.window(now_handle)
            self.elements = self.driver.find_elements(*loc)
            sleep(0.5)
            self.driver.implicitly_wait(self.timeout)
            logging.info("find the element %s succeed." % loc)
            return self.elements
        except NoSuchElementException as error:
            logging.erro(error)

    def refresh(self):
        self.driver.refresh()

    def execute_js(self, js):
        self.driver.execute_script(js)



