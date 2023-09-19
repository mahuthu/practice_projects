import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
print(response.json())
print(response.status_code)

todo = {"userId": 1, "title": "Wash car", "completed": True}
response = requests.put(api_url, json=todo)
print(response.json())
print(response.headers)
print(response.status_code)

todo2 = {"title": "Mow lawn"}
response = requests.patch(api_url, json=todo2)
print(response.json())

response = requests.delete(api_url)
print(response.json())

