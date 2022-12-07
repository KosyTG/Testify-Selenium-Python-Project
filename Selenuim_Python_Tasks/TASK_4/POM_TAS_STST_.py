import time
from POM_TAS import T_A_S
from POM_STST import S_T_S_T
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.testifyltd.com/contact')
    actionChain = ActionChains(driver)
    print("Academy Link:", academyLink.is_displayed())
    TAS = T_A_S(driver)
    print(TAS.title)
    STST = S_T_S_T(driver)
    print(STST.title)


if __name__ == '__main__':
    main()
