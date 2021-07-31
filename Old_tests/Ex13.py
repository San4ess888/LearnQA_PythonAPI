import requests
response1 = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check")
print(response1.text)
response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",headers={"User-Agent": "Some value here"})
print(response.text)
