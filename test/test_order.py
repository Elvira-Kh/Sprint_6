from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import user_1, user_2
import allure


class TestOrderPage:
    @allure.title('Проверка оформления заказа по кнопке "Заказать" в хедере')
    def test_create_order_header(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.accept_cookies()
        order_page.create_order_via_header_button(main_page,user_1)
        text = order_page.check_success_order()
        assert 'Заказ оформлен' in text

    @allure.title('Проверка оформления заказа по кнопке "Заказать" в середине страницы')
    def test_create_order_scooter(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.accept_cookies()
        order_page.create_order_via_main_button(main_page, user_2)
        text = order_page.check_success_order()
        assert 'Заказ оформлен' in text