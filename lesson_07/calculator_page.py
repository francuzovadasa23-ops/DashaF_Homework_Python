from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    DELAY_INPUT = (By.ID, "delay")
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_PLUS = (By.XPATH, "//span[text()='+']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_EQUALS = (By.XPATH, "//span[text()='=']")
    RESULT_DISPLAY = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 55)

    def open_page(self):
        self.driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay):
        delay_input = self.driver.find_element(*self.DELAY_INPUT)
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button(self):
        self.driver.find_element(*self.BUTTON_7).click()
        self.driver.find_element(*self.BUTTON_PLUS).click()
        self.driver.find_element(*self.BUTTON_8).click()
        self.driver.find_element(*self.BUTTON_EQUALS).click()

    def get_result(self):
        self.wait.until(
            EC.text_to_be_present_in_element(self.RESULT_DISPLAY, "15"))
        display = self.driver.find_element(*self.RESULT_DISPLAY)
        return display.text
