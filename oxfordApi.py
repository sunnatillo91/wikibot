import requests
import json
from pprint import pprint as print

# import sys
# sys.stdout.reconfigure(encoding='utf-8')

app_id = "9949aa54"
app_key = "526f6635fa6ecc4b9306f52508e0efe2"
language = "en-gb"

word_id = "anaconda"

url = "https://od-api-sandbox.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
# url = f"https://od-api.oxforddictionaries.com:443/api/v2/entries/{language}/{word_id.lower()}"

r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
# print(r.status_code)
res = r.json()
# print(res)

# Will return Definition of the word
print(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])

# Will return audiofile of the word
print(res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile'])