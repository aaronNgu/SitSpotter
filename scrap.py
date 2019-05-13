from urllib import urlopen
from bs4 import BeautifulSoup as soup
import sys


if (len(sys.argv) != 1):
  print("Invalid Parameter. Too many arguments")
  sys.exit()

URL = "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=PHIL&course=385&section=001"

# handle: different possible HTTPSresponse
page = urlopen(URL)
page_HTML = page.read()
page.close()
# print(page_HTML)
# print(page.info())
# print(page.geturl())
# print(page.getcode())
page_soup = soup(page_HTML, "html.parser")
search_text = "Total Seats Remaining:"
value =  page_soup.find(text=search_text).findNext("strong").text
print("Total Seats Remaing : " + value)
