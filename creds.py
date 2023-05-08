import os
import re
import mysql.connector as connector
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import shutil
from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as Firefox_Options
from pytesseract import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import pytz
import socket
from bs4 import BeautifulSoup

threshold = 70


class TesseractPath:
    if socket.gethostname() == 'CINOD10LTR067':
        path = r"C:\Users\NY9991041\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
    else:
        if os.name == 'nt':
            path = r"C:\Users\ss999749\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
        else:
            path = ""


class MySQLCredentials:
    if socket.gethostname() == "CINOD10LTR067":
        name = 'edu_scrapper'
        user = 'root'
        password = 'root'
        host = 'localhost'
        port = '3306'
    else:
        if os.name == 'nt':
            name = 'onicra_ops_scrap'
            user = 'root'
            password = 'root'
            host = 'localhost'
            port = '3306'
        else:
            name = 'new_edu_scrapping_data'
            user = 'helloadmin@helloverify-production-mysql'
            password = '9tTAXvWBedPx3KQ'
            host = 'helloverify-production-mysql.mysql.database.azure.com'
            port = '3306'


def mysql_connect():
    conn = connector.connect(
        database=MySQLCredentials.name,
        username=MySQLCredentials.user,
        password=MySQLCredentials.password,
        host=MySQLCredentials.host,
        port=MySQLCredentials.port
    )
    return conn


def filename_generator(roll_no, filename, extension='html', yop=None):
    """
    roll_no: int: roll number
    filename: str: filename
    extension: str: extension of the file
    """
    roll = f"{roll_no}_{filename}.{extension}"
    if yop:
        roll = f"{roll_no}_{yop}_{filename}.{extension}"
    return roll


def get_filter_data(roll_no, board_id, name=None, yop=None, extra=None):
    """
    roll_no: str: roll number
    board_id: auto id of board
    name: str: name od student
    yop: str/int: year of passing
    return: str: raw sql query
    """
    to_filter = ""
    if roll_no:
        to_filter = to_filter + f'roll_no = "{roll_no}"AND'
    if board_id:
        to_filter = to_filter + f'board_id = {board_id}AND'
    if name and not extra:
        to_filter = to_filter + f'name = "{name}"AND'
    if yop and not extra:
        to_filter = to_filter + f'year_of_passing = "{yop}"AND'
    to_filter = ' AND '.join(to_filter.split('AND')[:-1])
    return f'SELECT * FROM education WHERE {to_filter}'


def get_page_source(url):
    """
    url: str: api url
    htno: str: hall ticket number
    return: html: page source   Check your Register Number
    """
    result = ''
    try:
        res = requests.get(url)
        result = res.text
        if 'Check your Register Number' in result:
            result = ''
    except Exception as e:
        pass
    finally:
        return result


def roll_no_generator(format, length, count):
    """
    format: str: roll number format
    length: int: length of roll number
    count: int: roll number
    return: str: sample roll number
    """
    raw_roll_len = len(str(count))
    no_of_zeros = length - raw_roll_len
    roll = f"{'0'*no_of_zeros}{count}"
    return format.format(roll)


if os.name == 'nt':
    webdriver_loc = r"D:\Others Projects\WebDriver\chromedriver.exe"
    webdriver_loc_firefox = r"D:\Others Projects\WebDriver\geckodriver.exe"
else:
    webdriver_loc = "/usr/bin/chromedriver"
    webdriver_loc_firefox = '/home/azureuser/geckodriver'


class Email:
    to = [
        "sunil.singh@helloverify.com",
        "nitesh.yadav@helloverify.com"
    ]
    config = {
        'FromEmailID': 'noreply@helloverify.com',
        'FromEmailPassword': 'Welcome@886',
        'FromEmailHost': 'smtp.office365.com',
        'FromEmailPort': '587'
    }


def send_mail(subject, mail_body):
    try:
        username = Email.config['FromEmailID']
        password = Email.config['FromEmailPassword']
        mail_from = Email.config['FromEmailID']
        mail_to = ','.join(Email.to)
        mail_subject = subject
        mail_body = f"Service Stopped:-\n{'*'*50}\n{'*'*50}\n\n\t{mail_body}\n\n{'*'*50}\n{'*'*50}"
        mimemsg = MIMEMultipart()
        mimemsg['From'] = mail_from
        mimemsg['To'] = mail_to
        mimemsg['Subject'] = mail_subject
        mimemsg.attach(MIMEText(mail_body, 'plain'))
        connection = smtplib.SMTP(host=Email.config['FromEmailHost'], port=int(Email.config['FromEmailPort']))
        connection.starttls()
        connection.login(username, password)
        connection.send_message(mimemsg)
        connection.quit()
    except Exception as e:
        print(str(e))


