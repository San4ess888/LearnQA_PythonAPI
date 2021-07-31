import requests
from datetime import datetime
response1 = requests.get("https://playground.learnqa.ru/api/user/")
print(response1.status_code)
base_part = "lernqa"
domain = "example.com"
random_part = datetime.now().strftime("%m%d%Y%H%M%S")
email = f"{base_part}{random_part}@{domain}"
data = {'password':'1234',
            'username':'lernqa',
            'firstName':'lernqa',
            'lastName':'lernqa',
            'email': email
        }
response2 = requests.post("https://playground.learnqa.ru/api/user/", data = data)
print(response2.status_code)