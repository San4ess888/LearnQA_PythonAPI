from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
class TestUserDelete(BaseCase):
    def test_delete_user_2(self):
        # Login
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # GET1
        response5 = MyRequests.get(f"/user/2",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid},
                                   )
        Assertions.assert_code_status(response5, 200)

        # DEL
        response3 = MyRequests.delete(
            f"/user/2",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_code_status(response3, 400)
        assert response3.content.decode(
            "utf-8") == f"Please, do not delete test users with ID 1, 2, 3, 4 or 5.", f"Unexpected response content {response.content}"


    def test_delete_created_user(self):
        #Register
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
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
        response2 = MyRequests.post("/user/login", data= login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #GET1
        response5 = MyRequests.get(f"/user/{user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
        )
        Assertions.assert_code_status(response5, 200)

        #DEL
        response3 = MyRequests.delete(
            f"/user/{user_id}",
            headers = {"x-csrf-token":token},
            cookies = {"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response3, 200)

        #GET2
        response4 = MyRequests.get(f"/user/{user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
        )
        Assertions.assert_code_status(response4, 404)
        assert response4.content.decode(
            "utf-8") == f"User not found", f"Unexpected response content {response.content}"

    def test_delete_another_created_user(self):
        # Register1
        register_data1 = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data1)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json(response1, "id")

        email1 = register_data1['email']
        #first_name = register_data['firstName']
        # last_name = register_data['lastName']
        password1 = register_data1['password']
        user_id1 = self.get_json_value(response1, "id")

        # Login1
        login_data1 = {
            'email': email1,
            'password': password1
        }
        response2 = MyRequests.post("/user/login", data=login_data1)
        auth_sid1 = self.get_cookie(response2, "auth_sid")
        token1 = self.get_header(response2, "x-csrf-token")

        # GET1
        response5 = MyRequests.get(f"/user/{user_id1}",
                                   headers={"x-csrf-token": token1},
                                   cookies={"auth_sid": auth_sid1},
                                   )
        Assertions.assert_code_status(response5, 200)



        # Register2
        register_data2 = self.prepare_registration_data()
        response11 = MyRequests.post("/user/", data=register_data2)
        Assertions.assert_code_status(response11, 200)
        Assertions.assert_json(response11, "id")

        email2 = register_data2['email']
        # first_name = register_data['firstName']
        # last_name = register_data['lastName']
        password2 = register_data2['password']
        user_id2 = self.get_json_value(response11, "id")

        # Login2
        login_data2 = {
            'email': email2,
            'password': password2
        }
        response12 = MyRequests.post("/user/login", data=login_data2)
        auth_sid2 = self.get_cookie(response12, "auth_sid")
        token2 = self.get_header(response12, "x-csrf-token")

        # GET1
        response13 = MyRequests.get(f"/user/{user_id2}",
                                   headers={"x-csrf-token": token2},
                                   cookies={"auth_sid": auth_sid2},
                                   )
        Assertions.assert_code_status(response13, 200)

        # DEL
        response14 = MyRequests.delete(
            f"/user/{user_id1}",
        )

        Assertions.assert_code_status(response14, 400)
        assert response4.content.decode(
            "utf-8") == f"Auth token not supplied", f"Unexpected response content {response.content}"