def web_driver(webdriver='chrome'):
    driver = None
    try:
        if webdriver == 'firefox':
            options = Firefox_Options()
            options.add_argument('--headless')
            driver = Firefox(executable_path=webdriver_loc_firefox, options=options)
            driver.maximize_window()
            return driver
        else:
            options = Chrome_Options()
            options.add_argument('--headless')
            driver = Chrome(executable_path=webdriver_loc, options=options)
            driver.maximize_window()
            return driver
    except Exception as e:
        try:
            driver.close()
        except:
            pass


def web_driver_with_file(download_path, webdriver='chrome'):
    """
    ex_path: str: excutable_path for chrome webdriver
    cwd: str: directory path to download files

    return: object: chrome driver object
    """
    if webdriver == 'firefox':
        options = Firefox_Options()
    else:
        options = Chrome_Options()
    profile = {
        "download.default_directory": download_path,  # download to this directory
        "download.prompt_for_download": False,  # To auto download the file
        "plugins.always_open_pdf_externally": True  # It will not show PDF directly in chrome
    }
    # options.add_argument('--disable-extensions')
    options.add_experimental_option("prefs", profile)
    options.add_argument('--headless')
    try:
        if webdriver == 'firefox':
            driver = Firefox(executable_path=webdriver_loc_firefox, options=options)
        else:
            driver = Chrome(executable_path=webdriver_loc, options=options)
        driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_path}}
        driver.execute("send_command", params)
        # driver.maximize_window()
        return driver
    except:
        pass


def clear_folder(filepath):
    for root, dirs, files in os.walk(filepath):
        for f in files:
            os.unlink(os.path.join(root, f))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))


def wait_till_download_function(filepath, file_extension):
    while True:
        try:
            file = os.listdir(filepath)[0].split('.')
            ext = file[-1]
            if ext.lower() == file_extension:
                return
            else:
                pass
        except:
            continue


def get_current_dt():
    IST = pytz.timezone('Asia/Kolkata')
    return datetime.now(IST)


def update_records_to_db(validate=True, **kwargs):
    try:
        conn = mysql_connect()
        data = {
            'roll_no': kwargs.get('roll_no'),
            'board_id': kwargs.get('board_id'),
            'college_name': kwargs.get('college_name'),
            'name': kwargs.get('name'),
            'father_name': kwargs.get('father_name'),
            'gender': kwargs.get('gender'),
            'year_of_passing': kwargs.get('year_of_passing'),
            'year_of_appeared': kwargs.get('year_of_appeared'),
            'degree_name': kwargs.get('degree_name'),
            'exam_result': kwargs.get('exam_result'),
            'branch_name': kwargs.get('branch_name'),
            'filepath': kwargs.get('filepath'),
            'website_url': kwargs.get('website_url'),
            'created_at': kwargs.get('created_at'),
            'updated_at': kwargs.get('updated_at'),
            'created_by_id': kwargs.get('created_by_id'),
            'updated_by_id': kwargs.get('updated_by_id')
        }
        if validate:
            search_query = get_filter_data(
                roll_no=data['roll_no'],
                board_id=data['board_id'],
                name=data['name'],
                yop=data['year_of_passing'],
                extra=data.get('extra')
            )
            cursor = conn.cursor()
            cursor.execute(search_query)
            res = cursor.fetchall()
            cursor.close()
            if res:
                return True
        to_insert_fields = []
        payload = []
        for key, value in data.items():
            if data[key]:
                to_insert_fields.append(key)
                payload.append(value)
        _to_insert_fields = '(' + ', '.join(to_insert_fields) + ')'
        to_insert_formatter = '(' + ', '.join(['%s' for _ in range(len(to_insert_fields))]) + ')'
        insert_query = f"INSERT INTO education {_to_insert_fields} VALUES {to_insert_formatter}"
        cursor = conn.cursor()
        cursor.execute(insert_query, payload)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        return False


def rollno_generator_banglore_university(yoa, clg_code, branch_code, serial_no):
    """
    yoa: int/str: year of addmission
    clg_code: str: college code
    branch_code: str: branch code
    serial_no: int/str: serial number of student
    return: str: generated roll number
    """
    no_of_zero = 3 - len(str(serial_no))
    serial_no = f'{"0"*no_of_zero}{serial_no}'
    return f"{yoa}{clg_code}{branch_code}{serial_no}"


