import time
from ContactPage import ContactPage
from AboutUsPage import AboutUsPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    about_page = AboutUsPage(driver)
    print(about_page.title.text)
    contact_page = ContactPage(driver)
    print(contact_page.firstName_input, contact_page.lastName_input)
    contact_page.submit_button.click()
    time.sleep(10)


if __name__ == '__main__':
    main()
