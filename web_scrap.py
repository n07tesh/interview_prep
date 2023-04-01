from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.common.action_chains import Acions
from selenium.webdriver.common.by import By

## 'https://www.practo.com/' ##

# from bs4 import BeautifulSoup
# from selenium import webdriver

# driver = webdriver.Chrome()

class xpath:
    web_driver_loc = r"D:\web_driver\chromedriver.exe"
    url = 'https://www.practo.com/'
    location = ['Noida','']
    location_xpath = '/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/span[1]'

    def web_driver():
        options = Chrome_Options()
        options.add_argument('--incognito')
        driver = Chrome(executable_path=xpath.web_driver_loc,options=options)
        driver.maximize_window()
        return driver
        
# web_driver()

def scrap():
    driver = xpath.web_driver()
    driver.get(xpath.url)
    while True:
        pass


if __name__ == '__main__':
   scrap()

    


