# exchangerate-api.com 
import requests
from pprint import pprint as print

API_KEY = '50505c914c9e839696e4ce78'
currency = 'USD'

# Correct URL formatting using f-string
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"

# Making our request
response = requests.get(url)
# print(response.status_code)

# Check if the response is successful before parsing
if response.status_code == 200:
    jsondata = response.json()
    # print(data)
    print(f"Bugungi kurs: 1 AQSH dollari = {jsondata['conversion_rate']} so'm")
else:
    print(f"Error: Received status code {response.status_code}")

# print(response.json()['conversion_rate'])