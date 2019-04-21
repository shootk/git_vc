import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self,site):
        self.site = site
    
    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser ="html.parser"
        sp = BeautifulSoup(html,parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            cl = tag.get("class")
            if url is None:
                continue
            if cl == "VDXfz":
                url = url.replace(".","https://news.google.com")
                url = url.replace("en-US","ja")
                url = url.replace("US","JP")
                url = url.replace("en","ja")
                print("\n"+url)
news = "https://news.google.com/?hl=ja&gl=JP&ceid=JP:ja"
Scraper(news).scrape()