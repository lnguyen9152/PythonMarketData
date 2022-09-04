from bs4 import BeautifulSoup
import requests,time

class quote:

    def getQuote(self):
        url = "https://www.cnbc.com/quotes/.SPX"
        #url = "https://www.cnbc.com/quotes/ETH=?qsearchterm=eth"
        getWebsite = BeautifulSoup(requests.get(url).text, "html.parser")
        return getWebsite.find(class_="QuoteStrip-lastPrice").get_text().replace(',', '')
    