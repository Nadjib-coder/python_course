import json
from urllib.request import urlopen

with urlopen("https://query.yahooapis.com") as file:
    str_content = file.read()

data = json.loads(str_content)

print(json.dumps(data, indent=2))

print(len(data['list']['resources']))

usd_rates = dict()

for item in data['list']['resources']:
    name = item['resource']['field']['name']
    price = item['resource']['field']['price']
    # print(name, price)
    usd_rates[name] = price

print(50 * float(usd_rates['USD/EUR']))