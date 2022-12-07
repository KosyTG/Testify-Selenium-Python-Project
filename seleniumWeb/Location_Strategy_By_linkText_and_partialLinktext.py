from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def locate_by_Link_Test(driver):
    consulting = driver.find_element(By.LINK_TEXT, 'Consulting')
    print("Term Of Service:", consulting)







def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    locate_by_Link_Test(driver)


if __name__ == '__main__':
    main()
