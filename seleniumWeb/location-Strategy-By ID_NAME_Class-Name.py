from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def locate_by_id(driver):
    email_element = driver.find_element(By.ID, 'email')
    print("Email Element", email_element)
    password_element = driver.find_element(By.ID, 'passContainer')
    print("Password Element:", password_element)


def locate_by_name(driver):
    firstname_element = driver.find_element(By.NAME, 'firstname')
    print("Firstname Element:", firstname_element)
    lastname_element = driver.find_element(By.NAME, 'lastname')
    print("Lastname Element:", lastname_element)


def locate_by_class_name(driver):
    firstChd_element = driver.find_element(By.CLASS_NAME, 'chakra-heading')
    print("FirstChd Element", firstChd_element)
    firstChd_element = driver.find_elements(By.CLASS_NAME, 'chakra-heading')
    for firstChd_element in firstChd_element:
        print("FirstChd Element", firstChd_element.text)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.metricks.io")
    # locate_by_id(driver)
    # locate_by_name(driver)
    locate_by_class_name(driver)


if __name__ == '__main__':
    main()
