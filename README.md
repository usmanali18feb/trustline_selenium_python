```markdown
# Trustline Selenium Python

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.x
- Google Chrome browser
- ChromeDriver
- Selenium package

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/usmanali18feb/trustline_selenium_python
   cd trustline_selenium_python
   ```
2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```
3. Install the required packages: 
   ```bash
   pip install selenium
   ```
4. Download ChromeDriver:
   - Download the ChromeDriver that matches your installed version of Chrome from [here].
   - Place the downloaded `chromedriver` executable in a directory included in your system's PATH, or specify its location in the script.

## Usage
The script `register_expert.py`, `login.py`, and `forget_password.py` test various scenarios of the authentication process on the Trustline website.

## Running the Script
1. Run the script:
   - To run test cases of register expert:  `python3 register_expert.py`
   - To run test cases of login:  `python3 login.py`
   - To run test cases of forget password:  `python3 forget_password.py`

## Devices 
The script tests cover the following devices:
- Desktop
- iPad
- iPhone X

## Test Cases for Register Expert
- Registration with a username that is already in use.
- Registration with valid data.
- Registration with an email that is already registered.
- Password and confirm password mismatch.
- Invalid password (less than 8 characters).
- Un-checked 'Terms and Conditions'.
- Invalid username.
- Empty full name field.
- Empty email field.
- Email with double `@@`.
- Invalid email format (missing `@`).

## Test Cases for Login
- Login with a wrong password.
- Login with valid data.
- Login with a wrong email.
- Login with an empty password.
- Login with an empty email.
- Login with both email and password fields empty.
- Login with an invalid email (missing @).
- Login with an email containing double @@.

## Test Cases for Forget Password
- Forget Password with valid email.
- Forget Password with an invalid email (missing @).
- Forget Password with an email that is not a registered user.
- Forget Password with an empty email field.
- Forget Password with an email containing double @@.

## Future Improvements
In the future, we can apply POM (Page Object Model) and Pytest (Testing Framework).
```
