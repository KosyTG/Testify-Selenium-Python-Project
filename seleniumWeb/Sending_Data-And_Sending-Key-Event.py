import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def send_key_to_element(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    send_key_to_element(driver.find_element(By.NAME, 'firstname'), "Emmanuel")
    send_key_to_element(driver.find_element(By.NAME, "lastname"), 'Kosisochukwu')
    time.sleep(20)
    send_key_to_element(driver.find_element(By.NAME, "email"), Keys.COMMAND, 'v')
    send_key_to_element(driver.find_element(By.NAME, 'phone'), '081338974633')
    time.sleep(10)


if __name__ == '__main__':
    main()
