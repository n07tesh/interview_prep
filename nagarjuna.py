import creds
from time import sleep
import os
import re
from bs4 import BeautifulSoup

## with captcha
# mtech = {
#     2019: {
#         'https://www.nagarjunauniversity.ac.in/mtech4semregjun19.php': ''
#     },
#     2020: {
#         'https://www.nagarjunauniversity.ac.in/mtech4semregdec2020.php': ''
#     }
# }
# barch = {
#     2020: {
#         'http://www.nagarjunauniversity.ac.in/5by5batchlorarch2semregoct2020.php': ''
#     },
#     2021: {
#         'http://www.nagarjunauniversity.ac.in/55barch2semregresjuly2021.php': ''
#     }
# }
# mca = {
#     2019: {
#         'https://www.nagarjunauniversity.ac.in/mca6semregjul19.php': ''
#     },
#     2020: {
#         'https://www.nagarjunauniversity.ac.in/mca6thsemregdegexasept2020.php': ''
#     }
# }
# mba = {
#     2020: {
#         'https://www.nagarjunauniversity.ac.in/mbahspadm4semregsept2020.php': ''
#     }
# }
# mcom = {
#     2020: {
#         'https://www.nagarjunauniversity.ac.in/mcom4semregsept2020.php': ''
#     },
#     2021: {
#         'https://www.nagarjunauniversity.ac.in/mcm4thsemregaug2021.php': ''
#     }
# }
# ma = {
#     2021: {
#         'https://www.nagarjunauniversity.ac.in/maarchaeology4semregaug2021.php': 'ARCHAEOLOGY',
#         'https://www.nagarjunauniversity.ac.in/masan4semregaug2021.php': 'SANSKRIT',
#         'https://www.nagarjunauniversity.ac.in/mahistory4semregaug2021.php': 'HISTORY',
#         'https://www.nagarjunauniversity.ac.in/mapolsci4semregaug2021.php': 'POLITICAL',
#         'https://www.nagarjunauniversity.ac.in/mapubadmin4semregaug2021.php': 'ADMINISTRATION',
#         'https://www.nagarjunauniversity.ac.in/maruraldeve4semregaug2021.php': 'RURAL DEVELOPMENT'
#     },
#     2020: {
#         'https://www.nagarjunauniversity.ac.in/maarch4semregsept2020.php': 'ARCHAEOLOGY',
#         'https://www.nagarjunauniversity.ac.in/mahistory4semregsep2020.php': 'HISTORY',
#         'https://www.nagarjunauniversity.ac.in/masan4semregsept2020.php': 'SANSKRIT',
#         'https://www.nagarjunauniversity.ac.in/masocio4semregsept2020.php': 'SOCIOLOGY',
#         'https://www.nagarjunauniversity.ac.in/mard4semregsept2020.php': 'RURAL DEVELOPMENT'
#     }
# }
# bpharma = {
#     2019: {
#         'https://www.nagarjunauniversity.ac.in/bpharma6semregnov19.php': ''
#     },
#     2020: {
#         'https://www.nagarjunauniversity.ac.in/bpharma8semregsept2020.php': ''
#     },
#     2021: {
#         'https://www.nagarjunauniversity.ac.in/44bpharmacy8semregaug2021.php': ''
#     }
# }
# # without captcha
# bed = {
#     2020: {
#         'https://www.nagarjunauniversity.ac.in/bed4thsemregdec2020.php': ''
#     }
# }
url_btech = {
    16: 'http://www.nagarjunauniversity.ac.in/4by4btech2ndsemregsept2020.php',
    17: 'http://www.nagarjunauniversity.ac.in/44btech2semregaug2021.php'
}
course_btech = ['CS', 'EE', 'EC', 'ME', 'CE']
college_btech = ['32', '12', '13', '26', '27', '28']


class FileSaveLocationNew:
    if os.name == 'nt':
        anu = r"D:\saved_files"
    else:
        anu = '/new_education_data/acharya_nagarjuna_univ'


def get_captcha(driver):
    captcha_path = os.path.join(creds.AcharyaNagarjunaCreds.captcha_path, creds.AcharyaNagarjunaCreds.raw_captcha_name)
    driver.save_screenshot(captcha_path)
    captcha_text = creds.anu_image_to_text()
    return captcha_text


