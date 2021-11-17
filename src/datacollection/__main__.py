"""
Main file to launch the collection of tweets
"""
import json
import pandas as pd
from collect import twitter_setup,get_candidate_queries,get_tweets_from_candidates_search_queries
from collect import get_replies_to_candidate,get_retweets_of_candidate
from storetweet import store_tweets,extractjson

def collection(keywords):
    """
    Collects and stores the tweets talking about one of the studied celebrity
    :param celebrity_amount: (int) number of celebrities studied
    :return: (list) list of 3-element-lists corresponding to one celebrity,
    each containing their number, name and a dataframe with the tweets about them
    """
    collect=[]
    tweets=[]
    name=keywords[0]
    candidate_tweets = get_tweets_from_candidates_search_queries(keywords,twitter_api)
    replies = get_replies_to_candidate(num_celebrity,twitter_api)
    retweets = get_retweets_of_candidate(num_celebrity,twitter_api)
    if replies == "This twitter user does not exist." or retweets == "This twitter user does not exist.":
        return "This twitter user does not exist."
    result = candidate_tweets + replies + retweets
    for status in result:
        try:
            tweets.append(status._json) #pylint: disable=protected-access
        except AttributeError:
            tweets.append(json.loads(status.decode('utf-8')))
        store_tweets(tweets,name)
        dataframe=pd.DataFrame.from_dict(extractjson('Data/' + name + '.json'))
        collect.append([int(num_celebrity),name,dataframe])
    return collect

print(collection(1))