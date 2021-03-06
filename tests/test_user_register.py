from lib.my_requests import MyRequests
from datetime import datetime
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserRegister(BaseCase):

    def test_creat_user_succesfully(self):
        base_part = "lernqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        email = f"{base_part}{random_part}@{domain}"
        data = {'password': '1234',
                'username': 'lernqa',
                'firstName': 'lernqa',
                'lastName': 'lernqa',
                'email': email
                }
        response = MyRequests.post("/user/", data= data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)
        response = MyRequests.post("/user/", data= data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"
        #print(response.status_code)
        #print(response.content)