class BangaloreUniversityCreds:
    url = 'https://buofc.inhawk.com/Examresults/'
    search_inp_id = 'ContentPlaceHolder1_txtSearch'
    search_btn_id = 'ContentPlaceHolder1_btnSearch'
    clear_btn_id = 'ContentPlaceHolder1_btnclear'
    not_found_id = 'Image1'


class AcharyaNagarjunaCreds:
    url = "http://www.nagarjunauniversity.ac.in/4by4btech2ndsemregsept2020.php"
    captcha_error_xpath = '/html/body/section[3]/div/div/table/tbody/tr/td/div/table/tbody/tr/td/table/tbody/tr[2]/td/div'
    roll_error_xpath = '/html/body/div/div[3]/div/table/tbody/tr/td/div/table/tbody/tr[4]/td/div/font/strong'
    enter_roll_id = 'hno'
    enter_captcha_id = 'anu_captcha_code'
    submit_xpath = '/html/body/section[3]/div/div/table/tbody/tr/td/div/table/tbody/tr/td/table/tbody/tr[3]/td/div/form/table/tbody/tr[5]/td/div/label/input'
    captcha_id = "captchaimg"
    try_back_xpath = '/html/body/div/div[3]/div/table/tbody/tr/td/div/table/tbody/tr[7]/td/div/font/strong/a'
    back_xpath = '/html/body/div/div[3]/div/table/tbody/tr/td/div/table/tbody/tr/td/table/tbody/tr[6]/td/div/font/a/strong'
    raw_captcha_name = 'anu_captcha.png'
    processed_captcha_name = 'anu_captcha_processed.png'
    if os.name == 'nt':
        captcha_path = r"D:\saved_files\captcha"
    else:
        captcha_path = "/new_education_data/edu_temp/captcha"


def anu_image_to_text():
    image_captcha_path = os.path.join(AcharyaNagarjunaCreds.captcha_path, AcharyaNagarjunaCreds.raw_captcha_name)
    im = Image.open(image_captcha_path)
    if os.name == 'nt':
        im = im.crop((545, 425, 660, 465))
    else:
        im = im.crop((310, 495, 428, 535))
    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')
    processed_captcha_path = os.path.join(AcharyaNagarjunaCreds.captcha_path, AcharyaNagarjunaCreds.processed_captcha_name)
    im.save(processed_captcha_path)
    if os.name == 'nt':
        pytesseract.tesseract_cmd = TesseractPath.path
    text = pytesseract.image_to_string(Image.open(processed_captcha_path))
    return re.sub('[^a-zA-Z0-9]', '', text.split('\n')[0].strip())


class VTUCreds:
    url = "https://results.vtu.ac.in/JAEcbcs/index.php"
    enter_roll_xpath = '//*[@id="raj"]/div[1]/div/input'
    enter_captcha_xpath = '//*[@id="raj"]/div[2]/div[1]/input'
    submit_id = 'submit'
    captcha_xpath = '//*[@id="raj"]/div[2]/div[2]/img'
    raw_captcha_name = 'vtu_captcha.png'
    processed_captcha_name = 'vtu_captcha_processed.png'
    if os.name == 'nt':
        captcha_path = r"D:\saved_files\captcha"
    else:
        captcha_path = "/new_education_data/edu_temp/captcha"


def vtu_image_to_text():
    try:
        image_captcha_path = os.path.join(VTUCreds.captcha_path, VTUCreds.raw_captcha_name)
        im = Image.open(image_captcha_path)
        if os.name == 'nt':
            # im = im.crop((700, 350, 855, 420))
            im = im.crop((50, 350, 205, 420))
        else:
            im = im.crop((50, 350, 205, 420))
        im = im.filter(ImageFilter.MaxFilter())
        enhancer = ImageEnhance.Contrast(im)
        im = enhancer.enhance(2)
        im = im.convert('1')
        processed_captcha_path = os.path.join(VTUCreds.captcha_path, VTUCreds.processed_captcha_name)
        im.save(processed_captcha_path)
        if os.name == 'nt':
            pytesseract.tesseract_cmd = TesseractPath.path
        text = pytesseract.image_to_string(Image.open(processed_captcha_path))
        return re.sub('[^a-zA-Z0-9]', '', text.split('\n')[0].strip())
    except:
        return '000'


