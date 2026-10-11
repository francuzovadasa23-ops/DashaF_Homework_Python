from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 16 Pro", "+79001234567"),
    Smartphone("Samsung", "Galaxy S25 Ultra", "+79162345678"),
    Smartphone("Xiaomi", "Xiaomi 15", "+79253456789"),
    Smartphone("Google", "Pixel 9", "+79034567890"),
    Smartphone("Huawei", "Pura 70 Pro", "+79995678901")
    ]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} - {smartphone.number}")
