import requests
import pytest
class TestCookie:
    def test_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        cookie1 = dict(response.cookies)
        print(dict(response.cookies))
        assert cookie1 == {'HomeWork': 'hw_value'}, "Wrong cookies"



