from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium_test.locators.locators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser: webdriver.Chrome, timeout=10):
        """Инициализация браузера"""

        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def open(self, url):
        """Открыть страницу"""

        self.browser.get(url)

    def element_is_present(self, how, what):
        """Элемент присутствует на странице"""

        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def elements_are_present(self, how, what):
        """Элементы присутствуют на странице"""

        try:
            self.browser.find_elements(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """Элемент отсутствует на странице"""

        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        """Элемент исчезает со страницы"""

        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    def scroll_to_element(self, element):
        """Проскролить страницу до элемента"""

        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    def click_add_button(self):
        """Нажать на кнопку Добавить"""

        self.browser.find_element(*BasePageLocators.ADD_BUTTON).click()

    def get_element(self, by: str, value: str):
        """Получить элемент"""

        return self.browser.find_element(by, value)
