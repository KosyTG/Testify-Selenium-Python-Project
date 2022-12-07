from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def print_element_attributes(element):
    print("ID:", element.get_attribute("id"))
    print("CLASS:", element.get_attribute("class"))
    print("STYLE:", element.get_attribute("STYLE"))
    print("INNER TEXT:", element.get_attribute("innerText"))
    print("INNER HTML:", element.get_attribute("innerHtml"))


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/")
    Discover_More = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div[1]/div[1]/div/a')
    print_element_attributes(Discover_More)


if __name__ == '__main__':
    main()
