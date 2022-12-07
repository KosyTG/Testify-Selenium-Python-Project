from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def print_element_fields(element):
    print("Text:", element.text)
    print("Size:", element.size)
    print("Tag Name", element.tag_name)
    print("Accessbile_Name", element.accessible_name)
    print("Rectangle", element.rect)
    print("Location", element.location)
    print("ID", element.id)
    print("Area_role", element.aria_role)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    element = driver.find_element(By.TAG_NAME, "h2")
    print_element_fields(element)


if __name__ == '__main__':
    main()
