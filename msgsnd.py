import numpy as np
import pandas as pd
import yfinance as yf
import requests
import json
from onesignal_sdk.client import Client
from onesignal_sdk.error import OneSignalHTTPError

appid = "684398e2-dbda-4cf0-985c-f115614fcc49"



client = Client(app_id=appid, rest_api_key="YWEyZGYxYmQtMWQwNC00MGY5LWEzMjAtZTIyOWFjZDZlY2Ez", user_auth_key="NDMyOTQ1MDItNDJkNS00ZDhmLTgzNTMtZDc3MjllNDk0Zjdh")
symbol = '^SPX'

def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return str(round(todays_data['Close'][0],2))

def send(arg):
    try:
        response = client.send_notification(data)
    except OneSignalHTTPError as e:
        print("Error in Text")

curr = get_current_price(symbol)

data = {
    "app_id": appid,
    "included_segments": ["All"],
    "contents": {"en": "Buy @ " + curr},
    "headings": {"en": "Long Signal"}
}

send(data)

print("Sent data value at price:" + curr)
