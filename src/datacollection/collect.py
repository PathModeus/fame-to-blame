"""
All the functions to do a twitter collect
"""
import sys
import time
import tweepy


def twitter_setup(abs_path):
    """
    Utility function to setup the Twitter's API
    with an access keys provided in a file credentials.py
    :return: the authentified API
    :param abs_path: (str) absolute path of the folder containing credentials.py
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
    Generate and return a list of string queries for the API from the file file_path_number.txt
    :param number: the number of the celebrity
    :param file_path: the common part of the path to the datas, ex : path/to/keywords_celebrity_
    :return: (list) a list of string queries that can be done to the search API independently
    """
    try:
        final_path = file_path+str(number)+".txt"
        with open(final_path, 'r',encoding='utf-8') as fichier:
            queries = []
            for ligne in fichier:
                ligne = ligne.rstrip()
                queries.append(ligne)
            return queries
    except FileNotFoundError:
        return "The requested datas are not available in our database."

def get_tweets_from_candidates_search_queries(queries, twitter_api):
    """
    returns the tweets corresponding to the queries
    :param queries: list of strings containing queries for the api (mostly keywords)
    :param twitter_api: API obtained with the function twitter_setup
    :return: (list) a list of tweets corresponding to the queries

    """
    tweets = []
    for query in queries:
        result = collect(query,twitter_api)
        for tweet in result:
            tweets.append(tweet)
    return tweets

def get_replies_to_candidate(name, twitter_api):
    """
    returns the tweets replying to the candidate
    :param number: the number of the celebrity
    :param twitter_api: API obtained with the function twitter_setup
    :return: (list) a list containing the tweets replying to the candidate

    """
    user_id=get_id(name,twitter_api)
    if user_id == "This twitter user does not exist.":
        return user_id
    user_tweets = collect_by_user(user_id, twitter_api, 20)
    tweets_id = []
    for user_tweet in user_tweets:
        tweets_id.append(user_tweet.id)
    pot_replies = collect('to'+name, twitter_api)
    replies=[]
    for pot_reply in pot_replies:
        if pot_reply.in_reply_to_status_id in tweets_id:
            replies.append(pot_reply)
    return replies


def get_retweets_of_candidate(name, twitter_api):
    """
    returns the retweets of the last tweet of the candidate
    :param number: the number of the celebrity
    :twitter_api: API obtained with the function twitter_setup
    :return: (list) a list containing the tweets retweeting the last tweet of the candidate

    """
    user_id=get_id(name,twitter_api)
    if user_id == "This twitter user does not exist.":
        return user_id
    user_tweets = collect_by_user(user_id, twitter_api, 20)
    tweets_id = []
    for user_tweet in user_tweets:
        tweets_id.append(user_tweet.id)
    pot_retweets = collect('@' + name, twitter_api, 1000)
    retweets = []
    for pot_retweet in pot_retweets:
        if pot_retweet.is_quote_status :
            if pot_retweet.quoted_status_id in tweets_id:
                retweets.append(pot_retweet)
    return retweets


def stream(keywords,duration,path_to_credentials):
    """
    return a list of tweets containing one of the keywords captured live by streaming
    :param keywords: (list) a list of strings containing the keywords we want to search
    :param duration: (float) the duration we want to be streaming for
    :param path_to_credentials: (str) the absolute path to the file containing the API credentials
    :return: (list) list containing the captured tweets containing (at least) one of the keywords
    """
    sys.path.insert(1, path_to_credentials)
    from credentials import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET
    class MyListener(tweepy.Stream):
        """
        Launches the stream
        """
        def on_data(self, raw_data):
            if time.time()-starting_time>duration:
                twitter_stream.disconnect()
                return False
            streamed_tweets.append(raw_data)
            return True


        # Initialize instance of the subclass
    starting_time=time.time()
    streamed_tweets=[]
    twitter_stream = MyListener(
        CONSUMER_KEY, CONSUMER_SECRET,
        ACCESS_TOKEN, ACCESS_SECRET
    )
    if keywords == []:
        return "Please insert keywords"
    twitter_stream.filter(track=keywords)
    return streamed_tweets

def get_id(screen_name,twitter_api):
    """
    returns the id of a user using his screen name
    :param screen_name: (str) the twitter screen_name of the account which id we want to obtain
    :param twitter_api: API object obtained with the function twitter_setup
    :return: (int) the user's id
    """
    if screen_name == '':
        return "Please enter a screen name."
    try:
        user = twitter_api.get_user(screen_name=screen_name)
        user_id = user.id_str
        return user_id
    except tweepy.errors.NotFound:
        return "This twitter user does not exist."


def collect(keyword,twitter_api,count = 1000,language='en'):
    """
    returns a list of tweets containing a specific keyword
    :param keyword: (str) the keyword we want to search
    :param twitter_api: API object obtained with the function twitter_setup
    :return: (list) a list of tweets containing the keyword
    """
    if not(isinstance(keyword,str)) or keyword == '':
        return "Please enter a valid keyword (string)."
    result = []
    tweets = twitter_api.search_tweets(q=keyword, count = count, lang=language)
    for tweet in tweets:
        result.append(tweet)
    return result


def collect_by_user(user_id,twitter_api, limit=200):
    """
    returns a list of the last tweets from a user using his id
    :param user_id: (int) the user's twitter id
    :param twitter_api: API object obtained with the function twitter_setup
    :return: (list) a list of the last tweets of the user
    """
    statuses = twitter_api.user_timeline(user_id=user_id, count=limit)
    return statuses
