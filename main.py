
import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
print(response.json())
print(response.status_code)
print(response.headers)

api_url1 = "https://jsonplaceholder.typicode.com/todos"
todo = {"userid": 1, "title": "buy milk", "completed": False}
response1 = requests.post(api_url1, todo)
print(response1.json())
print(response1.status_code)
print(response1.headers)
