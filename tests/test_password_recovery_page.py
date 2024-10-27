import helpers
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from conftest import *
import allure

class TestForgotPasswordPage:  # Страница Восстановления пароля

    @allure.title('Проверка перехода на страницу Восстановления пароля по кнопке "Восстановить пароль"')
    def test_navigate_to_forgot_password_page(self, driver):
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        login_page.open_login_page()
        login_page.click_on_restore_password_link()

        assert forgot_password_page.verify_password_recovery_page()

    @allure.title('Проверка ввода почты и работа кнопки "Восстановить" на странице Восстановления пароля')
    def test_email_submission_for_password_recovery(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)
        forgot_password_page.navigate_to_password_recovery()
        email = helpers.generate_user_info()['email']
        forgot_password_page.submit_email_for_recovery(email)

        assert reset_password_page.verify_password_reset_page()

    @allure.title('Клик по кнопке "глаз" у пароля делает поле активным — подсвечивает его')
    def test_highlight_password_field(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)
        forgot_password_page.navigate_to_password_recovery()
        forgot_password_page.submit_email_for_recovery(helpers.generate_user_info()['email'])
        attribute_password = reset_password_page.reveal_password_and_get_attribute()

        assert 'status_active' in attribute_password


