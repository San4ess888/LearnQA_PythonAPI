import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime
class TestUserEdit(BaseCase):
    def test_edit_created_user(self):
        #Register
        register_data = self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        #last_name = register_data['lastName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        #Login
        login_data = {
            'email': email,
            'password': password
        }
        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data= login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #Edit
        new_name = "Changed Name"
        response3 = requests.put()


