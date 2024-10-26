from pages.base_page import BasePage
from locators import *
from config import Urls
import allure


class OrderPage(BasePage):

    @allure.step('Открываем страницу Ленты заказов')
    def go_to_order_feed_page(self):
        self.navigate_to(Urls.ORDER_LIST_URL)

    @allure.step('Проверяем открытие страницы Ленты заказов')
    def check_page(self):
        return self.verify_page_opened(Urls.ORDER_LIST_URL, OrdersFeedLocators.ORDERS_FEED_HEADER)

    @allure.step('Кликаем на последний заказ в списке')
    def click_last_order(self):
        self.is_element_invisible(OrderFeedLocators.LOADING_ICON)
        self.click_element(OrdersFeedLocators.MOST_RECENT_ORDER)

    @allure.step('Проверяем наличие модального окна с деталями заказа')
    def check_open_order_detail_modal_window(self):
        return self.is_element_visible(OrdersFeedLocators.ORDER_CONTENT_LABEL)

    @allure.step('Получаем номер последнего заказа в ленте')
    def get_order_number(self):
        return self.get_text(OrdersFeedLocators.MOST_RECENT_ORDER_ID)

    @allure.step('Получаем значение счетчика "Выполнено за все время"')
    def get_completed_for_all_time_counter(self):
        return self.get_text(OrdersFeedLocators.TOTAL_COMPLETED_COUNTER)

    @allure.step('Получаем значение счетчика "Выполнено за сегодня"')
    def get_executed_today_counter(self):
        return self.get_text(OrdersFeedLocators.TODAY_COMPLETED_COUNTER)

    @allure.step('Ожидаем и получаем отображение номера заказа "В работе"')
    def get_order_number_in_the_work_list(self):
        if self.wait_for_text_change(OrdersFeedLocators.ACTIVE_ORDER_LIST_ITEMS, 'Все текущие заказы готовы!'):
            return self.get_text(OrdersFeedLocators.ACTIVE_ORDER_LIST_ITEMS)
        else:
            self.print_error(f'Проблема: отображается {OrdersFeedLocators.ACTIVE_ORDER_LIST_ITEMS}')

    @allure.step('Проверяем открытие страницы истории заказов')
    def check_history_page(self):
        return self.verify_page_opened(Urls.USER_ORDER_HISTORY_URL, UserProfileLocators.ORDER_HISTORY_PAGE_LINK)

    @allure.step('Получаем номер первого заказа в истории')
    def get_first_order_number(self):
        return self.get_text(OrderHistoryLocators.INITIAL_ORDER_ID)


