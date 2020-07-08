# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 11:00
# @Author  : suk
# @FileName: exec_case.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/
from common.parse import Parse
from common.log import logging
from pages.exec_case import ExecCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import yaml
import getpass
import os
from selenium.webdriver.chrome.options import Options


def exec_case(driver, page, yml):
    # 解析测试数据，返回dict
    parse = Parse()
    parse.call_pre_case(driver, page, yml)

    # 确认用例编号查询定位方式，属性内容
    query_loc = "By." + str.upper(parse.data['test_step'][0]["loc_type"])
    query_attr_name = parse.data["test_step"][0]["name"]

    # 确认用例执行标签定位方式，属性内容
    exec_span_loc = "By." + str.upper(parse.data["test_step"][1]["loc_type"])
    exec_span_attr_name = parse.data["test_step"][1]["name"]

    # 确认用例执行页面通过按钮的定位方式，属性内容
    pass_loc = "By." + str.upper(parse.data['test_step'][2]["loc_type"])
    pass_attr_name = parse.data["test_step"][2]["name"]

    # 确认用例执行页面不通过按钮的定位方式，属性内容
    fault_loc = "By." + str.upper(parse.data['test_step'][3]["loc_type"])
    fault_attr_name = parse.data["test_step"][3]["name"]

    # 确认用例执行页面阻塞按钮的定位方式，属性内容
    block_loc = "By." + str.upper(parse.data['test_step'][4]["loc_type"])
    block_attr_name = parse.data["test_step"][4]["name"]

    # 确认从缺陷填报页面返回我的用例页面定位方式，属性内容
    back_from_issue_loc = "By." + \
                          str.upper(parse.data['test_step'][5]["loc_type"])
    back_from_issue_attr_name = parse.data["test_step"][5]["name"]

    # 确认从用例执行页面返回我的用例页面定位方式，属性内容
    back_from_exec_loc = "By." + \
                         str.upper(parse.data['test_step'][6]["loc_type"])
    back_from_exec_attr_name = parse.data["test_step"][6]["name"]

    # 切换页面
    next_page_loc = "By." + str.upper(parse.data['test_step'][7]["loc_type"])
    next_page_attr_name = parse.data["test_step"][7]["name"]

    # 执行页面code
    code_num_loc = "By." + str.upper(parse.data['test_step'][8]["loc_type"])
    code_num_attr_name = parse.data["test_step"][8]["name"]

    # # 确认预期结果定位方式、属性值
    expect_loc = "By." + str.upper(parse.data["expect_output"]["loc_type"])
    expect_attr_name = parse.data["expect_output"]["name"]

    execc = ExecCase(driver)
    fault_cases = parse.data["input_params"]["fault"]
    block_cases = parse.data["input_params"]["block"]
    pass_case = parse.data["input_params"]["success"][0]
    js = "var q=document.documentElement.scrollTop=1000"
    # 没有加非空判断
    if fault_cases is not None:
        for fault in fault_cases:
            fault_case = False
            fault_case_no = exec_span_attr_name.replace("caseno", fault)
            execc.query_case(query_loc, query_attr_name, fault)
            while (not fault_case):
                try:
                    execc.enter_exec_page(exec_span_loc, fault_case_no)
                    fault_case = True
                except:
                    execc.next_page(next_page_loc, next_page_attr_name)
            execc.exec_case(fault_loc, fault_attr_name)
            execc.back_from_issue(back_from_issue_loc, back_from_issue_attr_name)
            logging.info("executed the case No. %s to Fail" % fault)
        logging.info("executed the Fail Cases %s" % fault_cases)

    # 没有加非空判断
    if block_cases is not None:
        for block in block_cases:
            execc.query_case(query_loc, query_attr_name, block)
            block_case = True
            block_case_no = exec_span_attr_name.replace("caseno", block)
            while (block_case):
                try:
                    execc.enter_exec_page(exec_span_loc, block_case_no)
                    block_case = False
                except:
                    execc.next_page(next_page_loc, next_page_attr_name)
            execc.exec_case(block_loc, block_attr_name)
            try:
                execc.back_from_issue(back_from_exec_loc, back_from_exec_attr_name)
            except:
                logging.info("back to my case list.")
            logging.info("executed the case No. %s to Block" % block)

        logging.info("executed the Block Cases %s" % block_cases)

    execc.query_case(query_loc, query_attr_name, pass_case)
    case_no = exec_span_attr_name.replace("caseno", pass_case)
    execc.enter_exec_page(exec_span_loc, case_no)
    execc.exec_case(pass_loc, pass_attr_name)
    logging.info("executed the case %s to Pass." % pass_case)
    result = False
    while (not result):
       try:
           code_value = execc.execute_js("return document.getElementById('code').value")
           execc.exec_case(pass_loc, pass_attr_name)
           logging.info("executed the case %s to Pass." % code_value)
       except:
           execc.get_expect(expect_loc, expect_attr_name)
           result = True
           logging.info("Completed execute TestCase!")
           break

    return result


