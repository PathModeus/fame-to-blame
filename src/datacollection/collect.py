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
    from credentials import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET

    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api

def get_candidate_queries(number, file_path):
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_number.txt
    :param number: the number of the celebrity
    :param file_path: the path to the folder containing the datas
    :return: (list) a list of string queries that can be done to the search API independently
    """
    try:
        final_path = file_path+str(number)+".txt"
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
    returns the tweets corresponding to the queries
    :param queries: list of strings containing queries for the api (mostly keywords)
    :param twitter_api: API obtained with the function twitter_setup
    :return: (list) a list of tweets corresponding to the queries

    """
    L = []
    for query in queries:
        tweets = twitter_api.search_tweets(query)
        for tweet in tweets:
            L.append(tweet)
    return L

def get_replies_to_candidate(number, twitter_api):
    """
    returns the tweets replying to the candidate
    :param number: the number of the celebrity
    :param twitter_api: API obtained with the function twitter_setup
    :return: (list) a list containing the tweets replying to the candidate

    """
    name = get_candidate_queries(
        number, 'Data\keywords_candidate_')[0]
    id = get_id(name,twitter_api)
    tweet = collect_by_user(id, twitter_api, 1)
    tweet_id = tweet[0].id
    replies = tweet
    pot_replies = twitter_api.search_tweets(q='to:'+name)
    for t in pot_replies:
        if (t.in_reply_to_status_id_str == str(tweet_id)):
            replies.append(t)
    return replies


def get_retweets_of_candidate(number, twitter_api):
    """
    returns the retweets of the last tweet of the candidate
    :param number: the number of the celebrity
    :twitter_api: API obtained with the function twitter_setup
    :return: (list) a list containing the tweets retweeting the last tweet of the candidate

    """
    name = get_candidate_queries(number, 'Data\keywords_candidate_')[0]
    id = get_id(name, twitter_api)
    tweet = collect_by_user(id, twitter_api, 1)
    tweet_id = tweet[0].id
    retweets = twitter_api.get_retweets(id=tweet_id)
    return retweets


def stream(keywords,duration,path_to_credentials):
    """
    return a list of tweets containing one of the keywords captured live by streaming
    :param keywords: (list) a list of strings containing the keywords we want to search
    :param duration: (float) the duration we want to be streaming for
    :param path_to_credentials: (string) the absolute path to the file containing the API credentials
    :return: (list) a list containing the tweets sent during the stream containing (at least) one of the keywords
    """
    sys.path.insert(1, path_to_credentials)
    from credentials import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET
    class MyListener(tweepy.Stream):
            
        def on_data(self, data):
            if time.time()-t0>duration:
                twitter_stream.disconnect()
            else:
                L.append(data)
                return True


        # Initialize instance of the subclass
    t0=time.time()
    L=[]
    twitter_stream = MyListener(
        CONSUMER_KEY, CONSUMER_SECRET,
        ACCESS_TOKEN, ACCESS_SECRET
    )
    twitter_stream.filter(track=keywords)
    return L

def get_id(screen_name,twitter_api):
    """
    returns the id of a user using his screen name
    :param screen_name: (string) the twitter screen_name of the account which we want to obtain the id
    :param twitter_api: API object obtained with the function twitter_setup
    :return: (int) the user's id
    """
    user = twitter_api.get_user(screen_name=screen_name)
    ID = user.id_str
    return ID


def collect(keyword,twitter_api):
    """
    returns a list of tweets containing a specific keyword
    :param keyword: (str) the keyword we want to search
    :param twitter_api: API object obtained with the function twitter_setup
    :return: (list) a list of tweets containing the keyword
    """
    L = []
    tweets = twitter_api.search_tweets(
        keyword, language="french", rpp=100)
    for tweet in tweets:
        L.append(tweet)
    return L


def collect_by_user(user_id,twitter_api, limit=200):
    """
    returns a list of the last tweets from a user using his id
    :param user_id: (int) the user's twitter id
    :param twitter_api: API object obtained with the function twitter_setup
    :return: (list) a list of the last tweets of the user
    """
    statuses = twitter_api.user_timeline(user_id=user_id, count=limit)
    return statuses