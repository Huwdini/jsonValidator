## module utilised to submit http request for testing
import requests
import json
from b_clean import cleanJson

BASE = "http://127.0.0.1:5000/"

def testGet():
  schemaId = "config.json"
  response = requests.get(BASE + (f"schema/{schemaId}"))
  print(response.json())

def testUpload():
  f = open('storage/config.json')
  uploadData = json.load(f)
  #uploadData = cleanJson(uploadData)
  response = requests.put(BASE + "schema/config-schemaTest", uploadData)
  print(response.json())
  print(response.status_code)

if __name__ == '__main__':
  #testGet()
  testUpload()
