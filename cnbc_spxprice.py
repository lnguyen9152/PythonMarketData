from bs4 import BeautifulSoup
import requests

url = "https://www.cnbc.com/quotes/.SPX"

result = requests.get(url)
getWebsite = BeautifulSoup(result.text, "html.parser")

currentPrice = getWebsite.find_all(class_="QuoteStrip-lastPrice")

print(currentPrice)