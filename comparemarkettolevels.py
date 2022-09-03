import requests

url = "https://cnbc.p.rapidapi.com/symbols/get-chart"

querystring = {"symbol":"36276","interval":"1d"}

headers = {
	"X-RapidAPI-Key": "3d3fb04a9fmsh708fbe6dc2a14cap123a14jsn0f3294d3730e",
	"X-RapidAPI-Host": "cnbc.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
