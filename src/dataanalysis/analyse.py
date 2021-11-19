'''
The module analyses different datas on the tweets collected,
like the frequency of salty tweets, the mean of the lenght of salty tweets...
'''
import numpy as np



def salty_test(tweet):
    '''
    Returns True if the tweet contains an insult and False if not
    '''
    if tweet==[]:
        return False
    return True


def insult_frequency(tweets):
    """returns the frequency of tweet containing insults

    Parameters
    ----------
    tweets : a list of tweets format string

    Returns
    --------
    pos/tot : the proportion of tweets that are insulting in the list
    """
    tot=len(tweets)
    prop=0 #number of salty tweets
    for single_tweet in tweets:
        if salty_test(single_tweet):
            #the function salty tests if the tweet is salty
            prop+=1
    return prop/tot
