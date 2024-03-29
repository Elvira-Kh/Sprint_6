import allure
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from data import *

class TestMainPage:
    @allure.title('Проверка переадресации при клике на логотип Яндекс')
    def test_redirect_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        main_page.switch_to_window()
        main_page.wait_navigating_url(data.dzen)
        assert main_page.get_url() == data.dzen

    @allure.title('Проверка возврата на главную страницу при клике на логотип Самоката')
    def test_redirect_samokat_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_samokat_logo()
        main_page.wait_navigating_url(data.scooter)
        assert main_page.get_url() == data.scooter
