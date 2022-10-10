import requests
import json

url = ""

file = open("C:\\Users\\dtyjdtyjdyt\\Desktop\\Api_testing_file.json","r")
json_input = file.read()
requests_json = json.loads(json_input)
  
response = requests.post(url, requests_json)
print(response.content)
print(response)




