from pages.order_feed_page import OrderFeedPage
from pages.home_page import HomePage
from pages.order_history_page import OrderHistoryPage
from pages.personal_account_page import PersonalAccountPage
from conftest import *
import allure


class TestFeedPage:

    @allure.title('Проверка открытия всплывающего окна с деталями при клике на заказ')
    def test_displaying_modal_order_details_success(self, driver):
        home_page = HomePage(driver)
        order_feed_page = OrderFeedPage(driver)
        home_page.click_header_feed_button()
        order_feed_page.click_on_order_card()
        assert 'бургер' in order_feed_page.get_text_on_title_of_modal_order()

    @allure.title('Проверка отображения существующего заказа из истории пользователя в ленте')
    def test_displaying_in_feed_new_order_from_history_success(self, driver, create_user_and_order_and_delete,
                                                               set_user_tokens):
        home_page = HomePage(driver)
        personal_account_page = PersonalAccountPage(driver)
        order_history_page = OrderHistoryPage(driver)
        order_feed_page = OrderFeedPage(driver)
        home_page.click_on_personal_account_in_header()
        personal_account_page.click_on_order_history_button()
        order_id = order_history_page.get_id_of_order_card()
        home_page.click_header_feed_button()
        assert order_feed_page.check_id_order_in_feed(order_id)

    @allure.title('Проверка увеличения числа на счетчике общего количества выполненных заказов')
    def test_changes_counter_for_quantity_of_orders_success(self, driver, set_user_tokens):
        home_page = HomePage(driver)
        order_feed_page = OrderFeedPage(driver)
        home_page.click_header_feed_button()
        orders_count_1 = order_feed_page.get_quantity_of_orders()
        home_page.click_on_button_constructor()
        home_page.click_on_button_login_in_main()
        home_page.drag_and_drop_ingredient_to_order()
        home_page.click_on_button_make_order()
        home_page.click_on_button_close_confirmation_modal()
        home_page.click_header_feed_button()
        orders_count_2 = order_feed_page.get_quantity_of_orders()
        assert orders_count_1 < orders_count_2

    @allure.title('Проверка увеличения числа на счетчике ежедневного количества выполненных заказов')
    def test_changes_counter_for_daily_quantity_of_orders_success(self, driver, set_user_tokens):
        home_page = HomePage(driver)
        order_feed_page = OrderFeedPage(driver)
        home_page.click_header_feed_button()
        orders_count_1 = order_feed_page.get_daily_quantity_of_orders()
        home_page.click_on_button_constructor()
        home_page.click_on_button_login_in_main()
        home_page.drag_and_drop_ingredient_to_order()
        home_page.click_on_button_make_order()
        home_page.click_on_button_close_confirmation_modal()
        home_page.click_header_feed_button()
        orders_count_2 = order_feed_page.get_daily_quantity_of_orders()
        assert orders_count_1 < orders_count_2

    @allure.title('Проверка появления нового заказа в разделе "В работе"')
    def test_displaying_new_order_in_progress_feed_success(self, driver, set_user_tokens):
        home_page = HomePage(driver)
        order_feed_page = OrderFeedPage(driver)
        home_page.click_on_button_login_in_main()
        home_page.drag_and_drop_ingredient_to_order()
        home_page.click_on_button_make_order()
        new_order_id = home_page.get_number_of_order_in_modal_confirmation()
        home_page.click_on_button_close_confirmation_modal()
        home_page.click_header_feed_button()
        assert order_feed_page.get_order_number_in_feed_progress_section() == '0'+new_order_id
