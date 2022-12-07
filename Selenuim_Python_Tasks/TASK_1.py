import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com/")
    explore_courses = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div/div[1]/div/button')
    print("Explore Courses:", explore_courses)
    subscribe_element = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[11]/div/div/div[1]/h2')
    print("Subscribe Element:", subscribe_element.text)
    time.sleep(10)


if __name__ == '__main__':
    main()
