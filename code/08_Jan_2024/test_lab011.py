# https://www.ebay.com/

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")

    assert driver.current_url == "https://www.ebay.com/"

    search_box = driver.find_element(By.XPATH, "//input[@id='gh-ac']")
    search_box.send_keys("16 gb")

    search_button = driver.find_element(By.XPATH, "//input[@id='gh-btn']")
    search_button.click()

    list_items = driver.find_elements(By.XPATH, "//span[@role='heading']")
    for i in list_items:
        print(i.text)

    time.sleep(3)
    driver.quit()
