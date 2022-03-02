#from helpers.config import config
import tweepy, time, ssl
from helpers.get_user_id import author_id, client

from rich.console import Console
console = Console()


def tweet_lookup():

    lookup = client.get_users_tweets(id=author_id, media_fields='preview_image_url', exclude = ["retweets", "replies"], max_results = 100)
    time.sleep(0.1)
    return lookup
    
lookup = tweet_lookup()


tweet_list = []

for i in lookup.data:
    tweet_list.append(i.id)

next_token = lookup.meta.get("next_token")

#console.print(tweet_list, style ="bold green")

for i in range(500):
    if next_token is not None:
        lookup2 = client.get_users_tweets(id=author_id, media_fields='preview_image_url', exclude = ["retweets", "replies"], pagination_token=next_token, max_results = 100)

        for i in lookup2.data:
            tweet_list.append(i.id)
    else:
        #console.print("Last Page",style = 'bold red')
        break;
        

#console.print(tweet_list, style = "bold yellow")
console.print(f"Total Tweets Includes Media : {len(tweet_list)}", style= "Bold Red")




