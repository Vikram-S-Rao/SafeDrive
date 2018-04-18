import urllib2
import requests

req = urllib2.Request('http://192.168.43.66:5000/user/suspected/SD001')
response = urllib2.urlopen(req)
print ('Server Response: '+str(response))
