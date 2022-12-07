import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def send_element(element, *keys):
    element.send_keys(keys)


def Main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.google.com/ ")
    send_element(driver.find_element(By.TAG_NAME, 'input'), "Python")
    driver.find_element(By.TAG_NAME, 'input').send_keys(Keys.ENTER)
    wikipedia_text = driver.find_element(By.CLASS_NAME, "kno-rdesc")
    print("WIKIPEDIA TEXT:", wikipedia_text.text)
    time.sleep(10)
    driver.quit()


if __name__ == '__main__':
    Main()
