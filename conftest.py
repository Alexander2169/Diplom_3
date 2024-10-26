import pytest
from helpers import register_and_authenticate_user
from config import Urls
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param
    browser = None
    try:
        if browser_name == "chrome":
            browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser_name == "firefox":
            browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        else:
            raise ValueError("Unsupported browser: {}".format(browser_name))
        browser.maximize_window()
        yield browser
    finally:
        if browser:
            browser.quit()

@pytest.fixture
def generate_user_credentials():
    return create_random_email(), create_random_password(), create_random_name()

@pytest.fixture(scope='function')
def login_new_user(driver):
    tokens = register_and_authenticate_user()
    driver.get(Urls.BASE_URL)
    token_script = (f'localStorage.setItem("accessToken", "{tokens["accessToken"]}");'
                    f'localStorage.setItem("refreshToken", "{tokens["refreshToken"]}");')
    driver.execute_script(token_script)
    yield tokens
    delete_user_account(tokens['accessToken'])

