import requests

r = requests.get("https://api.warframe.market/v1/items")

print(r.json())