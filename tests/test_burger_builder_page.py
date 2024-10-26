from pages.burger_builder_page import BurgerBuilderPage
from helpers import *
from conftest import *
import allure
from time import sleep  # Импортируем sleep для ожидания

class TestBurgerBuilderPage:

    @allure.title('Проверка открытия всплывающего окна с деталями, если кликнуть на ингредиент')
    def test_open_modal_window_on_ingredient_click(self, driver):
        burger_builder_page = BurgerBuilderPage(driver)
        burger_builder_page.navigate_to_constructor()
        ingredient_id = fetch_random_ingredient_id()
        burger_builder_page.select_random_ingredient(ingredient_id)

        assert burger_builder_page.verify_ingredient_detail_modal(ingredient_id)

    @allure.title('Проверка закрытия всплывающего окна с деталями ингридиента, если кликнуть на "крестик"')
    def test_close_modal_window_on_cross_click(self, driver):
        burger_builder_page = BurgerBuilderPage(driver)
        burger_builder_page.navigate_to_constructor()
        ingredient_id = fetch_random_ingredient_id()
        burger_builder_page.select_random_ingredient(ingredient_id)
        burger_builder_page.close_ingredient_detail_modal()

        assert burger_builder_page.verify_ingredient_detail_modal_closed()

    @allure.title('Проверка увеличения счетчика ингредиента при добавлении этого ингредиента в заказ')
    def test_increase_counter_on_ingredient_addition(self, driver):
        burger_builder_page = BurgerBuilderPage(driver)
        burger_builder_page.navigate_to_constructor()
        ingredient_id = fetch_random_ingredient_id()
        before_ingredient_counter = burger_builder_page.get_ingredient_counter_value(ingredient_id)
        burger_builder_page.move_ingredient_to_basket(ingredient_id)

        # Добавляем ожидание для обновления интерфейса
        sleep(1)  # Замените на WebDriverWait для более надежного ожидания

        after_ingredient_counter = burger_builder_page.get_ingredient_counter_value(ingredient_id)

        assert int(after_ingredient_counter) > int(before_ingredient_counter)

    @allure.title('Проверка оформления заказа авторизованным пользователем')
    def test_order_creation_by_logged_in_user(self, driver, login_new_user):
        burger_builder_page = BurgerBuilderPage(driver)
        burger_builder_page.navigate_to_constructor()

        bun_id = fetch_random_bun_id()
        ingredient_id = fetch_random_ingredient_id()
        burger_builder_page.move_ingredient_to_basket(bun_id)
        burger_builder_page.move_ingredient_to_basket(ingredient_id)
        burger_builder_page.press_order_button()

        # Добавляем ожидание для успешного оформления заказа
        sleep(1)  # Замените на WebDriverWait для более надежного ожидания

        assert burger_builder_page.verify_success_screen_with_order_number()




