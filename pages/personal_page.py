from base_page import BasePage
from locators import *
from config import Urls
import allure

class PersonalPage(BasePage):

    @allure.step('Открываем Личный кабинет')
    def open_personal_account(self):
        self.navigate_to(Urls.USER_ACCOUNT_URL)

    @allure.step('Проверяем открытие страницы с Личным кабинетом')
    def verify_personal_account_page(self):
        return self.verify_page_opened(Urls.USER_PROFILE_URL, UserProfileLocators.PROFILE_PAGE_LINK)

    @allure.step('Нажимаем на ссылку "История заказов"')
    def access_order_history(self):
        self.is_element_invisible(UserProfileLocators.LOADING_ICON)
        self.click_element(UserProfileLocators.ORDER_HISTORY_PAGE_LINK)

    @allure.step('Нажимаем на ссылку "Выход"')
    def logout(self):
        self.is_element_invisible(UserProfileLocators.LOADING_ICON)
        self.click_element(UserProfileLocators.LOGOUT_BUTTON)


