from pages.base_page import BasePage
from locators import *
from config import *
import allure


class BurgerBuilderPage(BasePage): # Страница конструктора

    @allure.step('Переход на страницу конструктора')
    def navigate_to_constructor(self):
        self.navigate_to(Urls.CONSTRUCTOR_PAGE_URL)

    @allure.step('Проверка загрузки страницы конструктора')
    def verify_constructor_page(self):
        return self.verify_page_opened(Urls.CONSTRUCTOR_PAGE_URL, BurgerConstructorLocators.BANNER_TEXT)

    @allure.step('Получение локатора случайного ингредиента')
    def get_random_ingredient_locator(self, random_ingredient_id, element_locator):
        method, ingredient_locator = element_locator
        formatted_locator = (method, ingredient_locator.format(ingredient_id=random_ingredient_id))
        return formatted_locator

    @allure.step('Выбор случайного ингредиента')
    def select_random_ingredient(self, random_ingredient_id):
        ingredient_locator = self.get_random_ingredient_locator(random_ingredient_id,
                                                                BurgerConstructorLocators.INGREDIENT_LINK_ITEM)
        self.scroll_to(ingredient_locator)
        self.click_element(ingredient_locator)

    @allure.step('Проверка видимости модального окна с информацией об ингредиенте')
    def verify_ingredient_detail_modal(self, ingredient_id):
        return (self.is_element_visible(BurgerConstructorLocators.INGREDIENT_INFO_HEADER)
                and self.verify_page_opened(Urls.INGREDIENT_DETAIL_URL.format(id=ingredient_id), BurgerConstructorLocators.INGREDIENT_INFO_HEADER))

    @allure.step('Закрытие модального окна с информацией об ингредиенте')
    def close_ingredient_detail_modal(self):
        self.click_element(BurgerConstructorLocators.CLOSE_INGREDIENT_INFO_BUTTON)

    @allure.step('Проверка закрытия модального окна с информацией об ингредиенте')
    def verify_ingredient_detail_modal_closed(self):
        return self.is_element_invisible(BurgerConstructorLocators.INGREDIENT_INFO_HEADER)

    @allure.step('Перемещение ингредиента в корзину')
    def move_ingredient_to_basket(self, random_ingredient_id):
        ingredient_locator = self.get_random_ingredient_locator(random_ingredient_id,
                                                                BurgerConstructorLocators.INGREDIENT_LINK_ITEM)
        self.scroll_to(ingredient_locator)
        self.drag_and_drop(ingredient_locator, BurgerConstructorLocators.BASKET_SECTION)

    @allure.step('Получение значения счётчика для добавленного ингредиента')
    def get_ingredient_counter_value(self, random_ingredient_id):
        ingredient_counter = self.get_random_ingredient_locator(random_ingredient_id,
                                                                BurgerConstructorLocators.INGREDIENT_QUANTITY)
        return self.get_text(ingredient_counter)

    @allure.step('Нажатие на кнопку "Оформить заказ"')
    def press_order_button(self):
        self.click_element(BurgerConstructorLocators.SUBMIT_ORDER_BUTTON)

    @allure.step('Проверка отображения успешного окна с номером заказа')
    def verify_success_screen_with_order_number(self):
        if self.wait_for_text_change(BurgerConstructorLocators.SUCCESS_ORDER_ID, '9999'):
            return self.is_element_visible(BurgerConstructorLocators.ORDER_IN_PROGRESS_TEXT)
        else:
            return False


