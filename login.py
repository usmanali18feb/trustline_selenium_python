from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login(email, password, onDevice):

    if onDevice == "iPhone X":
        mobile_emulation = {"deviceName": "iPhone X"}
        driver = webdriver.ChromeOptions()
        driver.add_experimental_option("mobileEmulation", mobile_emulation)
        driver = webdriver.Chrome(options=driver)
        driver.maximize_window()

    elif onDevice == "iPad":
        mobile_emulation = {"deviceName": "iPad"}
        driver = webdriver.ChromeOptions()
        driver.add_experimental_option("mobileEmulation", mobile_emulation)
        driver = webdriver.Chrome(options=driver)
        driver.maximize_window()

    elif onDevice == "Desktop":
        driver = webdriver.Chrome()
        driver.maximize_window()

    driver.get("https://dev.trustline.sa/login")
    # TC-00 Validate the login page title
    assert driver.title == "Login | Trustline"
    #  TC-09 - Validate the heading "Log in to your account" in page source
    assert "Log in to your account" in driver.page_source
    #  TC-10 - Validate the email field in page source.
    assert "floatingInputCustomEmailForExpert" in driver.page_source
    #  TC-11 - Validate the password field in page source.
    assert "floatingPasswordCustomPasswordForExpert" in driver.page_source
    #  TC-12 - Validate the login button in page source
    assert driver.find_element(By.XPATH, '//button[@type="submit"]//h1[text()="Login"]')

    driver.find_element(By.ID, "floatingInputCustomEmailForExpert").send_keys(email)
    driver.find_element(By.ID, "floatingPasswordCustomPasswordForExpert").send_keys(
        password
    )
    driver.find_element(
        By.XPATH, '//button[@type="submit"]//h1[text()="Login"]'
    ).click()

    try:
        if email == "usman.ali18feb@gmail.com" and password == "@Mani112233":
            element = WebDriverWait(driver, 4).until(
                EC.visibility_of_element_located((By.XPATH, ".//h4"))
            )

            # TC-13 - Validate the username after succesfull login in page source
            assert (
                element.text == "usmanali18feb"
            ), f"Expected text not found. Found text: {element.text}"
            # TC-14 -  Validate the current URL after succesfull login
            assert "dashboard-experts" in driver.current_url
            print(
                "Test case for 'Account is logged in' is PASSED for login on "
                + onDevice
            )

        elif email == "usman.ali18feb@gmail.com" and password == "@Mani123456":
            element = WebDriverWait(driver, 2.5).until(
                EC.visibility_of_element_located((By.XPATH, "//div/h2"))
            )
            expected_text = "Email or password is wrong"
            # TC-15 - Validate the prompt for 'Email or password is wrong'
            assert (
                element.text == expected_text
            ), f"Expected text '{expected_text}' not found. Found text: '{element.text}'"
            print("Test case for 'Wrong password' is PASSED for login on " + onDevice)

        elif email == "usman.alifeb@gmail.com" and password == "@Mani112233":
            element = WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//div/h2"))
            )
            expected_text = "Email or password is wrong"
            # TC-15 - Validate the prompt for 'Email or password is wrong'
            assert (
                element.text == expected_text
            ), f"Expected text '{expected_text}' not found. Found text: '{element.text}'"
            print("Test case for 'Wrong email' is PASSED for login on " + onDevice)

        elif email == "usman.alifeb@gmail.com" and password == "":
            element_p = WebDriverWait(driver, 0.5).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "//p[@class='validation_message undefined' and @role='alert']",
                    )
                )
            )
            expected_text_p = "This field is required"
            # TC-16 - Validate the validation error for empty password
            assert (
                element_p.text == expected_text_p
            ), f"Expected text '{expected_text_p}' not found. Found text: '{element_p.text}'"
            print("Test case for 'Empty password' is PASSED for login on " + onDevice)

        elif email == "" and password == "@Mani112233":
            element_p = WebDriverWait(driver, 0.5).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "//p[@class='validation_message undefined' and @role='alert']",
                    )
                )
            )
            expected_text_p = "This field is required"
            # TC-17 - Validate the validation error for empty email
            assert (
                element_p.text == expected_text_p
            ), f"Expected text '{expected_text_p}' not found. Found text: '{element_p.text}'"
            print("Test case for 'Empty email' is PASSED for login on " + onDevice)

        elif email == "" and password == "":
            element_p = WebDriverWait(driver, 0.5).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "//p[@class='validation_message undefined' and @role='alert']",
                    )
                )
            )
            expected_text_p = "This field is required"
            assert (
                element_p.text == expected_text_p
            ), f"Expected text '{expected_text_p}' not found. Found text: '{element_p.text}'"
            print(
                "Test case for 'Empty email and password' is PASSED for login on "
                + onDevice
            )

        elif email == "usman.alifeb":
            email_input = WebDriverWait(driver, 0.5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']"))
            )
            validation_message = email_input.get_attribute("validationMessage")
            expected_message = "Please include an '@' in the email address. 'usman.alifeb' is missing an '@'."
            # TC-18 - Validate the validation message for invalid email without '@'
            assert (
                validation_message == expected_message
            ), f"Expected validation message '{expected_message}', but got '{validation_message}'"
            print("Test case for 'Invalid email' is PASSED for login on " + onDevice)

        elif email == "usman.ali18feb@@gmail.com":
            email_input = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']"))
            )
            validation_message = email_input.get_attribute("validationMessage")
            expected_message = "A part following '@' should not contain the symbol '@'."

            # TC-19 - Validate the validation message for invalid email with '@@'
            assert (
                validation_message == expected_message
            ), f"Expected validation message '{expected_message}', but got '{validation_message}'"
            print(
                "Test case for 'Double @ in email' is PASSED for forget password on "
                + onDevice
            )

    except Exception as e:
        print(f"Exception: {e}")


