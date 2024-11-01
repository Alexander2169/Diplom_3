import logging

class Urls:
    # Основной URL сайта
    BASE_URL = 'https://stellarburgers.nomoreparties.site'

    # URL для главной страницы конструктора
    CONSTRUCTOR_PAGE_URL = f'{BASE_URL}/'

    # URL для карточки ингредиента
    INGREDIENT_DETAIL_URL = BASE_URL + '/ingredient/{id}'

    # URL для ленты заказов
    ORDER_LIST_URL = f'{BASE_URL}/feed'

    # URL для карточки заказа в ленте
    ORDER_DETAIL_URL = BASE_URL + '/feed/{id}'

    # URL для страницы регистрации
    SIGN_UP_URL = f'{BASE_URL}/register'

    # URL для страницы входа
    SIGN_IN_URL = f'{BASE_URL}/login'

    # URL для восстановления пароля
    PASSWORD_RECOVERY_URL = f'{BASE_URL}/forgot-password'

    # URL для сброса пароля
    PASSWORD_RESET_URL = f'{BASE_URL}/reset-password'

    # URL для аккаунта пользователя
    USER_ACCOUNT_URL = f'{BASE_URL}/account'

    # URL для профиля пользователя
    USER_PROFILE_URL = f'{USER_ACCOUNT_URL}/profile'

    # URL для истории заказов
    USER_ORDER_HISTORY_URL = f'{USER_ACCOUNT_URL}/order-history'

    # URL для карточки заказа в истории заказов
    USER_ORDER_DETAIL_URL = USER_ACCOUNT_URL + '/order-history/{id}'


class Endpoints:
    # Эндпоинт для создания аккаунта пользователя
    USER_ACCOUNT_CREATION = '/api/auth/register'

    # Эндпоинт для входа пользователя
    USER_LOGIN = '/api/auth/login'

    # Эндпоинт для удаления аккаунта пользователя
    USER_ACCOUNT_DELETION = '/api/auth/user'

    # Эндпоинт для получения ингредиентов
    INGREDIENTS_RETRIEVAL = '/api/ingredients'

    # Эндпоинт для создания заказа
    ORDER_CREATION = '/api/orders'


class BunIds:
    BUN_IDS = ['61c0c5a71d1f82001bdaaa70', '61c0c5a71d1f82001bdaaa77']

# Настройка логирования
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

