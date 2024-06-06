from datetime import time
from pprint import pprint


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=6)
    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)

    if current_time.hour >= 22 or current_time.hour <= 6:
        is_dark_theme = True
    else:
        is_dark_theme = False

    print('1. Время:', current_time)
    print('   Темная тема:', is_dark_theme)
    assert is_dark_theme is True


test_dark_theme_by_time()


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """

    current_time = time(hour=23)
    dark_theme_enabled_by_user = None
    # TODO переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную

    if dark_theme_enabled_by_user:
        is_dark_theme = True
    elif dark_theme_enabled_by_user is None:
        if current_time.hour >= 22 or current_time.hour <= 6:
            is_dark_theme = True
        else:
            is_dark_theme = False
    else:
        is_dark_theme = False

    print('2. Время:', current_time)
    print('   Темная тема включена вручную:', dark_theme_enabled_by_user)
    print('   Темная тема:', is_dark_theme)
    assert is_dark_theme is True


test_dark_theme_by_time_and_user_choice()


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"
    for user in users:
        if user["name"] == "Olga":
            suitable_users = user
            print('3. Пользователь: ')
            pprint(suitable_users)
            break

    assert suitable_users == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    suitable_users = []

    for user in users:
        if user["age"] <= 20:
            suitable_users.append(user)
    print('4. Все пользователи младше 20 лет:')
    pprint(suitable_users)

    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


test_find_suitable_user()


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def print_function_name_and_args(func, *args):
    func_name = func.__name__.replace('_', ' ').title()
    args_name = ", ".join([*args])
    print(f"{func_name} [{args_name}]")
    return f"{func_name} [{args_name}]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    print('5. Название функции 1:')
    actual_result = print_function_name_and_args(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


open_browser(browser_name="Chrome")


def go_to_companyname_homepage(page_url):
    print('6. Название функции 2:')
    actual_result = print_function_name_and_args(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


go_to_companyname_homepage(page_url="https://companyname.com")


def find_registration_button_on_login_page(page_url, button_text):
    print('7. Название функции 3:')
    actual_result = print_function_name_and_args(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"


find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")