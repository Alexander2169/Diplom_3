from base_page import BasePage
from locators import *
from config import *
import allure

class ForgotPasswordPage(BasePage):

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


