#import libraries
import importlib
import urllib.request
from bs4 import BeautifulSoup
from readFile import useSearch
import re
import pandas as pd
import numpy as np
import csv

#This module creates a list of URLs for every drug in the FDA drug file then scrapes each website to get the explanation of each use code associated with each drug and stores both things to a CSV
#THIS FILE TAKES A LONG TIME TO RUN DUE TO THE SHEER NUMBER OF WEB PAGES - ONLY RUN IF THE DATA NEEDS UPDATING (ONCE A MONTH PREFERABLY)

def createURL(df):
    constructedURL = []
    
    with open('FDA_Module/urls.csv', mode = 'w') as url_file:
        use_writer = csv.writer(url_file, delimiter=',')
        use_writer.writerow(['Product_No','Appl_No','Appl_Type','URL'])
        for index, row in df.iterrows():
            prodNo = row['Product_No']
            appNo = row['Appl_No']
            appType = row['Appl_Type']
            constructURL = 'https://www.accessdata.fda.gov/scripts/cder/ob/patent_info.cfm?Product_No={}&Appl_No={}&Appl_type={}'
            constructedURL.append(constructURL.format(prodNo,appNo,appType))
            print(index)
            use_writer.writerow([prodNo,appNo,appType,constructedURL[index]])
            
        return constructedURL


def getUse(urlList):

    with open('FDA_Module/uses.csv', mode = 'w') as use_file:
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
                print(urls)
       

url_list = createURL(useSearch())

getUse( url_list)
