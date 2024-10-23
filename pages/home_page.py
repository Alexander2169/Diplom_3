from pages.base_page import BasePage
from locators import MainPageLocators
import allure


class HomePage(BasePage): # Класс для работы с главной страницей

    @allure.title('Кликнуть по кнопке перехода в личный кабинет в хэдере')
    def click_on_personal_account_in_header(self):
        self.wait_visibility_of_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_on_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.title('Кликнуть по кнопке "Лента заказов" в хэдере')
    def click_header_feed_button(self):
        self.wait_visibility_of_element(MainPageLocators.ORDER_FEED_BUTTON_IN_HEADER)
        self.click_on_element(MainPageLocators.ORDER_FEED_BUTTON_IN_HEADER)

    @allure.title('Переход на страницу конструктора')
    def click_on_button_constructor(self):
        self.wait_visibility_of_element(MainPageLocators.CONSTRUCTOR_HEADER_BUTTON)
        self.click_on_element(MainPageLocators.CONSTRUCTOR_HEADER_BUTTON)

    @allure.title('Получение главного заголовка конструктора')
    def get_text_on_title_of_constructor(self):
        return self.get_text_on_element(MainPageLocators.CONSTRUCTOR_SECTION_TITLE)

    @allure.title('Кликнуть по кнопке "Войти в аккаунт" на главной')
    def click_on_button_login_in_main(self):
        self.click_on_element(MainPageLocators.LOGIN_BUTTON_ON_MAIN)

    @allure.title('Проверить отображение окна о создании заказа')
    def check_displaying_of_confirmation_modal_of_order(self):
        self.wait_visibility_of_element(MainPageLocators.ORDER_CONFIRMATION_MODAL)
        return self.check_displaying_of_element(MainPageLocators.ORDER_CONFIRMATION_MODAL)

    @allure.title('Кликнуть по ингредиенту')
    def click_on_ingredient(self):
        self.wait_visibility_of_element(MainPageLocators.FIRST_INGREDIENT)
        self.click_on_element(MainPageLocators.FIRST_INGREDIENT)

    @allure.title('Проверить отображение окна "Детали ингредиента"')
    def check_displaying_of_modal_details(self):
        self.wait_visibility_of_element(MainPageLocators.MODAL_DETAILS_HEADER)
        return self.check_displaying_of_element(MainPageLocators.MODAL_DETAILS_HEADER)

    @allure.title('Проверить, что окно "Детали ингредиента" не отображается')
    def check_not_displaying_of_modal_details(self):
        self.wait_for_closing_of_element(MainPageLocators.MODAL_DETAILS_HEADER)
        if not self.check_displaying_of_element(MainPageLocators.MODAL_DETAILS_HEADER):
            return True

    @allure.title('Закрыть окно "Детали ингредиента"')
    def close_modal(self):
        self.wait_visibility_of_element(MainPageLocators.CLOSE_MODAL_BUTTON)
        self.click_on_element(MainPageLocators.CLOSE_MODAL_BUTTON)

    @allure.title('Добавить ингредиенты')
    def drag_and_drop_ingredient_to_order(self):
        source_element = self.find_element_with_wait(MainPageLocators.INGREDIENT_IMAGE)
        target_element = self.find_element_with_wait(MainPageLocators.INGREDIENTS_DROP_AREA)
        self.drag_and_drop_element(source_element, target_element)

    @allure.title('Получить количество ингредиентов')
    def get_count_of_ingredients(self):
        return self.get_text_on_element(MainPageLocators.INGREDIENT_COUNT)

    @allure.title('Кликнуть на кнопку создания заказа')
    def click_on_button_make_order(self):
        self.click_on_element(MainPageLocators.MAKE_ORDER_BUTTON_IN_CONSTRUCTOR)

    @allure.title('Проверить отображение окна о создании заказа')
    def check_displaying_of_confirmation_modal_of_order(self):
        return self.check_displaying_of_element(MainPageLocators.ORDER_CONFIRMATION_MODAL)

    @allure.title('Получить номер в окне о создании заказа')
    def get_number_of_order_in_modal_confirmation(self):
        self.wait_for_element_to_change_text(MainPageLocators.CONFIRMED_ORDER_NUMBER, '7777')
        return self.get_text_on_element(MainPageLocators.CONFIRMED_ORDER_NUMBER)

    @allure.title('Кликнуть на кнопку закрытия окна о создании заказа')
    def click_on_button_close_confirmation_modal(self):
        self.check_element_is_clickable(MainPageLocators.CLOSE_CONFIRMATION_BUTTON)
        self.click_on_element(MainPageLocators.CLOSE_CONFIRMATION_BUTTON)
