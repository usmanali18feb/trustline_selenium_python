from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


# Function to test register-expert
def test_register_expert(
    fullName, userName, email, password, confirm_password, confirm_read, onDevice
):

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
        driver = (
            webdriver.Chrome()
        ) 
        driver.maximize_window()

    driver.get("https://dev.trustline.sa/register-expert")

    WebDriverWait(driver, 1).until(EC.title_is("Trustline | Create a new account"))
    # TC-31 - Validate page title for register expert page
    assert driver.title == "Trustline | Create a new account"
    # TC-32 - Validate the heading "Create a Hacker account" in page source
    assert "Create a Hacker account" in driver.page_source
    # TC-33 - Validate the Full name field in page source
    assert "floatingInputFullName" in driver.page_source
    # TC-34 - Validate the User name field in page source
    assert "floatingInputUsername" in driver.page_source
    # TC-35 - Validate the email field in page source
    assert "email" in driver.page_source
    # TC-36 - Validate the password field in page source
    assert "floatingPasswordCustomPassword" in driver.page_source
    # TC-37 - Validate the confirm password field in page source
    assert "floatingPasswordCustomRePassword" in driver.page_source
    # TC-38 - Validate the checkbox for subscribe in page source
    assert "isAgreeToSubscribeToNewsletter" in driver.page_source
    # TC-39 - Validate the checkbox for confirm read in page source
    assert "herebyConfirmRead" in driver.page_source
    # TC-40 - Validate the Create button in page source
    assert driver.find_element(By.XPATH, '//button[@type="submit"][text()="Create"]')

    # Scenario: Username is already used
    driver.find_element(By.ID, "floatingInputFullName").send_keys(fullName)
    driver.find_element(By.ID, "floatingInputUsername").send_keys(userName)
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "floatingPasswordCustomPassword").send_keys(password)
    if onDevice == "iPhone X" or "iPad":
        # Scroll down by 200 pixels
        driver.execute_script("window.scrollBy(0, 250);")
    driver.find_element(By.ID, "floatingPasswordCustomRePassword").send_keys(
        confirm_password
    )
    driver.find_element(By.ID, "isAgreeToSubscribeToNewsletter").click()
    if confirm_read == "Yes":
        driver.find_element(By.ID, "herebyConfirmRead").click()
    create_button = driver.find_element(
        By.XPATH, '//button[@type="submit"][text()="Create"]'
    )
    driver.execute_script("arguments[0].click();", create_button)

    try:

        if (
            fullName == "Usman Ali"
            and password == "@Mani11223344"
            and confirm_password == "@Mani11223344"
            and confirm_read == "Yes"
        ):

            element = WebDriverWait(driver, 4).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[@class='text-center col-md-12']/h1")
                )
            )
            # TC-41 - Validate the prompt for account is created
            assert (
                element.text
                == "Your account has been created Please verify your email."
            ), f"Expected text not found. Found text: {element.text}"
            print(
                "Test case for 'Register an expert' is PASSED for expert register on "
                + onDevice
            )

        if (
            fullName == "Usman Ali"
            and userName == "usmanalifeb"
            and email == "usman.ali18feb@gmail.com"
            and password == "@Mani112233"
            and confirm_password == "@Mani112233"
            and confirm_read == "Yes"
        ):
            # Wait for the div element containing the h2 element to be present and visible
            element = WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located((By.XPATH, "//div/h2"))
            )
            
            # Assert the text of the h2 element
            expected_text = "This email is registered"
            assert (
                element.text == expected_text
            ), f"Expected text '{expected_text}' not found. Found text: '{element.text}'"
            print(
                "Test case for 'Expert account is already registered' is PASSED for expert register on "
                + onDevice
            )

        if (
            fullName == "Usman Ali"
            and userName == "usmanali18feb"
            and email == "usman.ali10@gmail.com"
            and password == "@Mani112233"
            and confirm_password == "@Mani112233"
            and confirm_read == "Yes"
        ):

            # Wait for the div element containing the h2 element to be present and visible
            element = WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, "//div/h2"))
            )

            # Assert the text of the h2 element
            expected_text = "This username is registered"
            assert (
                element.text == expected_text
            ), f"Expected text '{expected_text}' not found. Found text: '{element.text}'"
            # Attempt to find the account creation confirmation

            print(
                "Test case for 'This username is already registered' is PASSED for expert register on "
                + onDevice
            )

        if (
            fullName == "Usman Ali"
            and userName == "usmanali10"
            and email == "usman.ali10@gmail.com"
            and password == "@Mani112233"
            and confirm_password == "@Mani123456"
            and confirm_read == "Yes"
        ):

            # Wait for the p element with the class 'validation_message undefined' to be present and visible
            element_p = WebDriverWait(driver, 0.01).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "//p[@class='validation_message undefined' and @role='alert']",
                    )
                )
            )

            # Assert the text of the p element
            expected_text_p = "Password & confirm password are not match"
            assert (
                element_p.text == expected_text_p
            ), f"Expected text '{expected_text_p}' not found. Found text: '{element_p.text}'"

            print(
                "Test case for 'Password & confirm password are not match' is PASSED for expert register on "
                + onDevice
            )

        if (
            fullName == "Usman Ali"
            and userName == "usmanali10"
            and email == "usman.ali10@gmail.com"
            and password == "@Mani"
            and confirm_password == "@Mani"
            and confirm_read == "Yes"
        ):

            # Wait for the p element with the class 'validation_message undefined' to be present and visible
            element_p = WebDriverWait(driver, 0.01).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "//p[@class='validation_message undefined' and @role='alert']",
                    )
                )
            )

            # Assert the text of the p element
            expected_text_p = "Password must at least contain 8 characters"
            assert (
                element_p.text == expected_text_p
            ), f"Expected text '{expected_text_p}' not found. Found text: '{element_p.text}'"
            print(
                "Test case for 'Password must at least contain 8 characters' is PASSED for expert register on "
                + onDevice
            )
        if (
            fullName == "Usman Ali"
            and userName == "usman.ali10"
            and email == "usman.ali10@gmail.com"
            and password == "@Mani112233"
            and confirm_password == "@Mani112233"
            and confirm_read == "Yes"
        ):

            # Wait for the p element with the class 'validation_message undefined' to be present and visible
            element_p = WebDriverWait(driver, 0.01).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "//p[@class='validation_message undefined' and @role='alert']",
                    )
                )
            )

            # Assert the text of the p element
            expected_text_p = "Username is not valid"
            assert (
                element_p.text == expected_text_p
            ), f"Expected text '{expected_text_p}' not found. Found text: '{element_p.text}'"
            print(
                "Test case for 'Username is not valid' is PASSED for expert register on "
                + onDevice
            )
            
        if (
            fullName == ""
            and userName == "usmanali10"
            and email == "usman.ali10@gmail.com"
            and password == "@Mani112233"
            and confirm_password == "@Mani112233"
            and confirm_read == "Yes"
        ):

            # Wait for the p element with the class 'validation_message undefined' to be present and visible
            element_p = WebDriverWait(driver, 0.01).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "//p[@class='validation_message undefined' and @role='alert']",
                    )
                )
            )

            # Assert the text of the p element
            expected_text_p = "This field is required"
            assert (
                element_p.text == expected_text_p
            ), f"Expected text '{expected_text_p}' not found. Found text: '{element_p.text}'"
            print(
                "Test case for 'Empty full name' is PASSED for expert register on "
                + onDevice
            )
        
        if (
            fullName == "Usman Ali"
            and userName == "usmanali10"
            and email == ""
            and password == "@Mani112233"
            and confirm_password == "@Mani112233"
            and confirm_read == "Yes"
        ):

            # Wait for the p element with the class 'validation_message undefined' to be present and visible
            element_p = WebDriverWait(driver, 0.01).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "//p[@class='validation_message undefined' and @role='alert']",
                    )
                )
            )

            # Assert the text of the p element
            expected_text_p = "This field is required"
            assert (
                element_p.text == expected_text_p
            ), f"Expected text '{expected_text_p}' not found. Found text: '{element_p.text}'"
            print(
                "Test case for 'Empty full name' is PASSED for expert register on "
                + onDevice
            )



        if (
            fullName == "Usman Ali"
            and userName == "usmanali10"
            and email == "usman.ali10@gmail.com"
            and password == "@Mani"
            and confirm_password == "@Mani"
            and confirm_read == ""
        ):

            # Wait for the p element with the class 'validation_message undefined' to be present and visible
            element_p = WebDriverWait(driver, 0.01).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "//p[@class='validation_message undefined' and @role='alert']",
                    )
                )
            )

            # Assert the text of the p element
            expected_text_p = "You should accept Terms and Conditions"
            assert (
                element_p.text == expected_text_p
            ), f"Expected text '{expected_text_p}' not found. Found text: '{element_p.text}'"

            print(
                "Test case for 'You should accept Terms and Conditions' is PASSED for expert register on "
                + onDevice
            )
            
        if (
            fullName == "Usman Ali"
            and userName == "usmanali10"
            and email == "usman.ali18feb@@gmail.com"
            and password == "@Mani112233"
            and confirm_password == "@Mani112233"
            and confirm_read == "Yes"
        ):

            # Locate the email input field
            email_input = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']"))
            )

            # Get the validation message from the email input field
            validation_message = email_input.get_attribute("validationMessage")

            # Expected validation message
            expected_message = "A part following '@' should not contain the symbol '@'."

            # Assert the validation message
            assert validation_message == expected_message, (
                f"Expected validation message '{expected_message}', but got '{validation_message}'"
            )
            print(
                "Test case for 'Double @ in email' is PASSED for forget password on " + onDevice
            )
        if (
            fullName == "Usman Ali"
            and userName == "usmanali10"
            and email == "usman.alifeb"
            and password == "@Mani112233"
            and confirm_password == "@Mani112233"
            and confirm_read == "Yes"
        ):

            # Locate the email input field
            email_input = WebDriverWait(driver, 1.5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']"))
            )

            # Get the validation message from the email input field
            validation_message = email_input.get_attribute("validationMessage")

            # Expected validation message
            expected_message = "Please include an '@' in the email address. 'usman.alifeb' is missing an '@'."

            # Assert the validation message
            assert validation_message == expected_message, (
                f"Expected validation message '{expected_message}', but got '{validation_message}'"
            )
            print(
                "Test case for 'invalid email' is PASSED for forget password on " + onDevice
            )
            
            
            
    except Exception as e:
        print(f"Exception: {e}")

