# This code came from https://tripadvisor-content-api.readme.io/reference/getlocationreviews with a few modifications

import requests
import api_keys.hntd_api_key

url = f"https://api.content.tripadvisor.com/api/v1/location/56003/reviews?language=en&key={api_keys.hntd_api_key}&limit=100"
print(url)

# headers = {"accept": "application/json"}

# response = requests.get(url, headers=headers)

# with open("prototype_code/api_caller/data.txt", "w") as f:
#     f.write(response.text)
