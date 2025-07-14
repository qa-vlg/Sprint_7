import requests
from endpoints import Urls

class CourierMethods:

    @staticmethod
    def courier_login(payload):
        response = requests.post(Urls.COUIRIER_LOGIN_URL, json=payload)
        status_code = response.status_code
        formated_response = response.json()
        return status_code, formated_response
    
    @staticmethod
    def courier_create(payload):
        response = requests.post(Urls.COURIER_URL, json=payload)
        status_code = response.status_code
        formated_response = response.json()
        return status_code, formated_response
    
    @staticmethod
    def courier_delete(id):
        payload = {
            "id": id
            }
        endpoint = f'{Urls.COURIER_URL}{id}'
        response = requests.delete(endpoint, json=payload)
        status_code = response.status_code
        formated_response = response.json()
        return status_code, formated_response
    