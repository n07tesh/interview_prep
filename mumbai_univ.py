import os
import extractors
import requests
import PyPDF2
import re

import creds



not_words = [
    'economic', 'growth', 'international', 'trade', 'public', 'policy', 'credit',
    'total', 'bioanalytic', 'science', 'political', 'technology', 'engineer',
    'engg', 'computer', 'information', 'arts', 'social', 'degree', 'instrumentation',
    'electrical', 'foreign', 'national', 'philosophy', 'westd', 'conscious', 'buddhist',
    'psychology', 'meditat', 'buddhism', 'education', 'german', 'management', 'pharmacy',
    'bachelor', 'strategic', 'function', 'finance', 'financial', 'services', 'modeling',
    'contemporary', 'project', 'creating', 'inclusive', 'autotronics', 'dynamic', 'vehicle',
    'design', 'drive', 'control', 'digital', 'image', 'industrial', 'automation', 'voltage', 'system',
    'mechatronic', 'simulation', 'software', 'advance', 'artificial', 'enterprise', 'regulation',
    'navigation', 'aviation', 'aircraft', 'engine', 'java', 'programming', 'object', 'network', 'database',
    'security', 'customer', 'relationship', 'human', 'nutrition', 'food', 'dissertation', 'movement', 'psephology',
    'research', 'methodology', 'auditing', 'direct', 'indirect', 'fund', 'risk', 'corporate', 'restructuring', 'private',
    'venture', 'percentage', ' cgp', 'center', 'college', 'ideal', 'centre', 'result', 'remark', 'total', 'mark', ' and ',
    'patenting', 'performance', 'university', 'mumbai', 'th in'
]

