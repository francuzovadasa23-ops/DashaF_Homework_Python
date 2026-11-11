from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    CHECKOUT_BUTTON = (By.ID, "checkout")
    TITLE_CART = (By.CSS_SELECTOR, "[data-test='title']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_cart_title(self):
        title_element = self.wait.until(
            EC.visibility_of_element_located(self.TITLE_CART))
        return title_element.text

    def click_checkout_button(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
