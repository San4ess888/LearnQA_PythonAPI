import requests
response = requests.get("https://playground.learnqa.ru/api/homework_header")
#print(response.headers)
head = dict(response.headers)
print(head)
