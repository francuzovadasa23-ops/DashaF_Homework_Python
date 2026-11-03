from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 50)
    # 1. Откройте страницу:
    # https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
    # в Google Chrome.
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # 2. В поле ввода по локатору #delay введите значение 45.
    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # 3. Нажмите на кнопки: 7+8=
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # 4. Проверьте (assert), что в окне отобразится результат 15
    # через 45 секунд.
    wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, ".screen"), "15"))
    result = driver.find_element(By.CSS_SELECTOR, ".screen")
    assert result.text.strip() == "15"

    driver.quit()
