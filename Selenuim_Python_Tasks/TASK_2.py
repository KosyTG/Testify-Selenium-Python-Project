from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def print_element(element):
    print("Text:", element.text)
    print("Attributes:", element.get_attribute("class"))
    print("Properties:", element.get_property(element))



def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com/")
    element = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[2]/div[2]')
    print_element(element)


if __name__ == '__main__':
    main()
