
from selenium import webdriver

import time

def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    driver.maximize_window()
    print(driver.title)

    time.sleep(15)

    # interview question
    # driver.close()
    # driver.quit()

    driver.close()
    # Close will close the current window or Tab but not other tabs
    # session ID != None
    # Most of the times we will use this only

    time.sleep(15)

    driver.quit()
    # session ID== None
    # Close all the Tabs (Windows)

