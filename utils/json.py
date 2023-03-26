import json
import logging

def create_config() -> None:
    default_config = {
        "gebruikersnaam":"",
        "wachtwoord":"",
    }
    with open("config.json", "w") as file:
        try:
            json.dump(default_config, file, indent=4)
            print("Created blank config file.")
        except Exception as exception:
            logging.error("Error creating config file.")
            logging.error(exception)

def read_config() -> dict:
    with open("config.json", "r") as file:
        return json.load(file)
