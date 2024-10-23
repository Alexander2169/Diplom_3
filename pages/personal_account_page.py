from pages.base_page import BasePage
from locators import PersonalAccountPageLocators
import allure


class PersonalAccountPage(BasePage): # Класс для работы со страницей Личного кабинета

    @allure.title('Кликнуть по кнопке "История заказов"')
    def click_on_order_history_button(self):
        self.click_on_element(PersonalAccountPageLocators.ORDER_HISTORY_LINK)

    @allure.title('Кликнуть по кнопке "Выйти"')
    def click_on_logout_button(self):
        self.click_on_element(PersonalAccountPageLocators.LOGOUT_BUTTON)

    @allure.title('Подождать прогрузки текста описания раздела')
    def wait_visibility_of_description(self):
        self.wait_visibility_of_element(PersonalAccountPageLocators.SECTION_DESCRIPTION)

    @allure.title('Проверить отображение описания раздела')
    def check_displaying_of_description(self):
        return self.check_displaying_of_element(PersonalAccountPageLocators.SECTION_DESCRIPTION)

    @allure.title('Подождать прогрузки кнопки "Зарегистрироваться"')
    def wait_visibility_of_button_register(self):
        self.wait_visibility_of_element(PersonalAccountPageLocators.REGISTER_BUTTON)

    @allure.title('Проверить отображение кнопки "Зарегистрироваться"')
    def check_displaying_of_button_register(self):
        return self.check_displaying_of_element(PersonalAccountPageLocators.REGISTER_BUTTON)


