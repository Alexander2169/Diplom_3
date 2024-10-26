import pytest
from config import Urls
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from helpers import register_and_authenticate_user, delete_user_account


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    """Фикстура для создания экземпляра веб-драйвера.

    Параметризована для использования браузеров Chrome и Firefox.
    После завершения теста драйвер закрывается.
    """
    browser_name = request.param
    browser = None
    try:
        if browser_name == "chrome":
            # Инициализация драйвера Chrome
            browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser_name == "firefox":
            # Инициализация драйвера Firefox
            browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        else:
            raise ValueError("Unsupported browser: {}".format(browser_name))
        # Максимизация окна браузера
        browser.maximize_window()
        yield browser
    finally:
        if browser:
            # Закрытие браузера после завершения теста
            browser.quit()


@pytest.fixture
def generate_user_credentials():
    """Фикстура для генерации случайных учетных данных пользователя.

    Возвращает кортеж, содержащий случайную электронную почту,
    пароль и имя.
    """
    return create_random_email(), create_random_password(), create_random_name()


@pytest.fixture(scope='function')
def login_new_user(driver):
    """Фикстура для регистрации и аутентификации нового пользователя.

    Использует функцию register_and_authenticate_user для получения
    токенов доступа и обновления, затем устанавливает их в локальное
    хранилище браузера. Удаляет учетную запись пользователя после
    завершения теста.
    """
    tokens = register_and_authenticate_user()
    driver.get(Urls.BASE_URL)
    token_script = (f'localStorage.setItem("accessToken", "{tokens["accessToken"]}");'
                    f'localStorage.setItem("refreshToken", "{tokens["refreshToken"]}");')
    driver.execute_script(token_script)
    yield tokens
    # Удаление учетной записи пользователя после завершения теста
    delete_user_account(tokens['accessToken'])


