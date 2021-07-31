import requests
parameters = ["POST", "PUT", "GET","DELETE"]
response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":"GET"})
print(response1.text)
response2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"HEAD"})
print(response2.text)
for i in range(len(parameters)):
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":parameters[i]})
    print(response.text)
for i in range(len(parameters)):
    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":parameters[i]})
    print(response.text)
for i in range(len(parameters)):
    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":parameters[i]})
    print(response.text)
for i in range(len(parameters)):
    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":parameters[i]})
    print(response.text)