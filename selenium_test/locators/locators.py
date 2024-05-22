from selenium.webdriver.common.by import By


class BasePageLocators:
    ADD_BUTTON = (By.XPATH, "//button[text()='Добавить']")


class AuthLocators:
    LOGIN_INPUT = (By.XPATH, "//label[text()='Логин']/parent::*//input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")


class OrdersListPageLocators:
    SETTINGS_BUTTON = (By.XPATH, "//button[text()='Настроить']")
    FILTER_SETTINGS_MODAL = (By.XPATH, "//div[@role='dialog']//*[text()='Настройка фильтров']")
    FILTER_CHECKBOXES = (By.XPATH, "//div[@role='dialog']//input")
    FILTER_SAVE_BUTTON = (By.XPATH, "//div[@role='dialog']//button[text()='Сохранить']")
    FILTER_RESET_BUTTON = (By.XPATH, "//div[@role='dialog']//button[text()='Сбросить']")
    EXPAND_MORE = (By.XPATH, "//*[text()='Фильтры']/following-sibling::button/*[@data-testid='ExpandMoreIcon']")
    APPLY_FILTERS = (By.XPATH, "//button[text()='Применить']")
    FILTER_CUSTOMER = (By.XPATH, "//h6[text()='Покупатель']/parent::div/following-sibling::div")
