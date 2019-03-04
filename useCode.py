#import libraries
import importlib
import urllib.request
from bs4 import BeautifulSoup
import readFile
import re
import pandas as pd


useCode = 'https://www.accessdata.fda.gov/scripts/cder/ob/patent_info.cfm?Product_No=001&Appl_No=207589&Appl_type=N'
test = 'https://www.accessdata.fda.gov/scripts/cder/ob/patent_info.cfm?Product_No=006&Appl_No=204242&Appl_type=N'
multiUse = 'https://www.accessdata.fda.gov/scripts/cder/ob/patent_info.cfm?Product_No=001&Appl_No=209501&Appl_type=N'



testing = readFile.useSearch().head(1)
prodNo = testing['Product_No'].values[0]
appNo = testing['Appl_No'].values[0]
appType = testing['Appl_Type'].values[0]
constructURL = 'https://www.accessdata.fda.gov/scripts/cder/ob/patent_info.cfm?Product_No={}&Appl_No={}&Appl_type={}'
constructedURL = constructURL.format(prodNo,appNo,appType)
print(constructedURL)
page_html = urllib.request.urlopen(constructedURL)

soup = BeautifulSoup(page_html,'html.parser') #soup is the HTML for the web page

for x in soup.find_all():
    if len(x.text) == 0:
        x.extract()

use = soup.find_all(class_="tooltiptext")#This is the class that contains the drug infor within the HTML page
useCodes= soup.find_all(text=re.compile('U-'))
numUseCodes= len(soup.find_all(text=re.compile('U-')))


#soup.find_all( class_ = 'tooltip')[0].get_text()
#print(soup.find_all( class_ = 'tooltip')[2].find('span',class_='tooltiptext').get_text())


for i in range(numUseCodes):
    print(useCodes[i]+ " : " + use[i].text)