# url_2021 = {
#     "bsc": {
#         # 'http://www.mumresults.in/F21/1S00726CBCS.pdf': None,
#         # 'http://www.mumresults.in/F21/1S00916.pdf': None,
#         # 'http://www.mumresults.in/F21/1S00726.pdf': None,
#         # 'http://www.mumresults.in/F21/1S00426AA.pdf': None,
#         # 'http://www.mumresults.in/S20/1T01418.pdf': None,
#         # 'http://www.mumresults.in/S20/1S00156.pdf': None,
#         # 'http://www.mumresults.in/F21/1S001567.pdf': 'Computer Science',
#         # 'http://www.mumresults.in/F21/1T00728.pdf': 'Computer',
#         'http://www.mumresults.in/F21/1S00246R.pdf': 'Information Technology',
#         'http://www.mumresults.in/F21/1S00816.pdf': 'Forensic Science',
#     },
#     'ma': {
#         'http://www.mumresults.in/F21/4O00724.pdf': None,
#         'http://www.mumresults.in/F21/4O00624.pdf': None,
#         'http://www.mumresults.in/F21/4O00824.pdf': None,
#         'http://www.mumresults.in/F21/3A01214.pdf': None,
#         'http://www.mumresults.in/F21/3A00534.pdf': None,
#         'http://www.mumresults.in/F21/3A00524.pdf': None
#     },
#     'mca': {
#         'http://www.mumresults.in/F21/1T00124.pdf': None
#     },
#     'msc': {
#         'http://www.mumresults.in/F21/1S01334.pdf': None
#     },
#     'be': {
#         'http://www.mumresults.in/F21/1T00518.pdf': 'CHEMICAL ENGINEERING',
#         'http://www.mumresults.in/F21/1T00918.pdf': 'ELECTRONICS AND ELECTRICAL ENGINEERING',
#         'http://www.mumresults.in/F21/PT8CENU.pdf': 'Printing and Packaging',
#         'http://www.mumresults.in/F21/1T00218.pdf': 'Automobile',
#         'http://www.mumresults.in/F21/1T01718.pdf': 'Production',
#         'http://www.mumresults.in/F21/1T00818R.pdf': 'Electrical',
#         'http://www.mumresults.in/F21/1T01518.pdf': 'Mechtronics',
#         'http://www.mumresults.in/F21/1T00428.pdf': 'Bio Tech',
#         'http://www.mumresults.in/F21/1A00216.pdf': 'Production Engineering',
#         'http://www.mumresults.in/F21/1T00618R.pdf': 'Civil',
#         'http://www.mumresults.in/F21/1T01118R.pdf': 'Electronics Engineering',
#         'http://www.mumresults.in/F21/1T01018R.pdf': 'Electronics & Telecommunication',
#         'http://www.mumresults.in/F21/1T00228.pdf': 'Automobile',
#         'http://www.mumresults.in/F21/1T01328.pdf': 'Instrumentation',
#         'http://www.mumresults.in/F21/1T00328.pdf': 'Bio Medical',
#         'http://www.mumresults.in/F21/1T01128.pdf': 'Electronics',
#         'http://www.mumresults.in/F21/1T00718.pdf': 'Computer',
#         'http://www.mumresults.in/F21/1T00528.pdf': 'Chemical',
#         'http://www.mumresults.in/F21/1T01218.pdf': 'Informatiuon Technology',
#         'http://www.mumresults.in/F21/1T01028.pdf': 'Electronics and Telecommunication',
#         'http://www.mumresults.in/F21/1T01228.pdf': 'Information Technology',
#         'http://www.mumresults.in/F21/1T00628.pdf': 'Civil',
#         'http://www.mumresults.in/F21/1T01428.pdf': 'Mechanical',
#         'http://www.mumresults.in/F21/1T00828.pdf': 'Electrical',
#         'http://www.mumresults.in/F21/1T01418.pdf': 'Mechanical',
#         'http://www.mumresults.in/F21/1T01418R.pdf': 'Mechanical',
#     },
#     'bpharma': {
#         'http://www.mumresults.in/F21/1P00128.pdf': None,
#         'http://www.mumresults.in/F21/1P00138.pdf': None
#     },
#     'bed': {
#         'http://www.mumresults.in/F21/4E00144.pdf': None
#     },
#     'barch': {
#         'http://www.mumresults.in/F21/1A00214.pdf': None,
#         'http://www.mumresults.in/F21/1A00215.pdf': None,
#         'http://www.mumresults.in/F21/1A00216.pdf': None
#     },
#     'bms': {
#         'http://www.mumresults.in/F21/2M00156.pdf': None,
#         'http://www.mumresults.in/F21/2M00156AA.pdf': None,
#         'http://www.mumresults.in/F21/2M00146.pdf': None,
#         'http://www.mumresults.in/F21/2M01110.pdf': 'BMS-MBA',
#         'http://www.mumresults.in/F21/2M011107.pdf': 'BMS-MBA',
#         'http://www.mumresults.in/F21/2M00136.pdf': None
#     },
#     'mms': {
#         'http://www.mumresults.in/F21/2M00824.pdf': 'Digital Business',
#         'http://www.mumresults.in/F21/2M00724.pdf': None,
#         'http://www.mumresults.in/F21/2M00734.pdf': None
#     },
#     'march': {
#         'http://www.mumresults.in/F21/1A00524.pdf': None
#     }
# }
# url_2020 = {
#     'be': {
#         'http://www.mumresults.in/S20/1T00828.pdf': 'Electrical',
#         'http://www.mumresults.in/S20/1T01318.pdf': 'Instrumentation',
#         'http://www.mumresults.in/S20/1T01718R.pdf': 'Production',
#         'http://www.mumresults.in/S20/1T00618R.pdf': 'Civil',
#         'http://www.mumresults.in/S20/1T01418O.pdf': 'Mechanical',
#         'http://www.mumresults.in/S20/1T00518.pdf': 'Chemical',
#         'http://www.mumresults.in/S20/1T01128.pdf': 'Electronics',
#         'http://www.mumresults.in/S20/1T01218R.pdf': 'Information Technology',
#         'http://www.mumresults.in/S20/1T01018R.pdf': 'Electronics and Telecommunication',
#         'http://www.mumresults.in/S20/1T01418R.pdf': 'Mechanical',
#         'http://www.mumresults.in/S20/1T01018O.pdf': 'Electronics and Telecommunication',
#         'http://www.mumresults.in/S20/1T01228.pdf': 'Information Technology',
#         'http://www.mumresults.in/S20/1T01118R.pdf': 'Electonics',
#         'http://www.mumresults.in/S20/1T00718.pdf': 'Computer',
#         'http://www.mumresults.in/S20/1T00818R.pdf': 'Electrical',
#         'http://www.mumresults.in/S20/1T00318.pdf': 'Bio medical',
#         'http://www.mumresults.in/S20/1T00628.pdf': 'Civil',
#         'http://www.mumresults.in/S20/1T01428.pdf': 'Mechanical',
#         'http://www.mumresults.in/S20/1T01028.pdf': 'ELECTRONICS AND TELECOMMUNICATION ENGINEERING',
#         'http://www.mumresults.in/S20/1T00728.pdf': 'COMPUTER ENGINEERING',
#         'http://www.mumresults.in/S20/1T01327.pdf': 'INSTRUMENTATION ENGINEERING',
#         'http://www.mumresults.in/S20/1T00227.pdf': 'AUTOMOBILE ENGINEERING',
#     },
#     'mcom': {
#         'http://www.mumresults.in/S20/2C00524.pdf': None
#     },
#     'bcom': {
#         'http://www.mumresults.in/S20/2C00246.pdf': None,
#         'http://www.mumresults.in/S20/2C00146.pdf': None
#     },
#     'bpharma': {
#         'http://www.mumresults.in/S20/1P00138.pdf': None
#     },
#     'bsc': {
#         'http://www.mumresults.in/S20/1S00166A.pdf': 'Bio technology',
#         'http://www.mumresults.in/S20/1S002567.pdf': 'Information Technology',
#         'http://www.mumresults.in/S20/1S00256.pdf': 'Information Technology',
#         'http://www.mumresults.in/S20/1S00226.pdf': 'Information Technology',
#         'http://www.mumresults.in/S20/1S00246.pdf': 'Information Technology',
#         'http://www.mumresults.in/S20/1S00156.pdf': 'Computer science',
#         'http://www.mumresults.in/S20/1S00246A.pdf': 'Information Technology',
#         'http://www.mumresults.in/S20/1S00146.pdf': None,
#         'http://www.mumresults.in/S20/1S001467.pdf': None,
#         'http://www.mumresults.in/S20/1S00136.pdf': None,
#         'http://www.mumresults.in/S20/1S00326HU6.pdf': 'Human Development',
#         'http://www.mumresults.in/S20/1S00326HD.pdf': 'Human Development',
#         'http://www.mumresults.in/S20/1S00426BSH.pdf': 'Hospitality studies',
#         'http://www.mumresults.in/S20/1S00516.pdf': 'Aeronautics',
#         'http://www.mumresults.in/S20/1S00516A.pdf': 'Aeronautics'
#     },
#     'barch': {
#         'http://www.mumresults.in/S20/1A00214.pdf': None,
#         'http://www.mumresults.in/S20/1A00216.pdf': None
#     },
#     'mms': {
#         'http://www.mumresults.in/S20/2M00734.pdf': None
#     },
#     'march': {
#         'http://www.mumresults.in/S20/1A00524.pdf': 'Architectural and Urban Conservation',
#         'http://www.mumresults.in/S20/1A00524A.pdf': 'Architectural and Urban Conservation',
#         'http://www.mumresults.in/S20/1A00724.pdf': 'Project Management'
#     },
#     'bms': {
#         'http://www.mumresults.in/S20/2M00156.pdf': None,
#         'http://www.mumresults.in/S20/2M001567.pdf': None,
#         'http://www.mumresults.in/S20/2M00146.pdf': None,
#         'http://www.mumresults.in/S20/2M00136.pdf': None,
#         'http://www.mumresults.in/S20/2M00146A.pdf': None,
#         'http://www.mumresults.in/S20/COLL.pdf': None
#     },
#     'msc': {
#         'http://www.mumresults.in/S20/1S01414.pdf': 'Forensic science',
#         'http://www.mumresults.in/S20/1S01114.pdf': None,
#         'http://www.mumresults.in/S20/2M00136.pdf': None,
#         'http://www.mumresults.in/S20/1S01212A.pdf': None
#     },
#     'mca': {
#         'http://www.mumresults.in/S20/1T00146.pdf': None,
#         'http://www.mumresults.in/S20/1T00126.pdf': None
#     },
#     'bed': {
#         'http://www.mumresults.in/S20/4E00144.pdf': None
#     }
# }
# url_2019 = {
#     # 'be': {
#     #     'http://www.mumresults.in/S19/1T00318C.pdf': 'Bio-medical engineering',
#     #     'http://www.mumresults.in/S19/1T00318R.pdf': 'Bio-medical engineering',
#     #     'http://www.mumresults.in/S19/1T00317.pdf': 'Bio-medical engineering',
#     #     'http://www.mumresults.in/S19/1T00218C.pdf': 'Automobile engineering',
#     #     'http://www.mumresults.in/S19/1T01317.pdf': 'Instrumentation engineering',
#     # },
#     # 'bsc': {
#     #     'http://www.mumresults.in/S19/1S0025510C.pdf': 'Information Technology',
#     #     'http://www.mumresults.in/S19/1S00255.pdf': 'Information Technology',
#     #     'http://www.mumresults.in/S19/1S00815.pdf': 'Forensic science',
#     #     'http://www.mumresults.in/F19/1S00155A.pdf': 'Computer science',
#     # },
#     # 'bpharma': {
#     #     'http://www.mumresults.in/S19/1P00137.pdf': None
#     # },
#     'med': {
#         'http://www.mumresults.in/S19/4E00732.pdf':None
#     },
# }

