from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def locate_by_Sub_Element(driver):
    email_input = driver.find_elements(By.TAG_NAME, "email")
    print("found:", len(email_input), 'email')

    # form
    forms = driver.find_elements(By.TAG_NAME, "form")
    print("found:", len(forms), 'forms')
    first_email = forms[0]
    contact_email_forms = first_email.find_elements(By.TAG_NAME, "email")
    print("found:", len(contact_email_forms), 'email')


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    locate_by_Sub_Element(driver)


if __name__ == '__main__':
    main()
