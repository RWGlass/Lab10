import requests

url = "http://api.icndb.com/jokes/random"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
