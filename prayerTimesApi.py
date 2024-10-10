import requests
# from jsonExtract import jsonExtract

# from pprint import pprint as print

# city='tashkent'
date = 10-10-2024
year = 2024
month = 10
# url = f"http://api.aladhan.com/v1/timings/{date}"
url = f"http://api.aladhan.com/v1/calendar/{year}/{month}"

# r = requests.get(url)
# print(r.status_code)

city='tashkent'

# url = f"https://api.pray.zone/v2/times/today.json?city={city}&school=5"
r = requests.get(url)
print(r.status_code)

# res = r.json()
# print(res['results']['datetime'][0]['times'])
