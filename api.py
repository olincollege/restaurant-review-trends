import requests
import apikeys

"""
url: A string containing the url with data points we want to pull.
headers: A list of strings containing the data types.
"""

location_id = "56003"
limit = "2"

url = f"https://api.content.tripadvisor.com/api/v1/location/{location_id}/reviews?&language=en&limit={limit}&key={apikeys.key_name}"


headers = {"accept": "application/json"}  # Review categories

# Scrape the data from the url, if time exceeds timeout then quit
response = requests.get(url, headers=headers, timeout=1000)

# Open scraped data in data.txt
with open("data.txt", "w") as f:
    f.write(response.text)
