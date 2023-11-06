# import requests

# # Замените этот URL на URL вашего API
# api_url = "https://lalafo.kg/"

# # Список категорий
# categories = ["Продажа авто", "Аренда квартир", "Продажа квартир"]

# # Словарь для хранения данных
# data = []

# for category in categories:
#     for i in range(1, 21):  # Получаем 20 объявлений из каждой категории
#         params = {
#             "category": category,
#             "page": i
#         }

#         response = requests.get(api_url, params=params)

#         if response.status_code == 200:
#             ad_data = response.json()
#             for ad in ad_data:
#                 ad_info = {
#                     "заголовок": ad["title"],
#                     "описание": ad["description"],
#                     "цена": ad["price"],
#                     "город": ad["city"],
#                     "категория": ad["category"],
#                     "фотки": ad["photos"],
#                     "телефон": ad["phone"],
#                     "автор": ad["author"]
#                 }
#                 data.append(ad_info)

# # Теперь в data у вас есть список словарей с данными по объявлениям

# response = requests.get(api_url, params=params)

# if response.status_code == 200:
#     print(response.text)  # Вывести текст ответа
#     ad_data = response.json()
#     # Остальной код для обработки данных
# else:
#     print("Ошибка запроса:", response.status_code)


import requests


api_url = "https://www.google.com/search?q=lalafo.kg&oq=&sourceid=chrome&ie=UTF-8"  # Замените на фактический URL API
categories = ["Продажа авто", "Аренда квартир", "Продажа квартир"]

data = []


import requests
import json

api_url = "https://www.google.com/search?q=lalafo.kg&oq=&sourceid=chrome&ie=UTF-8"
categories = ["Продажа авто", "Аренда квартир", "Продажа квартир"]
data = []

for category in categories:
    for i in range(1, 21):
        params = {
            "category": category,
            "page": i
        }

        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            try:
                ad_data = json.loads(response.text)  # Используем json.loads вместо response.json()
                for ad in ad_data:
                    ad_info = {
                        "заголовок": ad.get("title", ""),
                        "описание": ad.get("description", ""),
                        "цена": ad.get("price", ""),
                        "город": ad.get("city", ""),
                        "категория": ad.get("category", ""),
                        "фотки": ad.get("photos", []),
                        "телефон": ad.get("phone", ""),
                        "автор": ad.get("author", "")
                    }
                    data.append(ad_info)
            except json.JSONDecodeError as e:
                print(f"Ошибка при парсинге JSON: {e}")
        else:
            print("Ошибка запроса:", response.status_code, "URL:", response.url)










# for category in categories:
#     for i in range(1, 21):  # Получаем 20 объявлений из каждой категории
#         params = {
#             "category": category,
#             "page": i
#         }

#         response = requests.get(api_url, params=params)

#         if response.status_code == 200:
#             try:
#                 ad_data = response.json()
#                 for ad in ad_data:
#                     ad_info = {
#                         "заголовок": ad.get("title", ""),
#                         "описание": ad.get("description", ""),
#                         "цена": ad.get("price", ""),
#                         "город": ad.get("city", ""),
#                         "категория": ad.get("category", ""),
#                         "фотки": ad.get("photos", []),
#                         "телефон": ad.get("phone", ""),
#                         "автор": ad.get("author", "")
#                     }
#                     data.append(ad_info)
#             except ValueError:
#                 print("Ошибка в JSON-формате ответа. URL:", response.url)
#         else:
#             print("Ошибка запроса:", response.status_code, "URL:", response.url)

# # Теперь в 'data' у вас есть список словарей с данными по объявлениям.
