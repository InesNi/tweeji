import tweepy
import os
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()

consumer_key = os.getenv('TWEEJI_API_KEY')
consumer_secret = os.getenv('TWEEJI_API_SECRET')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')


auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

START_DATE = datetime(year=2020, month=5, day=19, hour=8)

# calculates index of quote to be used for given day
def calculate_index(start_date):
    check = datetime.now() - start
    index = 308 % check.days
    return index

def get_quote(file,index):
    with open(file) as t_file:
        quotes = t_file.readlines()
        quote = quotes[index]
    return quote

# updates twitter status
def update_status(quote):
    api.update_status(quote)

if __name__ == "__main__":
    index = calculate_index(START)
    quote = get_quote("quotes_lib.txt", index)
    update_status(quote)
