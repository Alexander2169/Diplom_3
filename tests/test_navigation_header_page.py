from pages.header_page import HeaderPage
from pages.burger_builder_page import BurgerBuilderPage
from pages.order_page import OrderPage
import allure
from conftest import *

class TestHeaderPage: # Заголовок страницы

    @allure.title('Проверка перехода на Главную страницу/Конструктор по клику на "Конструктор"')
    def test_navigate_to_constructor_page(self, driver):
        header_page = HeaderPage(driver)
        burger_builder_page = BurgerBuilderPage(driver)
        order_page = OrderPage(driver)
        order_page.open_order_feed()
        header_page.click_on_constructor_link()

        assert burger_builder_page.verify_constructor_page()

    @allure.title('Проверка перехода на Ленту заказов по клику на "Лента Заказов"')
    def test_navigate_to_order_feed_page(self, driver):
        header_page = HeaderPage(driver)
        order_page = OrderPage(driver)
        burger_builder_page = BurgerBuilderPage(driver)
        burger_builder_page.navigate_to_constructor()
        header_page.click_on_orders_feed_link()

        assert order_page.verify_order_feed_page()

