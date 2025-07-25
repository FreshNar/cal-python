import requests

url = "https://api.cal.com/v2/event-types"

querystring = {"username":"jake"}

headers = {"cal-api-version": "2024-06-14"}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())