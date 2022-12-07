import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.testifyltd.com/contact")
    time.sleep(5)
    driver.refresh()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[1]/div[2]/div/div[4]/ul/li[2]/a').click()
    time.sleep(5)
    driver.back()
    time.sleep(5)
    driver.forward()
    time.sleep(20)


if __name__ == '__main__':
    main()
