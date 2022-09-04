from turtle import clear
from onesignal_sdk.client import Client
from onesignal_sdk.error import OneSignalHTTPError
import currentprice
import currentprice, threading, queue, time, json

client = Client(app_id="684398e2-dbda-4cf0-985c-f115614fcc49", rest_api_key="YWEyZGYxYmQtMWQwNC00MGY5LWEzMjAtZTIyOWFjZDZlY2Ez", user_auth_key="NDMyOTQ1MDItNDJkNS00ZDhmLTgzNTMtZDc3MjllNDk0Zjdh")
q = queue.Queue()

def getPrice():
    while True:
        q.put(currentprice.quote().getQuote())

def send(arg):
    try:
        response = client.send_notification(arg)
    except OneSignalHTTPError as e:
        print("Error in Text")

def makeMsg(sent, stat):
    price = currentprice.quote().getQuote()
    if(sent == "l"):
        head = "Long Signal"
        cont = "Long Signal @ " + price
    else:
        head = "Short Signal"
        cont = "Short Signal @ " + price
    
    data = {
        "app_id": "684398e2-dbda-4cf0-985c-f115614fcc49",
        "included_segments": ["All"],
        "contents": {"en": cont},
        "headings": {"en": head}
    }
    return data

priceThread = threading.Thread(target = getPrice)
priceThread.start()


send(makeMsg("l", 0))
while True:
    print(q.get())
    

