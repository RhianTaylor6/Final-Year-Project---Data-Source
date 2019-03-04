#import libraries
import importlib
import urllib.request
from bs4 import BeautifulSoup
import readFile
import re


useCode = 'https://www.accessdata.fda.gov/scripts/cder/ob/patent_info.cfm?Product_No=001&Appl_No=207589&Appl_type=N'
test = 'https://www.accessdata.fda.gov/scripts/cder/ob/patent_info.cfm?Product_No=006&Appl_No=204242&Appl_type=N'
multiUse = 'https://www.accessdata.fda.gov/scripts/cder/ob/patent_info.cfm?Product_No=001&Appl_No=209501&Appl_type=N'
page_html = urllib.request.urlopen(useCode)

soup = BeautifulSoup(page_html,'html.parser') #soup is the HTML for the web page


use = soup.find_all(class_="tooltiptext")#This is the class that contains the drug infor within the HTML page





useCodes= soup.find_all(text=re.compile('U-'))
numUseCodes= len(soup.find_all(text=re.compile('U-')))



for i in range(numUseCodes):
    print(useCodes[i] + " : " + use[i].text)