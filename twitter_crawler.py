
import oauth2
from python_config_reader import read_config
import twitter

def main():
	config=read_config(filename='/media/kunal/Windows8_OS/ASU Fall 19/CSE-472 Social Media Mining/configs/config.twitter.ini',section='twitter')
	
	api = twitter.Api(consumer_key=config['api_key'],
                  consumer_secret=config['api_secret'],
                  access_token_key=config['token_key'],
                  access_token_secret=config['token_secret'])

	user_1=api.GetFriendIDs(screen_name='cricketcomau')
	print(len(user_1))
	print('############################################')
	user_2=api.GetFriendIDs(screen_name='ECB_cricket')
	print(len(user_2))
	print('############################################')
	user_3=api.GetFriendIDs(screen_name='BCCI')
	print(len(user_3))
	print('############################################')
	user_4=api.GetFriendIDs(screen_name='ESPNcricinfo')
	print(len(user_4))
	user_5=api.GetFriendIDs(screen_name='absycric')
	print(len(user_5))
	union=list(set().union(user_1,user_2,user_3,user_4,user_5))
	print('############################################')
	print(len(union))
	print(union)
	v_names,v_ids=getNames(id_set=union,api=api)
	print(v_names)
	print(v_ids)
	print(len(v_names))
	print(len(v_ids))

def getNames(api,id_set=[]):
	"""
	Returns two lists of verified Names 
	& user ids
	"""	
	verified_names=[]
	verified_ids=[]
	for i in id_set:
		print('Inside the loop')
		print(i)
		user=api.GetUser(user_id=i)
		if user.verified:
			verified_names.append(user.name)
			verified_ids.append(i)
	
	return verified_names,verified_ids		



def getUserFromName(name, api):
	"""
	Returns user_id,screen_name
	"""
	user_list = api.GetUsersSearch(term=name, page=1, count=1)
	return user_list[0]
	
def oauth_req(url, key, secret,token_key,token_secret,http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key=key, secret=secret)
    token = oauth2.Token(key=token_key, secret=token_secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content


if __name__ == '__main__':
	main()