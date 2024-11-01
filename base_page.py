from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains  # Импортируем ActionChains
from selenium.common import TimeoutException, NoSuchElementException
import allure
import logging

class BasePage:  # Базовый класс для работы со страницами в браузере

    def __init__(self, driver):  # Инициализация класса с драйвером браузера
        self.driver = driver

    def log_error(self, message):  # Логирует сообщение об ошибке
        logging.error(f'Ошибка: {message}')

    def get_visible_element(self, locator):  # Находит видимый элемент на странице по локатору
        try:
            return WebDriverWait(self.driver, 3).until(
                expected_conditions.visibility_of_element_located(locator))
        except (TimeoutException, NoSuchElementException):
            self.log_error(f'Элемент {locator} не найден в окне браузера')

    def is_element_visible(self, locator):  # Проверяет, отображается ли элемент на странице
        try:
            return self.get_visible_element(locator).is_displayed()
        except (AttributeError, TimeoutException, NoSuchElementException):
            return False

    def is_element_invisible(self, locator):  # Проверяет, что элемент невидим на странице
        try:
            WebDriverWait(self.driver, 3).until(
                expected_conditions.invisibility_of_element_located(locator))
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def wait_for_text_change(self, locator, old_text):  # Ожидает изменения текста элемента на странице
        try:
            WebDriverWait(self.driver, 5).until_not(
                expected_conditions.text_to_be_present_in_element(locator, old_text))
            return True
        except Exception as e:
            self.log_error(f'Проблема: {e}')
            return False

    def get_clickable_element(self, locator):  # Находит кликабельный элемент на странице по локатору
        try:
            return WebDriverWait(self.driver, 5).until(
                expected_conditions.element_to_be_clickable(locator))
        except (TimeoutException, NoSuchElementException):
            self.log_error(f'Элемент {locator} не найден/не кликабелен')

    def click_element(self, locator):  # Кликает на элемент, если он кликабелен
        try:
            self.get_clickable_element(locator).click()
        except (AttributeError, TimeoutException, NoSuchElementException):
            self.log_error(f'Элемент "{locator}" не найден/не кликабелен')

    def input_text(self, locator, text):  # Вводит текст в элемент
        self.get_visible_element(locator).send_keys(text)

    def get_text(self, locator):  # Получает текст из элемента
        return self.get_visible_element(locator).text

    def scroll_to(self, locator):  # Прокручивает страницу к указанному элементу
        element = self.get_visible_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_element_attribute(self, locator, attribute):  # Получает значение атрибута элемента
        element = self.get_visible_element(locator)
        return element.get_attribute(attribute)

    def drag_and_drop(self, source_locator, target_locator):  # Перетаскивает элемент из одного места в другое
        source_element = self.get_clickable_element(source_locator)
        target_area = self.get_clickable_element(target_locator)
        ActionChains(self.driver).drag_and_drop(source_element, target_area).perform()

    def navigate_to(self, url):  # Переходит по указанному URL
        self.driver.get(url)

    def get_current_page_url(self):  # Возвращает текущий URL страницы
        return self.driver.current_url

    def switch_tab(self, index):  # Переключается на вкладку по индексу
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[index])

    def verify_page_opened(self, expected_url, visible_element_locator):  # Проверяет, что страница открыта
        # и отображается ожидаемый элемент
        with allure.step(f'Проверяем открытие страницы "{expected_url}"'):
            self.is_element_visible(visible_element_locator)
            current_url = self.get_current_page_url()
            if self.compare_results(current_url, expected_url):
                return True
            else:
                self.log_error(f'Текущий URL [{current_url}] не соответствует ожидаемому URL [{expected_url}]')
                return False

    @staticmethod
    def compare_results(actual, expected):  # Сравнивает фактический результат с ожидаемым
        with allure.step(f'Сравниваем фактически полученный результат [{actual}] с ожидаемым [{expected}]'):
            return actual == expected

