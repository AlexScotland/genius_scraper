import sys
import urllib.request as urllib2 
from bs4 import BeautifulSoup
 
 
url = "https://www.azlyrics.com/lyrics/sheckwes/mobamba.html"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page,"html.parser")

#Open a txt file and writes data to it 
sys.stdout = open('PageUrl.txt','w')

print(soup.get_text())

