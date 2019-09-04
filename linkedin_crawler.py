
import urllib3
import requests

def main():
	API_KEY = 'xxxxxxxxxxxx'
	API_SECRET = 'xxxxxxxxxxx'
	RETURN_URL = 'http://localhost:8000'
	http = urllib3.PoolManager()
	accessTokenLink='https://www.linkedin.com/oauth/v2/accessToken'
	accessTokenConfig={
						'grant_type':'client_credentials',
						'client_id':API_KEY,
						'client_secret':API_SECRET
					  }
	print(accessTokenConfig)				  
	accessToken = http.request('GET',accessTokenLink,fields=accessTokenConfig)
	# r=requests.get(url=accessTokenLink,data=accessTokenConfig)
	print(accessToken.data)
	# print(r)
	print("DATA NOW")

if __name__ == '__main__':
	main()