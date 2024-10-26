from pages.header_page import HeaderPage
from pages.burger_builder_page import BurgerBuilderPage  # Исправлено на BurgerBuilderPage
from pages.order_page import OrderPage  # Исправлено на OrderPage
import allure


class TestHeaderPage:

    @allure.title('Проверка перехода на Главную страницу/Конструктор по клику на "Конструктор"')
    def test_go_to_constructor_page_by_clicking_constructor_link(self, driver):
        header_page = HeaderPage(driver)
        burger_builder_page = BurgerBuilderPage(driver)  # Исправлено на BurgerBuilderPage
        order_page = OrderPage(driver)  # Исправлено на OrderPage
        order_page.open_order_feed()  # Исправлено на open_order_feed
        header_page.click_on_constructor_link()  # Исправлено на click_on_constructor_link

        assert burger_builder_page.verify_constructor_page()  # Исправлено на verify_constructor_page


    @allure.title('Проверка перехода на Ленту заказов по клику на "Лента Заказов"')
    def test_go_to_order_feed_page_by_clicking_order_feed_link(self, driver):
        header_page = HeaderPage(driver)
        order_page = OrderPage(driver)  # Исправлено на OrderPage
        burger_builder_page = BurgerBuilderPage(driver)  # Исправлено на BurgerBuilderPage
        burger_builder_page.navigate_to_constructor()  # Исправлено на navigate_to_constructor
        header_page.click_on_orders_feed_link()  # Исправлено на click_on_orders_feed_link

        assert order_page.verify_order_feed_page()  # Исправлено на verify_order_feed_page
