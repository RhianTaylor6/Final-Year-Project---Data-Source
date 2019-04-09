#import libraries
import importlib
import urllib.request
from bs4 import BeautifulSoup
from use_mining import therapydf
import re
import pandas as pd
import numpy as np
import csv


def createURL(df):
    constructedURL = []
    with open('FDA_Module/therapyurls.csv', mode = 'w') as url_file:
        use_writer = csv.writer(url_file, delimiter=',')
        use_writer.writerow(['Therapy_area','URL'])
        for index, row in df.iterrows():
            URL = row['Link']
            constructURL = 'https://www.centerwatch.com{}'
            constructedURL.append(constructURL.format(URL))
            use_writer.writerow([row['Therapy_area'],constructedURL[index]])
        return constructedURL


def getUse(urlList):

    with open('FDA_Module/therapydrugs.csv', mode = 'w') as use_file:
        use_writer = csv.writer(use_file, delimiter=',')
        use_writer.writerow(['URL','Drug'])
        for urls in range(len(urlList)):
            
            page_html = urllib.request.urlopen(urlList[urls])
            soup = BeautifulSoup(page_html,'html.parser')
            '''
            for item in soup.find_all('h3'):
                if not "Drugs Approved in" in item.text:continue
                p_tag = item.find_next_sibling('p')
                for drug in p_tag.find_all('a'):
                    print(drug.text)
                        #print(urlList[urls])
                    use_writer.writerow([urlList[urls],drug.text])'''
            
            for section in soup.find_all('h3'):
                nextNode = section
                while True:
                    nextNode = nextNode.find_next_sibling()
                    if nextNode and nextNode.name == 'p':
                        print(nextNode.text)
                        use_writer.writerow([urlList[urls],nextNode.text])
                    else:
                        break
                
       

urls = createURL(therapydf())

getUse(urls)