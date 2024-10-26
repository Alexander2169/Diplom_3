from faker import Faker

fake = Faker()
fakeEN = Faker("en_US")  # Генератор данных на английском языке


def create_random_email(): # Генерирует случайный адрес электронной почты

    email = fake.free_email()
    return email


def create_random_password(): # Генерирует случайный пароль

    password = fake.password()
    return password


def create_random_name(): # Генерирует случайное имя пользователя

    username = fakeEN.first_name()
    return username
