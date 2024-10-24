'''
Simple script to open every submission from the grok marking page HTML file.
Right click page, hit save as, save into same location as this, and run this.
'''
from bs4 import BeautifulSoup
import webbrowser  
  
with open("Grok Academy.html") as fp:
    soup = BeautifulSoup(fp,'lxml') 
 
# remove the string for default browswer
browser = webbrowser.get('chromium')  
for a in soup.findAll('a'): 
    try:  
        if 'href' in a.attrs: 
            url = a.get('href')
            if url.startswith("https://groklearning.com/view-submissions"):
                browser.open(url, new=2, autoraise=False) 
    except Exception: 
        pass
