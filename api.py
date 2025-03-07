import requests
import apikeys

url = f"https://api.content.tripadvisor.com/api/v1/location/locationId/reviews?category=restaurant&key={apikeys.key_name}language=en&limit=2"

headers = {"accept": "application/json"}

response = requests.api.get(url, headers=headers, timeout=10)

print(response.text)
