import requests
import json
import time

response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
obj = json.loads(response2.text)
print(obj)
token = obj['token']
response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
status = json.loads(response3.text)
if status['status'] == "Job is NOT ready":
    print(response3.text)
time.sleep(obj['seconds'])
response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
status = json.loads(response1.text)
if status['status'] == "Job is ready" and status['result'] != "":
    print(response1.text)
