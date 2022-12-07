from selenium.webdriver.common.by import By


class ContactPage:

    def __init__(self, driver):
        driver.get("https://www.testifyltd.com/contact")
        self.firstName_input = driver.find_element(By.NAME, 'firstname')
        self.lastName_input = driver.find_element(By.NAME, 'lastname')
        self.email_input = driver.find_element(By.NAME, 'email')
        self.message_textbox = driver.find_element(By.NAME, 'message')
        self.submit_button = driver.find_element(By.TAG_NAME, 'form').find_element(By.TAG_NAME, 'button')




