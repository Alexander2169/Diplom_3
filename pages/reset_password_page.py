from base_page import BasePage
from locators import *
from config import *
import allure

class ResetPasswordPage(BasePage):

    @allure.step('Проверяем открытие страницы Сброса пароля')
    def verify_password_reset_page(self):
        return self.verify_page_opened(Urls.PASSWORD_RESET_URL, ChangePasswordLocators.SAVE_CHANGES_BUTTON)

    @allure.step('Кликаем по кнопке "глаз" и получаем атрибут поля Пароль')
    def reveal_password_and_get_attribute(self):
        self.is_element_invisible(ChangePasswordLocators.LOADING_ICON)
        self.click_element(ChangePasswordLocators.TOGGLE_PASSWORD_VISIBILITY_BUTTON)
        return self.get_element_attribute(ChangePasswordLocators.PASSWORD_INPUT_CONTAINER, 'class')