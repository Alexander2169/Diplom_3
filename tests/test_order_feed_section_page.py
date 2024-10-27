from pages.personal_page import PersonalPage
from pages.order_page import *
from helpers import *
from conftest import *
import allure

class TestOrderPage:  # Страница заказов

    @allure.title('Проверка открытия всплывающего окна с деталями, если кликнуть на заказ')
    def test_open_order_detail_modal(self, driver):
        order_page = OrderPage(driver)
        order_page.open_order_feed()
        order_page.select_last_order()

        assert order_page.is_order_detail_modal_visible()

    @allure.title('Проверка, что заказы пользователя из раздела "История заказов" отображаются на странице "Лента заказов"')
    def test_orders_in_history_and_feed(self, driver, login_new_user):
        access_token = login_new_user['accessToken']
        place_order(access_token)  # Создание заказа через API
        personal_page = PersonalPage(driver)
        personal_page.open_personal_account()
        personal_page.access_order_history()

        order_page = OrderHistoryPage(driver)
        history_order_number = order_page.fetch_first_order_number()

        order_page = OrderPage(driver)
        order_page.open_order_feed()
        feed_order_number = order_page.fetch_last_order_number()

        assert history_order_number == feed_order_number

    @allure.title('Проверка, что при создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_completed_counter_increased(self, driver, login_new_user):
        access_token = login_new_user['accessToken']
        order_page = OrderPage(driver)
        order_page.open_order_feed()
        counter_before_order = int(order_page.fetch_total_completed_counter())
        place_order(access_token)  # Создание заказа через API
        counter_after_order = int(order_page.fetch_total_completed_counter())

        assert (counter_after_order - counter_before_order == 1)

    @allure.title('Проверка, что при создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_today_counter_increased(self, driver, login_new_user):
        access_token = login_new_user['accessToken']
        order_page = OrderPage(driver)
        order_page.open_order_feed()
        counter_before_order = int(order_page.fetch_today_completed_counter())
        place_order(access_token)  # Создание заказа через API
        counter_after_order = int(order_page.fetch_today_completed_counter())

        assert (counter_after_order - counter_before_order == 1)

    @allure.title('Проверка, что после оформления заказа его номер появляется в разделе "В работе"')
    def test_order_number_in_progress(self, driver, login_new_user):
        access_token = login_new_user['accessToken']
        order_page = OrderPage(driver)
        order_page.open_order_feed()
        order_number = str(place_order(access_token))  # Создание заказа через API
        order_number_in_progress = order_page.fetch_order_number_in_progress()  # Получаем номер заказа в работе

        # Удаляем ведущие нули для корректного сравнения
        assert order_number.lstrip('0') == order_number_in_progress.lstrip('0'), \
            f"Ожидался номер заказа '{order_number}', но получено: '{order_number_in_progress}'"


