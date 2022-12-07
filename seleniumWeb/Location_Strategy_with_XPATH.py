from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def locate_by_xpath(driver):
    submit = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[3]/div[1]/div/div/div/div/a/button')
    print("Total Submit_Element:", len(submit))
    for submit in submit:
        print("Submit_Element:", submit)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.metricks.io")
    locate_by_xpath(driver)


if __name__ == '__main__':
    main()
