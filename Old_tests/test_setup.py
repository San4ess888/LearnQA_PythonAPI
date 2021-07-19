import requests
import pytest
class TestUserAuth:
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]
    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        responce1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        assert "auth_sid" in responce1.cookies, "there is no auth cookie in the responce"
        assert "x-csrf-token" in responce1.headers, "there is no x-csrf-toke in the responce"
        assert "user_id" in responce1.json(), "there is no user_id in the responce"

        self.auth_sid = responce1.cookies.get("auth_sid")
        self.token = responce1.headers.get("x-csrf-token")
        self.user_id_from_auth_metod = responce1.json()["user_id"]


    def test_user_auth(self):
        responce2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers = {"x-csrf-token":self.token},
            cookies = {"auth_sid":self.auth_sid}
        )
        assert "user_id" in responce2.json(), "there is no user_id in the second responce"
        user_id_from_check_method = responce2.json()["user_id"]
        assert self.user_id_from_auth_metod == user_id_from_check_method, "User_id from auth != user+id from check"

    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative(self, condition):
        if condition == "no_cookie":
            responce2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                headers = {"x-csrf-token": self.token}
            )
        else:
            responce2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                cookies = {"auth_sid":self.auth_sid}
            )
        assert "user_id" in responce2.json(), "there is no user_id in the second responce"
        user_id_from_check_method = responce2.json()["user_id"]
        assert user_id_from_check_method == 0, f"User auth with condition{condition}"


