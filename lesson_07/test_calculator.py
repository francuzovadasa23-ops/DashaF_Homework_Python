import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator(driver):
    page = CalculatorPage(driver)
    page.open_page()
    page.set_delay(45)
    page.click_button()
    result = page.get_result()
    assert result == "15", f"Ожидалось '15', но на экране: '{result}'"