# TC-01 - Test case for valid credentials
test_login("usman.ali18feb@gmail.com", "@Mani112233", "Desktop")
test_login("usman.ali18feb@gmail.com", "@Mani112233", "iPad")
test_login("usman.ali18feb@gmail.com", "@Mani112233", "iPhone X")


# TC-02 - Test case for wrong password
test_login("usman.ali18feb@gmail.com", "@Mani123456", "Desktop")
test_login("usman.ali18feb@gmail.com", "@Mani123456", "iPad")
test_login("usman.ali18feb@gmail.com", "@Mani123456", "iPhone X")

# TC-03 - Test case for wrong email
test_login("usman.alifeb@gmail.com", "@Mani112233", "Desktop")
test_login("usman.alifeb@gmail.com", "@Mani112233", "iPad")
test_login("usman.alifeb@gmail.com", "@Mani112233", "iPhone X")

# TC-04 - Test case for empty password
test_login("usman.alifeb@gmail.com", "", "Desktop")
test_login("usman.alifeb@gmail.com", "", "iPad")
test_login("usman.alifeb@gmail.com", "", "iPhone X")

# TC-05 - Test case for empty email
test_login("", "@Mani112233", "Desktop")
test_login("", "@Mani112233", "iPad")
test_login("", "@Mani112233", "iPhone X")


# TC-06 - Test case for empty email and empty password
test_login("", "", "Desktop")
test_login("", "", "iPad")
test_login("", "", "iPhone X")

# TC-07 - Test case for invalid email
test_login("usman.alifeb", "@Mani112233", "Desktop")
test_login("usman.alifeb", "@Mani112233", "iPad")
test_login("usman.alifeb", "@Mani112233", "iPhone X")


# TC-08 - Test case for double @ in  email
test_login("usman.ali18feb@@gmail.com", "@Mani112233", "Desktop")
test_login("usman.ali18feb@@gmail.com", "@Mani112233", "iPad")
test_login("usman.ali18feb@@gmail.com", "@Mani112233", "iPhone X")
