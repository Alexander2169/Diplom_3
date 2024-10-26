import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from helpers import create_random_email, create_random_password, create_random_name
import requests
from urls import Urls
import allure

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



@pytest.fixture
@allure.title('Создает пользователя и заказ для его аккаунта')
def create_user_and_order_and_delete(create_new_user_and_delete):
    access_token = create_new_user_and_delete[1]['accessToken']
    headers = {'Authorization': access_token}
    payload = {'ingredients': [
        '61c0c5a71d1f82001bdaaa70', '61c0c5a71d1f82001bdaaa6d',
        '61c0c5a71d1f82001bdaaa6f', '61c0c5a71d1f82001bdaaa77'
    ]}
    response_body = requests.post(Urls.ORDER_CREATE, data=payload, headers=headers)
    yield access_token, response_body
    requests.delete(Urls.USER_DELETE, headers={'Authorization': access_token})

@pytest.fixture
@allure.title('Фикстура создает пользователя с рандомными кредами и удаляет его из базы после теста')
def create_new_user_and_delete():
    payload_cred = {
        'email': create_random_email(),
        'password': create_random_password(),
        'name': create_random_name()
    }
    response = requests.post(Urls.USER_REGISTER, data=payload_cred)
    response_body = response.json()

    yield payload_cred, response_body

    access_token = response_body['accessToken']
    requests.delete(Urls.USER_DELETE, headers={'Authorization': access_token})

@pytest.fixture
@allure.title('Передает в драйвер токены созданного пользователя')
def set_user_tokens(driver, create_new_user_and_delete):
    driver.get(Urls.BASE_URL)
    user_data = create_new_user_and_delete[1]
    access_token = user_data.get('accessToken')
    refresh_token = user_data.get('refreshToken')
    if access_token and refresh_token:
        driver.execute_script(f'window.localStorage.setItem("accessToken", "{access_token}");')
        driver.execute_script(f'window.localStorage.setItem("refreshToken", "{refresh_token}");')



