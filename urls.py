class Urls:
    # Базовый URL для API
    BASE_URL = 'https://stellarburgers.nomoreparties.site'

    # URL для регистрации нового пользователя
    USER_REGISTER = f'{BASE_URL}/api/auth/register'

    # URL для удаления пользователя
    USER_DELETE = f'{BASE_URL}/api/auth/user'

    # URL для создания нового заказа
    ORDER_CREATE = f'{BASE_URL}/api/orders'


