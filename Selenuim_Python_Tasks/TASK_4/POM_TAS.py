from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains



class T_A_S:

    def __init__(self, driver):
        driver.get('https://academy.testifyltd.com/courses/test-automation-simplified')
        actionChain = ActionChains(driver)

        # self.first_enrolNow = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div/div[1]/div')
        # self.course = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/header/div/div/div[2]/button')
        # self.success_story = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/header/div/div/div[2]/a')
        self.title = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div/div[1]/h1')
        academyLink = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section['
                                                                       '1]/header/div/div/div[2]/a[1]')


