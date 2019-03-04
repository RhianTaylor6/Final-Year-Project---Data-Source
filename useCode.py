#import libraries
import importlib
import urllib.request
from bs4 import BeautifulSoup
import readFile
import re
import pandas as pd


def createURL(df):
    rows = df.count
    
    prodNo = df['Product_No'].values[0]
    appNo = df['Appl_No'].values[0]
    appType = df['Appl_Type'].values[0]
    constructURL = 'https://www.accessdata.fda.gov/scripts/cder/ob/patent_info.cfm?Product_No={}&Appl_No={}&Appl_type={}'
    constructedURL = constructURL.format(prodNo,appNo,appType)
    return constructedURL



page_html = urllib.request.urlopen(createURL(readFile.useSearch()))

soup = BeautifulSoup(page_html,'html.parser')

for x in soup.find_all():
    if len(x.text) == 0:
        x.extract()

use = soup.find_all(class_="tooltiptext")
useCodes= soup.find_all(text=re.compile('U-'))
numUseCodes= len(soup.find_all(text=re.compile('U-')))

for i in range(numUseCodes):
    print(useCodes[i]+ " : " + use[i].text)

