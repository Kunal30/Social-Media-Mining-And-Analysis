import urllib3
import facebook
import requests
print("Hello Just Testing")
token = "xxxxxxxxxxxx"
graph = facebook.GraphAPI(access_token=token, version = 3.1)

rest_api_link= "https://graph.facebook.com/v3.1/xxxxxxxxxxx/feed?access_token="+token

pagesdata = requests.get(rest_api_link).json()
print((pagesdata))
