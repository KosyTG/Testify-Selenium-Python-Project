import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Login import loginPage
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def send_element_key(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com/")
    login_page = loginPage(driver)
    send_element_key(driver.find_element(login_page.emailInput).send_keys("emmanuelkosi19@gmail.com"))
    send_element_key(driver.find_element(login_page.passwordInput).send_keys("Kosi9126"))
    time.sleep(10)
    send_element_key(driver.find_element(login_page.passwordInput).click())


if __name__ == '__main__':
    main()
