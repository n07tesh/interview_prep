# Rajeev Ghandhi Prodhyogiki Vishvavidyalaya
import re
import creds
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from time import sleep
import os

streams = ['be', 'btech', 'mtech', 'mca']
colleges = {
    'be': {
        # '0103':  'Lakshmi Narain College of Technology',
        # '0101':  'University Institute of  Technology',
        # '0104':  'RKDF Institute of Science',
        # '0105':  'Oriental Institute of Science',
        # '0108':  'Samrat Ashok Technological Institute',
        # '0109':  'Sri Satya Sai Institute of Science',
        # '0111':  'Technocrat Institute of Technology',
        # '0112':  'Bansal Institute of Science',
        # '0114':  'Truba Institute of Engg',
        # '0115':  'NRI Institute of Information Science',
        # '0116':  "All Saints' College of Technology",
        # '0121':  'Scope College of Engineering',
        # '0124':  'Bhopal Institute of Technology',
        # '0125':  'Shree Institute of Science',
        # '0126':  'Oriental College of Technology',
        # '0127':  'Bansal College of Engineering',
        # '0128':  'Patel College of Science',
        # '0129':  'Bhabha Engineering Research Institute',
        # '0130':  'Globus Engineering College',
        # '0131':  'J.N. College of Technology',
        # '0132':  'Radha Raman Institute of Technology',
        # '0133':  'Sagar Institute of Research',
        # '0156':  'RKDF College of Engineering',
        # '0157':  'Lakshmi Narain College of Technology',
        # '0158':  'Radharaman Engineering College',
        # '0159':  'Rajeev Gandhi Proudyogiki Mahavidylaya',
        # '0160':  'Swami Vivekanand College of Science',
        # '0161':  'VNS Group of Institutions',
        # '0171':  'Acropolis Institute of Technology',
        # '0172':  "All Saints' College of Engineering",
        # '0173':  'Bansal Institute of Research',
        # '0174':  'Bhopal Institute of Technology',
        # '0176':  'Lakshmi Narain College of Technology Excellence',
        # '0177':  "IES's College of Technology",
        # '0178':  'Jai Narain College of Technology',
        # '0179':  'Millennium Institute of Technology',
        # '0180':  'Mittal Institute of Technology',
        # '0181':  'Patel Institute of Technology',
        # '0182':  "People's College of Research & Technology",
        # '0185':  'Rukmani Devi Institute of Science',
        # '0186':  'Sagar Institute of Research',
        # '0187':  'Sagar Institute of Science',
        # '0188':  'SAM College of Engineering',
        # '0191':  'Technocrats Institute of Technology',
        # '0192':  'Technocrats Institute of Technology',
        # '0198':  'Trinity Institute of Technology',
        # '0199':  'Technocrats Institute of Technology',
        # '0201':  'Jabalpur Engineering College',
        # '0202':  'Guru Ramdas Khalsa Institute of Science',
        # '0203':  'Hitkarni College of Engineering',
        # '0205':  'Shri Ram Institute of Technology',
        '0206':  'Gyan Ganga Institute of Technology',
        '0207':  'Takshshila Institute of Engineering',
        '0208':  'Gyan Ganga College of Technology',
        '0213':  'Shri Ram Institute of Science',
        '0214':  'Vindhya Institute of Technology',
        '0215':  'Laxmi Bai Sahuji Institute of Engineering',
        '0216':  'SGBM Institute of Technology',
        '0217':  'Lakshmi Narain College of Technology',
        '0219':  'Saraswati Institute of Engineering',
        '0220':  'Oriental Institute of Science',
        '0221':  'Sardar Patel College of Technology',
        '0223':  'St. Aloysius Institute of Technology',
        '0224':  'Radhaswami Institute of Technology',
        '0225':  'Faculty of Engg',
        '0227':  'Prakash Institute of Engg',
        '0228':  'Shri Ram Group of Institutions',
        '0236':  'Annie Institute of Technology and Research Centre',
        '0301':  'Rewa Engineering College',
        '0302':  'Vindhya Institute of Technology',
        '0303':  'Rewa Institute of Technology',
        '0306':  'Jawaharlal Nehru College of Technology',
        '0307':  'Aditya College of Technology',
        '0308':  'UIT Shahdol',
        '0501':  'Sagar Institute of Research',
        '0502':  'Corporate Institute of Science',
        '0503':  'IASSCOM Fortune Institute of Technology',
        '0505':  'Kailash Narayan Patidar College of Science',
        '0506':  'Bansal Institute of Research',
        '0508':  'Surabhi College of Engineering',
        '0509':  'Patel Institute of Engineering',
        '0510':  'Laxmipati Institute of Science',
        '0511':  'NRI Institute of Research',
        '0525':  'Bagula Mukhi College of Technology',
        '0526':  'IES Institute of Technology and Management',
        '0527':  'RKDF College of Technology',
        '0529':  'Mansarover Institute of Science',
        '0530':  'Madhav Proudyogiki Mahavidyalaya',
        '0531':  'Vidhyapeeth Institute of Science',
        '0532':  'Sha-Shib College of Technology',
        '0533':  'Truba College of Science',
        '0534':  'Maxim Institute of Technology',
        '0535':  'Girdhar Siksha Evam Samaj Kalyan Samiti Group of Inst',
        '0536':  'Sagar Institute of Science Technology',
        '0537':  'Sagar Institute of Science',
        '0538':  'Kopal Institute of Science',
        '0539':  'Bhopal Institute of Technology',
        '0540':  'Millennium Institute of Technology',
        '0541':  'Shri Ram College of Technology',
        '0542':  'Satyam Edu. & Social Welfare Society Group of Instt.',
        '0543':  'Malhotra Technical Research Institute',
        '0544':  'AISECT Institute of Science',
        '0545':  'Shri Balaji Institute of Technology',
        '0546':  'Vaishnavi Inst',
        '0548':  'Sparta Institute of Tech',
        '0552':  'Corporate Institute of Research',
        '0553':  'H.L. Agrawal College of Engineering',
        '0601':  'I G Engineering College',
        '0607':  'Ojaswini Institute of Management',
        '0608':  'Babulal Tarabai Research',
        '0610':  'Infinity Management',
        '0612':  'Adina Institute of Science',
        '0613':  'Gyan Sagar College of Engineering',
        '0614':  'Pt.Devprabhakar Shastri College of Tech.',
        '0616':  'Engineering College Nowgong',
        '0701':  'Ujjain Engineering College',
        '0702':  'Mandsaur Institute of Technology',
        '0704':  'Mahakal Institute of Technology',
        '0712':  'Mahakal Institute of Technology',
        '0713':  'Alpine Institute of Technology',
        '0714':  'Mahakal Institute of Technology',
        '0715':  'Prashanti Institute of Technology',
        '0716':  'Late Ramoti Devi Institute of Engineering',
        '0717':  'Synergy Institute of Technology',
        '0718':  'Shri Yogindra Sagar Institute of Technology',
        '0722':  'Shri Guru Sandipani Institute of Technology',
        '0723':  'Srajan Institute of Technology Management',
        '0725':  'New-Tech Institute  of Engineering Science',
        '0801':  'SHRI G',
        '0802':  'Shri Vaishnav Institute  of  Technology',
        '0805':  'Jawaharlal Institute of Technology',
        '0808':  'Institute of Engineering',
        '0812':  'Medicap Institute of Technology',
        '0817':  'Lakshmi Narain College of Technology and Science',
        '0818':  'Indore Institute of Science',
        '0819':  'Central India Institute of Technology',
        '0820':  'Lakshmi Narain College of Technology',
        '0821':  'Malwa Institute of Technology',
        '0822':  'Swami Vivekanand College of Engineering',
        '0823':  'Sri Dadaji Institute of Technology',
        '0827':  'Acropolis Institute of Technology',
        '0828':  'Patel College of Science',
        '0829':  'Sushila Devi Bansal College of Technology',
        '0830':  'Sagar Institute of Research',
        '0831':  'Astral Institute of Technology',
        '0832':  'CHAMELI DEVI GROUP OF INSTITUTIONS',
        '0834':  'Sushila Devi Bansal College of Engineering',
        '0835':  'LNCT',
        '0837':  'Sanghvi Institute of Management',
        '0838':  'Techno Engineering College Indore',
        '0839':  'Vindhya Institute of Technology',
        '0850':  'B M College of Technology',
        '0852':  'Mathura Devi Institute of Technology',
        '0853':  'Oriental Institute of Science',
        '0854':  'Priyatam Institute of Technology',
        '0855':  'RKDF School of Engineering',
        '0856':  'Shiv Kumar Singh Institute of Technology',
        '0857':  'Star Academy of Technology',
        '0858':  'Vikrant Institute of Technology',
        '0861':  'Sanghvi Institute of Engineering',
        '0862':  'Malwa Institute of Science',
        '0863':  'Prestige Institute of Engineering Management',
        '0870':  'Global Institute of Engineering',
        '0872':  'Nalin Institute of Technology',
        '0873':  'Sri Aurobindo Institute of Technology',
        '0874':  'Indore Institute of Science',
        '0875':  'Shivajirao Kadam Institute of Technology and Management - Technical Campus',
        '0876':  'Medi-Caps Institute of Science',
        '0880':  'Mandsaur Inst',
        '0881':  'Sardar Patel Inst',
        '0882':  'Shreejee Inst',
        '0884':  'THAKUR SHIVKUMAR SINGH MEMORIAL ENGINEERING COLLEGE',
        '0885':  'Vidyasagar Institute of Technology',
        '0886':  'Sri Parashuram Institute of Technology and Research',
        '0887':  'UIT JHABUA',
        '0901':  'Madhav Institute of Technology',
        '0902':  'Rustam Ji Institute  of Technology',
        '0903':  'Maharana Pratap College of Technology',
        '0904':  'Shri Ram College of Engineering',
        '0905':  'Institute of Technology',
        '0913':  'Shri Rawatpura Sarkar Institute of Technology',
        '0915':  'Institute of Information Technology',
        '0916':  'Gwalior Engineering College',
        '0917':  'Nagaji Institute of Technology',
        '0928':  'IPS College of Technology',
        '0929':  'Shri Ram Institute of Information Technology',
        '0932':  'Gwalior Institute of Information Technology',
        '0934':  'Nagaji Institute of Technology',
        '0936':  'Vikrant Institute of Technology',
        '0937':  'NRI College of Engineering',
        '0938':  'IMT Group of Institutions',
        '0939':  'Malwa Institute of Technology',
        '0940':  'Lakshmi Narain College of Technology',
        '0946':  'Hindustan Inst',
        '0947':  'Integral Institute of Information Technology',
        '0953':  'Bethesda Institute of Technology',
        '0954':  'SAKSHI INSTITUTE OF TECHNOLOGY',
    },
    'mca': {
        '0101':  'University Institute of  Technology',
        '0103':  'Lakshmi Narain College of Technology',
        '0104':  'RKDF Institute of Science',
        '0105':  'Oriental Institute of Science',
        '0107':  'Govt. Geetanjali Girls College',
        '0108':  'Samrat Ashok Technological Institute',
        '0109':  'Sri Satya Sai Institute of Science',
        '0111':  'Technocrat Institute of Technology',
        '0112':  'Bansal Institute of Science',
        '0115':  'NRI Institute of Information Science',
        '0116':  'All Saints College of Technology',
        '0117':  'Maharishi Centre For Educational Excellence',
        '0118':  'Institute of Professional Education',
        '0121':  'Scope College of Engineering',
        '0126':  'Oriental College of Technology',
        '0128':  'Patel College of Science',
        '0129':  'Bhabha Engineering Research Institute',
        '0133':  'Sagar Institute of Research',
        '0156':  'RKDF College of Engineering',
        '0157':  'Lakshmi Narain College of Technology',
        '0163':  'Technocrat Institute of Technology',
        '0167':  'Oriental Institute of Science',
        '0168':  "People's Institute of Management & Research",
        '0173':  'Bansal Institute of Research',
        '0188':  'SAM College of Engineering',
        '0191':  'Technocrats Institute of Technology',
        '0192':  'Technocrats Institute of Technology',
        '0194':  'Technocrats Institute of Technology',
        '0196':  'Oriental College of Management',
        '0199':  'Technocrats Institute of Technology',
        '0201':  'Jabalpur Engineering College',
        '0202':  'Guru Ramdas Khalsa Institute of Science',
        '0203':  'Hitkarni College of Engineering',
        '0205':  'Shri Ram Institute of Technology',
        '0206':  'Gyan Ganga Institute of Technology',
        '0208':  'Gyan Ganga College of Technology',
        '0210':  'Shri Ram Institute of Technology',
        '0222':  'Shri Ram Institute of Management',
        '0223':  'St. Aloysius Institute of Technology',
        '0230':  'Shri Ram Group of Institutions',
        '0235':  'Guru Ramdas Khalsa Institute of Science',
        '0302':  'Vindhya Institute of Technology',
        '0303':  'Rewa Institute of Technology',
        '0306':  'Jawaharlal Nehru College of Technology',
        '0550':  'Bansal Institute of Science',
        '0551':  'Bhabha Engineering Research Institute',
        '0608':  'Babulal Tarabai Research',
        '0702':  'Mandsaur Institute of Technology',
        '0705':  'Shri Sai Institute of Technology',
        '0709':  'Prestige Institute of Management',
        '0712':  'Mahakal Institute of Technology',
        '0724':  'Gyanodaya Institute of Professional Studies Neemuch',
        '0801':  'SHRI G.S. INSTITUTE OF TECHNOLOGY & SCIENCE',
        '0802':  'Shri Vaishnav Institute  of  Technology',
        '0803':  'Maharaja Ranjit Singh Group of Institutions',
        '0805':  'Jawaharlal Institute of Technology',
        '0807':  'Shri Vaishnav Institute of Management',
        '0808':  'Institute of Engineering',
        '0810':  'School of Computer Application',
        '0814':  'Pioneer Institute of Professional Studies',
        '0815':  'SHRI RAOJIBHAI GOKALBHAI PATEL GUJARATI PROFESSIONAL INSTITUTE',
        '0817':  'Lakshmi Narain College of Technology and Science',
        '0818':  'Indore Institute of Science',
        '0819':  'Central India Institute of Technology',
        '0820':  'Lakshmi Narain College of Technology',
        '0821':  'Malwa Institute of Technology',
        '0822':  'Swami Vivekanand College of Engineering',
        '0823':  'Sri Dadaji Institute of Technology',
        '0827':  'Acropolis Institute of Technology',
        '0829':  'Sushila Devi Bansal College of Technology',
        '0834':  'Sushila Devi Bansal College of Engineering',
        '0835':  'LNCT (Bhopal) Indore Campus',
        '0837':  'Sanghvi Institute of Management',
        '0838':  'Techno Engineering College Indore',
        '0852':  'Mathura Devi Institute of Technology',
        '0853':  'Oriental Institute of Science',
        '0855':  'RKDF School of Engineering',
        '0859':  'Sanghvi Institute of Management',
        '0871':  'Indore Institute of Computer Application',
        '0901':  'Madhav Institute of Technology',
        '0902':  'Rustam Ji Institute  of Technology',
        '0903':  'Maharana Pratap College of Technology',
        '0905':  'Institute of Technology',
        '0906':  'Boston College for Professional Studies',
        '0907':  'Prestige Institute of Management',
        '0915':  'Institute of Information Technology',
        '0917':  'Nagaji Institute of Technology',
        '0926':  'Institute of Technology',
        '0951':  'Divine International Group of Institution'
    },
    'btech': {
        '0967': 'SHIVPURI INSTITUTE OF TECHNOLOGY',
    },
    'mtech': {
        '0002':  'School of Information Technology',
        '0003':  'School of Energy',
        '0004':  'School of Bio-Technology',
        '0005':  'School of Nanotechnology',
        '0012':  'National Institute of Technical Teacher',
        '0101':  'University Institute of  Technology',
        '0103':  'Lakshmi Narain College of Technology',
        '0104':  'RKDF Institute of Science',
        '0105':  'Oriental Institute of Science',
        '0108':  'Samrat Ashok Technological Institute',
        '0109':  'Sri Satya Sai Institute of Science',
        '0111':  'Technocrat Institute of Technology',
        '0112':  'Bansal Institute of Science',
        '0114':  'Truba Institute of Engg.',
        '0115':  'NRI Institute of Information Science',
        '0116':  'All Saints',
        '0121':  'Scope College of Engineering',
        '0124':  'Bhopal Institute of Technology',
        '0125':  'Shree Institute of Science',
        '0126':  'Oriental College of Technology',
        '0128':  'Patel College of Science',
        '0129':  'Bhabha Engineering Research Institute',
        '0131':  'J.N. College of Technology',
        '0132':  'Radha Raman Institute of Technology',
        '0133':  'Sagar Institute of Research',
        '0156':  'RKDF College of Engineering',
        '0157':  'Lakshmi Narain College of Technology',
        '0158':  'Radharaman Engineering College',
        '0159':  'Rajeev Gandhi Proudyogiki Mahavidylaya',
        '0160':  'Swami Vivekanand College of Science',
        '0161':  'VNS Group of Institutions',
        '0171':  'Acropolis Institute of Technology',
        '0172':  'All Saints',
        '0173':  'Bansal Institute of Research',
        '0174':  'Bhopal Institute of Technology',
        '0176':  'Lakshmi Narain College of Technology Excellence',
        '0177':  'IES',
        '0179':  'Millennium Institute of Technology',
        '0180':  'Mittal Institute of Technology',
        '0181':  'Patel Institute of Technology',
        '0185':  'Rukmani Devi Institute of Science',
        '0186':  'Sagar Institute of Research',
        '0187':  'Sagar Institute of Science',
        '0188':  'SAM College of Engineering',
        '0191':  'Technocrats Institute of Technology',
        '0192':  'Technocrats Institute of Technology',
        '0198':  'Trinity Institute of Technology',
        '0199':  'Technocrats Institute of Technology',
        '0201': 'Jabalpur Engineering College',
        '0202': 'Guru Ramdas Khalsa Institute of Science',
        '0205':  'Shri Ram Institute of Technology',
        '0206':  'Gyan Ganga Institute of Technology',
        '0207':  'Takshshila Institute of Engineering',
        '0208':  'Gyan Ganga College of Technology',
        '0213':  'Shri Ram Institute of Science',
        '0214':  'Vindhya Institute of Technology',
        '0217':  'Lakshmi Narain College of Technology',
        '0219':  'Saraswati Institute of Engineering',
        '0225':  'Faculty of Engg. Global Nature Care Sangathan Group of Instt.',
        '0228':  'Shri Ram Group of Institutions',
        '0232':  'Shri Ram Group of Institutions',
        '0302':  'Vindhya Institute of Technology',
        '0303':  'Rewa Institute of Technology',
        '0306':  'Jawaharlal Nehru College of Technology',
        '0307':  'Aditya College of Technology',
        '0501':  'Sagar Institute of Research',
        '0502':  'Corporate Institute of Science',
        '0503':  'IASSCOM Fortune Institute of Technology',
        '0505':  'Kailash Narayan Patidar College of Science',
        '0508':  'Surabhi College of Engineering',
        '0509':  'Patel Institute of Engineering',
        '0511':  'NRI Institute of Research',
        '0525':  'Bagula Mukhi College of Technology',
        '0526':  'IES Institute of Technology and Management',
        '0527':  'RKDF College of Technology',
        '0529':  'Mansarover Institute of Science',
        '0530':  'Madhav Proudyogiki Mahavidyalaya',
        '0531':  'Vidhyapeeth Institute of Science',
        '0533':  'Truba College of Science',
        '0534':  'Maxim Institute of Technology',
        '0536':  'Sagar Institute of Science Technology',
        '0537':  'Sagar Institute of Science',
        '0538':  'Kopal Institute of Science',
        '0540':  'Millennium Institute of Technology',
        '0542':  'Satyam Edu.',
        '0543':  'Malhotra Technical Research Institute',
        '0545':  'Shri Balaji Institute of Technology',
        '0546':  'Vaishnavi Inst. of Tech.',
        '0607':  'Ojaswini Institute of Management',
        '0608':  'Babulal Tarabai Research',
        '0610':  'Infinity Management',
        '0612':  'Adina Institute of Science',
        '0701':  'Ujjain Engineering College',
        '0702':  'Mandsaur Institute of Technology',
        '0704':  'Mahakal Institute of Technology',
        '0713':  'Alpine Institute of Technology',
        '0714':  'Mahakal Institute of Technology',
        '0715':  'Prashanti Institute of Technology',
        '0801':  'SHRI G.S. INSTITUTE OF TECHNOLOGY',
        '0802':  'Shri Vaishnav Institute  of  Technology',
        '0805':  'Jawaharlal Institute of Technology',
        '0808':  'Institute of Engineering',
        '0812':  'Medicap Institute of Technology',
        '0817':  'Lakshmi Narain College of Technology and Science (RIT)',
        '0818':  'Indore Institute of Science',
        '0819':  'Central India Institute of Technology',
        '0820':  'Lakshmi Narain College of Technology',
        '0821':  'Malwa Institute of Technology',
        '0822':  'Swami Vivekanand College of Engineering',
        '0823':  'Sri Dadaji Institute of Technology',
        '0827':  'Acropolis Institute of Technology',
        '0828':  'Patel College of Science',
        '0829':  'Sushila Devi Bansal College of Technology',
        '0830':  'Sagar Institute of Research',
        '0831':  'Astral Institute of Technology',
        '0832':  'CHAMELI DEVI GROUP OF INSTITUTIONS',
        '0834':  'Sushila Devi Bansal College of Engineering',
        '0835':  'LNCT (Bhopal) Indore Campus',
        '0837':  'Sanghvi Institute of Management',
        '0839':  'Vindhya Institute of Technology',
        '0850':  'B M College of Technology',
        '0855':  'RKDF School of Engineering',
        '0856':  'Shiv Kumar Singh Institute of Technology',
        '0858':  'Vikrant Institute of Technology',
        '0861':  'Sanghvi Institute of Engineering',
        '0862':  'Malwa Institute of Science',
        '0863':  'Prestige Institute of Engineering Management',
        '0873':  'Sri Aurobindo Institute of Technology',
        '0874':  'Indore Institute of Science',
        '0875':  'Shivajirao Kadam Institute of Technology and Management - Technical Campus',
        '0876':  'Medi-Caps Institute of Science',
        '0901':  'Madhav Institute of Technology',
        '0902':  'Rustam Ji Institute  of Technology',
        '0903':  'Maharana Pratap College of Technology',
        '0904':  'Shri Ram College of Engineering',
        '0905':  'Institute of Technology',
        '0915':  'Institute of Information Technology',
        '0917':  'Nagaji Institute of Technology',
        '0928':  'IPS College of Technology',
        '0934':  'Nagaji Institute of Technology',
        '0936':  'Vikrant Institute of Technology'
    }
}
branches = {
    'btech': ['CS', 'ME', 'CE', 'EC', 'CM', 'IT', 'EE', 'EX', 'AU', 'MI', 'EI'],
    'be': ['CS', 'ME', 'CE', 'EC', 'CM', 'IT', 'EE', 'EX', 'AU', 'MI', 'EI'],
    'mtech': ['CS', 'ME', 'CE', 'EC', 'CM', 'IT', 'EE', 'EX', 'AU', 'MI', 'EI'],
    'mca': ['CA'],
    # 'mtech': ['AU', 'ME', 'IP', 'CE', 'IEM', 'TX', 'EC', 'CM', 'CS', 'IT', 'EE', 'EX', 'EI', 'FT', 'AT', 'MI', 'BT', 'BM'],
    # 'me': ['AU', 'ME', 'IP', 'CE', 'IEM', 'TX', 'EC', 'CM', 'CS', 'IT', 'EE', 'EX', 'EI', 'FT', 'AT', 'MI', 'BT', 'BM'],
    # 'be': ['CS', 'ME', 'IP', 'CE', 'IEM', 'TX', 'EC', 'CM', 'AU', 'IT', 'EE', 'EX', 'EI', 'FT', 'AT', 'MI', 'BT', 'BM']
}
durations = {
    'btech': 4,
    'be': 4,
    'mtech': 2,
    'me': 2,
    'mca': 3
}
ids = {
    'be': 'radlstProgram_1',
    'btech': 'radlstProgram_1',
    'me': 'radlstProgram_8',
    'mtech': 'radlstProgram_8',
    'mca': 'radlstProgram_2'
}


