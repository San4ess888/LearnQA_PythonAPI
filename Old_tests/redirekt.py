import requests
response = requests.get("https://playground.learnqa.ru/api/long_redirect")
print(response.history)
l = len(response.history)
redirekts = l-1
print((redirekts))
last_url = response.history[l-1]
print(last_url.url)


