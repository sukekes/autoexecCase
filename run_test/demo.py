from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()

driver.get("http://10.215.142.114/LightTower/login")
driver.implicitly_wait(5)

driver.maximize_window()
driver.find_element(By.NAME, "userBase.userName").send_keys("username")
driver.find_element(By.NAME, "userBase.password").send_keys("password")
driver.find_element(By.ID, "submit_button").click()

driver.find_element(By.XPATH, "//a[@role='tasks']").click()

driver.find_element(By.XPATH, "//td[@title='合同预编号录入']/a").click()

driver.find_element(By.XPATH, "//a[@role='tasks-testcases']").click()

driver.find_element(By.XPATH, "//div[text()='用例编号']")

driver.find_element(By.XPATH, "//td[@title='C115']/following::td[@title='查看执行']/child::a[text()='执行']").click()

sleep(5)

driver.quit()
