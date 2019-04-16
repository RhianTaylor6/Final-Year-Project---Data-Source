import importlib
import urllib.request
from bs4 import BeautifulSoup
from lxml import etree
import setuptools
import re
import numpy as np
from subprocess import call
import pytz #timezones

#This module gets the zip file containing the majority of the drug data from the FDA website, downloads it and unzips it and stores it in the project.
#The file is updated monthly so to be up to date the files should be re-downloaded every month.

def get_link_from_fda():
    fdaSite = 'https://www.fda.gov/Drugs/InformationOnDrugs/ucm129662.htm'
    #the file is under additional resources, Orange Book Data files
    page_html = urllib.request.urlopen(fdaSite) #needed to add the .request. to make it work for python3
    soup = BeautifulSoup(page_html, 'html.parser')

    soupStr = soup.find_all('a')

    for link in soupStr:
        #print(str(link.get('href')))
        if "Orange Book Data Files (compressed)" in str(link): #checking each a tag for the target file
            return str('https://www.fda.gov' + str(link).split('"')[1])

call(['rm','-r','tmpfda*']) #removing any files starting with with tmpfda so we don't have multiple copies
urllib.request.urlretrieve(get_link_from_fda(),"tmpfda.zip")# retrieveing the file, 
call(['unzip', 'tmpfda.zip', '-d', 'tmpfdazip'])#unzipping the new copy








        
  



