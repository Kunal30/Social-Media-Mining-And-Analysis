import urllib3
import facebook
import requests
print("Hello Just Testing")
token = "xxxxxxxxxxxxxx"
graph = facebook.GraphAPI(access_token=token, version = 3.1)

rest_api_link= "https://graph.facebook.com/v3.1/xxxxxxxx/friends?access_token="+token

linkedinlink="https://www.linkedin.com/oauth/v2/accessToken?grant_type=client_credentials&client_id=862ldul9drgoii&client_secret=7so2Xj12hLDozNUg"
pagesdata = requests.get(linkedinlink).json()
print((pagesdata))
