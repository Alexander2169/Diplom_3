from conftest import *
from pages.personal_account_page import PersonalAccountPage
from pages.home_page import HomePage
from pages.order_history_page import OrderHistoryPage

class TestPersonalAccountPage: # Личный кабинет

    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    def test_click_go_to_your_personal_account(self, driver, set_user_tokens):
        home_page = HomePage(driver)
        personal_account_page = PersonalAccountPage(driver)

        # Переход в личный кабинет
        home_page.click_on_personal_account_in_header()
        personal_account_page.wait_visibility_of_description()
        assert personal_account_page.check_displaying_of_description()+

    @allure.title('Проверка перехода в раздел «История заказов»')
    def test_go_to_order_history_section(self, driver, set_user_tokens, create_user_and_order_and_delete):
        home_page = HomePage(driver)
        personal_account_page = PersonalAccountPage(driver)
        order_history_page = OrderHistoryPage(driver)

        # Переход в разднл "История заказов"
        home_page.click_on_personal_account_in_header()
        personal_account_page.wait_visibility_of_description()
        personal_account_page.click_on_order_history_button()
        order_history_page.wait_visibility_of_order_card()
        assert 'метеоритный' in order_history_page.get_text_of_order_card_title()

    @allure.title('Проверка выхода из аккаунта')
    def test_logout(self, driver, set_user_tokens):
        home_page = HomePage(driver)
        personal_account_page = PersonalAccountPage(driver)

        # Выход из аккаунта
        home_page.click_on_personal_account_in_header()
        personal_account_page.wait_visibility_of_description()
        personal_account_page.click_on_logout_button()
        personal_account_page.wait_visibility_of_button_register()
        assert personal_account_page.check_displaying_of_button_register()



