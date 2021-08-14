from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import json
class TestUserEdit(BaseCase):
    def test_edit_not_auth_user(self):
        #Edit
        new_name = "Changed Name"
        response = MyRequests.put(
            f"/user/2",
            #headers = {"x-csrf-token":token},
            #cookies = {"auth_sid": auth_sid},
            data = {"firstName": new_name}
        )
        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Auth token not supplied", f"Unexpected response content {response.content}"

    def test_edit_another_user(self):
        # Register
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        last_name = register_data['lastName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # Login
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # Edit
        new_name = "Changed Name"
        response3 = MyRequests.put(
            f"/user/1",
            headers={"x-csrf-token": token},
            #cookies={"auth_sid": auth_sid},
            data={"username": new_name}
        )

        Assertions.assert_code_status(response3, 400)
        assert response3.content.decode(
            "utf-8") == f"Auth token not supplied", f"Unexpected response content {response.content}"

        response4 = MyRequests.get(f"/user/1",
                                 #headers = {"x-csrf-token": token},
                                 #cookies = {"auth_sid": auth_sid}
        )
        expected_fields = ["username" ]
        Assertions.assert_json_has_keys(response4, expected_fields)

    def test_edit_email(self):
        # Register
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        last_name = register_data['lastName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # Login
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # Edit
        new_email = "vinkotovexample.com"
        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"email": new_email}
        )
        Assertions.assert_code_status(response3, 400)
        assert response3.content.decode(
            "utf-8") == f"Invalid email format", f"Unexpected response content {response.content}"

    def test_edit_short_name(self):
        # Register
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        last_name = register_data['lastName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # Login
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # Edit
        new_name = "v"
        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )
        Assertions.assert_code_status(response3, 400)
        status = json.loads(response3.text)

        assert status['error'] == "Too short value for field firstName", f"Unexpected response content {response.content}"










