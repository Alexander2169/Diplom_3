import requests
import random
import allure
from faker import Faker
from config import *

@allure.step('Генерация данных пользователя')
def generate_user_info():
    fake = Faker()
    user_info = {
        'email': fake.email(),
        'password': fake.password(),
        'name': fake.name()
    }
    return user_info

@allure.step('Регистрация и авторизация нового пользователя через API, возвращение авторизационных данных')
def register_and_authenticate_user():
    user_info = generate_user_info()
    url_reg = f'{Urls.BASE_URL}{Endpoints.USER_ACCOUNT_CREATION}'
    url_log = f'{Urls.BASE_URL}{Endpoints.USER_LOGIN}'
    response_reg = requests.post(url_reg, data=user_info)
    if response_reg.status_code == 200 and response_reg.json()['success'] == True:
        login_info = {
            'email': user_info['email'],
            'password': user_info['password']
        }
        response_log = requests.post(url_log, data=login_info)
        if response_log.status_code == 200 and response_log.json()['success'] == True:
            tokens = {
                'accessToken': response_log.json()['accessToken'],
                'refreshToken': response_log.json()['refreshToken']
            }
            return tokens
        else:
            logging.error('Проблема с авторизацией пользователя')
    else:
        logging.error('Проблема с регистрацией пользовательского аккаунта')

@allure.step('Удаление учетной записи пользователя через API')
def delete_user_account(access_token):
    url = f'{Urls.BASE_URL}{Endpoints.USER_ACCOUNT_DELETION}'
    response = requests.delete(url, headers={'Authorization': access_token})
    if not (response.status_code == 202 and response.json()['success'] == True):
        logging.error('Проблема с удалением пользовательского аккаунта')

@allure.step('Определение случайного id ингридиента через API')
def fetch_random_ingredient_id():
    url = f'{Urls.BASE_URL}{Endpoints.INGREDIENTS_RETRIEVAL}'
    response = requests.get(url)
    ingredient_id = response.json()['data'][random.randint(0, len(response.json()['data']) - 1)]['_id']
    return ingredient_id

@allure.step('Определение случайного id булки для заказа')
def fetch_random_bun_id():
    return random.choice(BunIds.BUN_IDS)

@allure.step('Создание заказа через API')
def place_order(access_token):
    url = f'{Urls.BASE_URL}{Endpoints.ORDER_CREATION}'
    ingredient_list = [fetch_random_bun_id(), fetch_random_ingredient_id()]
    headers = {'Authorization': access_token}
    payload = {'ingredients': ingredient_list}
    with allure.step('Отправка запроса на создание заказа пользователя'):
        response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()['order']['number']
    else:
        logging.error('Проблема с созданием ордера пользователя через API')

