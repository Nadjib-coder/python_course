import json
from urllib.request import urlopen

with urlopen("https://query.yahooapis.com") as response:
    source = response.read()

print(source)
