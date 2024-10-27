from pages.header_page import HeaderPage
from pages.personal_page import PersonalPage
from pages.order_page import OrderHistoryPage
from pages.login_page import LoginPage
from conftest import *
import allure


class TestPersonalAccountPage:  # Страница личного кабинета

    @allure.title('Проверка перехода в профиль по кнопке "Личный Кабинет"')
    def test_navigate_to_profile_page_via_personal_area_button(self, driver, login_new_user):
        header_page = HeaderPage(driver)
        personal_page = PersonalPage(driver)
        header_page.click_on_personal_account_link()

        assert personal_page.verify_personal_account_page()

    @allure.title('Проверка перехода в раздел "История заказов"')
    def test_navigate_to_order_history_page_via_order_history_link(self, driver, login_new_user):
        personal_page = PersonalPage(driver)
        order_history_page = OrderHistoryPage(driver)
        personal_page.open_personal_account()
        personal_page.access_order_history()

        assert order_history_page.verify_order_history_page()

    @allure.title('Проверка разлогина юзера по кнопке "Выход"')
    def test_logout_via_exit_link(self, driver, login_new_user):
        personal_page = PersonalPage(driver)
        login_page = LoginPage(driver)
        personal_page.open_personal_account()
        personal_page.logout()

        assert login_page.verify_login_page_opened()

