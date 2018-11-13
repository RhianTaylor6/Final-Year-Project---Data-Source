import importlib
import urllib
from bs4 import BeautifulSoup

fdaSite = 'https://www.fda.gov/Drugs/InformationOnDrugs/ucm129662.htm'
#the file is under additional resources, Orange Book Data files
page_html = urllib.urlopen(fdaSite)
soup = BeautifulSoup(page_html, 'html.parser')

#for link in soup.find_all('a'):
    #print(link.get('href'))

for i in soup.find_all('li'):
    #need an if li contains Orange Book Data files then print i
    print(i)



