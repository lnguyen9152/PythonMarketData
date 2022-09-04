import numpy as np
import pandas as pd
import requests
import json
from onesignal_sdk.client import Client
from onesignal_sdk.error import OneSignalHTTPError


class message:
    appid = "684398e2-dbda-4cf0-985c-f115614fcc49"
    client = Client(app_id=appid, rest_api_key="YWEyZGYxYmQtMWQwNC00MGY5LWEzMjAtZTIyOWFjZDZlY2Ez", user_auth_key="NDMyOTQ1MDItNDJkNS00ZDhmLTgzNTMtZDc3MjllNDk0Zjdh")
    def send(arg):
        try:
            response = client.send_notification(data)
        except OneSignalHTTPError as e:
            print("Error in Text")

    data = {
        "app_id": appid,
        "included_segments": ["All"],
        "contents": {"en": "Buy @ " },
        "headings": {"en": "Long Signal"}
    }

    send(data)

    print("Sent data value at price:" )
