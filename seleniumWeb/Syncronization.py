import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def to_be_visible(driver):
    web_driver_wait = WebDriverWait(driver, 25)
    web_driver_wait.until(EC.visibility_of_any_elements_located(
        (By.XPATH, '//*[@id="__next"]/section/div/div[1]/div[2]/div/div[4]/ul/li[2]/a')))
    partner = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[1]/div[2]/div/div[4]/ul/li[2]/a')
    partner.click()
    time.sleep(5)


def to_be_clickable(driver):
    web_driver_wait = WebDriverWait(driver, 25)
    web_driver_wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Hire')))
    hire_link = driver.find_element(By.LINK_TEXT, 'Hire')
    hire_link.click()
    time.sleep(10)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.testifyltd.com/contact")
    # to_be_clickable(driver)
    to_be_visible(driver)


if __name__ == '__main__':
    main()
