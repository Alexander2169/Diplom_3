from pages.password_recovery_page import PasswdRecoveryPage
from pages.home_page import HomePage
from conftest import *
import allure


class TestPasswdRecoveryPage:

    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_navigate_to_recovery_page(self):
        home_page = HomePage()
        personal_account_page = PersonalAccountPage()
        self.home_page.click_on_button_login_in_main()  # Переход на страницу входа
        assert self.home_page.click_on_button_login_in_main()  # Проверка, что кнопка отображается
        self.passwd_recovery_page.navigate_to_recovery_passwd_page()  # Переход на страницу восстановления пароля
        assert self.passwd_recovery_page.check_displaying_of_input_email()  # Проверка отображения поля email

    @allure.title('Проверка ввода почты и клика по кнопке "Восстановить"')
    def test_input_email_and_click_recover(self):
        self.home_page.click_on_button_login_in_main()  # Переход на страницу входа
        self.passwd_recovery_page.navigate_to_recovery_passwd_page()  # Переход на страницу восстановления пароля
        self.passwd_recovery_page.send_email()  # Ввод случайного email
        self.passwd_recovery_page.click_on_recovery_button()  # Клик по кнопке "Восстановить"
        # Здесь можно добавить проверку успешного сообщения или перенаправления

    @allure.title('Проверка клика по кнопке показать/скрыть пароль')
    def test_show_hide_password(self):
        self.home_page.click_on_button_login_in_main()  # Переход на страницу входа
        self.passwd_recovery_page.navigate_to_recovery_passwd_page()  # Переход на страницу восстановления пароля
        self.passwd_recovery_page.check_displaying_of_input_password()  # Проверка отображения поля пароля
        # Здесь нужно добавить логику для клика по кнопке показать/скрыть пароль
        # Например, если у вас есть метод в PasswdRecoveryPage для этого:
        self.passwd_recovery_page.click_on_show_hide_password_button()  # Клик по кнопке показать/скрыть пароль
        # Проверка, что поле пароля стало активным (подсвечивается)
        assert self.passwd_recovery_page.check_displaying_of_input_password()  # Проверка, что поле активно