url_2018 = {
    ' B.Arch' : {
           'http://www.mumresults.in/F18/T8818.pdf': None
    },
        'be' : {
        'http://www.mumresults.in/F18/T4228.pdf'  : 'CHEMICAL ENGINEERING',
        'http://www.mumresults.in/F18/T4927.pdf'  : 'ELECTRONICS AND TELECOMMUNICATION ENGINEERING',
        'http://www.mumresults.in/F18/T4128.pdf'  : 'BIO-TECHNOLOGY ENGINEERING',
        'http://www.mumresults.in/F18/T5128U.pdf' : 'INFORMATION TECHNOLOGY ENGINEERING',
        'http://www.mumresults.in/F18/T5128L2.pdf' : 'INFORMATION TECHNOLOGY ENGINEERING',
        'http://www.mumresults.in/F18/T5628.pdf' : 'PRODUCTION',
        'http://www.mumresults.in/F18/T2228.pdf' : 'MECHATRONICS ENGINEERING',
    },
        'mca' : {
        'http://www.mumresults.in/F18/T8726.pdf': None
        }


}
pdf_urls = {
    # 2021: url_2021,
    # 2020: url_2020,
    # 2019: url_2019,
     2018: url_2018,
}


def get_splitter(string):
    """
    string: str: data
    return: str: splitter pattern
    """
    result = 0
    patterns = re.findall('[-]+', string)
    if patterns:
        for pattern in patterns:
            if len(pattern) > result:
                result = len(pattern)
    return result - 1


