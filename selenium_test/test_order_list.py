from selenium_test.pages.orders_list_page import OrdersListPage
from selenium_test.locators.locators import OrdersListPageLocators
from config import *


class TestFilters:
    link = f"{STAND_URL}/orders-list"

    def test_check_all_filters(self, browser):
        """Включение и выключение фильтров на странице заказов"""

        page = OrdersListPage(browser)
        page.open(self.link)
        page.click_settings_button()
        assert page.element_is_present(
            *OrdersListPageLocators.FILTER_SETTINGS_MODAL
        ), "Модальное окно настроек фильтров не открылось"
        page.click_checkbox(0)
        assert page.all_checkboxes_checked(), "Не все чекбоксы выбраны"
        page.click_save_button()
        assert page.is_disappeared(
            *OrdersListPageLocators.FILTER_SETTINGS_MODAL
        ), "Модальное окно настроек фильтров не закрылось"

        page.expand_filters()
        assert page.check_display_filters(0), "Не включились фильтры"
        page.click_settings_button()
        assert page.all_checkboxes_checked(), "Не все чекбоксы выбраны"
        page.click_checkbox(0)
        assert page.all_checkboxes_not_checked(), "Не все чекбоксы сняты"
        page.click_checkbox(0)
        page.click_reset_button()
        assert page.all_checkboxes_not_checked(), "Не все чекбоксы сняты"
        page.click_save_button()
        assert page.is_disappeared(
            *OrdersListPageLocators.FILTER_CUSTOMER
        ), "Фильтры не выключились"
