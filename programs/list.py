from click import command
from selenium.webdriver.common.by import By
from rich.table import Table
from rich.console import Console

from utils.login import login
from utils.format import format

@command(help="Lists registered hours.")
def list():
    hour_table = Table()

    column_names = ["Nr.", "Duration", "Subject", "Magister code", "Room"]
    
    for name in column_names:
        hour_table.add_column(name, header_style="bold dark_orange3", style="deep_sky_blue3")

    driver = login()

    hours = driver.find_elements(By.CLASS_NAME, "fc-title")

    for hour in hours:
        hour = hour.text.split("\n")
        hour_formatted = format(hour[0])

        # Splits string at gets first item to prevent printing extra information.
        hour_table.add_row(hour_formatted[0], hour_formatted[1], hour_formatted[2], hour_formatted[3], hour_formatted[4])

    console = Console()
    console.print(hour_table)
