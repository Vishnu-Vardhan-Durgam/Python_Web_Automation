# https://app.vwo.com
# User name --> contact+atb5x@thetestingacademy.com
# Password --> ATBx@1234

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)
import os
from dotenv import load_dotenv


@pytest.mark.positive
# pytest -k "posivite"  --> this will run all the positive test cases
def test_open_login_positive():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    # driver.implicitly_wait(20) # --> Implicit waits

    email_ele = driver.find_element(By.XPATH, "//input[@id='login-username']")
    email_ele.send_keys(os.getenv("EMAIL"))

    password_ele = driver.find_element(By.XPATH, "//input[@id='login-password']")
    password_ele.send_keys(os.getenv("PASSWORD"))

    sign_in_button_ele = driver.find_element(By.XPATH, "//button[@id='js-login-btn']")
    sign_in_button_ele.click()

    # time.sleep(15) # --> Implicit waits

    # Explicit waits --> Add a condition so that webdriver should wait for that condition
    WebDriverWait(driver, 15).until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".page-heading"), "Dashboard"))

    # or

    # Explicit waits --> with Aman
    # WebDriverWait(driver,15).until(expected_conditions.text_to_be_present_in_element((By.XPATH,"//span[@data-qa='lufexuloga']"), "Aman"))

    heading_element = driver.find_element(By.XPATH, "//span[@data-qa='lufexuloga']")
    # assert heading_element.text == os.getenv("USERNAME")  # OP --> Failing (Aman != admin)
    assert heading_element.text == "Aman"

    time.sleep(5)
    driver.quit()
