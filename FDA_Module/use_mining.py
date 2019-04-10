import importlib
import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
import csv

#This module returns a dataframe containg a URL for the page of each general therapy area which lists the drugs approved by the FDA in that category to pass to therapy_area.py
dtype_dic = {' Use Code': str,
             'Use': str,
             'Appl_No': str,
             'Product_No': str,
             'Type' : str,
             'Patent_No' : str
             }
             

usedf = pd.read_csv("FDA_Module/uses_list.csv", dtype=dtype_dic)
fdadf = pd.read_csv("FDA_Module/fda.csv", dtype=dtype_dic)
fdadf = fdadf.drop_duplicates()

uses = usedf['Use'] #convert from df to series
trying = uses.str.contains("PSORIASIS")

page_html = urllib.request.urlopen("https://www.centerwatch.com/drug-information/fda-approved-drugs/therapeutic-areas")
soup = BeautifulSoup(page_html,'html.parser')
links = []
therapy_area = []
h1 = soup.find('h1')
ul = h1.find_next_sibling('ul')
for link in ul.find_all('a'):
    links.append(link.get('href'))
    therapy_area.append(link.text)



def therapydf():
    therapydf = pd.DataFrame({'Therapy_area' : therapy_area, 'Link': links})
    return therapydf

