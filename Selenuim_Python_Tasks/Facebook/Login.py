from selenium.webdriver.common.by import By
from selenium import webdriver


class loginPage:

    def __init__(self, driver):
        driver.get("https://www.facebook.com/")
        self.emailInput = driver.find_element(By.ID, 'email')
        self.passwordInput = driver.find_element(By.ID, 'pass')
        self.submit_button = driver.find_element(By.TAG_NAME, 'button')
