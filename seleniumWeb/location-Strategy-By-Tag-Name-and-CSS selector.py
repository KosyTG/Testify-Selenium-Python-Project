from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def locate_by_tag_name(driver):
    first_div = driver.find_element(By.TAG_NAME, "div")
    print("First_Div Element:", first_div)


def locate_by_CSS_selector(driver):
    pass


def main():
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.metricks.io")
        locate_by_tag_name(driver)


if __name__ == '__main--':
    main()
