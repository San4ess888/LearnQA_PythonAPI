import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime
class TestUserEdit(BaseCase):
    def test_edit_created_user(self):
