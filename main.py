import requests
import json
from pprint import pprint

r = requests.get("https://api.warframe.market/v1/items/rubico_prime_blueprint")

# with open("item_info.txt", "w") as write_file:
#    json.dump(r.json(), write_file)

with open("item_info.txt", "r") as handle:
   parsed = json.load(handle)

pprint(parsed)