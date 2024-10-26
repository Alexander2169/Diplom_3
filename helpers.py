from faker import Faker

fake = Faker()
fakeEN = Faker(locale='en_US')  # Генератор данных на английском языке


def create_random_email(): # Генерирует случайный адрес электронной почты

    email = fake.free_email()
    return email


def create_random_password(length=10): # Генерирует случайный пароль, содержащий буквы, цифры и специальные символы.

    password = fake.password(length=length, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return password


def create_random_name(): # Генерирует случайное имя пользователя

    username = fakeEN.first_name()
    return username
