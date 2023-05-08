# Shivaji University, Kolhapur
import re

import creds
from time import sleep
from selenium.webdriver.common.by import By
import os
import PyPDF2
import fitz
from selenium.common.exceptions import TimeoutException

stream_ids = ['02', '03', '04', '05', '06', '07', '08', '09', '10']  # '01',
url = "http://14.139.121.222/studentresult/"


class SukCreds:
    enter_prn_id = 'PRNNO'
    view_result_name = 'Sign In'
    error_url = 'http://210.212.190.39:89/'
    if os.name == 'nt':
        default_download_path = r"D:\saved_files\default_shivaji"
        if not os.path.exists(default_download_path):
            os.makedirs(default_download_path)
    else:
        default_download_path = "/new_education_data/edu_temp/shivaji_res"


class FileSaveLocationNew:
    if os.name == 'nt':
        suk = r"D:\saved_files"
    else:
        suk = '/new_education_data/shivaji_univ'


def roll_generator(yop, stream_code, stream_name, count):
    yoa = 0
    if stream_name == 'btech':
        yoa = yop - 4
    no_of_zero = 4 - len(str(count))
    count = f"{'0'*no_of_zero}{count}"
    return f"{yoa}{stream_code}{count}"


def scrapping(roll):
    result = dict()
    result['status'] = False
    creds.wait_till_download_function(SukCreds.default_download_path, 'pdf')
    try:
        file = ""
        all_file = os.listdir(SukCreds.default_download_path)
        for files in all_file:
            ext = files.split('.')[-1]
            if ext.lower() == 'pdf':
                file = os.path.join(SukCreds.default_download_path, files)
                break
        pdf = PyPDF2.PdfFileReader(file)
        page_obj = pdf.getPage(0)
        page_text = page_obj.extractText().replace('\n', ' ').replace(':', '')
        name = re.search('(?:name|Name|NAME)(?:[\s]+|\s+)?:?(?:[\s]+|\s+)?([a-zA-Z\s\.]+)(?:mother|Mother|MOTHER)', page_text).group(1)
        # roll_no = re.search('(?:prn|PRN)(?:[\s]+|\s+)?:?(?:[\s]+|\s+)?([0-9]+)', page_text)
        college_name = re.search('(?:College|college|COLLEGE)(?:[\s]+|\s+)?:?(?:[\s]+|\s+)?([a-zA-Z\s\.&]+)', page_text)
        branch_name = re.search('(?:branch|Branch|BRANCH)(?:[\s]+|\s+)?:?(?:[\s]+|\s+)?([a-zA-Z\.\s]+)(?:category|Category|CATEGORY)', page_text)
        year_of_passing = re.search('(?:examination|Examination)(?:[\s]+|\s+)?([\d\sa-zA-Z-]+)', page_text)
        degree_name = re.search('(?:statement|Statement)s?(?:[\s]+|\s+)?(?:of|Of|OF)(?:[\s]+|\s+)?(?:mark|Mark|MARK)s?(?:[\s]+|\s+)?(?:for|For|FOR)(?:[\s]+|\s+)?:?(?:[\s]+|\s+)?([a-zA-Z\.\s]+)(?:part|Part|PART|\(|-)', page_text)
        exam_result = re.search('(?:result|Result|RESULT)(?:s|S)?(?:[\s]+|\s+)?-?(?:[\s]+|\s+)?([A-Z\s]+)(?:result|Result)', page_text)
        exam_result_1 = re.search('(?:Rseult|rseult|RSEULT)(?:s|S)?(?:[\s]+|\s+)?-?(?:[\s]+|\s+)?([A-Za-z]+)(?:[\s]+|\s+)?', page_text)
        result['name'] = name.strip()
        result['roll_no'] = roll
        if college_name:
            result['college_name'] = college_name.group(1).strip()
        if branch_name:
            result['branch_name'] = branch_name.group(1).strip()
        if year_of_passing:
            result['year_of_passing'] = year_of_passing.group(1).strip()
        if degree_name:
            degree_name = degree_name.group(1).replace('Part No', '').strip()
            result['degree_name'] = degree_name
        if exam_result:
            result['exam_result'] = exam_result.group(1).strip()
        else:
            if exam_result_1:
                result['exam_result'] = exam_result_1.group(1).strip()
        now = creds.get_current_dt()
        result['created_at'] = now
        result['updated_at'] = now
        result['board'] = "shivaji university"
        result['board_id'] = 21
        result['website_url'] = url
        if degree_name:
            filename = f'{"_".join(result["board"].replace(",", "").split())}_' + '_'.join(result['degree_name'].lower().replace('.', '').split())
        else:
            filename = f'{"_".join(result["board"].replace(",", "").split())}_'
        if year_of_passing:
            filepath = creds.filename_generator(result['roll_no'], filename, yop=result['year_of_passing'].lower(), extension='pdf')
        else:
            filepath = creds.filename_generator(result['roll_no'], filename, extension='pdf')
        filepath = os.path.join(FileSaveLocationNew.suk, filepath)
        doc = fitz.open(file)
        doc.save(filepath, garbage=3)
        doc.close()
        result['filepath'] = filepath
        result['status'] = True
    except Exception as e:
        result['status'] = False
        print(e)
    finally:
        return result


def scrap_suk(yop=2021, stream_name='btech'):
    driver = creds.web_driver_with_file(SukCreds.default_download_path)
    roll = ""
    try:
        for ids in stream_ids:
            thresh = 0
            for i in range(1, 10000):
                if ids == '02' and i <= 1008:
                    continue
                roll = roll_generator(yop, ids, stream_name, i)
                # roll = '2017011273'  # testing purposes
                is_found = True
                while True:
                    try:
                        creds.clear_folder(SukCreds.default_download_path)
                        driver.get(url)
                        driver.find_element(By.ID, SukCreds.enter_prn_id).send_keys(roll)
                        driver.find_element(By.NAME, SukCreds.view_result_name).click()
                        sleep(1)
                        new_url = ''
                        try:
                            driver.set_page_load_timeout(5)
                            new_url = driver.current_url
                        except TimeoutException as e:
                            is_found = False
                            driver.set_page_load_timeout(60)
                            break
                        if new_url != url:
                            is_found = False
                        break
                    except Exception as e:
                        sleep(30)
                        try:
                            driver.close()
                            driver.quit()
                        except:
                            pass
                        try:
                            driver = creds.web_driver_with_file(SukCreds.default_download_path)
                        except:
                            pass
                if not is_found:
                    if thresh >= 30:
                        creds.send_mail(f'Shivaji University Skipped To Next after- {roll} :: Skipped', 'Completed')
                        break
                    thresh += 1
                    continue
                thresh = 0
                scrap_data = scrapping(roll)
                if scrap_data['status']:
                    creds.update_records_to_db(validate=False, **scrap_data)
        creds.send_mail('Shivaji University :: Success', 'Completed')
    except Exception as e:
        creds.send_mail(f"Shivaji University: Error- {roll}", str(e))
    finally:
        try:
            driver.close()
            driver.quit()
        except:
            pass


if __name__ == '__main__':
    scrap_suk()
