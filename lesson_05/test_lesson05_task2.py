from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    # Откройте страницу https://httpbin.qa-territory.online/forms/post.
    driver.get("https://httpbin.qa-territory.online/forms/post")
    sleep(3)
    # Найдите поле ввода с названием custname.
    # Введите в него ваше имя.
    driver.find_element(
        By.NAME, "custname").send_keys("Dasha")
    sleep(3)
    # Найдите кнопку Submit и нажмите на нее.
    driver.find_element(
        By.CSS_SELECTOR, "[type='submit']").click()
    sleep(3)
    # Проверьте, что после нажатия URL изменился
    # на https://httpbin.qa-territory.online/post.
    driver.current_url == "https://httpbin.qa-territory.online/post"

    driver.quit()
