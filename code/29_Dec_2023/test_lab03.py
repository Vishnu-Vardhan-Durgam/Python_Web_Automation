
from selenium import webdriver
import time

# Chrome  --> Chrome extensions
# firefox --> firefox extensions
# edge    --> edge extensions



def test_open_login():
    chrome_options = webdriver.ChromeOptions()
    # give some extra argument or extension or anything to chrome
    # Chrome options - chrome with the extension , window size , proxy , JS disabled

    # Chrome extension crx download ---- search to download

    extension_path = "/Users/admin/Downloads/AdBlocker.crx" # Add blocker path
    chrome_options.add_extension(extension_path)

    chrome_options.add_argument("--start-maximized") # This will maximize the window


    driver = webdriver.Chrome(options = chrome_options)
    driver.get("https://www.google.com/")


    print(driver.title)
    time.sleep(10)




