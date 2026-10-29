from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()
    # Откройте страницу https://gitflic.ru/.
    driver.get("https://gitflic.ru/")

    # Установите cookie пользователя 1.
    driver.add_cookie({
        "name": "SESSION",
        "value": "NzdiYTIzMGUtZDY0ZC00NWJiLThjMTctNzUxMTYzOTkwMzNk",
        "domain": "gitflic.ru"
    })
    # Обновите страницу.
    driver.refresh()
    # Перейдите на страницу пользователя 1.
    driver.get("https://gitflic.ru/user/airsworld")
    # Сохраните текущий URL.
    current_url_1 = driver.current_url
    assert "gitflic.ru/user/airsworld" in current_url_1
    # Разлогиньтесь (очистите куки).
    driver.delete_all_cookies()

    # Установите cookie пользователя 2.
    driver.add_cookie({
        "name": "SESSION",
        "value": "OTkwYjllZGItNzI5MS00ZGMxLWJhOWUtZTk5YjhhNTQyMzhm",
        "domain": "gitflic.ru"
    })
    # Обновите страницу.
    driver.refresh()
    # Перейдите на страницу пользователя 2.
    driver.get("https://gitflic.ru/user/tiktakgrabber")
    # Сохраните текущий URL.
    current_url_2 = driver.current_url
    assert "gitflic.ru/user/tiktakgrabber" in current_url_2

    # Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
    assert current_url_1 != current_url_2

    driver.quit()