def scrapping(yop, req=None):
    """
    yop: str/int: year of passing
    req: request parameter if available
    """
    ignored_names = ['A O', 'BELOW', 'CGPI', 'PAGE', 'Dyslexia']
    _url = ""
    _br = ""
    temp_filepath = os.path.join(extractors.FileSaveLocation.temp, 'mu.pdf')
    api_urls = pdf_urls.get(yop)
    if not api_urls:
        print('Mumbai University Urls not mentioned')
        creds.send_mail('Error: University Of Mumbai', 'PDF urls not available!!!!')
        return
    if req:
        user = req.user.pk
    else:
        user = req
    try:
        conn = creds.mysql_connect()
        for degree, values in api_urls.items():
            degree_name = degree.upper()
            for url, branch in values.items():
                _url = url
                _br = branch
                res = requests.get(url)
                res = res.content
                with open(temp_filepath, 'wb') as f:
                    f.write(res)
                with open(temp_filepath, 'rb') as f:
                    pdf = PyPDF2.PdfFileReader(f)
                    pages = pdf.numPages
                    for page in range(pages):
                        # if yop == 2021 and degree == 'bms' and url == 'http://www.mumresults.in/F21/2M00156.pdf' and page < 2091:
                        #     continue
                        page_obj = pdf.getPage(page)
                        page_text = page_obj.extractText().replace('\n', '')
                        page_text = page_text.replace('/', '')
                        page_text = re.sub('\s+', ' ', page_text)
                        splitter = get_splitter(page_text)
                        try:
                            page_text_list = page_text.split('-'*splitter)
                        except Exception as e:
                            continue
                        for text in page_text_list:
                            text = re.sub('[^\da-zA-Z\s]', '', text)
                            roll_name = re.findall('([0-9]{7})\s?([a-zA-z\s]+)', text.strip())
                            if not roll_name:
                                roll_name = re.findall('([0-9]{5})\s?([a-zA-z\s]+)', text.strip())
                            if not roll_name:
                                roll_name = re.findall('([0-9]{4,12})\s?([a-zA-z\s]+)', text.strip())
                            if roll_name:
                                for rollname in roll_name:
                                    flag = None
                                    cand_roll = rollname[0].strip()
                                    cand_name = rollname[1].strip()
                                    if cand_name == 0 or cand_name == '0' or cand_name == ' ' or not cand_name:
                                        continue
                                    if len(cand_name) < 3:
                                        print(cand_name)
                                        continue
                                    if cand_name.strip() in ignored_names:
                                        continue
                                    for word in not_words:
                                        if word in cand_name.lower():
                                            flag = True
                                            break
                                    if flag:
                                        continue
                                    # query = creds.get_filter_data(
                                    #     roll_no=cand_roll,
                                    #     board_id=12,
                                    #     name=cand_name,
                                    #     yop=yop
                                    # )
                                    # try:
                                    #     cursor = conn.cursor()
                                    # except:
                                    #     conn = creds.mysql_connect()
                                    #     cursor = conn.cursor()
                                    # cursor.execute(query)
                                    # _res = cursor.fetchall()
                                    # cursor.close()
                                    # if _res:
                                    #     continue
                                    scrap_data = extractors.scrap_mumbai_univ(
                                        roll=cand_roll,
                                        name=cand_name,
                                        degree=degree_name,
                                        temp_filepath=temp_filepath,
                                        yop=yop,
                                        branch=branch
                                    )
                                    if scrap_data['status']:
                                        if user:
                                            scrap_data['created_by_id'] = user
                                        insert_query = "INSERT INTO education (name, degree_name, roll_no, exam_result, website_url, filepath, board_id, created_at, updated_at, year_of_passing, created_by_id, branch_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                        payload = (
                                            scrap_data['name'],
                                            scrap_data['degree_name'],
                                            scrap_data['roll_no'],
                                            scrap_data['exam_result'],
                                            scrap_data['website_url'],
                                            scrap_data['filepath'],
                                            scrap_data['board_id'],
                                            scrap_data['created_at'],
                                            scrap_data['updated_at'],
                                            scrap_data['year_of_passing'],
                                            scrap_data.get('created_by_id'),
                                            scrap_data.get('branch_name')
                                        )
                                        try:
                                            cursor = conn.cursor()
                                        except:
                                            conn = creds.mysql_connect()
                                            cursor = conn.cursor()
                                        cursor.execute(insert_query, payload)
                                        conn.commit()
                                        cursor.close()
        conn.close()
        print("Mumbai University Done")
        creds.send_mail("Mumbai University Scrapping -- Done", "Completed")
        os.remove(temp_filepath)
    except Exception as e:
        creds.send_mail('Error: University Of Mumbai', str(e) + " :: till --> " + f"url: {_url} & {_br}")


if __name__ == '__main__':
    for year in pdf_urls.keys():
        scrapping(year)
