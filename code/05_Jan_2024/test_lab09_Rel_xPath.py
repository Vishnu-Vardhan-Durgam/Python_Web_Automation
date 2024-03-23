# https://www.idrive360.com/enterprise/login


from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")

    # Relative xPath
    absolute_Xpath_username = driver.find_element(By.XPATH, "//input[@type='email']")
    absolute_Xpath_username.send_keys("augtest_040823@idrive.com")

    # By name
    absolute_Xpath_password = driver.find_element(By.XPATH, "//input[@name='password']")
    absolute_Xpath_password.send_keys("Admin@123")

    # # By class - not recommonded
    # absolute_Xpath_pass = driver.find_element(By.XPATH, "//input[@class='id-form-ctrl']")
    # absolute_Xpath_pass.send_keys("Admin@123")



    time.sleep(3)
    driver.quit()
