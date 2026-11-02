from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)
    # 1. Откройте страницу:
    # https://bonigarcia.dev/selenium-webdriver-java/data-types.html
    # в браузере Edge (если вы работаете в Windows).
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # 2. Заполните форму значениями:
    # First name: Иван
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    # Last name: Петров
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    # Address: Ленина, 55-3
    driver.find_element(
        By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
    # Email: test@skypro.com
    driver.find_element(
        By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
    # Phone number: +7985899998787
    driver.find_element(
        By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
    # Zip code: *оставить пустым
    driver.find_element(By.NAME, "zip-code").clear()
    # City: Москва
    driver.find_element(
        By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
    # Country: Россия
    driver.find_element(
        By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
    # Job position: QA
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    # Company: SkyPro
    driver.find_element(
        By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")

    # 3. Нажмите кнопку Submit.
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # 4. Проверьте (assert), что поле Zip code подсвечено красным.
    zip_code = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div[id='zip-code']")))
    assert "alert-danger" in zip_code.get_attribute("class")

    # 5. Проверьте (assert), что остальные поля подсвечены зеленым.
    success_alerts = driver.find_elements(By.CSS_SELECTOR, ".alert-success")
    assert len(success_alerts) == 9

    driver.quit()