class FileSaveLocationNew:
    if os.name == 'nt':
        rgpv = r"D:\saved_files"
    else:
        rgpv = '/new_education_data/rajeev_gandhi_vishwavidyalaya'


def roll_generator(clg_code, br_code, yoa, stream_name, count):
    stream_code = ""
    count = f"0{count}" if count < 10 else str(count)
    if stream_name == 'be' or stream_name == 'btech' or stream_name == 'mca':
        stream_code = '10'
    elif stream_name == 'mtech':
        stream_code = 'MT'
    elif stream_name == 'me':
        stream_code = 'ME'
    roll = f"{clg_code}{br_code}{yoa}{stream_code}{count}"
    return roll


def get_pagesource(roll, stream):
    driver = None
    semester = ''
    if stream == 'be' or stream == 'btech':
        semester = '8'
    elif stream == 'me' or stream == 'mtech':
        semester = '4'
    elif stream == 'mca':
        semester = '6'
    captcha_path = os.path.join(creds.RgpvCreds.captcha_path, creds.RgpvCreds.raw_captcha_name)
    url = creds.RgpvCreds.url
    while True:
        try:
            driver = creds.web_driver()
            driver.get(url)
            # sleep(1)
            driver.find_element_by_id(ids[stream]).click()
            driver.save_screenshot(captcha_path)
            captcha = creds.rgpv_image_to_text().upper().strip()
            roll_entry = driver.find_element_by_id(creds.RgpvCreds.enter_roll_id)
            roll_entry.clear()
            roll_entry.send_keys(roll)
            options = Select(driver.find_element_by_id(creds.RgpvCreds.select_semester_id))
            options.select_by_visible_text(semester)
            captcha_entry = driver.find_element_by_id(creds.RgpvCreds.enter_captcha_id)
            captcha_entry.clear()
            captcha_entry.send_keys(captcha)
            sleep(4)
            driver.find_element_by_id(creds.RgpvCreds.view_result_id).click()
            try:
                alert = driver.switch_to.alert
                alert_text = alert.text
                alert.accept()
                if 'wrong' in alert_text.lower():
                    driver.get(url)
                    driver.find_element_by_id(ids[stream]).click()
                    driver.close()
                    continue
                driver.close()
                return None
            except Exception as e:
                pagesource = driver.page_source
                driver.close()
                return pagesource
        except Exception as e:
            try:
                driver.close()
            except:
                pass
            sleep(60)
            try:
                driver = creds.web_driver()
                driver.get(url)
                driver.find_element_by_id(ids[stream]).click()
            except Exception as e:
                pass


