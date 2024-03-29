from selenium.webdriver.common.by import By


class MainPageLocators:

    YANDEX_BUTTON = [By.XPATH, '//img[@src="/assets/ya.svg"]']
    MAKE_ORDER_HEADER_BUTTON = [By.XPATH, "//button[contains(text(), 'Статус заказа')]/preceding-sibling::button"]
    MAKE_ORDER_SCOOTER_BUTTON = [By.XPATH, ".//button[contains(@class, 'Button_Middle')]"]
    COOKIE_BUTTON = [By.XPATH, '//*[@id="rcc-confirm-button"]']
    SCOOTER_ICON = [By.XPATH, '//img[@src="/assets/scooter.svg" and @alt="Scooter"]']
