### Дипломный проект. Задание 3: Тестирование веб-приложения Stellar Burgers.

### Проект для тестирования веб-приложения Stellar Burgers имеет следующую структуру. 

*config.py* - cодержит классы Urls и Endpoints, которые хранят основные URL-адреса и API-эндпоинты, используемые 
              в проекте. Это упрощает управление URL и делает код более читаемым.

*locators.py* - cодержит классы с локаторами для различных элементов на страницах. Каждый класс соответствует 
                определенной странице и содержит локаторы для элементов, которые будут использоваться в тестах.

*conftest.py* - cодержит фикстуры для тестов, такие как создание экземпляра веб-драйвера (Chrome или Firefox) 
                и генерация случайных учетных данных пользователя. Эти фикстуры используются в тестах для настройки 
                окружения.

*helpers.py* - cодержит вспомогательные функции для генерации данных пользователя, регистрации и аутентификации 
               через API, а также для создания заказов. Эти функции помогают упростить тесты, предоставляя необходимые 
               действия.

*base_page.py* - cодержит класс BasePage, который является базовым классом для всех страниц в проекте. Он включает 
                 методы для взаимодействия с элементами на странице, такие как нахождение видимых элементов, клик 
                 по элементам, ввод текста и т.д. Это позволяет избежать дублирования кода в других классах страниц.

# папка pages # - содержит классы, представляющие различные страницы веб-приложения (Page Object Model), состоит из:

*burger_builder_page.py* - содержит класс BurgerBuilderPage, который реализует методы для взаимодействия со страницей 
                           конструктора бургеров. Методы включают навигацию, выбор ингредиентов, проверку модальных 
                           окон и оформление заказа.
*forgot_password_page.py* - содержит класс ForgotPasswordPage, который реализует методы для работы со страницей 
                            восстановления пароля. Методы включают навигацию на страницу и отправку email 
                            для восстановления пароля.
*header_page.py* - содержит класс HeaderPage, который реализует методы для взаимодействия с заголовком страницы. 
                   Методы включают переход на страницы конструктора, ленты заказов и личного кабинета.
*login_page.py* - содержит класс LoginPage, который реализует методы для работы со страницей авторизации. 
                  Методы включают открытие страницы и переход на страницу восстановления пароля.
*order_page.py* - содержит класс OrderPage, который реализует методы для работы со страницей ленты заказов.
                  Методы включают открытие страницы, выбор последнего заказа и проверку наличия модального окна 
                  с деталями заказа.
*personal_page.py* - содержит класс PersonalPage, который реализует методы для работы с личным кабинетом пользователя. 
                     Методы включают открытие страницы, доступ к истории заказов и выход из аккаунта.
*reset_password_page.py* - содержит класс ResetPasswordPage, который реализует методы для работы со страницей сброса 
                           пароля. Методы включают проверку открытия страницы и взаимодействие с полем ввода пароля.

# папка test # - содержит тестовые файлы, которые предназначены для проверки функциональности веб-приложения, состоит из:

*test_burger_builder_page.py* - cодержит тесты для проверки функциональности страницы конструктора бургеров. 
                                Тесты включают проверку открытия модального окна с деталями ингредиента, закрытие окна 
                                и оформление заказа.
*test_navigation_header_page.py* - cодержит тесты для проверки навигации по заголовку страницы. Тесты включают переход 
                                   на главную страницу и ленту заказов.
*test_order_feed_section_page.py* - cодержит тесты для проверки функциональности страницы заказов. Тесты включают 
                                    открытие модального окна с деталями заказа и проверку соответствия заказов 
                                    в истории и ленте.
*test_password_recovery_page.py* - cодержит тесты для проверки функциональности страницы восстановления пароля. 
                                   Тесты включают переход на страницу восстановления и проверку работы кнопки 
                                   восстановления.
*test_personal_account_page.py* - cодержит тесты для проверки функциональности личного кабинета. Тесты включают переход 
                                  в профиль, доступ к истории заказов и выход из аккаунта.

### gitignore - файл, содержащий локальные файлы;
### README.md - файл, содержащий текстовую часть о проделанной работе; 
### requirements.txt - файл, содержащий список внешних зависимостей.

### Тесты для вывода из терминала - проверены командой: pytest -v.
### Команда для запуска с записью отчета в allure_results: `pytest tests --alluredir=allure_results`.
### Отчёт в формате веб-страницы: `allure serve allure_results`. 
