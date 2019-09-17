
import oauth2
from python_config_reader import read_config
import twitter
import pickle

def main():
	config=read_config(filename='/media/kunal/Windows8_OS/ASU Fall 19/CSE-472 Social Media Mining/configs/config.twitter.ini',section='twitter')
	
	api = twitter.Api(consumer_key=config['api_key'],
                  consumer_secret=config['api_secret'],
                  access_token_key=config['token_key'],
                  access_token_secret=config['token_secret'])

	f=open("v_names.pickle","rb")
	v_names=pickle.load(f)
	f=open("v_ids.pickle","rb")
	v_ids=pickle.load(f)	
	
	# Removing duplicates
	v_names=list(set(v_names))	
	v_ids=list(set(v_ids))	
	
	edges=create_edges(v_names=v_names,v_ids=v_ids,api=api)

def create_edges(v_names,v_ids,api):
	"""
	Create edges between v_ids
	"""
	for v in v_ids:
		following_list=api.GetFriendIDs(user_id=v)
		print(following_list)
		print('############################################')

def get_all_data(api):
	"""
	Uses twitter api to get following data 
	of cricketcomau, ECB Cricket, BCCI, ESPN_Cricinfo,absycric
	and dumps the data in a pickle file

	Returns Union of all followers
	"""

	user_1=api.GetFriendIDs(screen_name='cricketcomau')
	f = open("user_1.pickle", "wb")
	pickle.dump(user_1,f)

	user_2=api.GetFriendIDs(screen_name='ECB_cricket')
	f = open("user_2.pickle", "wb")
	pickle.dump(user_2,f)

	user_3=api.GetFriendIDs(screen_name='BCCI')
	f = open("user_3.pickle", "wb")
	pickle.dump(user_3,f)

	user_4=api.GetFriendIDs(screen_name='ESPNcricinfo')
	f = open("user_4.pickle", "wb")
	pickle.dump(user_4,f)

	user_5=api.GetFriendIDs(screen_name='absycric')
	f = open("user_5.pickle", "wb")
	pickle.dump(user_5,f)

	user_6=api.GetFriendIDs(screen_name='cricbuzz')
	f = open("user_6.pickle", "wb")
	pickle.dump(user_6,f)

	union=list(set().union(user_1,user_2,user_3,user_4,user_5,user_6))
	return union

def getNames(api,id_set=[]):
	"""
	Returns two lists of verified Names 
	& user ids
	"""	
	f=open('v_names.pickle','rb')
	verified_names=pickle.load(f)
	f=open('v_ids.pickle','rb')
	verified_ids=pickle.load(f)

	try:
		for i in id_set:
			print('Inside the loop')
			print(i)
			user=api.GetUser(user_id=i)
			if user.verified:
				print(user.name)
				verified_names.append(user.name)
				verified_ids.append(i)
	
	except Exception as	error:
		print(error)
		f=open("verified_names.pickle","wb")
		pickle.dump(verified_names,f)
		f=open("verified_ids.pickle","wb")
		pickle.dump(verified_ids,f)		

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