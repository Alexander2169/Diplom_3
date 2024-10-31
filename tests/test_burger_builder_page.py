from pages.burger_builder_page import BurgerBuilderPage
from helpers import *
from conftest import *
import allure

class TestBurgerBuilderPage:  # Страница конструктора бургеров

    @allure.title('Проверка открытия всплывающего окна с деталями, если кликнуть на ингредиент')
    def test_open_modal_window_on_ingredient_click(self, driver):
        burger_builder_page = BurgerBuilderPage(driver)
        burger_builder_page.navigate_to_constructor()
        ingredient_id = fetch_random_ingredient_id()
        burger_builder_page.select_random_ingredient(ingredient_id)

        burger_builder_page.wait_for_ingredient_detail_modal_to_open()
        assert burger_builder_page.verify_ingredient_detail_modal(ingredient_id)

    @allure.title('Проверка закрытия всплывающего окна с деталями ингридиента, если кликнуть на "крестик"')
    def test_close_modal_window_on_cross_click(self, driver):
        burger_builder_page = BurgerBuilderPage(driver)
        burger_builder_page.navigate_to_constructor()
        ingredient_id = fetch_random_ingredient_id()
        burger_builder_page.select_random_ingredient(ingredient_id)
        burger_builder_page.close_ingredient_detail_modal()

        burger_builder_page.wait_for_ingredient_detail_modal_to_close()
        assert burger_builder_page.verify_ingredient_detail_modal_closed()

    @allure.title('Проверка увеличения счетчика ингредиента при добавлении этого ингредиента в заказ')
    def test_increase_counter_on_ingredient_addition(self, driver):
        burger_builder_page = BurgerBuilderPage(driver)
        burger_builder_page.navigate_to_constructor()
        ingredient_id = fetch_random_ingredient_id()
        before_ingredient_counter = burger_builder_page.get_ingredient_counter_value(ingredient_id)
        burger_builder_page.move_ingredient_to_basket(ingredient_id)

        burger_builder_page.wait_for_ingredient_counter_to_increase(ingredient_id, before_ingredient_counter)
        after_ingredient_counter = burger_builder_page.get_ingredient_counter_value(ingredient_id)

        assert int(after_ingredient_counter) > int(before_ingredient_counter), f"Expected counter to increase: {before_ingredient_counter} -> {after_ingredient_counter}"

    @allure.title('Проверка оформления заказа авторизованным пользователем')
    def test_order_creation_by_logged_in_user(self, driver, login_new_user):
        burger_builder_page = BurgerBuilderPage(driver)
        burger_builder_page.navigate_to_constructor()

        bun_id = fetch_random_bun_id()
        ingredient_id = fetch_random_ingredient_id()
        burger_builder_page.move_ingredient_to_basket(bun_id)
        burger_builder_page.move_ingredient_to_basket(ingredient_id)
        burger_builder_page.press_order_button()

        assert burger_builder_page.verify_success_screen_with_order_number(), "Order was not successfully created."






