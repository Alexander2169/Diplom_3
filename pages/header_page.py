from base_page import BasePage
from locators import NavigationHeaderLocators
import allure

class HeaderPage(BasePage):

    @allure.step('Нажимаем на ссылку "Конструктор"')
    def click_on_constructor_link(self):
        self.is_element_invisible(NavigationHeaderLocators.LOADING_ICON)
        self.click_element(NavigationHeaderLocators.CONSTRUCTOR_LINK)

    @allure.step('Нажимаем на ссылку "Лента Заказов"')
    def click_on_orders_feed_link(self):
        self.is_element_invisible(NavigationHeaderLocators.LOADING_ICON)
        self.click_element(NavigationHeaderLocators.ORDERS_FEED_LINK)

    @allure.step('Нажимаем на ссылку "Личный кабинет"')
    def click_on_personal_account_link(self):
        self.is_element_invisible(NavigationHeaderLocators.LOADING_ICON)
        self.click_element(NavigationHeaderLocators.ACCOUNT_LINK)

