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

    # # 确认预期结果定位方式、属性值
    expect_loc = "By." + str.upper(parse.data["expect_output"]["loc_type"])
    expect_name = parse.data["expect_output"]["name"]

    execc = ExecCase(driver)
    fault_cases = parse.data["input_params"]["fault"]
    block_cases = parse.data["input_params"]["block"]
    pass_case = parse.data["input_params"]["sucess"]
    for fault in fault_cases:
        execc.query_case(query_loc, query_attr_name).send_keys(fault)
        case_no = exec_span_attr_name.replace("caseno", fault)
        execc.enter_exec_page(exec_span_loc, case_no)
        execc.exec_case(fault_loc, fault_attr_name)
        execc.back_from_issue(back_from_issue_loc, back_from_issue_attr_name)
        logging.info("executed the case No. %s to Fail" % fault)
    logging.info("executed the Fail Case %s" % fault_cases)

    for block in block_cases:
        execc.query_case(query_loc, query_attr_name).send_keys(block)
        case_no = exec_span_attr_name.replace("caseno", block)
        execc.enter_exec_page(exec_span_loc, case_no)
        execc.exec_case(block_loc, block_attr_name)
        execc.back_from_issue(back_from_exec_loc, back_from_exec_attr_name)
        logging.info("executed the case No. %s to Block" % fault)

    logging.info("executed the Fail Case %s" % block_cases)

    exec_case(execc.query_case(query_loc, query_attr_name).send_keys(pass_case))
    case_no = exec_span_attr_name.replace("caseno", pass_case)
    execc.enter_exec_page(exec_span_loc, case_no)
    result = True
    while(result):
        execc.exec_case(pass_loc, pass_attr_name)

        if WebDriverWait(driver, 10).until(EC.presence_of_element_located(eval(expect_loc), expect_name)):
            result = False
            logging.info("executed the Pass Cases")
            break
        else:
            continue
    return result




