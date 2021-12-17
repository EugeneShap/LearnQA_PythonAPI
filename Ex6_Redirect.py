import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

for x in response.history:
    print(x.url)