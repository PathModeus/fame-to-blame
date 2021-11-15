import tweepy
import sys
import time


def twitter_setup(abs_path):
    """
    Utility function to setup the Twitter's API
    with an access keys provided in a file credentials.py
    :return: the authentified API
    
    Input :
        The function asks for a str which is the absolute path of credentials.py 
        ex : 'c:/absolute/path/of'
    """
    #adding credentials.py to the path and importing var:
    sys.path.insert(1, abs_path)
    from credentials import *

    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api

def get_candidate_queries(num_candidate, file_path):
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """
    try:
        final_path = file_path+str(num_candidate)+".txt"
        fichier = open(final_path, 'r',encoding='utf-8')
        L = []
        for ligne in fichier:
            ligne = ligne.rstrip()
            L.append(ligne)
        fichier.close()
        return L
    except FileNotFoundError:
        return "The requested datas are not available in our database."

def get_tweets_from_candidates_search_queries(queries, twitter_api):
    """
    returns the tweets corresponding to the query
    """
    L = []
    for query in queries:
        tweets = twitter_api.search_tweets(query)
        for tweet in tweets:
            L.append(tweet)
    return L

def get_replies_to_candidate(num_candidate, twitter_api):
    """
    converts candidate's ID into his name and returns the tweets answering to the candidate
    """
    name = get_candidate_queries(
        num_candidate, 'Data\keywords_candidate_')[0]
    id = get_id(name)
    tweet = collect_by_user(id, 1)
    tweet_id = tweet[0].id
    replies = tweet
    pot_replies = twitter_api.search_tweets(q='to:'+name)
    for t in pot_replies:
        if (t.in_reply_to_status_id_str == str(tweet_id)):
            replies.append(t)
    return replies


def get_retweets_of_candidate(num_candidate, twitter_api):
    """
    
    """
    name = get_candidate_queries(
        num_candidate, 'Data\keywords_candidate_')[0]
    id = get_id(name)
    tweet = collect_by_user(id, 1)
    tweet_id = tweet[0].id
    retweets = twitter_api.get_retweets(id=tweet_id)
    return retweets


# print(get_replies_to_candidate(2, twitter_setup()))
# print(get_retweets_of_candidate(2, twitter_setup()))

def stream(keywords,duration):
    class MyListener(tweepy.Stream):
            
        def on_data(self, data):
            if time.time()-t0>duration:
                print("Disconnecting...")
                twitter_stream.disconnect()
            else:
                L.append(data)
                return True


        # Initialize instance of the subclass
    t0=time.time()
    L=[]
    print("Streaming")
    twitter_stream = MyListener(
        CONSUMER_KEY, CONSUMER_SECRET,
        ACCESS_TOKEN, ACCESS_SECRET
    )
    twitter_stream.filter(track=keywords)
    return L

def get_id(screen_name):
    api = twitter_setup()
    user = api.get_user(screen_name=screen_name)
    ID = user.id_str
    return ID


def collect(keyword):
    L = []
    connexion = twitter_setup()
    tweets = connexion.search_tweets(
        keyword, language="french", rpp=100)
    for tweet in tweets:
        L.append(tweet)
    return L


def collect_by_user(user_id, limit=200):
    api = twitter_setup()
    statuses = api.user_timeline(user_id=user_id, count=limit)
    return statuses