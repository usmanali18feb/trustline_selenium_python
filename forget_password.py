from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to test forget password
def test_forget_password(email, onDevice):

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

    #  TC-59 - Validate the fotget password button in page source
    assert "Forget password? " in driver.page_source

    forget_password_link = driver.find_element(
        By.CSS_SELECTOR, 'a.create_account[href="/forget-password"]'
    )
    forget_password_link.click()

    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located(
            (By.XPATH, "//h1[text()='did you forget password?']")
        )
    )

    driver.find_element(By.ID, "floatingInputCustomEmail").send_keys(email)
    driver.find_element(By.XPATH, '//button[@type="submit"][text()="Send"]').click()
    # # TC-60 - Validate page title for forget password page
    # assert driver.title == "Forget password?  | Trustline"
    # TC-61 Validate the URL for forget password
    assert "forget-password" in driver.current_url
    # TC-62 - Validate the Email field in page source
    assert "floatingInputCustomEmail" in driver.page_source

    try:
        if email == "usman.ali18feb@gmail.com":

            element = WebDriverWait(driver, 4).until(
                EC.visibility_of_element_located((By.XPATH, "//div/h2"))
            )
            expected_text = "Email sent to your account, please verify the email to activate your account"
            # TC-63 - Validate the prompt for Email sent to your account
            assert (
                element.text == expected_text
            ), f"Expected text '{expected_text}' not found. Found text: '{element.text}'"
            print(
                "Test case for 'Email sent to your account' is PASSED for forget password on "
                + onDevice
            )

        elif email == "usman.alifeb":
            email_input = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']"))
            )

            validation_message = email_input.get_attribute("validationMessage")
            expected_message = "Please include an '@' in the email address. 'usman.alifeb' is missing an '@'."
            # TC-64 - Validate the error message on invalid email
            assert (
                validation_message == expected_message
            ), f"Expected validation message '{expected_message}', but got '{validation_message}'"
            print(
                "Test case for 'Invalid email' is PASSED for forget password on "
                + onDevice
            )

        elif email == "usman.alifeb123@gmail.com":
            element = WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located((By.ID, "swal2-html-container"))
            )

            expected_text = "This User is not found"
            assert (
                element.text == expected_text
            ), f"Expected text '{expected_text}' not found. Found text: '{element.text}'"
            print(
                "Test case for 'This User is not found' is PASSED for forget password on "
                + onDevice
            )

        elif email == "":
            element_p = WebDriverWait(driver, 0.5).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "//p[@class='validation_message undefined' and @role='alert']",
                    )
                )
            )
            expected_text_p = "This field is required"
            # TC-65 - Validate the error message on empty Email
            assert (
                element_p.text == expected_text_p
            ), f"Expected text '{expected_text_p}' not found. Found text: '{element_p.text}'"
            print("Test case for 'Empty email' is PASSED for login on " + onDevice)

        elif email == "usman.ali18feb@@gmail.com":
            email_input = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']"))
            )
            validation_message = email_input.get_attribute("validationMessage")
            expected_message = "A part following '@' should not contain the symbol '@'."
            #  TC-66 - Validate the error message on double @ on email
            assert (
                validation_message == expected_message
            ), f"Expected validation message '{expected_message}', but got '{validation_message}'"
            print(
                "Test case for 'Double @ in email' is PASSED for forget password on "
                + onDevice
            )

    except Exception as e:
        print(f"Exception: {e}")


# TC-53 Test case for valid email
test_forget_password("usman.ali18feb@gmail.com", "Desktop")
test_forget_password("usman.ali18feb@gmail.com", "iPad")
test_forget_password("usman.ali18feb@gmail.com", "iPhone X")


# TC -55 Test case for invalid email
test_forget_password("usman.alifeb", "Desktop")
test_forget_password("usman.alifeb", "iPad")
test_forget_password("usman.alifeb", "iPhone X")

# TC - 56 Test Case for not a user
test_forget_password("usman.alifeb123@gmail.com", "Desktop")
test_forget_password("usman.alifeb123@gmail.com", "iPad")
test_forget_password("usman.alifeb123@gmail.com", "iPhone X")

# TC - 57 Test case for Empty email
test_forget_password("", "Desktop")
test_forget_password("", "iPad")
test_forget_password("", "iPhone X")

# TC-58 Test case for double @ in email
test_forget_password("usman.ali18feb@@gmail.com", "Desktop")
test_forget_password("usman.ali18feb@@gmail.com", "iPad")
test_forget_password("usman.ali18feb@@gmail.com", "iPhone X")
