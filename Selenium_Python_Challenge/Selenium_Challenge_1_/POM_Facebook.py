import time

from Facebook_Login import facebookLogin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def send_element_data(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.facebook.com/")
    form = driver.find_element(By.TAG_NAME, "form")
    send_element_data(form.find_element(By.ID, "email"), "emmanuelmonday450@gmail.com")
    send_element_data(form.find_element(By.ID, "pass"), "Treakings")
    time.sleep(5)
    loginButton = form.find_element(By.TAG_NAME, "button")
    loginButton.click()
    time.sleep(20)


if __name__ == '__main__':
    main()
