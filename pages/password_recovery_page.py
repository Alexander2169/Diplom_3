from base_page import BasePage
from locators import *
from config import *
import allure

class PasswordRecoveryPage(BasePage):

    @allure.step('Открываем страницу Восстановления пароля')
    def navigate_to_password_recovery(self):
        self.navigate_to(Urls.PASSWORD_RECOVERY_URL)

    @allure.step('Проверяем открытие страницы Восстановления пароля')
    def verify_password_recovery_page(self):
        return self.verify_page_opened(Urls.PASSWORD_RECOVERY_URL, PasswordRecoveryLocators.RESTORE_PASSWORD_BUTTON)

    @allure.step('Вводим email и нажимаем кнопку "Восстановить"')
    def submit_email_for_recovery(self, email):
        self.is_element_invisible(PasswordRecoveryLocators.LOADING_ICON)
        self.input_text(PasswordRecoveryLocators.EMAIL_FIELD, email)
        self.click_element(PasswordRecoveryLocators.RESTORE_PASSWORD_BUTTON)

    @allure.step('Проверяем открытие страницы Сброса пароля')
    def verify_password_reset_page(self):
        return self.verify_page_opened(Urls.PASSWORD_RESET_URL, ResetPasswordPageLocators.SAVE_BUTTON)

    @allure.step('Кликаем по кнопке "глаз" и получаем атрибут поля Пароль')
    def reveal_password_and_get_attribute(self):
        self.is_element_invisible(ResetPasswordPageLocators.LOADING_ICON)
        self.click_element(ResetPasswordPageLocators.EYE_BUTTON)
        return self.get_element_attribute(ResetPasswordPageLocators.PASSWORD_DIV, 'class')
