#import libraries
import importlib
import urllib.request
from bs4 import BeautifulSoup
import readFile
import re
import pandas as pd
import numpy as np
import csv


def createURL(df):
    constructedURL = []
    for index, row in df.iterrows():
        prodNo = row['Product_No']
        appNo = row['Appl_No']
        appType = row['Appl_Type']
        constructURL = 'https://www.accessdata.fda.gov/scripts/cder/ob/patent_info.cfm?Product_No={}&Appl_No={}&Appl_type={}'
        constructedURL.append(constructURL.format(prodNo,appNo,appType))
        #print(constructedURL[index])
    return constructedURL


def getUse(urlList):

    with open('uses.csv', mode = 'w') as use_file:
        use_writer = csv.writer(use_file, delimiter=',')
        use_writer.writerow(['URL',' Use Code','Use'])
        for urls in range(len(urlList)):
            #print("\n"+urlList[urls]+"\n")
            page_html = urllib.request.urlopen(urlList[urls])

            soup = BeautifulSoup(page_html,'html.parser')

            for x in soup.find_all():
                if len(x.text) == 0:
                    x.extract()

            use = soup.find_all(class_="tooltiptext")
            useCodes= soup.find_all(text=re.compile('U-'))
            numUseCodes= len(soup.find_all(text=re.compile('U-')))

            for codes in range(numUseCodes):
                #print(useCodes[codes]+ " : " + use[codes].text)
                use_writer.writerow([urlList[urls],useCodes[codes],use[codes].text])
            
    
    



    
        

url_list = createURL(readFile.useSearch())

getUse( url_list)
df = readFile.useSearch()
df['URL']=url_list

