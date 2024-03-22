
from selenium import webdriver

import time

def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    # driver.maximize_window()
    print(driver.title)

    driver.back()
    driver.get("https://www.bing.com/")
    print(driver.title)

    driver.forward()
    print(driver.title)

    driver.refresh()
    driver.get("https://www.facebook.com/")
    print(driver.title)




    time.sleep(5)
    # driver.close()
    driver.quit()


