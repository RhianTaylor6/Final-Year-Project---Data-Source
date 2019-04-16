#import libraries
import importlib
import urllib
from bs4 import BeautifulSoup
import PyPDF2

#import pdfminer

def fixPDF(a):
    #source : https://mail.python.org/pipermail/python-list/2010-November/592460.html
    try:
        fileOpen = open(a, "a")
        fileOpen.writer("%%EOF")
        fileOpen.close
        return "fixed"
    except Exception:
        return "unable to open"

#specify URL
fda_website = "https://www.accessdata.fda.gov/scripts/cder/ob/index.cfm"

#query website and return HTML to variable
page_html = urllib.urlopen(fda_website)

#parse to beautiful soup format to work in it
soup = BeautifulSoup(page_html,'html.parser')

#print(soup.prettify())

#input1 = soup.find(input="drugname")
#print(input1)
url = "https://www.fda.gov/downloads/Drugs/DevelopmentApprovalProcess/UCM071118.pdf"
webFile = urllib.urlopen(url)
pdfFile = open(url.split('/')[-1], 'w')
pdfFile.write(webFile.read())
webFile.close()
#pdfFile.close()

pdfName = pdfFile.name
print(pdfName)
fixPDF(pdfName)

#with open(pdfName, "rb") as infile:
    #source : https://www.reddit.com/r/Python/comments/8pepw9/im_struggling_to_read_text_from_a_pdf_using_the/
   # input1 = PyPDF2.PdfFileReader(infile)
   # print("document1.pdf has %d pages." % input1.getNumPages())


pdfOpen = open('zq008603_Coursework_1_24008603.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfOpen)
print(pdfReader.numPages)

for i in range(pdfReader.numPages):
    page = pdfReader.getPage(i)
    print('Page no - ' + str(1+pdfReader.getPageNumber(page)))
    content = page.extractText()
   # print(content)

