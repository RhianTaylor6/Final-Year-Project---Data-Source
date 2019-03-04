#import libraries
import importlib
import urllib.request
from bs4 import BeautifulSoup
import readFile
import re
import pandas as pd
import numpy as np


def createURL(df):
    constructedURL = []
    for index, row in df.head().iterrows():
        prodNo = row['Product_No']
        appNo = row['Appl_No']
        appType = row['Appl_Type']
        constructURL = 'https://www.accessdata.fda.gov/scripts/cder/ob/patent_info.cfm?Product_No={}&Appl_No={}&Appl_type={}'
        constructedURL.append(constructURL.format(prodNo,appNo,appType))
        print(constructedURL[index])
    return constructedURL


"""
page_html = urllib.request.urlopen()

soup = BeautifulSoup(page_html,'html.parser')

for x in soup.find_all():
    if len(x.text) == 0:
        x.extract()

use = soup.find_all(class_="tooltiptext")
useCodes= soup.find_all(text=re.compile('U-'))
numUseCodes= len(soup.find_all(text=re.compile('U-')))

for i in range(numUseCodes):
    print(useCodes[i]+ " : " + use[i].text)
"""
createURL(readFile.useSearch())