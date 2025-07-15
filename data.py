

class OrderData:

    order_data_color_black = {

        "firstName": "Зинаида",
        "lastName": "Агафьева",
        "address": "Банный проезд, строение 5",
        "metroStation": 2,
        "phone": "+7 800 355 22 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "ну что сказать!?",
        "color": [
            "BLACK"
        ]
    }
    order_data_no_color = {

        "firstName": "Алекс",
        "lastName": "Алексеев",
        "address": "Амурская улица 34б кв 47",
        "metroStation": 4,
        "phone": "+7 111 355 35 35",
        "rentTime": 1,
        "deliveryDate": "2020-06-06",
        "comment": "Не торопитесь, я еще не дома."
    }
    order_data_both_colors = {

        "firstName": "Иван",
        "lastName": "Сергеев",
        "address": "Большой Чудов переулок 3б кв 89",
        "metroStation": 7,
        "phone": "8 800 355 35 35",
        "rentTime": 2,
        "deliveryDate": "2020-06-06",
        "comment": "Как можно быстрее пож!",
        "color": [
            "BLACK",
            "GREY"
        ]
    }

class CourierLoginData:
    
    valid_courier_credentials = {
        "login": "qa_vlg_test_courier_1",
        "password": "qwerty12345"
    }
    courier_credentials_invalid_pwd = {
        "login": "qa_vlg_test_courier",
        "password": "qwerty1234"
    }
    courier_credentials_invalid_login = {
        "login": "vlg_test_courier",
        "password": "qwerty12344"
    }
    courier_credentials_invalid_pwd = {
        "login": "vlg_test_courier",
        "password": "qwerty1234"
    }
    courier_credentials_empty_login = {
        "login": "",
        "password": "qwerty12344"
    }
    courier_credentials_empty_pwd = {
        "login": "qa_vlg_test_courier",
        "password": ""
    }

class CourierSignUpData:

    existing_courier_credentials = {
        "login": "qa_vlg_test_courier_1",
        "password": "qwerty12345",
        "firstName": "AlexVlg"
    }
    courier_credentials_empty_login = {
        "login": "",
        "password": "qwerty123",
        "firstName": "Alexx"
    }
    courier_credentials_empty_pwd = {
        "login": "some_test_data",
        "password": "",
        "firstName": "Samm"
    }

class LoginErrors:

    missing_login_info = "Недостаточно данных для входа"
    wrong_login_info = "Учетная запись не найдена"

class SignUpErrors:

    missing_user_info = "Недостаточно данных для создания учетной записи"
    existing_account = "Этот логин уже используется"

class DeleteCourierErrors:
    missing_courier_id = "Not Found."
    wrong_courier_id = "Курьера с таким id нет."

class GetOrderInfoErrors:
    missing_order_id = "Недостаточно данных для поиска"
    invalid_order_id = "Заказ не найден"

class GetAcceptOrderErrors:
    already_accepted = "Этот заказ уже в работе"
    missing_order_id = "Not Found."
    invalid_order_id = "Заказа с таким id не существует"
    invalid_courier_id = "Курьера с таким id не существует"
