from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME = [By.XPATH, "//input[@placeholder='* Имя']"]
    LAST_NAME = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    ADDRESS = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    METRO = [By.CSS_SELECTOR, "input[placeholder='* Станция метро']"]
    STATION_1 = [By.XPATH, "//li[@class='select-search__row' and @data-index='0' and @data-value='1']"]
    STATION_2 = [By.XPATH, "//li[@class='select-search__row' and @data-index='3' and @data-value='4']"]
    PHONE = [By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']"]
    NEXT = [By.XPATH, "//button[text()='Далее']"]
    CALENDAR = [By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']"]
    DATE_1 = [By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--014']"]
    DATE_2 = [By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--015']"]
    RENT = [By.XPATH, "//div[text()='* Срок аренды']"]
    TERM_1 = [By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']"]
    TERM_2 = [By.XPATH, "//div[@class='Dropdown-option' and text()='трое суток']"]
    BLACK = [By.ID, "black"]
    GREY = [By.ID, "grey"]
    COMMENTS = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    ORDER = [By.XPATH, '//*[contains(@class,"Order_Buttons")]//button[text()="Заказать"]']
    YES = [By.XPATH, "//button[text()='Да']"]
    NO = [By.XPATH, "//button[text()='Нет']"]
    ORDER_SUCCESS_WINDOW = [By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]"]