from selenium.webdriver.common.by import By

class PersonalAccountPageLocators: # Локаторы страницы аккаунта
    # Раздел "Профиль"
    PROFILE_LINK = (By.XPATH, '//a[@href = "/account/profile"]')

    # Раздел "История заказов"
    ORDER_HISTORY_LINK = (By.XPATH, '//a[@href = "/account/order-history"]')

    # Кнопка "Выйти", логаут
    LOGOUT_BUTTON = (By.XPATH, '//button[@type = "button"]')

    # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, '//a[text() = "Зарегистрироваться"]')

    # Описание раздела: "В этом разделе вы можете изменить свои персональные данные"
    SECTION_DESCRIPTION = (By.XPATH, '//p[contains(@class, "Account_text")]')


class OrderFeedPageLocators: # Локаторы страницы ленты заказов
    # Раздел заказов
    ORDERS_LIST_SECTION = (By.XPATH, '//ul[contains(@class, "OrderFeed_list")]')

    # Заголовок ленты заказов
    ORDERS_FEED_TITLE = (By.XPATH, '//div[contains(@class, "OrderFeed_orderFeed")]/h1')

    # Карточка заказа в ленте
    FEED_ORDER_CARD = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]')

    # Всплывающее окно с деталями заказа
    ORDER_MODAL = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains(@class, "Modal_orderBox")]')

    # Заголовок всплывающего окна с деталями заказа
    MODAL_ORDER_TITLE = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains(@class, "Modal_orderBox")]//h2')

    # Счетчик заказов "Выполнено за все время"
    TOTAL_ORDERS_COUNT = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')

    # Счетчик заказов "Выполнено за сегодня"
    DAILY_ORDERS_COUNT = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')

    # Заказ в разделе "В работе"
    IN_PROGRESS_ORDER = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li')

    # Номер заказа в разделе "В работе"
    IN_PROGRESS_ORDER_NUMBER = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li[contains(@class, "text_type_digits-default")]')

    # Номер заказа в ленте — заготовка, в которую нужно подставить id искомого заказа
    ORDER_CARD_IN_FEED_WITH_SUBSTITUTIONS = (By.XPATH, './/*[text()="{order_id}"]')


class BasePageLocators: # Локаторы базовой страницы
    # Кнопка "Войти в аккаунт" на главной
    LOGIN_BUTTON_ON_MAIN = (By.XPATH, './/button[text() = "Войти в аккаунт"]')

    # Кнопка "Личный кабинет"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]/parent::a')

    # Кнопка "Оформить заказ"
    MAKE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')

    # Кнопка "Конструктор" в шапке сайта
    CONSTRUCTOR_HEADER_BUTTON = (By.XPATH, '//p[text() = "Конструктор"]')

    # Селектор, помечающий выбранный раздел конструктора как активный
    ACTIVE_BUTTON_SELECTOR = (By.XPATH, '//div[@class = "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]')

    # Заголовок раздела "Конструктор"
    CONSTRUCTOR_SECTION_TITLE = (By.XPATH, '//section[contains(@class, "BurgerIngredients_ingredients")]/h1')

    # Заголовок раздела "Булки" в меню конструктора
    BUNS_SECTION_TITLE = (By.XPATH, '//span[text() = "Булки"]')

    # Заголовок раздела "Соусы" в меню конструктора
    SAUCES_SECTION_TITLE = (By.XPATH, '//span[text() = "Соусы"]')

    # Заголовок раздела "Начинки" в меню конструктора
    FILLINGS_SECTION_TITLE = (By.XPATH, '//span[text() = "Начинки"]')

    # Кнопка "Лента заказов"
    ORDER_FEED_BUTTON_IN_HEADER = (By.XPATH, '(.//p[@class="AppHeader_header__linkText__3q_va ml-2"]')

    # Ингредиент
    FIRST_INGREDIENT = (By.XPATH, '(.//p[@class="BurgerIngredient_ingredient__text__yp3dH"])[1]')

    # Заголовок окна "Детали ингредиента"
    MODAL_DETAILS_HEADER = (By.XPATH, '//h2[contains(@class, "Modal_modal__title") and contains(text(), "Детали")]')

    # Кнопка с крестиком, закрывающая окно "Детали ингредиента"
    CLOSE_MODAL_BUTTON = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//button[contains(@class, "close")]')

    # Картинка ингредиента в общем списке
    INGREDIENT_IMAGE = (By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]')

    # Куда перетаскиваются ингредиенты
    INGREDIENTS_DROP_AREA = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')

    # Состав заказа в условной "Корзине"
    ORDER_CONTENT = (By.CSS_SELECTOR, '.constructor-element_pos_top .constructor-element__row')

    # Кнопка "Оформить заказ"
    MAKE_ORDER_BUTTON_IN_CONSTRUCTOR = (By.CLASS_NAME, 'button_button__33qZ0')

    # Количество экземпляров ингредиента в заказе (счетчик)
    INGREDIENT_COUNT = (By.XPATH, './/a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]//p[@class="counter_counter__num__3nue1"][1]')

    # Окно подтверждения создания заказа
    ORDER_CONFIRMATION_MODAL = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]/div[contains(@class, "Modal_modal__container")]')

    # Номер созданного заказа в окне подтверждения
    CONFIRMED_ORDER_NUMBER = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//h2')

    # Кнопка с крестиком, закрывающая окно подтвержденного заказа
    CLOSE_CONFIRMATION_BUTTON = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//button[contains(@class, "close")]')


class OrderHistoryPageLocators: # Локаторы страницы истории заказов
    # Карточка заказа в истории заказов
    ORDER_CARD = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]')

    # Заголовок карточки заказа с названием бургера
    ORDER_CARD_TITLE = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]//h2')

    # Номер заказа в карточке заказа
    ORDER_CARD_ID = (By.XPATH, '(//div[contains(@class, "OrderHistory_textBox")]/p[contains(@class, "text_type_digits-default")])[1]')


class PasswordRecoveryLocators: # Локаторы восстановления пароля
    # Кнопка "Восстановить пароль" на экране входа
    FORGOT_PASSWORD_BUTTON = (By.XPATH, '//a[text() = "Восстановить пароль"]')

    # Поле ввода email
    EMAIL_INPUT = (By.CLASS_NAME, 'input__textfield')

    # Кнопка "Восстановить" на странице ввода email
    RECOVER_BUTTON = (By.CLASS_NAME, 'button_button__33qZ0')

    # Поле ввода пароля
    PASSWORD_INPUT = (By.CSS_SELECTOR, '.input_type_password .input__textfield')

    # Иконка, скрывающая (показывающая) пароль
    EYE_ICON = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]')

    # Пароль со статусом видимости
    VISIBLE_PASSWORD_STATUS = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, "input_status_active")]')

    # Пароль скрыт
    INVISIBLE_PASSWORD_STATUS = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, "input_type_password")]')
