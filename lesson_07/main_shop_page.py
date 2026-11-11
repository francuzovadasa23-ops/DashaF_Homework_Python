from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class MainShopPage:
    BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    BOLT_T_SHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_items_and_go_to_cart(self):
        self.driver.find_element(*self.BACKPACK).click()
        self.driver.find_element(*self.BOLT_T_SHIRT).click()
        self.driver.find_element(*self.ONESIE).click()

        self.driver.find_element(*self.CART_LINK).click()
