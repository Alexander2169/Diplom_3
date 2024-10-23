from pages.base_page import BasePage
from locators import PasswordRecoveryLocators
from helpers import *
import allure


class PasswdRecoveryPage(BasePage): # Класс для работы со страницей восстановления пароля

    @allure.title('Открыть страницу восстановления пароля')
    def navigate_to_recovery_passwd_page(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.FORGOT_PASSWORD_BUTTON)
        self.click_on_element(PasswordRecoveryLocators.FORGOT_PASSWORD_BUTTON)

    @allure.title('Проверить отображение поля email')
    def check_displaying_of_input_email(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.EMAIL_INPUT)

    @allure.title('Ввести email')
    def send_email(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.EMAIL_INPUT)
        email = create_random_email()
        self.send_keys_to_input(PasswordRecoveryLocators.EMAIL_INPUT, email)

    @allure.title('Кликнуть на кнопку "Восстановить"')
    def click_on_recovery_button(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.RECOVER_BUTTON)
        self.click_on_element(PasswordRecoveryLocators.RECOVER_BUTTON)

    @allure.title('Проверить отображение поля password')
    def check_displaying_of_input_password(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.PASSWORD_INPUT)

