import random
import string
import pytest
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

    def test_create_user_with_uncorrect_email(self):
        email = 'vinkotovexample.com'
        data = self.prepare_registration_data(email)
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Invalid email format", f"Unexpected response content {response.content}"

    def test_create_user_with_short_name(self):
        base_part = "lernqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        email = f"{base_part}{random_part}@{domain}"
        data = {'password': '1234',
                'username': 'l',
                'firstName': 'lernqa',
                'lastName': 'lernqa',
                'email': email
                }
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"The value of 'username' field is too short", f"Unexpected response content {response.content}"

    def test_creat_user_with_long_name(self):
        base_part = "lernqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        email = f"{base_part}{random_part}@{domain}"
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(251))
        data = {'password': '1234',
                'username': rand_string,
                'firstName': 'lernqa',
                'lastName': 'lernqa',
                'email': email
                }
        response = MyRequests.post("/user/", data= data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"The value of 'username' field is too long", f"Unexpected response content {response.content}"

    exclude_params = [
        ("no_password"),
        ("no_username"),
        ("no_firstName"),
        ("no_lastName"),
        ("no_email")
    ]

    @pytest.mark.parametrize('condition', exclude_params)
    def test_creat_user_without_fields(self, condition):
        if condition == "no_password":
            base_part = "lernqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"
            data = {'username': 'lernqa',
                    'firstName': 'lernqa',
                    'lastName': 'lernqa',
                    'email': email
                    }
            response = MyRequests.post("/user/", data=data)
            Assertions.assert_code_status(response, 400)
            assert response.content.decode(
                "utf-8") == f"The following required params are missed: password", f"Unexpected response content {response.content}"
        elif condition == "no_username":
            base_part = "lernqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"
            data = {'password': '1234',
                    'firstName': 'lernqa',
                    'lastName': 'lernqa',
                    'email': email
                    }
            response = MyRequests.post("/user/", data=data)
            Assertions.assert_code_status(response, 400)
            assert response.content.decode(
                "utf-8") == f"The following required params are missed: username", f"Unexpected response content {response.content}"
        elif condition == "no_firstName":
            base_part = "lernqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"
            data = {'password': '1234',
                    'username': 'lernqa',
                    'lastName': 'lernqa',
                    'email': email
                    }
            response = MyRequests.post("/user/", data=data)
            Assertions.assert_code_status(response, 400)
            assert response.content.decode(
                "utf-8") == f"The following required params are missed: firstName", f"Unexpected response content {response.content}"
        elif condition == "no_lastName":
            base_part = "lernqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"
            data = {'password': '1234',
                    'username': 'lernqa',
                    'firstName': 'lernqa',
                    'email': email
                    }
            response = MyRequests.post("/user/", data=data)
            Assertions.assert_code_status(response, 400)
            assert response.content.decode(
                "utf-8") == f"The following required params are missed: lastName", f"Unexpected response content {response.content}"
        elif condition == "no_email":
            base_part = "lernqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"
            data = {'password': '1234',
                    'username': 'lernqa',
                    'firstName': 'lernqa',
                    'lastName': 'lernqa'
                    }
            response = MyRequests.post("/user/", data=data)
            Assertions.assert_code_status(response, 400)
            assert response.content.decode(
                "utf-8") == f"The following required params are missed: email", f"Unexpected response content {response.content}"






