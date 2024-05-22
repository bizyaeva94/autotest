from .base_page import BasePage
from selenium_test.locators.locators import OrdersListPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class OrdersListPage(BasePage):
    locators = OrdersListPageLocators

    def click_settings_button(self):
        """Клик на кнопку 'Настройки' фильтров"""

        settings_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.locators.SETTINGS_BUTTON)
        )
        settings_button.click()

    def click_save_button(self):
        """Клик на кнопку 'Сохранить' фильтры"""

        save_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.locators.FILTER_SAVE_BUTTON)
        )
        save_button.click()

    def expand_filters(self):
        """Развернуть фильтры"""

        if not self.browser.find_element(*OrdersListPageLocators.APPLY_FILTERS).is_displayed():
            self.browser.find_element(*self.locators.EXPAND_MORE).click()

    def click_reset_button(self):
        """Клик на кнопку 'Сбросить' фильтры"""

        reset_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.locators.FILTER_RESET_BUTTON)
        )
        reset_button.click()

    def click_checkbox(self, index):
        """
        Клик на чекбокс с указанным индексом
        :param index: индекс чекбокса в списке всех чекбоксов
        """

        self.browser.find_elements(*self.locators.FILTER_CHECKBOXES)[index].click()

    def check_checkbox(self, index):
        """
        Проверяет, включен ли чекбокс с указанным индексом
        :param index: индекс чекбокса в списке всех чекбоксов
        :return: True - включен, False - выключен
        """

        return self.browser.find_elements(*self.locators.FILTER_CHECKBOXES)[index].is_selected()

    def all_checkboxes_checked(self):
        """
        Проверяет, что все чекбоксы включены
        :return: True - все чекбоксы включены, False - есть выключенные чекбоксы
        """

        counter = len(self.browser.find_elements(*self.locators.FILTER_CHECKBOXES))
        all_checkboxes = []
        for i in range(counter):
            all_checkboxes.append(self.browser.find_elements(*self.locators.FILTER_CHECKBOXES)[i].is_selected())
        return all(all_checkboxes)

    def all_checkboxes_not_checked(self):
        """
        Проверяет, что все чекбоксы выключены
        :return: True - все чекбоксы выключены, False - есть включенные чекбоксы
        """

        counter = len(self.browser.find_elements(*self.locators.FILTER_CHECKBOXES))
        all_checkboxes = []
        for i in range(counter):
            all_checkboxes.append(not self.browser.find_elements(*self.locators.FILTER_CHECKBOXES)[i].is_selected())
        return all(all_checkboxes)

    def check_display_filters(self, index):
        """
        Проверяет, что фильтры на странице отображаются
        :param index: индекс конкретного фильтра из списка всех фильтров
        :return: True - фильтры есть на странице, False - фильтров нет на странице
        """

        return self.browser.find_elements(*self.locators.FILTER_CUSTOMER)[index].is_displayed()
