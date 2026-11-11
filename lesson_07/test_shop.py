import pytest
from selenium import webdriver
from login_page import LoginPage
from main_shop_page import MainShopPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(driver):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("standard_user", "secret_sauce")

    main_page = MainShopPage(driver)
    main_page.add_items_and_go_to_cart()

    cart_page = CartPage(driver)
    assert cart_page.get_cart_title() == "Your Cart", \
        "Заголовок корзины неверный!"
    cart_page.click_checkout_button()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_personal_info("Даша", "Кошкина", "241000")

    total_price = checkout_page.get_total_price()
    assert total_price == "Total: $58.29", \
        f"Ожидалась сумма $58.29, но получено: {total_price}"
