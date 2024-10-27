import helpers
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from conftest import *
import allure


class TestForgotPasswordPage:

    @allure.title('Проверка перехода на страницу Восстановления пароля по кнопке "Восстановить пароль"')
    def test_go_to_password_recovery_page_by_clicking_recover_password_button(self, driver):
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        # Открываем страницу авторизации
        login_page.open_login_page()

        # Переходим на страницу восстановления пароля
        login_page.click_on_restore_password_link()

        # Проверяем, что страница восстановления пароля открыта
        assert forgot_password_page.verify_password_recovery_page()

    @allure.title('Проверка ввода почты и работа кнопки "Восстановить" на странице Восстановления пароля')
    def test_recovery_button_functionality(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)

        # Открываем страницу восстановления пароля
        forgot_password_page.navigate_to_password_recovery()

        # Генерируем случайный email и отправляем его для восстановления
        email = helpers.generate_user_info()['email']
        forgot_password_page.submit_email_for_recovery(email)

        # Проверяем, что страница сброса пароля открыта
        assert reset_password_page.verify_password_reset_page()

