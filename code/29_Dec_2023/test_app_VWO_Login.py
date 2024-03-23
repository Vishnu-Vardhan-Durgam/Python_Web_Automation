# Open the browser
# Navigate to a URL
# Find the Email web element and enter "EmailID"
# Fine the password web element and enter "Password"
# Click on the button "Sign in


# Verify the Dashboard is loaded
# create a report to send to QA lead  - HTML - Allure report


from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import time


def test_vwo_login():
    # selenium API - Create a session
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()

    # to maximize the window
    driver.maximize_window()

    # to open the URL
    driver.get("https://app.vwo.com")

    # < input
    # type = "email"
    # class ="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi"
    # >

    # Selenium how to find Elements
    # find_element by_id  ---> by unique ID attribute
    # find_element by_name  --->by unique name attribute
    # find_element by_xpath  --->by using Xpath expression
    # find_element by_link_text  --->by visible text
    # find_element by_partial_link_text  --->by partial match
    # find_element by_tag_name  --->by HTML Tag name
    # find_element by_class_name  --->by CSS class name

    email_ele = driver.find_element(By.ID, "login-username")
    password_ele = driver.find_element(By.NAME, "password")

    sign_in_button_ele = driver.find_element(By.ID, "js-login-btn")

    # sending the data email and password than click
    # sendkeys and click()

    # email_ele.send_keys("vardhan.vishn557@gmail.com")
    email_ele.send_keys("contact+atb5x@thetestingacademy.com")

    # password_ele.send_keys("Vishnu557")
    password_ele.send_keys("ATBx@1234")

    sign_in_button_ele.click()

    time.sleep(5)

    LOGGER.info('Title is -->' + driver.title)
    assert "Dashboard" in driver.title