# TC-20 - Test case for register expert account
test_register_expert(
    "Usman Ali",
    f"usmanali{random.randint(1,9999)}",
    f"usman.ali{random.randint(1,9999)}@gmail.com",
    "@Mani11223344",
    "@Mani11223344",
    "Yes",
    "Desktop",
)
test_register_expert(
    "Usman Ali",
    f"usmanali{random.randint(1,9999)}",
    f"usman.ali{random.randint(1,9999)}@gmail.com",
    "@Mani11223344",
    "@Mani11223344",
    "Yes",
    "iPad",
)
test_register_expert(
    "Usman Ali",
    f"usmanali{random.randint(1,9999)}",
    f"usman.ali{random.randint(1,9999)}@gmail.com",
    "@Mani11223344",
    "@Mani11223344",
    "Yes",
    "iPhone X",
)


# TC-21 Test case for expert account is already registered
test_register_expert(
    "Usman Ali",
    "usmanalifeb",
    "usman.ali18feb@gmail.com",
    "@Mani112233",
    "@Mani112233",
    "Yes",
    "Desktop",
)
test_register_expert(
    "Usman Ali",
    "usmanalifeb",
    "usman.ali18feb@gmail.com",
    "@Mani112233",
    "@Mani112233",
    "Yes",
    "iPad",
)
test_register_expert(
    "Usman Ali",
    "usmanalifeb",
    "usman.ali18feb@gmail.com",
    "@Mani112233",
    "@Mani112233",
    "Yes",
    "iPhone X",
)


