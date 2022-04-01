from doctest import UnexpectedException
from turtle import width
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import selenium.common.exceptions
from logos import logos
import random
from search_db import *
import csv
from datetime import datetime
from fake_useragent import UserAgent

### Intro ###
start_message = random.choice(logos)
print(start_message)


### User choise ###
print("""
Please choose a type of search:
(1) SQL related search type
(2) Password related search
(3) Public buckets search
""")
user_search_choise = ""
while user_search_choise not in ("1", "2", "3"):
    user_search_choise = input("borekas ~# ")

if user_search_choise == "1":
    searches = sql_searches
elif user_search_choise == "2":
    searches = passwd_searches
    domain = input("Please type a domain or keyword: ")
elif user_search_choise == "3":
    searches = bucket_searches
    domain = input("Please type a domain: ")

csv_choise = ""
while csv_choise not in ("y", "n"):
    csv_choise = input("Export results to CSV? (y/n): ")
if csv_choise == "y":
    csv_choise = True
else:
    csv_choise = False


### Driver path ###
driver_path_mac = Service(r'/Users/hailisambrano/Coding/burekas tirdof/chromedriver_mac')
driver_path_win = Service(r"C:\Users\haili.sambrano\Desktop\burekas tirdof\chromedriver_win.exe")
driver_path = ""
os_choise = ""
print("""
Please Choose OS:
(1) Mac
(2) Windows
""")
while os_choise not in ("1", "2"):
    os_choise = input("borekas ~# ")
if os_choise == "1":
    driver_path = driver_path_mac
else:
    driver_path = driver_path_win

### Headless things ###
headless = ""
while headless not in ("y", "n"):
    webdriver.Chrome.close
    headless = input("Headless? (y/n): ")
    if headless != "n":
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options, service=driver_path)
    else:
        driver = webdriver.Chrome(service=driver_path)


### Viewport ###
def set_viewport_size(driver, width, height):
    window_size = driver.execute_script("""
        return [window.outerWidth - window.innerWidth + arguments[0],
          window.outerHeight - window.innerHeight + arguments[1]];
        """, width, height)
    driver.set_window_size(*window_size)
set_viewport_size(driver, 800, 600)   
print("Wiewport: " + str(driver.execute_script("return [window.innerWidth, window.innerHeight];")))

### Search Parameters ###
google = 'https://www.google.com/'
google_search = 'search?q='

site_coil = '+site%3Aco.il'
inurl_coil = '+inurl%3Aco.il'
site_govil = '+site%3Agov.il'
inurl_govil = '+inurl%3Agov.il'
site_il = '+site%3A.il'
inurl_il = '+inurl%3A.il'
urlendings = [
    site_coil,
    # inurl_coil,
    # site_govil,
    # inurl_govil,
    # site_il,
    # inurl_il,
]


### Opening CSV ###
if csv_choise == True:
    now = datetime.now()
    now = now.strftime("%d.%m.%Y %H-%M-%S")
    csvfile = open("Burekas_Export - {}.csv".format(now), "w", newline="", encoding='utf-8-sig')
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['Title', 'Site URL', 'Description', 'Google Search', 'Google Search URL'])


### Preform the search ###
for i in searches:
    for url in urlendings:
        search_url = str(google + google_search + i + url)
        print("=== Search ===")
        try:
            driver.get(search_url)
        except:
            "Check for CAPTCHA error!"
        print("Search URL: " + search_url)
        search_value = (i + url).replace('%3A', ':').replace('+', ' ')
        print("Search: " + search_value)
        result_number = 0

        ### Fake user-agents ###
        ua = UserAgent(verify_ssl=False)
        userAgent = ua.random
        chrome_options.add_argument(f'user-agent={userAgent}')

        for element in driver.find_elements(by=By.XPATH, value='.//*[@class="g tF2Cxc"]'):
            title = ""
            title = element.find_element(by=By.XPATH, value='.//h3').text
            title.encode('UTF-8')
            siteurl = element.find_element(by=By.XPATH, value='.//div[@class="yuRUbf"]/a').get_attribute('href')
            description = ""
            for des_element in element.find_elements(by=By.XPATH, value='.//*[@class="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf"]/span'):
                description = description + " " + des_element.text
                description.encode('UTF-8')
            result_number += 1
            if csv_choise == True:
                writer.writerow([title, siteurl, description, search_value, search_url])
            if title == "":
                print("No Results...")
            else:
                print("=== Result {} ===".format(result_number))
                print("Title: " + title)
                print("Site URL: " + siteurl)
                print("Description: " + description)
                print("User-Agent: " + userAgent)
        driver.implicitly_wait(10)


### Closing stuff ###
if headless not in ("n"):
    webdriver.Chrome.close
if csv_choise == True:
    csvfile.close()
