"""
Main file to launch the collection of tweets
"""
import json
import pandas as pd
from src.datacollection.collect import twitter_setup,get_tweets_from_candidates_search_queries
from src.datacollection.collect import get_replies_to_candidate,get_retweets_of_candidate
from src.datacollection.storetweet import store_tweets,extractjson

def collection(keywords,abs_path):
    """
    Collects and stores the tweets talking about one of the studied celebrity
    :param keywords: (list) list of the keywords we want to search
    :return: (list) list of 3-element-lists corresponding to one celebrity,
    each containing their number, name and a dataframe with the tweets about them
    """
    twitter_api = twitter_setup(abs_path)
    tweets=[]
    name=keywords[0]
    celebrity_tweets = get_tweets_from_candidates_search_queries(keywords,twitter_api)
    replies = get_replies_to_candidate(name, twitter_api)
    retweets = get_retweets_of_candidate(name, twitter_api)
    if replies == "This twitter user does not exist." or retweets == "This twitter user does not exist.":
        return "This twitter user does not exist."
    result = celebrity_tweets + replies + retweets
    for status in result:
        try:
            tweets.append(status._json) #pylint: disable=protected-access
        except AttributeError:
            tweets.append(json.loads(status.decode('utf-8')))
    store_tweets(tweets,name)
    dataframe=pd.DataFrame.from_dict(extractjson('Data/' + name + '.json'))
    return [name,dataframe]
