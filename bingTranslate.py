##IMPORT REQUIRED LIBRARIES
import json
import uuid
import requests

#Add your subscription key and endpoint
with open("secretKey.json", "r") as file:
  subscription_key = json.load(file)["key"]
endpoint = "https://api.cognitive.microsofttranslator.com"

#Add your location, also known as region. The default is global. This is required if using a Cognitive Services resource.
location = "westus2"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version':'3.0',
    'from':'en',
    'to':['de', 'it']
}
constructed_url = endpoint + path

headers = {
    'Ocp-Apim-Subscription-Key':subscription_key,
    'Ocp-Apim-Subscription-Region':location,
    'Content-type':'application/json',
    'X-ClientTraceId':str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
    'text': 'Hello World!'
}]

request = requests.post(constructed_url,params=params,headers=headers,json=body)
response = request.json()

print(json.dumps(response,sort_keys=True,ensure_ascii=False,indent=4,separators=(',', ': ')))