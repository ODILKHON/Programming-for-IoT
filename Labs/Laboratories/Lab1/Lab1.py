import requests
url = "https://catalog-p4iot.onrender.com/all"
#1. Fetching the data from the website
response = requests.get(url)
#2. Parse the JSON directly into a Python dictionary or list
data= response.json()
