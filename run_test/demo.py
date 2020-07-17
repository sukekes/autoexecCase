from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

options = Options()

options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920,1080')

# driver = webdriver.Chrome(chrome_options=options)
driver = webdriver.Chrome()
driver.get("http://10.215.142.114/LightTower/login")
driver.implicitly_wait(15)

driver.maximize_window()
# 登录
driver.find_element(By.NAME, "userBase.userName").send_keys("xu_j22")
driver.find_element(By.NAME, "userBase.password").send_keys("xu_j22@ecidi")
driver.find_element(By.ID, "submit_button").click()

# 进入我的用例页面
driver.find_element(By.XPATH, "//a[@role='tasks']").click()
sleep(2)
driver.find_element(By.NAME, "projectInformation.projectName").send_keys("合同预编号")
driver.find_element(By.NAME, "projectInformation.projectName").send_keys(Keys.ENTER)
sleep(3)
driver.find_element(By.XPATH, "//td[@title='合同预编号']/a").click()
sleep(2)
driver.find_element(By.XPATH, "//a[@role='tasks-testcases']").click()
# driver.find_element(By.XPATH, "//div[text()='用例编号']").click()

# driver.find_element(By.XPATH, "//td[@title='C419']/following::td[@title='查看执行']/child::a[text()='执行']").click()

# a = EC.presence_of_element_located("//td[@title='C198']")
# try:
#     driver.find_element(By.XPATH, "//td[@title='C198']")
#     print("not none")
# except:
#     print("none")
#
# driver.quit()

# a = driver.find_element(By.XPATH, "//span[text()='请选择版本：']")
# driver.find_element(By.XPATH, "//td[@id='next_testcase_jqgrid_pager']").click()
# a = driver.find_element(By.ID, "code")
# driver.refresh()
# driver.find_element(By.ID, "pass").click()
# a = driver.execute_script("return document.getElementById('code').value")
# b = driver.find_element(By.ID, "code").text
a = Select(driver.find_element(By.ID, "version_name"))
a.select_by_visible_text("v2.7")
# a = driver.find_element(By.ID, "code")
# print(a.value_of_css_property("code"))
sleep(20)
driver.quit()
