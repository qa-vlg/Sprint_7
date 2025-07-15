import requests
import allure
from endpoints import Urls

class CourierMethods:

    @staticmethod
    @allure.step('Логин Курьера')
    def courier_login(payload):
        response = requests.post(Urls.COUIRIER_LOGIN_URL, json=payload)
        status_code = response.status_code
        formated_response = response.json()
        return status_code, formated_response
    
    @staticmethod
    @allure.step('Создание Курьера')
    def courier_create(payload):
        response = requests.post(Urls.COURIER_URL, json=payload)
        status_code = response.status_code
        formated_response = response.json()
        return status_code, formated_response
    
    @staticmethod
    @allure.step('Удаление Курьера')
    def courier_delete(id):
        payload = {
            "id": id
            }
        endpoint = f'{Urls.COURIER_URL}{id}'
        response = requests.delete(endpoint, json=payload)
        status_code = response.status_code
        formated_response = response.json()
        return status_code, formated_response
    