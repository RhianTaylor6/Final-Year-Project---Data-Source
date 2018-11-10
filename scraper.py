#import libraries
import importlib
import urllib
from bs4 import BeautifulSoup

#specify URL
fda_website = "https://www.accessdata.fda.gov/scripts/cder/ob/index.cfm"

#query website and return HTML to variable
page_html = urllib.urlopen(fda_website)

#parse to beautiful soup format to work in it
soup = BeautifulSoup(page_html,'html.parser')

#print(soup.prettify())

input1 = soup.find(input="drugname")
print(input1)