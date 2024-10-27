import pytest
from config import Urls
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from helpers import register_and_authenticate_user, delete_user_account


@pytest.fixture(params=["chrome", "firefox"]) # Параметризована для использования браузеров Chrome и Firefox
def driver(request): # Фикстура для создания экземпляра веб-драйвера

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


@pytest.fixture # Фикстура для генерации случайных учетных данных пользователя
def generate_user_credentials():

    return create_random_email(), create_random_password(), create_random_name()


@pytest.fixture(scope='function') # Фикстура для регистрации и аутентификации нового пользователя.
def login_new_user(driver):

    tokens = register_and_authenticate_user()

    # Проверка, что токены не равны None
    if tokens is None:
        raise Exception("Не удалось зарегистрировать пользователя и получить токены.")

    driver.get(Urls.BASE_URL)
    token_script = (f'localStorage.setItem("accessToken", "{tokens["accessToken"]}");'
                    f'localStorage.setItem("refreshToken", "{tokens["refreshToken"]}");')
    driver.execute_script(token_script)
    yield tokens
    # Удаление учетной записи пользователя после завершения теста
    delete_user_account(tokens['accessToken'])


