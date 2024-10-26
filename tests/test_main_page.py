from pages.home_page import HomePage
from pages.order_feed_page import OrderFeedPage
from conftest import *
import allure


class TestMainPage: # Проверка основного функционала
    @allure.title('Проверка перехода по клику на "Конструктор"')
    def test_navigate_to_constructor_success(self, driver):
        home_page = HomePage(driver)
        home_page.click_header_feed_button()
        home_page.click_on_button_constructor()
        assert 'Соберите бургер' in home_page.get_text_on_title_of_constructor()

    @allure.title('Проверка перехода по клику на "Ленту заказов"')
    def test_navigate_to_order_history_success(self, driver):
        home_page = HomePage(driver)
        order_feed_page = OrderFeedPage(driver)
        home_page.click_header_feed_button()
        assert order_feed_page.get_text_on_title_of_orders_list() == 'Лента заказов'

    @allure.title('Проверка отображения окна "Детали ингредиента" при клике на ингредиент')
    def test_displaying_modal_window_details_of_ingredient_success(self, driver):
        home_page = HomePage(driver)
        home_page.click_on_ingredient()
        assert home_page.check_displaying_of_modal_details()

    @allure.title('Проверка закрытия окна "Детали ингредиента" кликом по крестику')
    def test_close_modal_window_details_of_ingredient_success(self, driver):
        home_page = HomePage(driver)
        home_page.click_on_ingredient()
        home_page.close_modal()
        assert home_page.check_not_displaying_of_modal_details()

    @allure.title('Проверка увеличения числа на счетчике при добавлении ингредиента в заказ')
    def test_changing_counter_for_ingredients_in_order_success(self, driver):
        home_page = HomePage(driver)
        home_page.drag_and_drop_ingredient_to_order()
        assert home_page.get_count_of_ingredients() == '2'

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_making_order_by_authenticated_user_success(self, driver, set_user_tokens):
        home_page = HomePage(driver)
        home_page.click_on_button_login_in_main()
        home_page.drag_and_drop_ingredient_to_order()
        home_page.click_on_button_make_order()
        assert home_page.check_displaying_of_confirmation_modal_of_order()
