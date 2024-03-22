# selenium

# selenium --3
# 1) you need to set up the browser drivers to machin PC/Mac
# 2) Problems with browers
#
# # selenium --4
# 1) w3c protocol, selenium manager - which will automatically download the driver browser for you

from selenium import webdriver

def test_open_login():
    driver = webdriver.Chrome()
    # Create a session with POST request (API POST request)
    # Fresh Chrome browser will be open - session ID created
    # sessionId - 68624727340877
    driver.get("https://www.google.com/")
    driver.maximize_window()
    print(driver.title)




