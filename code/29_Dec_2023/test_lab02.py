
from selenium import webdriver
import logging
import time

def test_open_login():
    driver = webdriver.Chrome()
    LOGGER = logging.getLogger(__name__)
    driver.get("https://www.google.com/")
    driver.maximize_window()
    LOGGER.info(driver.title)
    print(driver.title)

    time.sleep(200)




