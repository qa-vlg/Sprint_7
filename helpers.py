import random
import string

class CourierRandomData:

    @staticmethod
    def create_courier_data():
        login = ''.join(random.choices(string.ascii_letters + string.digits, k = random.choice(range(15, 25))))
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = random.choice(range(7, 25))))
        firstName = ''.join(random.choices(string.ascii_letters, k = random.choice(range(5, 15))))

        payload = {
            "login": login,
            "password": password,
            "firstName": firstName
        }
        return payload