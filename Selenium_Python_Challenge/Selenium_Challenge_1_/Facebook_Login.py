from selenium.webdriver.common.by import By


class facebookLogin:
    def __init__(self, driver):
        driver.get("https://www.facebook.com/")
        self.form = driver.find_element(By.TAG_NAME, "form")
        firstName = self.form.find_element(By.ID, "firstname")
        lastName = self.form.find_element(By.ID, "lastname")
        loginButton = self.form.find_element(By.ID, "u_0_5_nE")
