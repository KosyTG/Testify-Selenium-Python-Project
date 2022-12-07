from selenium.webdriver.common.by import By


class homePage:

    def __init__(self, driver):
        driver.maximize_window()
        driver.get("https://www.bbc.com/")
        self.news_1 = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[1]/div/a')
        self.news_2 = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[2]/div/a')
        self.news_3 = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[3]/div/a')
        self.news_4 = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[4]/div/a')
        self.news_5 = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[5]/div/a')
        self.news_6 = driver.find_element(By.XPATH, '//*[@id="page"]/section[4]/div/div/div[2]/div/section['
                                                    '1]/div/ul/li[1]/div/a')
        self.news_7 = driver.find_element(By.XPATH, '//*[@id="page"]/section[4]/div/div/div[2]/div/section['
                                                    '1]/div/ul/li[2]/div/a')
        self.news_8 = driver.find_element(By.XPATH, '//*[@id="page"]/section[4]/div/div/div[2]/div/section['
                                                    '1]/div/ul/li[3]/div/a')
        self.news_9 = driver.find_element(By.XPATH, '//*[@id="page"]/section[4]/div/div/div[2]/div/section['
                                                    '2]/div/ul/li[1]/div/a')
        self.news_10 = driver.find_element(By.XPATH, '//*[@id="page"]/section[4]/div/div/div[2]/div/section['
                                                     '2]/div/ul/li[3]/div/a')
