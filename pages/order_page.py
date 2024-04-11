from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
import allure


class OrderPage(BasePage):
    @allure.step('Клик на кнопку "Заказать" в хедере')
    def click_header_order_btn(self):
        self.click_to_element(MainPageLocators.ORDER_BTN_HEADER)

    @allure.step('Клик на кнопку "Заказать" в середине страницы')
    def click_main_order_btn(self):
        self.click_to_element(MainPageLocators.ORDER_BTN_PAGE)

    @allure.step('Заполнение поля "Имя"')
    def set_name(self, name):
        self.set_text(OrderPageLocators.NAME_FIELD, name)

    @allure.step('Заполнение поля "Фамилия"')
    def set_last_name(self, last_name):
        self.set_text(OrderPageLocators.LAST_NAME_FIELD, last_name)

    @allure.step('Заполнение поля "Адрес"')
    def set_address(self, address):
        self.set_text(OrderPageLocators.ADDRESS_FIELD, address)

    @allure.step('Выбор станции метро')
    def set_metro(self, station_locator):
        self.click_to_element(OrderPageLocators.METRO_FIELD)
        self.click_to_element(station_locator)

    @allure.step('Заполнение поля "Телефон"')
    def set_phone(self, phone):
        self.set_text(OrderPageLocators.PHONE_FIELD, phone)

    @allure.step('Клик по кнопке "Далее"')
    def click_next_btn(self):
        self.click_to_element(OrderPageLocators.NEXT_BTN)

    @allure.step('Выбор даты доставки')
    def set_date(self, date_locator):
        self.click_to_element(OrderPageLocators.DATE_FIELD)
        self.click_to_element(date_locator)

    @allure.step('Выбор срока аренды')
    def set_term(self, term_locator):
        self.click_to_element(OrderPageLocators.RENT_FIELD)
        self.click_to_element(term_locator)

    @allure.step('Выбор цвета')
    def set_color(self, color_locator):
        self.click_to_element(color_locator)

    @allure.step('Заполнение поля "Комментарии"')
    def set_comments(self, comments):
        self.set_text(OrderPageLocators.COMMENTS, comments)

    @allure.step('Окно "Заказ оформлен"')
    def check_success_order(self):
        return self.get_text(OrderPageLocators.ORDER_SUCCESS_WINDOW)

    @allure.step('Создание заказа')
    def create_order(self, name, last_name, address, station_locator, phone, date_locator, term_locator, color_locator, comments):
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_metro(station_locator)
        self.set_phone(phone)
        self.click_next_btn()
        self.set_date(date_locator)
        self.set_term(term_locator)
        self.set_color(color_locator)
        self.set_comments(comments)
        self.click_to_element(OrderPageLocators.ORDER_BTN)
        self.click_to_element(OrderPageLocators.YES_BTN)

    @allure.step('Создание заказа через кнопку в хедере')
    def create_order_via_header_button(self, main_page, data):
        main_page.click_header_order_btn()
        self.create_order(data.name, data.last_name, data.address, data.station_locator, data.phone, data.date_locator,
                          data.term_locator, data.color_locator, data.comment)

    @allure.step('Создание заказа через кнопку в середине страницы')
    def create_order_via_main_button(self, main_page, data):
        main_page.click_main_order_btn()
        self.create_order(data.name, data.last_name, data.address, data.station_locator, data.phone, data.date_locator,
                          data.term_locator, data.color_locator, data.comment)