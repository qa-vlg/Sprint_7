import requests
import allure
from endpoints import Urls

class OrderMethods:

    @staticmethod
    @allure.step('Создание Заказа')
    def order_create(payload):
        response = requests.post(Urls.ORDER_URL, json=payload)
        status_code = response.status_code
        formated_response = response.json()
        return status_code, formated_response
    
    @staticmethod
    @allure.step('Получение списка Заказов')
    def get_list_of_orders():
        response = requests.get(Urls.ORDER_URL)
        status_code = response.status_code
        list_of_orders = response.json()
        return status_code, len(list_of_orders["orders"])
    
    @staticmethod
    @allure.step('Подтверждение Заказа')
    def order_accept(order_id, courier_id):
        endpoint = f'{Urls.ORDER_ACCEPT}{order_id}?courierId={courier_id}'
        response = requests.put(endpoint)
        status_code = response.status_code
        formated_response = response.json()
        return status_code, formated_response

    @staticmethod
    @allure.step('Получение информации о Заказе')
    def get_order_details(order_id):
        endpoint = f'{Urls.ORDER_TRACK_URL}?t={order_id}'
        response = requests.get(endpoint)
        status_code = response.status_code
        formated_response = response.json()
        return status_code, formated_response
