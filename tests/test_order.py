import allure
import pytest
from methods.order_methods import OrderMethods
from data import OrderData, GetOrderInfoErrors, GetAcceptOrderErrors

class TestCreateOrder:

    @allure.title('Позитивный сценарий создания Заказа.')
    @allure.description('Используя верные данные, выполняем создание заказа.')
    @pytest.mark.parametrize("payload", [OrderData.order_data_color_black, OrderData.order_data_no_color, OrderData.order_data_both_colors])
    def test_create_valid_order_true(self, payload):
        status_code, response_data = OrderMethods.order_create(payload)
        assert status_code == 201 and response_data['track'] is not None

class TestGetOrders:

    @allure.title('Позитивный сценарий получения списка Заказов.')
    @allure.description('Выполняем получения списка Заказов.')
    def test_get_order_true(self):
        status_code, number_of_orders = OrderMethods.get_list_of_orders()
        assert status_code == 200 and number_of_orders > 0
    
class TestGetOrderInfo:

    @allure.title('Позитивный сценарий получения информации о Заказе.')
    @allure.description('Используя верные данные, получаем информацию о заказе.')
    def test_get_order_info_true(self, order_details):
        tracking_id = order_details[1]["order"]["track"]
        status_code, response_data = OrderMethods.get_order_details(tracking_id)
        assert status_code == 200 and response_data["order"]["track"] == tracking_id
    
    @allure.title('Негативный сценарий получения информации о Заказе.')
    @allure.description('Используя неверные данные, пытаемся получить информацию о заказе.')
    @pytest.mark.parametrize("order_id, error, error_message", [('0', 404, GetOrderInfoErrors.invalid_order_id), 
                                                         ('', 400, GetOrderInfoErrors.missing_order_id)])
    def test_get_order_invalid_data_false(self, order_id, error, error_message):
        status_code, response_data = OrderMethods.get_order_details(order_id)
        assert status_code == error and response_data["message"] == error_message

class TestOrderAccept:

    @allure.title('Позитивный сценарий подтверждения Заказа.')
    @allure.description('Используя верные данные, подтверждаем Заказ.')
    def test_accept_valid_order_true(self, courier, order_details):
        order_id = order_details[1]["order"]["id"]
        courier_id = courier
        status_code, response_data = OrderMethods.order_accept(order_id, courier_id)
        assert status_code == 200 and response_data["ok"] == True

    @allure.title('Негативный сценарий подтверждения Заказа: Заказ уже подтвержден')
    @allure.description('Используя верные данные, подтверждаем уже подтвержденныый Заказ.')
    def test_accept_already_accepted_order_false(self, courier, order_details):
        order_id = order_details[1]["order"]["id"]
        courier_id = courier
        OrderMethods.order_accept(order_id, courier_id)
        status_code, response_data = OrderMethods.order_accept(order_id, courier_id)
        assert status_code == 409 and response_data["message"] == GetAcceptOrderErrors.already_accepted
    
    @allure.title('Негативный сценарий подтверждения Заказа: отсутствует order_id')
    @allure.description('Пытаемся подтвердить Заказ без order_id.')
    def test_accept_order_missing_order_id_false(self, courier):
        order_id = ''
        courier_id = courier
        status_code, response_data = OrderMethods.order_accept(order_id, courier_id)
        assert status_code == 404 and response_data["message"] == GetAcceptOrderErrors.missing_order_id

    @allure.title('Негативный сценарий подтверждения Заказа: неверный order_id')
    @allure.description('Пытаемся подтвердить Заказ используя неверный order_id.')
    def test_accept_order_invalid_order_id_false(self, courier):
        order_id = '00'
        courier_id = courier
        status_code, response_data = OrderMethods.order_accept(order_id, courier_id)
        assert status_code == 404 and response_data["message"] == GetAcceptOrderErrors.invalid_order_id

    @allure.title('Негативный сценарий подтверждения Заказа: неверный courier_id')
    @allure.description('Пытаемся подтвердить Заказ используя неверный courier_id.')
    def test_accept_order_invalid_courier_id_false(self, order_details):
        order_id = order_details[1]["order"]["id"]
        courier_id = '00'
        status_code, response_data = OrderMethods.order_accept(order_id, courier_id)
        assert status_code == 404 and response_data["message"] == GetAcceptOrderErrors.invalid_courier_id
        