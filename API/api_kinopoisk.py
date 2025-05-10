import requests
from config_API import Config_API

class Kinopoisk:
   
    def __init__(self):
        self.base_url = Config_API.API_URL
        self.my_headers = {
            'X-API-KEY': Config_API.API_key,
            'Content-Type': 'application/json'
            }

    def get_movie_by_id(self, id:str)->any:
        """
            Поиск фильма по id
        """
        url = self.base_url + "/api/v2.2/films/" + id
        payload = {
            'method': 'GET'
        }
        headers = self.my_headers
        resp = requests.request('GET' , url, json=payload, headers=headers)
        return resp
        

    def get_movie_by_keyword(self, keyword: str)->any:
        """
            Поиск фильма по названию
        """
        url = self.base_url + "/api/v2.1/films/search-by-keyword"
        payload = {
            'method': 'GET'
        }
        params={
            "keyword": keyword,
            "page" : 1
                }
        headers = self.my_headers
        resp = requests.request('GET' , url, json=payload, params = params, headers=headers)
        return resp


    def get_movie_without_keyword(self):
        """
            Поиск фильма по пустому названию
        """
        keyword = ""
        page = "1"
        url = self.base_url + "/api/v2.1/films/search-by-keyword?keyword=" + keyword + "&page=" + page
        payload = {
            'method': 'GET'
        }
        headers = self.my_headers
        resp = requests.request('GET' , url, json=payload, headers=headers)
        return resp
    
    def seach_name_person(self, name_person):
        """
            Поиск актера по имени
        """
        url = self.base_url + "/api/v1/persons?"
        payload = {
            'method': 'GET'
        }
        params={
            "name": name_person,
            "page" : 1
                }
        headers = self.my_headers
        response = requests.request('GET' , url, json=payload, params = params, headers = headers)
        return response