#import libraries
import importlib
import urllib
from bs4 import BeautifulSoup


cerubidine = 'https://www.accessdata.fda.gov/scripts/cder/ob/results_product.cfm?Appl_Type=A&Appl_No=064103'
jardiance = 'https://www.accessdata.fda.gov/scripts/cder/ob/results_product.cfm?Appl_Type=N&Appl_No=204629'
desferal = 'https://www.accessdata.fda.gov/scripts/cder/ob/results_product.cfm?Appl_Type=N&Appl_No=016267'
page_html = urllib.urlopen(cerubidine)

soup = BeautifulSoup(page_html,'html.parser') #soup is the HTML for the web page

#print(soup.prettify())

drug_info = soup.find(class_="ui-accordion-content ui-helper-reset ui-widget-content ui-corner-bottom" )#This is the class that contains the drug infor within the HTML page
#print(drug_info)

table = drug_info.select("p")#This p contains the actual listed items of indo related to the drug
#print(table)

list1 = (str(table).split('<br/>'))#break up the p based on the <br/> tags so we can itirate through to find approval date
print("LIST1:")
print(len(list1))

for i in range(len(list1)):
    #print(i)
    print(list1[i])
   
list2 = (str(list1).split('<strong>'))
print("LIST2:")
print(len(list2))
for i in range(len(list2)):
    #print(i)
    print(list2[i])

list3 = (str(list2).split('</strong>'))
print("LIST3:")
print(len(list3))
for i in range(len(list3)):
    #print(i)
    print(list3[i])

print(list2[10])

#try and pair items in the list by splitting on </strong>\\, use strip to get rid of \\r\\n  ',', then put the pairs into a dictionary