def scrapping(pagesource, college_name):
    result = dict()
    result['status'] = False
    result['board'] = 'rajiv gandhi proudyogiki vishwavidyalaya'
    try:
        soup = BeautifulSoup(pagesource, 'html.parser')
        rows = soup.find_all('table')[3].find('tbody').find_all('tr')[1:]
        personal_info = rows[0].find('table').find('tbody').find_all('tr')
        result_info = rows[13].find('table').find('tbody').find_all('tr')[-1]
        for i, personal in enumerate(personal_info):
            if i == 0:
                temp = re.search('([0-9]+)', personal.text)
                if temp:
                    result['year_of_passing'] = temp.group(1)
            else:
                temp = personal.find_all('td')
                temp1 = temp[0].text.lower()
                temp2 = temp[1].text.replace('\n', '').strip()
                temp3 = temp[2].text.lower()
                temp4 = temp[3].text.replace('\n', '').strip()
                if 'name' in temp1:
                    result['name'] = temp2
                elif 'course' in temp1:
                    result['degree_name'] = temp2
                if 'roll' in temp3:
                    result['roll_no'] = temp4
                elif 'branch' in temp3:
                    result['branch_name'] = temp4
        result['exam_result'] = re.sub('[^a-zA-Z0-9_\s]', '', result_info.text.replace('\n', '').strip())
        result['board_id'] = 19
        result['website_url'] = creds.RgpvCreds.url
        result['created_at'] = creds.get_current_dt()
        result['updated_at'] = creds.get_current_dt()
        result['college_name'] = college_name
        filename = f'{"_".join(result["board"].replace(",", "").split())}_' + '_'.join(result['degree_name'].replace('.', '').split())
        filepath = creds.filename_generator(result['roll_no'], filename, yop=result['year_of_passing'])
        filepath = os.path.join(FileSaveLocationNew.rgpv, filepath)
        with open(filepath, 'w', encoding="utf-8") as f:
            f.write(pagesource)
        result['filepath'] = filepath
        result['status'] = True
    except Exception as e:
        result['status'] = False
    finally:
        return result


