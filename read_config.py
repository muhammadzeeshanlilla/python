import json


with open("config.json", "r") as file:
    config = json.load(file)


print(config)


print(config["task_name"])
print(config["task_type"])
print(config["schedule"])