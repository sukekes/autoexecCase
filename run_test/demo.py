from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://10.215.142.114/LightTower/login")
driver.implicitly_wait(5)

driver.maximize_window()
# 登录
driver.find_element(By.NAME, "userBase.userName").send_keys("xu_j22")
driver.find_element(By.NAME, "userBase.password").send_keys("xu_j22@ecidi")
driver.find_element(By.ID, "submit_button").click()

# 进入我的用例页面
driver.find_element(By.XPATH, "//a[@role='tasks']").click()
sleep(2)
driver.find_element(By.NAME, "projectInformation.projectName").send_keys("合同预编号录入")
driver.find_element(By.NAME, "projectInformation.projectName").send_keys(Keys.ENTER)
sleep(3)
driver.find_element(By.XPATH, "//td[@title='合同预编号录入']/a").click()
sleep(2)
driver.find_element(By.XPATH, "//a[@role='tasks-testcases']").click()
# driver.find_element(By.XPATH, "//div[text()='用例编号']").click()

# driver.find_element(By.XPATH, "//td[@title='C1']/following::td[@title='查看执行']/child::a[text()='执行']").click()

# a = EC.presence_of_element_located("//td[@title='C198']")
# try:
#     driver.find_element(By.XPATH, "//td[@title='C198']")
#     print("not none")
# except:
#     print("none")
#
# driver.quit()

a = driver.find_element(By.XPATH, "//span[text()='请选择版本：']")
print(a)
sleep(5)
driver.quit()
