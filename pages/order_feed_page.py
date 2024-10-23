from pages.base_page import BasePage
from locators import FeedPageLocators
import allure


class OrderFeedPage(BasePage): # Класс для работы со страницей Ленты заказов

    @allure.title('Получить текст заголовка раздела заказов')
    def get_text_on_title_of_orders_list(self):
        return self.get_text_on_element(FeedPageLocators.ORDERS_FEED_TITLE)

    @allure.title('Кликнуть по первому (последнему) заказу в ленте')
    def click_on_order_card(self):
        self.wait_visibility_of_element(FeedPageLocators.FEED_ORDER_CARD)
        self.click_on_element(FeedPageLocators.FEED_ORDER_CARD)

    @allure.title('Получить текст заголовка окна с деталями заказа')
    def get_text_on_title_of_modal_order(self):
        return self.get_text_on_element(FeedPageLocators.MODAL_ORDER_TITLE)

    @allure.title('Получить количество заказов, выполненных за все время')
    def get_quantity_of_orders(self):
        self.find_element_with_wait(FeedPageLocators.TOTAL_ORDERS_COUNT)
        return self.get_text_on_element(FeedPageLocators.TOTAL_ORDERS_COUNT)

    @allure.title('Получить количество заказов, выполненных за сегодня')
    def get_daily_quantity_of_orders(self):
        self.find_element_with_wait(FeedPageLocators.DAILY_ORDERS_COUNT)
        return self.get_text_on_element(FeedPageLocators.DAILY_ORDERS_COUNT)

    @allure.title('Проверить наличие номера заказа в списке ленты')
    def check_id_order_in_feed(self, order_id):
        locator = FeedPageLocators.ORDER_CARD_IN_FEED_WITH_SUBSTITUTIONS
        locator_with_order_id = (locator[0], locator[1].format(order_id=order_id))
        self.find_element_with_wait(locator_with_order_id)
        return self.check_displaying_of_element(locator_with_order_id)

    @allure.title('Получить номер последнего заказа в разделе "В работе"')
    def get_order_number_in_feed_progress_section(self):
        return self.get_text_on_element(FeedPageLocators.IN_PROGRESS_ORDER_NUMBER)
