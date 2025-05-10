from main_kinopoisk import Kinopoisk
import allure


@allure.severity("blocker")
@allure.title("Отображения введенного названия фильма")
@allure.feature("Фильмы")
@allure.description("Ввод названия фильма в поиск")
def test_input_title(driver):
    with allure.step("Открытие главной страницы"):
        kinopoisk = Kinopoisk(driver)
    with allure.step("Содержимое поля ввода совпало с введенным названием"):
        result = kinopoisk.input_movie_title("Терминатор")
        assert result == "Терминатор"
    

@allure.severity("blocker")
@allure.title("Отображения информации о фильме")
@allure.feature("Фильмы")
@allure.description("Просмотр информации о конкретном фильме")
def test_movie_details(driver):
    with allure.step("Открытие главной страницы"):
        kinopoisk = Kinopoisk(driver)
    with allure.step("Сравнение последних слов в url"):
        url = kinopoisk.movie_details("Терминатор")
        assert url.endswith("details") == True
  
    

@allure.severity("blocker")
@allure.title("Переход в раздел Каналы")
@allure.feature("Главная страница")
@allure.description("Нажатие на кнопку Каналы") 
def test_channels(driver):
    with allure.step("Открытие главной страницы"):
        kinopoisk = Kinopoisk(driver)
    with allure.step("Сравнение итогового url с нужным"):
        res = kinopoisk.button_channels()
        assert res == "https://hd.kinopoisk.ru/channels"
   

@allure.severity("blocker")
@allure.title("Открытие окна авторизации")
@allure.feature("Главная страница")
@allure.description("Открытие окна формы авторизации")
def test_button_login(driver):
    with allure.step("Открытие главной страницы"):
        kinopoisk = Kinopoisk(driver)
    with allure.step("Сравнение заголовка регистрации с нужным"):
        result = kinopoisk.button_login()
        assert result == ("Введите номер телефона")
    

@allure.severity("blocker")
@allure.title("Переход к выбору подписки")
@allure.feature("Главная страница")
@allure.description("Открытие окна с выбором подписки")
def test_button_subcribe(driver):
    with allure.step("Открытие главной страницы"):
        kinopoisk = Kinopoisk(driver)
    with allure.step("Открытие окна с выбором подписки"):
        result = kinopoisk.button_subscription()
        assert result == "Попробовать бесплатно"
