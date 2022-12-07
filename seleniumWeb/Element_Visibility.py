import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def scroll_to_element(action, element):
    action.move_to_element(element).perform()


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    action = ActionChains(driver)
    form = driver.find_element(By.TAG_NAME, 'form')
    print("Form State:", form.is_displayed(), form.is_enabled())
    driver.maximize_window()
    scroll_to_element(action, driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div[1]/div[2]/form/div[5]/button'))
    submit_button = form.find_element(By.TAG_NAME, 'button')
    print("Submit Button:", submit_button.is_displayed(), submit_button.is_enabled())
    time.sleep(10)


if __name__ == '__main__':
    main()
