# -*- coding: utf-8 -*-
"""
Created on Fri May 12 15:25:25 2023

@author: tbata
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
import time

IFTTT_WEBHOOKS_KEY = "b8w6x6MOvszzdQi9XWWuHH"

def send_ifttt_notification():
    report = {}
    requests.post(f"https://maker.ifttt.com/trigger/notify/with/key/{IFTTT_WEBHOOKS_KEY}", data=report)

def check_availability():
    # setup the webdriver
    options = Options()
    options.add_argument("--headless")  # Enable headless mode
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver', options=options)
    driver.get('https://www.xior-booking.com/#')

    # Wait until the cards are loaded on the page
    WebDriverWait(driver, 10).until_not(EC.text_to_be_present_in_element((By.CLASS_NAME, 'card-title'), '~|city|~'))

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    cards = soup.find_all('div', {'class': 'card card-style'})

    found = False
    for card in cards:
        title = card.find('h5', {'class': 'card-title'})
        subtitle = card.find('h6', {'class': 'card-subtitle'})
        if title and subtitle and 'Den Haag' in title.text and 'Lutherse Burgwal' in subtitle.text:
            print("Card found!")
            send_ifttt_notification()
            found = True
            break
    if not found:
        print("Card not found. Retrying in 3 minutes...")
    
    driver.quit()
    return found

while True:
    found = check_availability()
    if found:
        break
    else:
        time.sleep(3 * 60)  # sleep for 3 minutes before retrying



