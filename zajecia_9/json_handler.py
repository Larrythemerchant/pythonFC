import json

with open("data.json", "r") as file:
    data = json.load(file.read())
    print(data)
    print(type(data))

with open("data.json", "w") as file:
    data = {}
    file.write(json.dumps(data))
