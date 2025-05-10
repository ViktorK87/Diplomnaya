from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure
from selenium.webdriver.support import expected_conditions as EC


class Kinopoisk:
    def __init__(self, driver):
        """
            Эта функция инициализирует параметры класса
        """
        self.base_url = "https://hd.kinopoisk.ru/"
        self._driver = driver


    def input_movie_title(self, title: str)->str:
        """
            Проверка отображения введенного названия фильма 
        """
        self._driver.get(self.base_url)
        search = self._driver.find_element(By.CSS_SELECTOR, "[data-tid = 'SearchButton']")
        search.click()
        input = self._driver.find_element(By.CSS_SELECTOR, "input[type='search']")
        input.click()
        input.send_keys(title)
        return input.get_property("value")
    

    def movie_details(self, title)->str:
        """
            Проверка отображения информации о фильме
        """
        self._driver.get(self.base_url)
        search = self._driver.find_element(By.CSS_SELECTOR, "[data-tid = 'SearchButton']")
        search.click()
        input = self._driver.find_element(By.CSS_SELECTOR, "input[type='search']")
        input.click()
        input.send_keys(title)
        self._driver.implicitly_wait(4)
        self._driver.find_element(By.CSS_SELECTOR, "#suggest-item-0,[href='/film/492c446642bf8dc88f0abcb9a4b02f7f]").click()
        self._driver.implicitly_wait(4)
        self._driver.find_element(By.XPATH, "//button[text()='Детали']").click()
        return self._driver.current_url
   

    def button_channels(self)->any:
        """
            Проверка кнопки Каналы
        """
        self._driver.get(self.base_url)
        self._driver.fullscreen_window()
        self._driver.implicitly_wait(5)
        channels = self._driver.find_element(By.CSS_SELECTOR, '#channels')
        channels.click()
        self._driver.implicitly_wait(10)
        self._driver.find_element(By.CSS_SELECTOR, ".styles_container__hOEjm")
        return self._driver.current_url

        
    
    def button_login(self):
        """
            Проверка кнопки Войти
        """
        self._driver.get(self.base_url) 
        login = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((
                    By.CSS_SELECTOR, "a.Link_root__Z3NLP.LoginLink_root__72GCB")))
        login.click()  
        auth_title = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((
                    By.CSS_SELECTOR, '.passp-add-account-page-title'))).text
        print(auth_title)
        with allure.step("Возврат заголовка"):
            return auth_title


    def button_subscription(self)->str:
        """
            Проверка кнопки подписка
        """
        self._driver.get(self.base_url)
        self._driver.find_element(By.CSS_SELECTOR, "[id=promo]").click()
        subscr_btn = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, ".style_button__PNtXT.style_buttonSize48__7RF4w"
            )))
        return subscr_btn.text
        

        