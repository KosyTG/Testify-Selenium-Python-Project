from selenium import webdriver


def main():
    driver = webdriver.Firefox(executable_path="/Users/mac/geckodriver")
    driver.get("https://www.metricks.io")
    driver.quit()


main()