class RgpvCreds:
    url = "http://result.rgpv.ac.in/result/ProgramSelect.aspx"
    enter_roll_id = 'ctl00_ContentPlaceHolder1_txtrollno'
    select_semester_id = 'ctl00_ContentPlaceHolder1_drpSemester'
    enter_captcha_id = 'ctl00_ContentPlaceHolder1_TextBox1'
    if os.name == 'nt':
        captch_a = 595
        captch_b = 290
        captcha_path = r"D:\saved_files\captcha"
    else:
        captch_a = 400
        captch_b = 275
        captcha_path = "/new_education_data/edu_temp/captcha"
    captch_c = captch_a + 175
    captch_d = captch_b + 50
    raw_captcha_name = "rgpv_captcha.png"
    processed_captcha_name = "rgpv_captcha_processed.png"
    view_result_id = 'ctl00_ContentPlaceHolder1_btnviewresult'
    reset_id = 'ctl00_ContentPlaceHolder1_btnReset'


def rgpv_image_to_text():
    try:
        image_captcha_path = os.path.join(RgpvCreds.captcha_path, RgpvCreds.raw_captcha_name)
        im = Image.open(image_captcha_path)
        im = im.crop((RgpvCreds.captch_a, RgpvCreds.captch_b, RgpvCreds.captch_c, RgpvCreds.captch_d))
        processed_captcha_path = os.path.join(RgpvCreds.captcha_path, RgpvCreds.processed_captcha_name)
        im.save(processed_captcha_path)
        if os.name == 'nt':
            pytesseract.tesseract_cmd = TesseractPath.path
        text = pytesseract.image_to_string(Image.open(processed_captcha_path))
        return re.sub('[^a-zA-Z0-9]', '', text.split('\n')[0].strip())
    except:
        return '00000'


class MakautCreds:
    enter_roll_id = 'username'
    select_semester_id = 'semester'  # values - SM01-SM10
    search_result_xpath = '//*[@id="result-search-panal"]/div[2]/div[1]/button'
    no_record_xpath = '//*[@id="resultDetails_view"]/div/div/h2'
    reset_xpath = '//*[@id="result-search-panal"]/div[2]/div[3]/a'


def get_cookies_requests(url, viewstate=False):
    """
    url: str: url of website
    viewstate: bool: True if viewstate required else False

    return: result with viewstate etc params and headers with cookies
    """
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    result = dict()
    res = requests.get(url)
    cookie = [f"{key}={value}" for key, value in res.cookies.items()][0]
    headers['Cookie'] = cookie
    if viewstate:
        soup = BeautifulSoup(res.text, 'html.parser')
        viewstate = soup.find('input', attrs={'id': '__VIEWSTATE'}).get('value').strip()
        viewstate_generator = soup.find('input', attrs={'id': '__VIEWSTATEGENERATOR'}).get('value').strip()
        event_validation = soup.find('input', attrs={'id': '__EVENTVALIDATION'}).get('value').strip()
        result['__LASTFOCUS'] = ""
        result['__VIEWSTATE'] = viewstate
        result['__VIEWSTATEGENERATOR'] = viewstate_generator
        result['__EVENTTARGET'] = ""
        result['__EVENTARGUMENT'] = ""
        result['__EVENTVALIDATION'] = event_validation
    return result, headers


def get_cookies_selenium(url, sample_roll, roll_path, submit_path, token_param='accessToken', roll_id=True, submit_id=True):
    """
    url: str: complete url
    sample_roll: str: sample roll number
    roll_path: str: roll number xpath/id
    submit_path: str: submit button xpath/id
    token_param: str: token parameter to search (mentioned in page source) | default is accessToken
    roll_id: bool: True if rol_path is id else False
    submit_id: bool: True if submit_path is id else False

    return: token and cookies
    """
    driver = web_driver()
    driver.get(url)
    if roll_id:
        driver.find_element_by_id(roll_path).send_keys(sample_roll)
    else:
        driver.find_element_by_xpath(roll_path).send_keys(sample_roll)
    if submit_id:
        driver.find_element_by_id(submit_path).click()
    else:
        driver.find_element_by_xpath(submit_path).click()
    ps = driver.page_source
    cookies = driver.get_cookies()
    driver.close()
    token = re.search(token_param + '=".*(\d+)', ps)
    if token:
        return token.group(1), cookies
