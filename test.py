from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver import Chrome
# from selenium.webdriver.common import actions_chains
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
class Xpath:
    name = '/html/body/div[2]/div[1]/section[2]/aside[1]/div[2]/form/div[2]/label/input'
    email = '/html/body/div[2]/div[1]/section[2]/aside[1]/div[2]/form/div[3]/label/input'
    join = '/html/body/div[2]/div[1]/section[2]/aside[1]/div[2]/form/input[9]'
    search = '/html/body/div[2]/div[1]/section[2]/aside[2]/form/div/input'
    search_id = 'wp-block-search__input-11'
    search_class = 'wp-block-search__input'
    button = 'wp-block-search__button'

def web_driver():
    try:
        options = Chrome_Options()
        options.add_argument('--incognito')
        options.add_experimental_option('detach',True)
        driver = Chrome(executable_path=r'D:\web_driver\chromedriver.exe',options=options)
        driver.maximize_window()
        driver.get('https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/')
        time.sleep(4)
        action = ActionChains(driver)
        # get element 
        element = driver.find_element(By.CSS_SELECTOR,'#es_subscription_form_submit_63e87c1868ac1')
        action.move_to_element(element).perform()
        element.click()
        login = driver.find_element(By.XPATH,Xpath.name).send_keys('Nitesh')
        email = driver.find_element(By.XPATH,Xpath.email).send_keys('niteshyadav071@gmail.com')
        subs = driver.find_element(By.XPATH,Xpath.join).click()
        time.sleep(2)
        element = driver.find_element(By.CSS_SELECTOR,'#wp-block-search__input-1')
        action.move_to_element(element).perform()
        element.click()
        search = driver.find_element(By.CLASS_NAME,'wp-block-search__input').send_keys('python')
        driver.find_element(By.CLASS_NAME,Xpath.button).click()
        page_source = driver.page_source
        soup = BeautifulSoup(page_source,'htmllib')
        soup.find_all()

    except:
        driver.close()



    # action.perform()
    

if __name__ == '__main__':
    web_driver()

