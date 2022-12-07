import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def send_element(element, *keys):
    element.send_keys(keys)


def Main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://youtube.com/ ")
    send_element(driver.find_element(By.ID, 'search-icon'),"John legend")
    driver.implicitly_wait(5)


if __name__ == '__main__':
    Main()
