'''
Simple script to open every submission from the grok marking page HTML file.
Just right click, hit save as into same location as this, and run this.
'''
from bs4 import BeautifulSoup
import webbrowser  
  
with open("Grok Academy.html") as fp:
    soup = BeautifulSoup(fp,'lxml') 
 
# comment out if you want to use default browser
browser = webbrowser.get('chromium')  
for h in soup.findAll('td'): 
    a = h.find('a') 
    try:  
        if 'href' in a.attrs: 
            url = a.get('href')
            if url.startswith("https://groklearning.com/view-submissions"):
                browser.open(url, new=2, autoraise=False) 
    except Exception: 
        pass

