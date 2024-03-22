 # https://katalon-demo-cura.herokuapp.com/


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # Match with ID
    make_appointment_button = driver.find_element(By.ID, "btn-make-appointment" )
    make_appointment_button.click()

    print(driver.current_url)

    # Verification of the URL
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login" ,"Error wrong URL"


    # <input
    # type="password" --> This is custom attribute - so use [type="password"] while searching the element
    # class="form-control"
    # id="txt-password"
    # name="password"
    # placeholder="Password" --> This is custom attribute - so use [type="password"] while searching the element
    # value="" autocomplete="off">
    # Custom attribute  -->  is other than --> ID , Name , Class -

    user_name = driver.find_element(By.NAME, "username")
    user_name.send_keys("John Doe")

    password = driver.find_element(By.ID, "txt-password")
    password.send_keys("ThisIsNotAPassword")

    submit_button = driver.find_element(By.ID, "btn-login")
    submit_button.click()

    # Verification of the URL
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment", "Error wrong URL"

    time.sleep(5)
    # driver.close()
    driver.quit()





