from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from helpers import generate_user_info
import allure


class TestForgotPasswordPage:

    @allure.title('Проверка перехода на страницу Восстановления пароля по кнопке "Восстановить пароль"')
    def test_go_to_password_recovery_page_by_clicking_recover_password_button(self, driver):
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        login_page.open_login_page()
        login_page.click_on_restore_password_link()

        assert forgot_password_page.verify_password_recovery_page()

    @allure.title('Проверка ввода почты и работа кнопки "Восстановить" на странице Восстановления пароля')
    def test_recovery_button_functionality(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)

        forgot_password_page.navigate_to_password_recovery()
        email = generate_user_info()['email']
        forgot_password_page.submit_email_for_recovery(email)

        assert reset_password_page.verify_password_reset_page()

