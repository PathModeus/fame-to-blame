'''
The module analyses different datas on the tweets collected,
like the frequency of salty tweets, the mean of the lenght of salty tweets...
'''
import numpy as np
from src.insult_detection.insult_detection import detect_insult_tweet

def salty_test(tweet):
    '''
    Returns True if the tweet contains an insult and False if not
    '''
    insult=detect_insult_tweet(tweet)
    if insult==[]: #if there's no insult in the tweet
        return False
    return True

def insult_frequency(tweets):
    """
    returns the frequency of tweet containing insults

    Parameters
    ----------
    tweets : a list of tweets format string

    Returns
    --------
    prop/tot : the proportion of tweets that are insulting in the list
    """
    tot=len(tweets)
    prop=0 #number of salty tweets
    for single_tweet in tweets:
        if salty_test(single_tweet):
            #the function salty tests if the tweet is salty
            prop+=1
    return prop/tot
