from faker import Faker

# Инициализация генератора случайных данных
fake = Faker()
fakeRU = Faker(locale='ru_RU')  # Генератор для русскоязычных данных


def create_random_email(): # Генерирует случайный адрес электронной почты

    email = fake.free_email()  # Генерация случайного адреса электронной почты
    return email


def create_random_password(length=10): # Генерирует случайный пароль, содержащий буквы, цифры и специальные символы.

    password = fake.password(length=length, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return password


def create_random_name(): # Генерирует случайное имя пользователя на русском языке

    username = fakeRU.first_name()  # Генерация случайного имени
    return username
