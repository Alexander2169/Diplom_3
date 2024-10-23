from locators import OrderHistoryPageLocators
from pages.base_page import BasePage
import allure


class OrderHistoryPage(BasePage): # Класс для работы со страницей Истории заказов

    @allure.title('Подождать прогрузки карточки заказа')
    def wait_visibility_of_order_card(self):
        self.wait_visibility_of_element(OrderHistoryPageLocators.ORDER_CARD)

    @allure.title('Получить текст карточки заказа')
    def get_text_of_order_card_title(self):
        return self.get_text_on_element(OrderHistoryPageLocators.ORDER_CARD_TITLE)

    @allure.title('Получить номер заказа в карточке')
    def get_id_of_order_card(self):
        return self.get_text_on_element(OrderHistoryPageLocators.ORDER_CARD_ID)
