from click import command
from selenium.webdriver.common.by import By

from utils.login import login

@command(help="Lists registered hours.")
def list():
    driver = login()

    hours = driver.find_elements(By.CLASS_NAME, "fc-title")

    for hour in hours:
        # Splits string at gets first item to prevent printing extra information.
        print(hour.text.split("\n")[0])
