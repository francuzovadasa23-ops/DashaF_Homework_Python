from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_page(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):

        user_name = self.driver.find_element(*self.USERNAME)
        user_name.clear()
        user_name.send_keys(username)

        user_password = self.driver.find_element(*self.PASSWORD)
        user_password.clear()
        user_password.send_keys(password)

        self.driver.find_element(*self.LOGIN_BUTTON).click()
