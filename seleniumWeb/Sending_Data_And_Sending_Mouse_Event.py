from selenium.webdriver import Keys
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def send_key_to_element(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    send_key_to_element(driver.find_element(By.NAME, 'firstname'), "Emmanuel")
    send_key_to_element(driver.find_element(By.NAME, "lastname"), 'Kosisochukwu')
    send_key_to_element(driver.find_element(By.NAME, "email"), Keys.COMMAND, 'v')
    send_key_to_element(driver.find_element(By.NAME, 'phone'), '081338974633')
    partnership_thickbOX = driver.find_element(By.ID, 'Partnership').click()
    send_key_to_element(driver.find_element(By.NAME, 'message'), 'Automation is fun if you know how to do it well ')
    submit_button = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div[1]/div[2]/form/div[5]/button').click()
    time.sleep(25)


if __name__ == '__main__':
    main()
