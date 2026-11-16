import cherrypy
import requests
import json
url = "https://catalog-p4iot.onrender.com"
"""
In this exercise, your Python script is no longer acting as the server; 
instead, it is acting as a client that talks to an external REST API(url).
using Python's requests package. 
It requests a list of connected devices from the catalog.
"""
#Saves the specific endpoint or path you want to visit
#on that server(in this case, asking for devices list)
resource = "/devices"
#Combines the base URL and the resource path
#and sends an HTTP GET request to fetch the data. 
#The server`s response is stored in the var `r`
r = requests.get(url + resource)
#Takes the raw data sent back by the server and 
#automatically converts it from JSON format 
#into a native Python dictionary or list,
#so you can easily work with it in your code.
output = r.json()
#json.dumps() takes Python data and formats it back
#into a text string, and indent = 4 adds clean 4 space
#indentation
print(json.dumps(output, indent = 4))

