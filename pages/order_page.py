from base_page import BasePage
from locators import *
from config import Urls
import allure


class OrderPage(BasePage):

    @allure.step('Открываем страницу Ленты заказов')
    def open_order_feed(self):
        self.navigate_to(Urls.ORDER_LIST_URL)

    @allure.step('Проверяем открытие страницы Ленты заказов')
    def verify_order_feed_page(self):
        return self.verify_page_opened(Urls.ORDER_LIST_URL, OrdersFeedLocators.ORDERS_FEED_HEADER)

    @allure.step('Кликаем на последний заказ в списке')
    def select_last_order(self):
        self.is_element_invisible(OrdersFeedLocators.LOADING_ICON)
        self.click_element(OrdersFeedLocators.MOST_RECENT_ORDER)

    @allure.step('Проверяем наличие модального окна с деталями заказа')
    def is_order_detail_modal_visible(self):
        return self.is_element_visible(OrdersFeedLocators.ORDER_CONTENT_LABEL)

    @allure.step('Получаем номер последнего заказа в ленте')
    def fetch_last_order_number(self):
        return self.get_text(OrdersFeedLocators.MOST_RECENT_ORDER_ID)

    @allure.step('Получаем значение счетчика "Выполнено за все время"')
    def fetch_total_completed_counter(self):
        return self.get_text(OrdersFeedLocators.TOTAL_COMPLETED_COUNTER)

    @allure.step('Получаем значение счетчика "Выполнено за сегодня"')
    def fetch_today_completed_counter(self):
        return self.get_text(OrdersFeedLocators.TODAY_COMPLETED_COUNTER)

    @allure.step('Ожидаем и получаем отображение номера заказа "В работе"')
    def fetch_order_number_in_progress(self):
        if self.wait_for_text_change(OrdersFeedLocators.ACTIVE_ORDER_LIST_ITEMS, 'Все текущие заказы готовы!'):
            return self.get_text(OrdersFeedLocators.ACTIVE_ORDER_LIST_ITEMS)
        else:
            self.print_error(f'Проблема: отображается {OrdersFeedLocators.ACTIVE_ORDER_LIST_ITEMS}')

class OrderHistoryPage(BasePage):
    @allure.step('Проверяем открытие страницы истории заказов')
    def verify_order_history_page(self):
        return self.verify_page_opened(Urls.USER_ORDER_HISTORY_URL, UserProfileLocators.ORDER_HISTORY_PAGE_LINK)

    @allure.step('Получаем номер первого заказа в истории')
    def fetch_first_order_number(self):
        return self.get_text(OrderHistoryLocators.INITIAL_ORDER_ID)

