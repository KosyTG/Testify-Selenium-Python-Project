from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.metricks.io")
    # header_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/h1')
    # print("Header Element", header_element, header_element.text)
    links = driver.find_elements(By.TAG_NAME, 'a')
    for links in links:
        print("links:", links.text)


if __name__ == '__main__':
    main()
