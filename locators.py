from selenium.webdriver.common.by import By

class BurgerConstructorLocators:
    BANNER_TEXT = [By.XPATH, '//h1[text() = "Соберите бургер"]']
    INGREDIENT_LINK_ITEM = [By.XPATH, '//a[@href = "/ingredient/{ingredient_id}"]']
    INGREDIENT_QUANTITY = [By.XPATH, '//a[@href = "/ingredient/{ingredient_id}"]//p']
    BASKET_SECTION = [By.CLASS_NAME, 'BurgerConstructor_basket__list__l9dp_']
    SUBMIT_ORDER_BUTTON = [By.XPATH, '//button[text() = "Оформить заказ"]']
    INGREDIENT_INFO_HEADER = [By.XPATH, '//h2[text() = "Детали ингредиента"]']
    CLOSE_INGREDIENT_INFO_BUTTON = [By.XPATH, '//h2[text() = "Детали ингредиента"]/parent::div/following-sibling::button[contains(@class, "modal__close")]']
    SUCCESS_ORDER_ID = [By.XPATH, '//p[text() = "идентификатор заказа"]/preceding-sibling::h2']
    ORDER_IN_PROGRESS_TEXT = [By.XPATH, '//p[text() = "Ваш заказ начали готовить"]']
    LOADING_ICON = [By.XPATH, '//img[@alt = "loading animation"]']

class PasswordRecoveryLocators:
    EMAIL_FIELD = [By.XPATH, '//label[text() = "Email"]/parent::div/input']
    RESTORE_PASSWORD_BUTTON = [By.XPATH, '//button[text() = "Восстановить"]']
    LOADING_ICON = [By.XPATH, '//img[@alt = "loading animation"]']

class NavigationHeaderLocators:
    ACCOUNT_LINK = [By.XPATH, '//p[text() = "Личный Кабинет"]']
    CONSTRUCTOR_LINK = [By.XPATH, '//p[text() = "Конструктор"]']
    ORDERS_FEED_LINK = [By.XPATH, '//p[text() = "Лента Заказов"]']
    LOADING_ICON = [By.XPATH, '//img[@alt = "loading animation"]']

class UserLoginLocators:
    SIGN_IN_BUTTON = [By.XPATH, '//button[text() = "Войти"]']
    FORGOT_PASSWORD_LINK = [By.XPATH, '//a[@href = "/forgot-password"]']
    LOADING_ICON = [By.XPATH, '//img[@alt = "loading animation"]']

class OrdersFeedLocators:
    ORDERS_FEED_HEADER = [By.XPATH, '//h1[text() = "Лента заказов"]']
    MOST_RECENT_ORDER = [By.XPATH, '//ul[contains(@class,"OrderFeed_list")]//a']
    ORDER_CONTENT_LABEL = [By.XPATH, '//p[text() = "Cостав"]']
    MOST_RECENT_ORDER_ID = [By.XPATH, '//ul[contains(@class,"OrderFeed_list")]//div[contains(@class,"OrderHistory_textBox")]//p[@class = "text text_type_digits-default"]']
    TOTAL_COMPLETED_COUNTER = [By.XPATH, '//p[text() = "Выполнено за все время:"]/following-sibling::p']
    TODAY_COMPLETED_COUNTER = [By.XPATH, '//p[text() = "Выполнено за сегодня:"]/following-sibling::p']
    ACTIVE_ORDER_LIST_ITEMS = [By.XPATH, '//ul[contains(@class,"OrderFeed_orderListReady")]/li']
    LOADING_ICON = [By.XPATH, '//img[@alt = "loading animation"]']

class OrderHistoryLocators:
    INITIAL_ORDER_ID = [By.XPATH, '//ul[contains(@class,"OrderHistory")]//div[contains(@class,"OrderHistory_textBox")]//p[@class = "text text_type_digits-default"]']
    LOADING_ICON = [By.XPATH, '//img[@alt = "loading animation"]']

class UserProfileLocators:
    PROFILE_PAGE_LINK = [By.XPATH, '//a[text() = "Профиль"]']
    ORDER_HISTORY_PAGE_LINK = [By.XPATH, '//a[text() = "История заказов"]']
    LOGOUT_BUTTON = [By.XPATH, '//button[text() = "Выход"]']
    LOADING_ICON = [By.XPATH, '//img[@alt = "loading animation"]']

class ChangePasswordLocators:
    NEW_PASSWORD_FIELD = [By.XPATH, '//input[@type = "password"]']
    SAVE_CHANGES_BUTTON = [By.XPATH, '//button[text() = "Сохранить"]']
    TOGGLE_PASSWORD_VISIBILITY_BUTTON = [By.XPATH, '//div[contains(@class, "input__icon")]']
    PASSWORD_INPUT_CONTAINER = [By.XPATH, '//input[@name = "Введите новый пароль"]/parent::div']
    LOADING_ICON = [By.XPATH, '//img[@alt = "loading animation"]']
