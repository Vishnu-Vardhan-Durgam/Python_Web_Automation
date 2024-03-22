# logging means - capturing the details which are useful while debugging
# and show the user details about execution of the program

# warning to the user
# information to the user
# errors , critical errors user


import logging   # (logging - is a module)

def test_print_logs():
    LOGGER = logging.getLogger(__name__) # if we pass __name__ it will use the
                                        # Root name means file name


    # driver.get("https://www.google.com")

    LOGGER.info("This is a Information Logs")
    LOGGER.warning("This is warning logs")
    LOGGER.error("This is error logs")
    LOGGER.critical("This  is critical logs")




















