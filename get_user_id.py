import config
import tweepy, json

#AUTH
##CLIENT
def get_client():
    client = tweepy.Client(bearer_token=config.BEARER_TOKEN, consumer_key=config.API_KEY, consumer_secret=config.API_SECRET, access_token=config.ACCESS_TOKEN,access_token_secret=config.ACCESS_TOKEN_SECRET,wait_on_rate_limit=False)
    return client
    
client = get_client()

##API
def get_api():
    auth = tweepy.OAuth2BearerHandler(bearer_token = config.BEARER_TOKEN)
    api = tweepy.API(auth=auth)
    return api
    
api = get_api()
username = input("Enter a twitter profile username, without '@' to download : ")

def get_user_timeline():
    user_data = client.get_user(username=username)
    
    return user_data.data.id

author_id = get_user_timeline()




