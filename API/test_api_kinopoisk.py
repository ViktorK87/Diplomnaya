from api_kinopoisk import Kinopoisk
import pytest
import allure
#Запуск тестов с аллюр: pytest --alluredir=./allure_result
#Просмотр результатов: allure serve allure_result
#Остановить сервер: Ctrl+C
#film_id = "4959136"

kinopoisk = Kinopoisk()

@allure.severity("blocker")
@allure.feature("Поиск")
@allure.description("API Запрос по id фильму")
@allure.title("Поиск фильма по id")
def test_by_id():
    with allure.step("Отправить API Запрос по id фильму"):
        resp = kinopoisk.get_movie_by_id("4959136").json()
    with allure.step("id фильма содержится в ответе"):
        assert resp['kinopoiskId'] == 4959136


@allure.severity("blocker")
@allure.feature("Поиск")
@allure.description("API Запрос по названию фильма")
@allure.title("Поиск по названию фильма")
@pytest.mark.parametrize("keyword", ["Аватар", "Прометей"])
def test_keyword(keyword):
    with allure.step("Отправить API Запрос по названию фильма"):
        resp = kinopoisk.get_movie_by_keyword(keyword)
    with allure.step("Статус код == 200"):
        assert resp.status_code == 200
    with allure.step("Название фильма содержится в ответе"):
        assert resp.json()["keyword"] == keyword


@allure.severity("minor")
@allure.feature("Поиск")
@allure.description("API Запрос без названия")
@allure.title("Поиск по пустому названию фильма")
def test_empty():
    with allure.step("Отправить API Запрос без названия фильма"):
        resp = kinopoisk.get_movie_without_keyword().json()
    with allure.step("Тело ответа пустое"):
        assert resp['films'] == []
    
@allure.severity("major")
@allure.feature("Поиск")
@allure.description("API Запрос по имени актера")
@allure.title("Поиск по имени актера")
@pytest.mark.parametrize("keyword", ["Джонни Депп", "Брэд Питт", "Arnold Schwarzenegger", "Sylvester Stallone"])
def test_seach_name_person(keyword):
    with allure.step("Отправить запрос по имени актера"):
        resp = kinopoisk.seach_name_person(keyword)
    with allure.step("Статус код == 200"):    
        assert resp.status_code == 200
    with allure.step("Имя актера содержится в ответе"):
        assert resp.json()["items"][0]["nameRu"] == keyword


@allure.severity("minor")
@allure.feature("Поиск")
@allure.description("API Запроc по неверному id")
@allure.title("Поиск по неверному id")
def test_wrong_id():
    with allure.step("Отправить запрос по айди фильма"):
        resp = kinopoisk.get_movie_by_id("2")
    with allure.step("Статус код == 404"):
        assert resp.status_code == 404
