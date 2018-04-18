import urllib2
import requests
import json
from bs4 import BeautifulSoup

data = {'USERNAME':'Nischi'}

req = urllib2.Request('http://192.168.43.225:5000/user/verifysuspect')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))
soup =  BeautifulSoup(response, "html.parser" ).encode('UTF-8')

print (soup)
