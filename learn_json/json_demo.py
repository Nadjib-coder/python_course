import json

with open("states.json", "r") as file:
    data = json.load(file)

for state in data['states']:
    del state['area_codes']

with open("new_states", "w") as file:
    json.dump(data, file, indent=2)
