import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from pynput.keyboard import Key, Controller


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


messenger_login = ""
messenger_password = ""
keyboard = Controller()
option = webdriver.ChromeOptions()

option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)
option.add_argument("window-size=1280,800")
option.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")


# For ChromeDriver version 79.0.3945.16 or over
option.add_argument('--disable-blink-features=AutomationControlled')


# Open Browser
browser = webdriver.Chrome(ChromeDriverManager().install(), options=option)
browser.get('https://www.messenger.com/t/')
browser.find_element_by_xpath(
    '/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[2]').click()
browser.find_element_by_name('email').send_keys(messenger_login)
# time.sleep(5)
browser.find_element_by_name('pass').send_keys(messenger_password)
keyboard.press(Key.enter)
time.sleep(30)
browser.get('https://www.messenger.com/t/')
time.sleep(5)
while True:
    keyboard.type('Repond !!!!')
    keyboard.press(Key.enter)
    time.sleep(0.5)
