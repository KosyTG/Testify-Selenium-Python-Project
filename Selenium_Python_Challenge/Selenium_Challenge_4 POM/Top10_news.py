import time

from selenium import webdriver
from homePage_Top10_News_elements import homePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def Main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.bbc.com/")
    Top_10_News = homePage(driver)
    print("News1:", Top_10_News.news_1.text)
    print("News2:", Top_10_News.news_2.text)
    print("News3:", Top_10_News.news_3.text)
    print("News4:", Top_10_News.news_4.text)
    print("News5:", Top_10_News.news_5.text)
    print("News6:", Top_10_News.news_6.text)
    print("News7:", Top_10_News.news_7.text)
    print("News8:", Top_10_News.news_8.text)
    print("News9:", Top_10_News.news_9.text)
    print("News10:", Top_10_News.news_10.text)







if __name__ == '__main__':
    Main()