def scrap_rgpv(yop):
    roll = ""
    try:
        for stream in streams:
            college = colleges[stream]
            branch = branches[stream]
            duration = durations[stream]
            for college_code, college_name in college.items():
                for branch_code in branch:
                    if stream == 'be' and college_code == '0206' and branch_code in ['CS']:  # , 'AU', 'IT', 'EE', 'EX', 'EI', 'MI', 'EC'
                        continue
                    thresh = 0
                    yoa = str(yop - duration)[-2:]
                    for i in range(1, 100):
                        if stream == 'be' and college_code == '0206' and branch_code == 'ME' and i <= 20:
                            continue
                        roll = roll_generator(college_code, branch_code, yoa, stream, i)
                        # roll = '0905CS171092'  # testing purpose
                        page_source = get_pagesource(roll, stream)
                        if not page_source:
                            if thresh >= 10:
                                break
                            thresh += 1
                            continue
                        scrap_data = scrapping(page_source, college_name)
                        if not scrap_data['status']:
                            if thresh >= 10:
                                break
                            thresh += 1
                            continue
                        creds.update_records_to_db(validate=False, **scrap_data)
        creds.send_mail('RGPV', 'Completed')
    except Exception as e:
        creds.send_mail(f'Error:: RGPV@{roll}', str(e))


if __name__ == '__main__':
    scrap_rgpv(2021)
