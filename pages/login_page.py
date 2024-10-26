from pages.base_page import BasePage
from locators import LoginPageLocators
from config import Urls
import allure


class LoginPage(BasePage):

    @allure.step('Открываем страницу Авторизации')
    def open_login_page(self):
        self.navigate_to(Urls.SIGN_IN_URL)

    @allure.step('Нажимаем на ссылку "Восстановить пароль"')
    def click_on_restore_password_link(self):
        self.is_element_invisible(LoginPageLocators.LOADING_ICON)
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step('Проверяем открытие страницы Авторизации')
    def verify_login_page_opened(self):
        return self.verify_page_opened(Urls.SIGN_IN_URL, LoginPageLocators.SIGN_IN_BUTTON)

