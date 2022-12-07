import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def send_key_to_element(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.facebook.com/")
    send_key_to_element(driver.find_element(By.ID, 'email'), 'emmanuelkosi19@gmail.com')
    send_key_to_element(driver.find_element(By.ID, 'pass'), 'Hitler336')
    web_driver_wait = WebDriverWait(driver, 10)
    web_driver_wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'button')))
    form = driver.find_element(By.TAG_NAME, 'form')
    submit_Button = form.find_element(By.TAG_NAME, 'button')
    submit_Button.click()
    # time.sleep(10)


if __name__ == '__main__':
    main()
