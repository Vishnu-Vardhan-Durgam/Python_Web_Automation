 # https://katalon-demo-cura.herokuapp.com/


 # Preferences -----
 # ID
 # Name
 # Class name
 # Tag name
 # Link text/Partical Link
 # CSS Selector
 # XPath

 # XPath --> 60%
 # CSS Selector --> 30%
 # ID, Name  --> 10%


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#     ID = "id"
#     XPATH = "xpath"
#     LINK_TEXT = "link text"
#     PARTIAL_LINK_TEXT = "partial link text"
#     NAME = "name"
#     TAG_NAME = "tag name"
#     CLASS_NAME = "class name"
#     CSS_SELECTOR = "css selector"

def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # Match with ID
    # make_appointment_button = driver.find_element(By.ID, "btn-make-appointment" )
    # make_appointment_button.click()

    # match with Partial link
    # make_appointment_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Appointment")
    # make_appointment_button.click()


    # match with Full link
    # make_appointment_button = driver.find_element(By.LINK_TEXT, "Make Appointment")
    # make_appointment_button.click()

    # match with Class - Multiple elements
    # make_appointment_button = driver.find_elements(By.CLASS_NAME, "btn.btn-dark.btn-lg")
    # make_appointment_button[1].click()

    # match with Tag name - Multiple elements
    make_appointment_button = driver.find_elements(By.TAG_NAME, "a")
    make_appointment_button[7].click()




    # < a
    # id = "btn-make-appointment"
    # href = "./index.php#appointment"
    # class ="btn btn-dark btn-lg" > Use (. -- dot ) instead of space
    # Make Appointment
    # < / a >

    time.sleep(5)
    driver.quit()





