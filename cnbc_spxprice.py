from bs4 import BeautifulSoup
import requests

url = "https://www.cnbc.com/quotes/.SPX"
getWebsite = BeautifulSoup(requests.get(url).text, "html.parser")
currentPrice = getWebsite.find(class_="QuoteStrip-lastPrice").get_text().replace(',', '')

print(currentPrice)