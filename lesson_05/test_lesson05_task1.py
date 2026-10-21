from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    # Откройте страницу https://httpbin.qa-territory.online.
    driver.get("https://httpbin.qa-territory.online/")
    sleep(3)
    # Найдите и кликните на ссылку HTML Form.
    driver.find_element(By.LINK_TEXT, "HTML Form").click()
    sleep(3)
    # Проверьте, что URL изменился на /forms/post.
    driver.current_url == "https://httpbin.qa-territory.online/forms/post"
    # Вернитесь назад на главную страницу.
    driver.back()
    sleep(3)
    # Проверьте, что вернулись на исходный URL.
    driver.current_url == "https://httpbin.qa-territory.online/"

    driver.quit()
