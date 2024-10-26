from selenium.webdriver.common.by import By

class BurgerConstructorLocators:
    # Локатор для заголовка баннера "Соберите бургер"
    BANNER_TEXT = [By.XPATH, '//h1[text() = "Соберите бургер"]']
    # Локатор для ссылки на ингредиент по его идентификатору
    INGREDIENT_LINK_ITEM = [By.XPATH, '//a[@href = "/ingredient/{ingredient_id}"]']
    # Локатор для отображения количества ингредиентов
    INGREDIENT_QUANTITY = [By.XPATH, '//a[@href = "/ingredient/{ingredient_id}"]//p']
    # Локатор для секции корзины
    BASKET_SECTION = [By.CLASS_NAME, 'BurgerConstructor_basket__list__l9dp_']
    # Локатор для кнопки оформления заказа
    SUBMIT_ORDER_BUTTON = [By.XPATH, '//button[text() = "Оформить заказ"]']
    # Локатор для заголовка информации об ингредиенте
    INGREDIENT_INFO_HEADER = [By.XPATH, '//h2[text() = "Детали ингредиента"]']
    # Локатор для кнопки закрытия информации об ингредиенте
    CLOSE_INGREDIENT_INFO_BUTTON = [By.XPATH, '//h2[text() = "Детали ингредиента"]/parent::div/following-sibling::button[contains(@class, "modal__close")]']
    # Локатор для идентификатора заказа после успешного оформления
    SUCCESS_ORDER_ID = [By.XPATH, '//p[text() = "идентификатор заказа"]/preceding-sibling::h2']
    # Локатор для текста о том, что заказ в процессе приготовления
    ORDER_IN_PROGRESS_TEXT = [By.XPATH, '//p[text() = "Ваш заказ начали готовить"]']
    # Локатор для иконки загрузки
    LOADING_ICON = [By.XPATH, '//img[@alt = "loading animation"]']

class PasswordRecoveryLocators:
    # Локатор для поля ввода email
    EMAIL_FIELD = [By.XPATH, '//label[text() = "Email"]/parent::div/input']
    # Локатор для кнопки восстановления пароля
    RESTORE_PASSWORD_BUTTON = [By.XPATH, '//button[text() = "Восстановить"]']
    # Локатор для иконки загрузки
    LOADING_ICON = [By.XPATH, '//img[@alt = "loading animation"]']

class NavigationHeaderLocators:
    # Локатор для ссылки на личный кабинет
    ACCOUNT_LINK = [By.XPATH, '//p[text() = "Личный Кабинет"]']
    # Локатор для ссылки на конструктор
    CONSTRUCTOR_LINK = [By.XPATH, '//p[text() = "Конструктор"]']
    # Локатор для ссылки на ленту заказов
    ORDERS_FEED_LINK = [By.XPATH, '//p[text() = "Лента Заказов"]']
    # Локатор для иконки загрузки
    LOADING_ICON = [By.XPATH, '//img[@alt = "loading animation"]']

class UserLoginLocators:
    # Локатор для кнопки входа
    SIGN_IN_BUTTON = [By.XPATH, '//button[text() = "Войти"]']
    # Локатор для ссылки на восстановление пароля
    FORGOT_PASSWORD_LINK = [By.XPATH, '//a[@href = "/forgot-password"]']
    # Локатор для иконки загрузки
    LOADING_ICON = [By.XPATH, '//img[@alt = "loading animation"]']

class OrdersFeedLocators:
    # Локатор для заголовка ленты заказов
    ORDERS_FEED_HEADER = [By.XPATH, '//h1[text() = "Лента заказов"]']
    # Локатор для самого последнего заказа
    MOST_RECENT_ORDER = [By.XPATH, '//ul[contains(@class,"OrderFeed_list")]//a']
    # Локатор для метки содержимого заказа
    ORDER_CONTENT_LABEL = [By.XPATH, '//p[text() = "Cостав"]']
    # Локатор для идентификатора самого последнего заказа
    MOST_RECENT_ORDER_ID = [By.XPATH, '//ul[contains(@class,"OrderFeed_list")]//div[contains(@class,"OrderHistory_textBox")]//p[@class = "text text_type_digits-default"]']
    # Локатор для счетчика выполненных заказов за все время
    TOTAL_COMPLETED_COUNTER = [By.XPATH, '//p[text() = "Выполнено за все время:"]/following-sibling::p']
    # Локатор для счетчика выполненных заказов за сегодня
    TODAY_COMPLETED_COUNTER = [By.XPATH, '//p[text() = "Выполнено за сегодня:"]/following-sibling::p']
    # Локатор для элементов списка активных заказов
    ACTIVE_ORDER_LIST_ITEMS = [By.XPATH, '//ul[contains(@class,"OrderFeed_orderListReady")]/li']
    # Локатор для иконки загрузки
    LOADING_ICON = [By.XPATH, '//img[@alt = "loading animation"]']

class OrderHistoryLocators:
    # Локатор для идентификатора начального заказа
    INITIAL_ORDER_ID = [By.XPATH, '//ul[contains(@class,"OrderHistory")]//div[contains(@class,"OrderHistory_textBox")]//p[@class = "text text_type_digits-default"]']
    # Локатор для иконки загрузки
    LOADING_ICON = [By.XPATH, '//img[@alt = "loading animation"]']

class UserProfileLocators:
    # Локатор для ссылки на страницу профиля
    PROFILE_PAGE_LINK = [By.XPATH, '//a[text() = "Профиль"]']
    # Локатор для ссылки на страницу истории заказов
    ORDER_HISTORY_PAGE_LINK = [By.XPATH, '//a[text() = "История заказов"]']
    # Локатор для кнопки выхода
    LOGOUT_BUTTON = [By.XPATH, '//button[text() = "Выход"]']
    # Локатор для иконки загрузки
    LOADING_ICON = [By.XPATH, '//img[@alt = "loading animation"]']

class ChangePasswordLocators:
    # Локатор для поля ввода нового пароля
    NEW_PASSWORD_FIELD = [By.XPATH, '//input[@type = "password"]']
    # Локатор для кнопки сохранения изменений
    SAVE_CHANGES_BUTTON = [By.XPATH, '//button[text() = "Сохранить"]']
    # Локатор для кнопки переключения видимости пароля
    TOGGLE_PASSWORD_VISIBILITY_BUTTON = [By.XPATH, '//div[contains(@class, "input__icon")]']
    # Локатор для контейнера ввода пароля
    PASSWORD_INPUT_CONTAINER = [By.XPATH, '//input[@name = "Введите новый пароль"]/parent::div']
    # Локатор для иконки загрузки
    LOADING_ICON = [By.XPATH, '//img[@alt = "loading animation"]']
