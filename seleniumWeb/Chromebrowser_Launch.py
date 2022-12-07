from selenium import webdriver


def main():
    driver = webdriver.Chrome(executable_path="/Users/mac/chromedriver")
    driver.get("https://www.metricks.io")
    driver.quit()


main()
