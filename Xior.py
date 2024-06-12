# -*- coding: utf-8 -*-
"""
Created on Mon May  8 18:07:49 2023

@author: tbata
"""

def simulate_human_delay():
    time.sleep(random.uniform(1.0, 3.0))  # Random sleep between 1 and 3 seconds


import time
import requests
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


IFTTT_WEBHOOKS_KEY = "" #insert key from IFTTT app

def send_ifttt_notification(event, value1=None, value2=None, value3=None):
    url = f"https://maker.ifttt.com/trigger/{event}/with/key/{IFTTT_WEBHOOKS_KEY}"
    payload = {"value1": value1, "value2": value2, "value3": value3}
    requests.post(url, json=payload)
    
    
def get_random_user_agent():
    user_agents = [
        # Add more user-agent strings here
        "Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36",
        "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    ]
    return random.choice(user_agents)

def simulate_human_delay():
    time.sleep(random.uniform(1.0, 2.0))  # Random sleep between 1 and 2 seconds
    
while True:
    chrome_options = Options()
    chrome_options.add_argument(f"user-agent={get_random_user_agent()}")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    #chrome_options.add_argument("--user-data-dir=/path/to/your/chrome/profile")  # Update this path with your Chrome profile's path
    driver = webdriver.Chrome("path/to/chromedriver", options=chrome_options)
    
    driver.get("https://www.xior-booking.com/#")
    time.sleep(2)  # Allow the page to load

    # # Wait for the 'city' dropdown to be clickable and click it
    # wait = WebDriverWait(driver, 10)
    # city_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "city")))
    # city_dropdown.click()

    # # Select the 'Den Haag' option
    # city_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='city']/option[5]")))
    # city_option.click()
    # time.sleep(2)  # Allow the page to load

    # # Wait for the 'location' dropdown to be clickable and click it
    # location_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "location")))
    # location_dropdown.click()

    # # Select the 'Lutherse Burgwal' option - this is for the exact location
    # location_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='location']/option[5]")))
    # location_option.click()
    # time.sleep(2)  # Allow the page to load

    # book_now_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'Book now!')]")

    if book_now_elements:
        print("Visual found. Sending IFTTT notification...")
        send_ifttt_notification("visual_found", "Visual Found", "The visual is present on the Lutherse Burgwal page.")
        driver.quit()  # Close the browser window and end the session
        break  # Stop the loop if the visual is found
    else:
        print("Visual not found. Retrying in 3 minutes...")
        driver.quit()  # Close the browser window and end the session

    time.sleep(180)  # Wait for 3 minutes (180 seconds) before checking again










#The script now searches for elements containing the text "Book now!" using the //*[contains(text(), 'Book now!')] XPath. If such elements are found, it will send you an email notification. Make sure to replace the email address and password in the send_email function with the appropriate credentials for the Gmail account you'll be using.
#select_complex_dropdown = Select(driver.find_element(By.ID, "location"))
#select_complex_dropdown.select_by_visible_text("Lutherse Burgwal")
#TELEGRAM_TOKEN = "6206400895:AAE3XWH8EUadNgkszVRMlWRh67p7xcKltbg"
#TELEGRAM_USER_ID = 6078864176
#IFTTT_WEBHOOKS_KEY = "b8w6x6MOvszzdQi9XWWuHH"
