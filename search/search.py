import tweepy
import datetime as dt
from pprint import pprint
import pandas as pd
import os 
class Twitter:

        

        # Function to get the latest tweet from a famous person
        def get_tweet(self):
            api_key = os.environ['api_key']
            api_key_secret = os.environ['api_key_secret']
            bearer_token = os.environ['bearer_token']
            access_token = os.environ['access_token']
            access_token_secret = os.environ['access_token_secret']

            # Authenticate to Twitter
            auth = tweepy.OAuthHandler(api_key, api_key_secret)
            auth.set_access_token(access_token, access_token_secret)
            api = tweepy.API(auth)

          
            begin_date = dt.date(2022, 1, 1)
            end_date = dt.date(2023, 4, 17)
            limit = 10000
            lang =  "english"


            tweets = []
            likes = []
            time = []
            user = 'FabrizioRomano'
            tweets= []
            tweet_id = []
            image_url = []

           
            for i in tweepy.Cursor(api.user_timeline, id=user, tweet_mode="extended",include_entities=True).items(limit):
                text = i.full_text
                each_tweet_images = []
                if 'here we go' in text:
                    tweets.append(i.full_text)
                    likes.append(i.favorite_count)
                    time.append(i.created_at)
                    
                    if 'media' in i.entities:
                        for image in i.entities['media']:
                            tweet_id.append(image['url'])
                            each_tweet_images.append(image['media_url'])
                    image_url.append(each_tweet_images)

            
            df = pd.DataFrame(list(zip(tweets,likes,time,tweet_id,image_url)))
            
            df.to_csv('tweets.csv')

            


















       