# TC- 22 Test case for username is already registered
test_register_expert(
    "Usman Ali",
    "usmanali18feb",
    "usman.ali10@gmail.com",
    "@Mani112233",
    "@Mani112233",
    "Yes",
    "Desktop",
)
test_register_expert(
    "Usman Ali",
    "usmanali18feb",
    "usman.ali10@gmail.com",
    "@Mani112233",
    "@Mani112233",
    "Yes",
    "iPad",
)
test_register_expert(
    "Usman Ali",
    "usmanali18feb",
    "usman.ali10@gmail.com",
    "@Mani112233",
    "@Mani112233",
    "Yes",
    "iPhone X",
)


# TC-23 Test case for password & confirm password are not match
test_register_expert(
    "Usman Ali",
    "usmanali10",
    "usman.ali10@gmail.com",
    "@Mani112233",
    "@Mani123456",
    "Yes",
    "Desktop",
)
test_register_expert(
    "Usman Ali",
    "usmanali10",
    "usman.ali10@gmail.com",
    "@Mani112233",
    "@Mani123456",
    "Yes",
    "iPad",
)
test_register_expert(
    "Usman Ali",
    "usmanali10",
    "usman.ali10@gmail.com",
    "@Mani112233",
    "@Mani123456",
    "Yes",
    "iPhone X",
)


