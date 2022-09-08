import requests
from apikey import API_TOKEN

params = {"q": "Krasnodar", "appid": API_TOKEN, "units": "metric"}
headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Host": "httpbin.org",
    "Referer": "http://httpbin.org/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-6318e7b1-0d2f87d816170ed622a6eeb2"
}

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
print(
    response.status_code)  # результат запроса 200-300 успешное подключение 300-400 перенаправление на другую страницу сайта 400-500 ошибки на стороне клиента 500-600 ошибки на стороне сервера
print(response.headers)  # служебная инфа которую передает сайт браузеру
print(response.content)  # содержимое страницы в виде байтовой строки
print(response.text)  # html-код в виде текста
x = response.json()
print(x["weather"][0]["main"])


pesponse2 = requests.get("http://httpbin.org/headers",headers=headers)
print(pesponse2.text)
data={"custname": "Qwer","custtel": 3244,"custemail": "qwer@gmail.com","size": "medium","topping": "cheese","delivery":"", "comments": "Оставить у двери"}
response3 = requests.post("http://httpbin.org/post",headers=headers,data=data)
print(response3.text)
