from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    # 1. Откройте сайт магазина: https://www.saucedemo.com/ в FireFox.
    driver.get("https://www.saucedemo.com/")

    # 2. Авторизуйтесь как пользователь standard_user.
    driver.add_cookie({
        "name": "session-username",
        "value": "standard_user",
        "domain": "www.saucedemo.com"
    })
    driver.refresh()
    driver.get("https://www.saucedemo.com/inventory.html")

    # 3. Добавьте в корзину товары:
    # - Sauce Labs Backpack.
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    # - Sauce Labs Bolt T-Shirt.
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    # - Sauce Labs Onesie.
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    # 4. Перейдите в корзину.
    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

    # 5. Нажмите Checkout.
    driver.find_element(By.ID, "checkout").click()

    # 6. Заполните форму своими данными:
    # - имя,
    driver.find_element(By.ID, "first-name").send_keys("Даша")
    # - фамилия,
    driver.find_element(By.ID, "last-name").send_keys("Кошкина")
    # - почтовый индекс.
    driver.find_element(By.ID, "postal-code").send_keys("241000")

    # 7. Нажмите кнопку Continue.
    driver.find_element(By.ID, "continue").click()

    # 8. Прочитайте со страницы итоговую стоимость (Total).
    wait.until(EC. visibility_of_element_located(
        (By.CSS_SELECTOR, ".summary_total_label")))

    # 9. Проверьте, что итоговая сумма равна $58.29.
    total_sum = driver.find_element(By.CSS_SELECTOR, ".summary_total_label")
    assert "$58.29" in total_sum.text

    # 9. Закройте браузер.
    driver.quit()
