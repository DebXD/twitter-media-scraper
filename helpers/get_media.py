from helpers.get_tweets import tweet_list
from rich.console import Console
from helpers.get_user_id import api 
import time

console = Console()

def get_tweet_media():
    console.print("Fetching Media...Kindly wait for a Moment...",style = "bold #00FFFF")

    media_list = []
    x = 1

    for tweet_id in tweet_list:
        status = api.get_status(tweet_id,tweet_mode='extended')
        time.sleep(0.1)
        console.print(f"Fetched : {x}")
        x += 1

        try:
            media_url = status._json.get("entities").get("media")[0].get("media_url_https")
            
            
            if len(media_url) < 80 :
                
                media_type = status._json.get("entities").get("media")[0].get("type")
                
                
                media_list.append(media_url)



            elif len(media_url) > 80:
                vid_type = status._json.get("extended_entities").get("media")[0].get("video_info").get("variants")[0].get("content_type")
            
                vid_url = status._json.get("extended_entities").get("media")[0].get("video_info").get("variants")[0].get("url")
                media_list.append(vid_url)

            else:
                console.print("None",style="bold yellow")

        except Exception as e:
            console.print(e)
       
    return media_list, media_type
       
       
media_list, media_type = get_tweet_media()
