import re

def parse_hour_data(hour_data: str) -> tuple[str, str, str, str, str]:
    hour_data = hour_data.replace("Lesuur: ", "")

    # Removes start and end time, will be added later in the dictionary.
    hour_time, = re.findall("\(.*\) ", hour_data)
    hour_data = hour_data.replace(hour_time, "")

    hour_id, subject, code, location = hour_data.split(" - ")

    return [hour_id, hour_time, subject, code, location]
