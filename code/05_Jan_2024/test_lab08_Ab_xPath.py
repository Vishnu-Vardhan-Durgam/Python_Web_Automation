# https://www.idrive360.com/enterprise/login


from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")

    # Absolute xPath
    absolute_Xpath = driver.find_element(By.XPATH,
                                         "/html/body/app-root/app-login/app-signin/div/section/div/div/form/div[2]/div[1]/fieldset/div[5]/div[1]/input")
    absolute_Xpath.send_keys("admin")

    time.sleep(3)
    driver.quit()
