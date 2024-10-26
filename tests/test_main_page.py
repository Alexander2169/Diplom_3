import pytest
import allure
from pages.home_page import *
from pages.personal_account_page import *
from pages.order_feed_page import *

@pytest.mark.usefixtures("driver", "set_user_tokens")
class TestMainFunctionality:



    @allure.title('Проверка перехода по клику на "Конструктор"')
    def test_navigate_to_constructor(self):
        self.home_page.click_on_button_constructor()
        assert self.home_page.get_text_on_title_of_constructor() == "Конструктор"

    @allure.title('Проверка перехода по клику на "Лента заказов"')
    def test_navigate_to_order_feed(self):
        self.home_page.click_header_feed_button()
        assert self.order_feed_page.get_text_on_title_of_orders_list() == "Лента заказов"

    @allure.title('Проверка всплывающего окна с деталями ингредиента')
    def test_ingredient_details_popup(self):
        self.home_page.click_on_ingredient()
        assert self.home_page.check_displaying_of_modal_details()  # Проверка, что модальное окно открыто
        self.home_page.close_modal()  # Закрытие модального окна
        assert not self.home_page.check_displaying_of_modal_details()  # Проверка, что модальное окно закрыто

    @allure.title('Проверка увеличения каунтера ингредиента при добавлении')
    def test_ingredient_counter_increase(self):
        initial_count = int(self.home_page.get_count_of_ingredients())
        self.home_page.drag_and_drop_ingredient_to_order()  # Добавление ингредиента
        new_count = int(self.home_page.get_count_of_ingredients())
        assert new_count == initial_count + 1  # Проверка, что каунтер увеличился на 1

    @allure.title('Проверка оформления заказа залогиненным пользователем')
    def test_place_order_as_logged_in_user(self):
        self.home_page.click_on_button_make_order()  # Клик по кнопке "Оформить заказ"
        assert self.home_page.check_displaying_of_confirmation_modal_of_order()  # Проверка, что модальное окно подтверждения заказа отображается
        order_number = self.home_page.get_number_of_order_in_modal_confirmation()  # Получение номера заказа
        assert order_number is not None  # Проверка, что номер заказа получен
        self.home_page.click_on_button_close_confirmation_modal()  # Закрытие модального окна

