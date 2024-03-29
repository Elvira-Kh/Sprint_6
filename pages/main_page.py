from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure


class MainPage(BasePage):
    @staticmethod
    @allure.step('Перейти по ссылке')
    def check_redirect_dzen(cls):
        cls.switch_to_window()
    @allure.step('Клик на вопрос')
    def click_question(self, number):
        method, locator = MainPageLocators.QUESTION
        locator = locator.format(number)
        self.click_to_element((method, locator))

    @allure.step('Получение ответа')
    def get_answer(self, number):
        method, locator = MainPageLocators.ANSWER
        locator = locator.format(number)
        return self.get_text((method, locator))

    @allure.step('Клик на лого Яндекс')
    def click_yandex_logo(self):
        self.click_to_element(MainPageLocators.YANDEX_LOGO)


    @allure.step('Клик на лого Самокат')
    def click_samokat_logo(self):
        self.click_to_element(MainPageLocators.SAMOKAT_LOGO)

    @allure.step('Клик на кнопку "Заказать" в хедере')
    def click_header_order_btn(self):
        self.click_to_element(MainPageLocators.ORDER_BTN_HEADER)

    @allure.step('Клик на кнопку "Заказать" в середине главной страницы')
    def click_main_order_btn(self):
        self.click_to_element(MainPageLocators.ORDER_BTN_PAGE)

    @allure.step('Принятие куки')
    def accept_cookies(self):
        self.click_to_element(MainPageLocators.COOKIES_BTN)

