import requests

url = ""

response = requests.delete(url)

print(response.status_code)

