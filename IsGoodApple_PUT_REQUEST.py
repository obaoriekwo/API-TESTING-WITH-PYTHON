import  requests
import json


# API URL
url = ""

#  Read Input Json file
file = open("C:\\Users\\dtyjdtyjdyt\\Desktop\\Api_testing_file.json","r")
json_input = file.read()
request_json = json.loads(json_input)

#  Make PUT request using json input body
response = requests.put(url,request_json)

# Codes to validate response code

assert response.status_code ==200
print(response)

