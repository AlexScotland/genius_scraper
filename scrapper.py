import sys
import urllib.request as urllib2 
from bs4 import BeautifulSoup
 
def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    text1 = re.sub(clean, '', text)
    return re.sub(r'\[.*?\]','', text1)

 
url = "https://www.azlyrics.com/lyrics/travisscott/sickomode.html"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page,"html.parser")

#Open a txt file and writes data to it 
sys.stdout = open('PageUrl.txt','w')

divs = soup.select("div:nth-of-type(5)")
print(remove_html_tags(str(divs[0])))


 