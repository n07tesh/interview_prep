from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
import time
from bs4 import BeautifulSoup
# import pandas as pd
import csv
class Xpath:
    url = 'https://mathup.com/games/crossbit'
    play_button = '/html/body/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[3]/div[1]'
    web_driver_loc = r'D:\web_driver\chromedriver.exe'
    div_class = 'GamePostStart_info__Rwi7G'
    file_name = 'scrap_data.csv'
    fields = ['S.no','Difficulty']    

    def web_driver(self,):
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
            rows = []
            with open(Xpath.file_name,'w') as csvfile:
                # writing the fields 
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(Xpath.fields)
                for i in range(10):
                    page_source_ = driver.page_source
                    soup = BeautifulSoup(page_source_,'html.parser')
                    time.sleep(1)
                    x = soup.find_all('div',{'class':'GamePostStart_info__Rwi7G'})[1].text.split(" ")[1]
                    temp = []
                    temp.append(i)
                    temp.append(x)
                    rows.append(temp)
                    # writing the data rows 
                    csv_writer.writerows(rows)
                    driver.refresh()
                    driver.find_element(By.XPATH,Xpath.play_button).click()
                    time.sleep(3)
                    continue

        except Exception as e:
            driver.close()

if __name__ == "__main__":
    x = Xpath()
    x.web_driver()