import requests
#import pytest
class TestHeader:
    def test_header(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        head = dict(response.headers)
        print(head)
        assert "Date" in head, "Wrong header"
        assert "Content-Type" in head, "Wrong header"
        assert "Content-Length" in head, "Wrong header"
        assert "Connection" in head, "Wrong header"
        assert "Keep-Alive" in head, "Wrong header"
        assert "Server" in head, "Wrong header"
        assert "x-secret-homework-header" in head, "Wrong header"
        assert "Cache-Control" in head, "Wrong header"
        assert "Expires" in head, "Wrong header"



