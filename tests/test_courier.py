import allure
import pytest
from helpers import CourierRandomData
from methods.courier_methods import CourierMethods
from data import CourierLoginData, CourierSignUpData, LoginErrors, SignUpErrors, DeleteCourierErrors


class TestCourierLogin:

    @allure.title('Позитивный сценарий проверки логина Курьера.')
    @allure.description('Используя активный аккаунт Курьера, выполняем логин.')
    @pytest.mark.parametrize("payload", [CourierLoginData.valid_courier_credentials])
    def test_courier_login_true(self, payload):
        status_code, response_data = CourierMethods.courier_login(payload)
        assert status_code == 200 and response_data['id'] is not None

    @allure.title('Негативный сценарий проверки логина Курьера: wrong values')
    @allure.description('Выполняем логин Курьера используя неверные данные.')
    @pytest.mark.parametrize("payload", [CourierLoginData.courier_credentials_invalid_login, CourierLoginData.courier_credentials_invalid_pwd])
    def test_courier_login_wrong_credentials_false(self, payload):
        status_code, response_data = CourierMethods.courier_login(payload)
        assert status_code == 404 and response_data["message"] == LoginErrors.wrong_login_info

    @allure.title('Негативный сценарий проверки логина Курьера: empty values')
    @allure.description('Выполняем логин Курьера используя пустые вводные данные.')
    @pytest.mark.parametrize("payload", [CourierLoginData.courier_credentials_empty_pwd, CourierLoginData.courier_credentials_empty_login])
    def test_courier_login_missing_credentials_false(self, payload):
        status_code, response_data = CourierMethods.courier_login(payload)
        assert status_code == 400 and response_data["message"] == LoginErrors.missing_login_info


class TestCourierCreate:

    @allure.title('Позитивный сценарий создания Курьера.')
    @allure.description('Используя верные данные, создаем Курьера.')
    def test_create_courier_true(self):
        payload = CourierRandomData.create_courier_data()
        status_code, response_data = CourierMethods.courier_create(payload)
        assert status_code == 201 and response_data["ok"] == True

    @allure.title('Негативный сценарий проверки создания Курьера: existing credentials')
    @allure.description('Выполняем создание Курьера используя данные уже существующего.')
    @pytest.mark.parametrize("payload", [CourierSignUpData.existing_courier_credentials])
    def test_create_courier_existing_false(self, payload):
        status_code, response_data = CourierMethods.courier_create(payload)
        assert status_code == 409 and response_data["message"] == SignUpErrors.existing_account

    @allure.title('Негативный сценарий проверки создания Курьера: empty values')
    @allure.description('Выполняем создание Курьера используя пустые вводные данные.')
    @pytest.mark.parametrize("payload", [CourierSignUpData.courier_credentials_empty_login, CourierSignUpData.courier_credentials_empty_pwd])
    def test_create_courier_existing_false(self, payload):
        status_code, response_data = CourierMethods.courier_create(payload)
        assert status_code == 400 and response_data["message"] == SignUpErrors.missing_user_info


class TestCourierDelete:
    
    @allure.title('Позитивный сценарий удаления Курьера.')
    @allure.description('Используя верные данные, удаляем Курьера.')
    def test_delete_existing_courier_true(self, courier):
        courier_id = courier
        status_code, response_data = CourierMethods.courier_delete(courier_id)
        assert status_code == 200 and response_data["ok"] == True

    @allure.title('Негативный сценарий проверки удаления Курьера: wrong values')
    @allure.description('Выполняем удаление Курьера используя неверные данные.')
    @pytest.mark.parametrize("courier_id, error_message", [('0', DeleteCourierErrors.wrong_courier_id), 
                                                         ('', DeleteCourierErrors.missing_courier_id)])
    def test_delete_courier_invalid_data_false(self, courier_id, error_message):
        status_code, response_data = CourierMethods.courier_delete(courier_id)
        assert status_code == 404 and response_data["message"] == error_message
