from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from utils.json import *

def login() -> webdriver.Chrome:
    try:
        config = read_config()
    except FileNotFoundError:
        create_config()
        exit()
    
    
    options = Options()
    options.add_argument("--headless=new")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(options=options, service=Service("chrome/chromedriver_win32.exe"))

    driver.get("https://dedinsdag.nl")

    username = driver.find_element(By.NAME, "code")
    password = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    username.send_keys(config.get("gebruikersnaam"))
    password.send_keys(config.get("wachtwoord"))
    login_button.click()

    return driver
