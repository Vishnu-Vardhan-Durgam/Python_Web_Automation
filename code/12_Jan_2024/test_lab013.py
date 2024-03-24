# Data Driven Testing


import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)
import os
from dotenv import load_dotenv
import openpyxl


def read_credentials_from_excel(file_path, username, password):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username.password = row
        credentials.append({"username": username, "password": password})
    return credentials


def test_vwo_login():
    file_path = os.getcwd()
    full_file_path = file_path+"/testdata_ddt.xlsx"
    credentials = read_credentials_from_excel(full_file_path)

    for user_cred in credentials:
        username = user_cred["username"]
        password = user_cred["password"]
        print(username, password)
        vwo_login(username, password)


def vwo_login(username, password):
    load_dotenv()
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")

    email_ele = driver.find_element(By.XPATH, "//input[@id='login-username']")
    email_ele.send_keys(username)

    password_ele = driver.find_element(By.XPATH, "//input[@id='login-password']")
    password_ele.send_keys(password)

    sign_in_button_ele = driver.find_element(By.XPATH, "//button[@id='js-login-btn']")
    sign_in_button_ele.click()

    time.sleep(5)
    # write the logic if test case pass
    # URL changes
    # Error message
    driver.quit()
