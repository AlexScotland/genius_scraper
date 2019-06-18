import sys
import urllib.request as urllib2 
from bs4 import BeautifulSoup
 
def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    text1 = re.sub(clean, '', text)
    return re.sub(r'\[.*?\]','', text1)

# Open a txt file and writes data to it 
sys.stdout = open('output.txt','w')

# List of links of lyrics on AZLYRICS

urls = ["https://www.azlyrics.com/lyrics/travisscott/sickomode.html","https://www.azlyrics.com/lyrics/sheckwes/mobamba.html"]
for url in urls:
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page,"html.parser")

    divs = soup.select("div:nth-of-type(5)")
    print(remove_html_tags(str(divs[0])))


 