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


discord_login = ""
discord_password = ""
keyboard = Controller()
option = webdriver.ChromeOptions()


# Removes navigator.webdriver flag

# For older ChromeDriver under version 79.0.3945.16
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)
option.add_argument("window-size=1280,800")
option.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")


# For ChromeDriver version 79.0.3945.16 or over
option.add_argument('--disable-blink-features=AutomationControlled')


# Open Browser
browser = webdriver.Chrome(ChromeDriverManager().install(), options=option)
# Initiate the browser

name = ""

browser.get('https://discord.com/channels/@me/782560016506814484')
# Login
browser.find_element_by_name('email').send_keys(discord_login)
time.sleep(5)
browser.find_element_by_name('password').send_keys(discord_password)
time.sleep(5)
# Spam
time.sleep(5)
browser.get('https://discord.com/channels/@me/782560016506814484')
time.sleep(5)
i = 0
while True:
    keyboard.type(name)
    keyboard.press(Key.enter)
    time.sleep(0.5)
    if i == 5:
        i = 0
        keyboard.type(get_random_string(random.randrange(1, 50)))
        keyboard.press(Key.enter)
        time.sleep(random.randrange(5, 30))
    i += 1
