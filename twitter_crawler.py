
import oauth2
from python_config_reader import read_config

def main():
	config=read_config(filename='/media/kunal/Windows8_OS/ASU Fall 19/CSE-472 Social Media Mining/configs/config.twitter.ini',section='twitter')
	home_timeline = oauth_req( 'https://api.twitter.com/1.1/followers/list.json', key=config['api_key'], secret=config['api_secret'],token_key=config['token_key'],token_secret=config['token_secret'] )
	print(home_timeline)
	
def oauth_req(url, key, secret,token_key,token_secret,http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key=key, secret=secret)
    token = oauth2.Token(key=token_key, secret=token_secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content


if __name__ == '__main__':
	main()