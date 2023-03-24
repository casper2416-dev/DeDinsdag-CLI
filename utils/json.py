import json

def create_config():
    default_config = {
        "gebruikersnaam":"",
        "wachtwoord":"",
    }
    with open("config.json", "w") as file:
        json.dump(default_config, file, indent=4)
        print("Created blank config file.")

def read_config():
    with open("config.json", "r") as file:
        return json.load(file)
