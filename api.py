import requests
import apikeys

location_id = "56003"  # Location we are getting data from: Houston, TX
limit = 1000  # Limit of number of ratings to scrape

url = f"https://api.content.tripadvisor.com/api/v1/location/{location_id}/reviews?&language=en&limit={limit}&key={apikeys.key_name}"


headers = {"accept": "application/json"}  # Review categories

# Scrape the data from the url, if time exceeds timeout then quit
response = requests.get(url, headers=headers, timeout=1000)

# Open scraped data in data.txt
with open("data.txt", "w") as f:
    f.write(response.text)
