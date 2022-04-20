from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException  
from logos import logos
import random
from search_db import *
import csv
from datetime import datetime
from fake_useragent import UserAgent
import os
import time,requests


### Intro ###
start_message = random.choice(logos)
time_to_sleep = random.randint(5,10)
print(start_message)
now = datetime.now()

### User choise ###
print("""
Please choose a type of search:
(1) SQL related search type
(2) Password related search
(3) Public buckets search
(4) robots.txt search
(5) Admin Portals search
(t) Test Search
""")
user_search_choise = ""
while user_search_choise not in (
    "1",
    "2",
    "3",
    "4",
    "5",
    "t",
    ):
    user_search_choise = input("borekas ~# ")

if user_search_choise == "1":
    searches = sql_searches
elif user_search_choise == "2":
    searches = passwd_searches
    domain = input("Please type a domain or keyword: ")
elif user_search_choise == "3":
    searches = bucket_searches
    domain = input("Please type a domain: ")
elif user_search_choise == "4":
    searches = robots_searches
elif user_search_choise == "5":
    searches = admin_searches
elif user_search_choise == "t":
    searches = test_search

csv_choise = ""
while csv_choise not in ("y", "n"):
    csv_choise = input("Export results to CSV? (y/n): ")
if csv_choise == "y":
    csv_choise = True
else:
    csv_choise = False


### Paths ###
driver_path_mac = Service(r'/Users/hailisambrano/Coding/burekas-tirdof/chromedriver_mac')
driver_path_win = Service(r'C:\Users\haili.sambrano\Desktop\burekas tirdof\chromedriver_win.exe')
root_folder_mac = r'/Users/hailisambrano/Coding/burekas-tirdof/'
root_folder_win = r'C:\Users\haili.sambrano\Desktop\burekas tirdof'
driver_path = ""
root_folder = ""
os_choise = ""
print("""
Please Choose OS:
(1) Mac
(2) Windows
""")
while os_choise not in ("1", "2", "3"):
    os_choise = input("borekas ~# ")
if os_choise == "1":
    driver_path = driver_path_mac
    root_folder = root_folder_mac
elif os_choise == "2":
    driver_path = driver_path_win
    root_folder = root_folder_win

### Headless things ###
headless = ""
while headless not in ("y", "n"):
    webdriver.Chrome.close
    headless = input("Headless? (y/n): ")
    chrome_options = Options()
    if headless != "n":
        chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=chrome_options, service=driver_path)

### Viewport ###
width = 1100
height = 1000
driver.set_window_size(width, height)
print("Wiewport: " + "[W:"+ str(width) + " H:" + str(height) + "]")

### Remove automation tags and shuting down stuff ###
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument("--mute-audio")


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
    inurl_coil,
    site_govil,
    inurl_govil,
    site_il,
    inurl_il,
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
        try:
            driver.get(search_url)
            try:
                ### Captcha bypass ###
                driver.find_element(by=By.XPATH, value='//*[@id="captcha-form"]')
                print("Bypassing Google CAPTCHA...")
                delayTime = 2
                audioToTextDelay = 10
                filename = '1.mp3'
                audio2text_site = 'https://speech-to-text-demo.ng.bluemix.net/'
                def audioToText(mp3Path):
                    print("Bypassing Google CAPTCHA...")
                    driver.execute_script('''window.open("","_blank");''')
                    driver.switch_to.window(driver.window_handles[1])
                    driver.get(audio2text_site)
                    delayTime = 10
                    time.sleep(1)
                    # Upload file
                    time.sleep(1)
                    root = driver.find_element(by=By.ID, value='root').find_element(by=By.XPATH, value='//*[@id="root"]/div')
                    btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/input')
                    btn.send_keys('{}/1.mp3'.format(root_folder))
                    # Audio to text is processing
                    time.sleep(delayTime)
                    #btn.send_keys(path)
                    # Audio to text is processing
                    time.sleep(audioToTextDelay)
                    text = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[7]/div/div/div').find_elements(by=By.TAG_NAME, value='span')
                    result = " ".join( [ each.text for each in text ] )
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    return result
                def saveFile(content,filename):
                    with open(filename, "wb") as handle:
                        for data in content.iter_content():
                            handle.write(data)
                driver.get(search_url)
                time.sleep(1)
                googleClass = driver.find_elements(by=By.CLASS_NAME, value='g-recaptcha')[0]
                time.sleep(2)
                outeriframe = googleClass.find_element(by=By.TAG_NAME, value='iframe')
                time.sleep(1)
                outeriframe.click()
                time.sleep(2)
                allIframesLen = driver.find_elements(by=By.TAG_NAME, value='iframe')
                time.sleep(1)
                audioBtnFound = False
                audioBtnIndex = -1
                for index in range(len(allIframesLen)):
                    driver.switch_to.default_content()
                    iframe = driver.find_elements(by=By.TAG_NAME, value='iframe')[index]
                    driver.switch_to.frame(iframe)
                    driver.implicitly_wait(delayTime)
                    try:
                        audioBtn = driver.find_element(by=By.ID, value='recaptcha-audio-button') or driver.find_element(by=By.ID, value='recaptcha-anchor')
                        audioBtn.click()
                        audioBtnFound = True
                        audioBtnIndex = index
                        break
                    except Exception as e:
                        pass
                if audioBtnFound:
                    try:
                        while True:
                            href = driver.find_element(by=By.ID, value='audio-source').get_attribute('src')
                            response = requests.get(href, stream=True)
                            saveFile(response,filename)
                            response = audioToText(os.getcwd() + '/' + filename)
                            # print(response)
                            driver.switch_to.default_content()
                            iframe = driver.find_elements(by=By.TAG_NAME, value='iframe')[audioBtnIndex]
                            driver.switch_to.frame(iframe)
                            inputbtn = driver.find_element(by=By.ID, value='audio-response')
                            inputbtn.send_keys(response)
                            inputbtn.send_keys(Keys.ENTER)
                            time.sleep(2)
                            errorMsg = driver.find_elements(by=By.CLASS_NAME, value='rc-audiochallenge-error-message')[0]
                            if errorMsg.text == "" or errorMsg.value_of_css_property('display') == 'none':
                                print("CAPTCHA bypass Failed.")
                                break
                    except Exception as e:
                            print(e)
                            print('CAPTCHA bypass Successed.')
                else:
                    print("Check for CAPTCHA error!")
                    break
            except NoSuchElementException:
                print("=== Search ===")
                print("Search URL: " + search_url)
                search_value = (i + url).replace('%3A', ':').replace('+', ' ')
                print("Search: " + search_value)
                result_number = 0

                ### Fake user-agents ###
                ua = UserAgent(verify_ssl=False)
                userAgent = ua.random
                chrome_options.add_argument(f'user-agent={userAgent}')
                print("User-Agent: " + userAgent)
                try:
                    driver.find_element(by=By.XPATH, value='//*[@id="topstuff"]/div')
                    print("No Results...")
                except:
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
                            print("=== Result {} ===".format(result_number))
                            print("Title: " + title)
                            print("Site URL: " + siteurl)
                            print("Description: " + description)
                driver.implicitly_wait(time_to_sleep)
        except NoSuchWindowException:
            break


### Closing stuff ###
driver.close
if csv_choise == True:
    csvfile.close()