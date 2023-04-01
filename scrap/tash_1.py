from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
import time
from bs4 import BeautifulSoup
import pandas as pd

class Xpath:
    url = 'https://mathup.com/games/crossbit'
    play_button = '/html/body/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[3]/div[1]'
    web_driver_loc = r'D:\web_driver\chromedriver.exe'
    div_class = 'GamePostStart_info__Rwi7G'
for i in range(10):
    def web_driver():
        try:
            options = Options()
            options.add_argument('--incognito')
            options.add_experimental_option('detach',True)
            driver = Chrome(executable_path=Xpath.web_driver_loc,options=options)
            driver.maximize_window()
            driver.get(Xpath.url)
            time.sleep(2)
            driver.find_element(By.XPATH,Xpath.play_button).click()
            time.sleep(3)
            page_source_ = driver.page_source
            soup = BeautifulSoup(page_source_,'html.parser')
            div_ = soup.find_all('div')[0:1]
            next_ = div_.find_all('div')[0]
            print(next_)

        except Exception as e:
            driver.close()

if __name__ == "__main__":
    web_driver()