import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def scroll_by_offset(action, delta_y):
    action.scroll_by_amount(0, delta_y).perform()


def Main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://youtu.be/Mk7-GRWq7wA")
    action = ActionChains(driver)
    scroll_by_offset(action, 500)
    webdriver_wait = WebDriverWait(driver, 60)
    webdriver_wait.until(EC.visibility_of_any_elements_located((By.XPATH, '//*[@id="content-text"]/span')))
    firstComment = driver.find_element(By.XPATH, '//*[@id="content-text"]/span')
    print("First Comment:", firstComment.text)
    secondComment = driver.find_element(By.XPATH, '//*[@id="content-text"]/span[1]')
    print("Second Comment:", secondComment.text)


if __name__ == '__main__':
    Main()
