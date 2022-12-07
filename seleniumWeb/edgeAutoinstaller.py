from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def main():
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    driver.get("http://www.jumia.com")
    driver.quit()


if __name__ == '__main__':
    main()
