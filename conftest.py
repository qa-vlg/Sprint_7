import pytest
from data import OrderData
from helpers import CourierRandomData
from methods.order_methods import OrderMethods
from methods.courier_methods import CourierMethods


@pytest.fixture
def courier():
    payload = CourierRandomData.create_courier_data()
    CourierMethods.courier_create(payload)
    response = CourierMethods.courier_login(payload)
    courier_id = response[1]["id"]
    yield courier_id
    CourierMethods.courier_delete(courier_id)

@pytest.fixture
def order_details():
    payload = OrderData.order_data_color_black
    created_order_data = OrderMethods.order_create(payload)
    order_track = created_order_data[1]["track"]
    order_details = OrderMethods.get_order_details(order_track)
    return order_details