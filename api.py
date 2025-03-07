import requests
import apikeys

"""
url: A string containing the url with data points we want to pull.
headers: 
"""

# url = f"https://api.content.tripadvisor.com/api/v1/location/60745/reviews?category=restaurant&key={apikeys.key_name}&language=en&limit=2"

url = f"https://api.content.tripadvisor.com/api/v1/location/60745/reviews?category=restaurant&language=en&limit=2&rating=1&key={apikeys.key_name}"


headers = {"accept": "application/json"}

response = requests.api.get(url, headers=headers, timeout=2)

print(response.text)