# 封装成exe使用
if __name__ == "__main__":
    parse_pre = Parse()
    parse_pre.yml_parse("loginpage", "login_by_manager")
    # 配置项目名称，用例
    if parse_pre.data['input_params']['username'] is None or parse_pre.data['input_params']['password'] is None:
        username = input("请输入用户名：")
        password = input("请输入密码：")
    project_name = input("请输入项目全称：")
    fault_cases = list(input("请输入执行失败的用例编号，以逗号隔开（请注意区分中英文字符）：").split(","))
    block_cases = list(input("请输入执行阻塞的用例编号，以逗号隔开（请注意区分中英文字符）：").split(","))
    pass_cases = input("请输入执行通过case中最大的编号：")

    # read login yaml
    if parse_pre.data['input_params']['username'] is None or parse_pre.data['input_params']['password'] is None:
        # 打包使用
        # with open("./testdata/loginpage/login_by_manager.yml", "r", encoding="utf-8") as read_login_file:
        # 直接执行
        with open("../../testdata/loginpage/login_by_manager.yml", "r", encoding="utf-8") as read_login_file:
            login_data = yaml.full_load(read_login_file.read())
            # print("赋值前" + data['input_params']['username'])
            login_data['input_params']['username'] = username
            login_data['input_params']['password'] = password
        read_login_file.close()
        # write login yaml
        with open("../../testdata/loginpage/login_by_manager.yml", "w", encoding="utf-8") as write_login_file:
            # allow_unicode 解决中文乱码问题
            yaml.dump(login_data, write_login_file, allow_unicode=True, default_flow_style=False)
        write_login_file.close()

    # read personal work yaml
    with open("../../testdata/personalwork/personal_work.yml", "r", encoding="utf-8") as read_personal_work:
        personal_work_data = yaml.full_load(read_personal_work.read())
        personal_work_data['input_params']['sendkeys'] = project_name
    read_personal_work.close()
    # write personal work yaml
    with open("../../testdata/personalwork/personal_work.yml", "w", encoding="utf-8") as write_personal_work:
        yaml.dump(personal_work_data, write_personal_work, allow_unicode=True, default_flow_style=False)
    write_personal_work.close()

    # read execute case yaml
    with open("../../testdata/execc/execc.yml", "r", encoding="utf-8") as read_exec_file:
        exec_case_data = yaml.full_load(read_exec_file.read())
        for i in range(len(fault_cases)):
            exec_case_data['input_params']['fault'][i] = fault_cases[i]
            i += 1
        for i in range(len(block_cases)):
            exec_case_data['input_params']['block'][i] = block_cases[i]
            i += 1
        exec_case_data['input_params']['success'][0] = pass_cases
    read_exec_file.close()
    # write execute case yaml
    with open("../../testdata/execc/execc.yml", "w", encoding="utf-8") as write_exec_file:
        yaml.dump(exec_case_data, write_exec_file, allow_unicode=True, default_flow_style=False)
    write_exec_file.close()

    # webdriver
    while(True):
        headless = str.upper(input("请选择是否查看运行过程，命令行模式/浏览器运行模式（Y/N）："))
        if headless == "Y":
            driver = webdriver.Chrome()
            break
        elif headless == "N":
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--window-size=1920,1080')
            driver = webdriver.Chrome(chrome_options=options)
            break
        else:
            logging.info("输入错误，请重新输入\n")
            sleep(0.5)
            continue
    anticipation = exec_case(driver, "execc", "execc")
    assert anticipation
    driver.quit()
