from selenium.webdriver.common.by import By


class S_T_S_T:

    def __init__(self, driver):
        driver.get('https://academy.testifyltd.com/courses/switch-to-software-testing')
        self.title = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div/div[1]/h1')
        # self.completionImage = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[4]/div/div/div[2]/div[1]/span/img')
        # self.enrol_button = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div/div[1]/div/button')
