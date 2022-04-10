from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os, sys
import time,requests
from bs4 import BeautifulSoup
from burekas_tirduf import chrome_options, root_folder, driver_path, now

# driver_path_mac = Service(r'/Users/hailisambrano/Coding/burekas-tirdof/chromedriver_mac')
# driver_path_win = Service(r'C:\Users\haili.sambrano\Desktop\burekas tirdof\chromedriver_win.exe')
delayTime = 2
audioToTextDelay = 10
filename = '1.mp3'
byPassUrl = 'https://www.google.com/recaptcha/api2/demo'
googleIBMLink = 'https://speech-to-text-demo.ng.bluemix.net/'
# option = webdriver.ChromeOptions()
chrome_options.options.add_argument('--disable-notifications')
chrome_options.add_argument("--mute-audio")
# option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# option.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")
def audioToText(mp3Path):
    print("1")
    driver.execute_script('''window.open("","_blank");''')
    driver.switch_to.window(driver.window_handles[1])
    print("2")
    driver.get(googleIBMLink)
    delayTime = 10
    # Upload file
    time.sleep(1)
    print("3")
    # Upload file
    time.sleep(1)
    root = driver.find_element(by=By.ID, value='root').find_element(by=By.XPATH, value='//*[@id="root"]/div')
    btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/input')
    btn.send_keys('{}/1.mp3'.format(root_folder))
    # Audio to text is processing
    time.sleep(delayTime)
    #btn.send_keys(path)
    print("4")
    # Audio to text is processing
    time.sleep(audioToTextDelay)
    print("5")
    text = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[7]/div/div/div').find_elements(by=By.TAG_NAME, value='span')
    print("5.1")
    result = " ".join( [ each.text for each in text ] )
    print("6")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("7")
    return result
def saveFile(content,filename):
    with open(filename, "wb") as handle:
        for data in content.iter_content():
            handle.write(data)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options, service=driver_path)
driver.get(byPassUrl)
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
            print(response)
            driver.switch_to.default_content()
            iframe = driver.find_elements(by=By.TAG_NAME, value='iframe')[audioBtnIndex]
            driver.switch_to.frame(iframe)
            inputbtn = driver.find_element(by=By.ID, value='audio-response')
            inputbtn.send_keys(response)
            inputbtn.send_keys(Keys.ENTER)
            time.sleep(2)
            errorMsg = driver.find_elements(by=By.CLASS_NAME, value='rc-audiochallenge-error-message')[0]
            if errorMsg.text == "" or errorMsg.value_of_css_property('display') == 'none':
                print("Success")
                break
    except Exception as e:
            print(e)
            print('Exception Caught.')
else:
    print('Button not found. This should not happen.')