# TC - 24 Test case for invalid password
test_register_expert(
    "Usman Ali",
    "usmanali10",
    "usman.ali10@gmail.com",
    "@Mani",
    "@Mani",
    "Yes",
    "Desktop",
)
test_register_expert(
    "Usman Ali",
    "usmanali10",
    "usman.ali10@gmail.com",
    "@Mani",
    "@Mani",
    "Yes",
    "iPad",
)

test_register_expert(
    "Usman Ali",
    "usmanali10",
    "usman.ali10@gmail.com",
    "@Mani",
    "@Mani",
    "Yes",
    "iPhone X",
)


# TC-25 Test case for un-check read policy
test_register_expert(
    "Usman Ali",
    "usmanali10",
    "usman.ali10@gmail.com",
    "@Mani112233",
    "@Mani112233",
    "",
    "Desktop",
)


test_register_expert(
    "Usman Ali",
    "usmanali10",
    "usman.ali10@gmail.com",
    "@Mani112233",
    "@Mani112233",
    "",
    "iPad",
)


test_register_expert(
    "Usman Ali",
    "usmanali10",
    "usman.ali10@gmail.com",
    "@Mani112233",
    "@Mani112233",
    "",
    "iPhone X",
)



# TC-26 Test case for invalid user
test_register_expert(
    "Usman Ali",
    "usman.ali10",
    "usman.ali10@gmail.com",
    "@Mani112233",
    "@Mani112233",
    "Yes",
    "Desktop",
)
test_register_expert(
    "Usman Ali",
    "usman.ali10",
    "usman.ali10@gmail.com",
    "@Mani112233",
    "@Mani112233",
    "Yes",
    "iPad",
)

test_register_expert(
    "Usman Ali",
    "usman.ali10",
    "usman.ali10@gmail.com",
    "@Mani112233",
    "@Mani112233",
    "Yes",
    "iPhone X",
)


# TC-27 Test case for empty full name
test_register_expert(
    "",
    "usmanali10",
    "usman.ali10@gmail.com",
    "@Mani112233",
    "@Mani112233",
    "Yes",
    "Desktop",
)
test_register_expert(
    "",
    "usmanali10",
    "usman.ali10@gmail.com",
    "@Mani112233",
    "@Mani112233",
    "Yes",
    "iPad",
)

test_register_expert(
    "",
    "usmanali10",
    "usman.ali10@gmail.com",
    "@Mani112233",
    "@Mani112233",
    "Yes",
    "iPhone X",
)



# TC-28 Test case for empty email
test_register_expert(
    "Usman Ali",
    "usmanali10",
    "",
    "@Mani112233",
    "@Mani112233",
    "Yes",
    "Desktop",
)
test_register_expert(
    "Usman Ali",
    "usmanali10",
    "",
    "@Mani112233",
    "@Mani112233",
    "Yes",
    "iPad",
)

test_register_expert(
    "Usman Ali",
    "usmanali10",
    "",
    "@Mani112233",
    "@Mani112233",
    "Yes",
    "iPhone X",
)

# TC-29 Test case for double @@ in email
test_register_expert(
    "Usman Ali",
    "usmanali10",
    "usman.ali18feb@@gmail.com",
    "@Mani112233",
    "@Mani112233",
    "Yes",
    "Desktop",
)
test_register_expert(
    "Usman Ali",
    "usmanali10",
    "usman.ali18feb@@gmail.com",
    "@Mani112233",
    "@Mani112233",
    "Yes",
    "iPad",
)

test_register_expert(
    "Usman Ali",
    "usmanali10",
    "usman.ali18feb@@gmail.com",
    "@Mani112233",
    "@Mani112233",
    "Yes",
    "iPhone X",
)

# TC - 30 Test case for invalid email
test_register_expert(
    "Usman Ali",
    "usmanali10",
    "usman.alifeb",
    "@Mani112233",
    "@Mani112233",
    "Yes",
    "Desktop",
)
test_register_expert(
    "Usman Ali",
    "usmanali10",
    "usman.alifeb",
    "@Mani112233",
    "@Mani112233",
    "Yes",
    "iPad",
)

test_register_expert(
    "Usman Ali",
    "usmanali10",
    "usman.alifeb",
    "@Mani112233",
    "@Mani112233",
    "Yes",
    "iPhone X",
)