def scrap_data_from_page_source(page_source, web_url):
    result = dict()
    result['status'] = False
    try:
        soup = BeautifulSoup(page_source, 'html.parser')
        result['board'] = soup.title.text.strip()
        tbl = soup.find('table').find('table').find_all('table')[2:4]
        stu_info = tbl[0].find_all('tr')[1:]
        for rows in stu_info:
            try:
                td = rows.find_all('td')
                if td:
                    td1 = td[0].text.replace('\n', '').lower()
                    td2 = td[1].text.replace('\n', '').strip()
                else:
                    continue
                if 'hall' in td1 and 'ticket' in td1:
                    result['roll_no'] = td2
                elif 'student' in td1 and 'name' in td1:
                    result['name'] = td2
                elif 'father' in td1 and 'name' in td1:
                    result['father_name'] = td2
                elif 'course' in td1:
                    temp1 = re.search('(?:I|II|III|IV|V)\s([a-zA-Z\.]+)', td2)
                    temp2 = re.search('(\d{4})', td2)
                    if temp2:
                        result['year_of_passing'] = temp2.group(1)
                    else:
                        result['year_of_passing'] = ""
                    if temp1:
                        result['degree_name'] = temp1.group(1)
                elif td1 == 'cgpa':
                    result['exam_result'] = td2
            except:
                pass
        result['board_id'] = 13
        result['created_at'] = creds.get_current_dt()
        result['updated_at'] = creds.get_current_dt()
        result['website_url'] = web_url
        filename = f'{"_".join(result["board"].replace(",", "").split())}_' + '_'.join(result['degree_name'].replace('.', '').split())
        filepath = creds.filename_generator(result['roll_no'], filename)
        filepath = os.path.join(FileSaveLocationNew.anu, filepath)
        with open(filepath, 'w', encoding="utf-8") as f:
            f.write(page_source)
        result['filepath'] = filepath
        result['status'] = True
    except Exception as e:
        pass
    finally:
        return result


def scrap_btech():
    print("start")
    threshold = 0
    driver = None
    try:
        for yoa, url in url_btech.items():
            driver = creds.web_driver()
            driver.get(url)
            flag = True
            for course in course_btech:
                for code in college_btech:
                    if yoa == 16 and course in ['CS', 'EE', 'EC', 'ME']:
                        continue
                    for i in range(1, 100):
                        if yoa == 16 and course == 'CE' and code in ['32', '12', '13', '26', '27']:
                            continue
                        if yoa == 16 and course == 'CE' and code == '28' and i == 1:
                            continue
                        i = '0'*(2-len(str(i))) + str(i)
                        roll = f"Y{yoa}{course}{code}{i}"
                        while True:
                            try:
                                captcha_text = get_captcha(driver)
                                sleep(1)
                                roll_ele = driver.find_element_by_id(creds.AcharyaNagarjunaCreds.enter_roll_id)
                            except:
                                try:
                                    driver.close()
                                    sleep(5)
                                except:
                                    pass
                                driver = creds.web_driver()
                                driver.get(url)
                                captcha_text = get_captcha(driver)
                                roll_ele = driver.find_element_by_id(creds.AcharyaNagarjunaCreds.enter_roll_id)
                            roll_ele.clear()
                            roll_ele.send_keys(roll)
                            captcha_ele = driver.find_element_by_id(creds.AcharyaNagarjunaCreds.enter_captcha_id)
                            captcha_ele.clear()
                            captcha_ele.send_keys(captcha_text)
                            driver.find_element_by_xpath(creds.AcharyaNagarjunaCreds.submit_xpath).click()
                            try:
                                driver.find_element_by_xpath(creds.AcharyaNagarjunaCreds.captcha_error_xpath)
                                driver.get(url)
                                continue
                            except:
                                try:
                                    driver.find_element_by_xpath(creds.AcharyaNagarjunaCreds.try_back_xpath).click()
                                    flag = False
                                    threshold += 1
                                    break
                                except:
                                    pass
                                threshold = 0
                                flag = True
                                break
                        if not flag:
                            if threshold >= 15:
                                break
                            continue
                        page_source = driver.page_source
                        scrap_data = scrap_data_from_page_source(page_source, url)
                        scrap_data['extra'] = 'anu'
                        driver.back()
                        creds.update_records_to_db(**scrap_data)
            driver.close()
        creds.send_mail('Nagarjuna University:: ', 'Completed')
    except Exception as e:
        creds.send_mail('Error: Nagarjuna University', str(e))
        print(e)
        pass
    finally:
        try:
            driver.close()
        except:
            pass


# if __name__ == '__main__':
#     scrap_btech()
