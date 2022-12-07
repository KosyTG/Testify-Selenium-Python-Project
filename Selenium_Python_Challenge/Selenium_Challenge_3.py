import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def Main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://weather.com/ ")
    currentTemperature = driver.find_element(By.XPATH, '//*[@id="WxuCurrentConditions-main-b3094163-ef75-4558-8d9a'
                                                       '-e35e6b9b1034"]/div/section/div/div[2]/div[1]/div[1]/span')
    print("Current Temp:", currentTemperature.text)
    morningTemperature = driver.find_element(By.XPATH, '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76'
                                                       '-7aea8e98520a"]/section/div/ul/li[1]/a/div[1]/span')
    print("Morning Temp:", morningTemperature.text)

    afternoonTemperature = driver.find_element(By.XPATH, '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76'
                                                         '-7aea8e98520a"]/section/div/ul/li[2]/a/div[1]/span')
    print("Afternoon Temp:", afternoonTemperature.text)

    eveningTemprature = driver.find_element(By.XPATH, '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76'
                                                      '-7aea8e98520a"]/section/div/ul/li[3]/a/div[1]/span')
    print("Evening Temp:", eveningTemprature.text)

    overnightTemperature = driver.find_element(By.XPATH, '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76'
                                                         '-7aea8e98520a"]/section/div/ul/li[4]/a/div[1]/span')
    print("Overnight Temp:", overnightTemperature.text)


if __name__ == '__main__':
    Main()
