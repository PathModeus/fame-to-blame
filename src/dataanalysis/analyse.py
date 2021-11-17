import numpy as np

'''
The module analyses different datas on the tweets collected,
like the frequency of salty tweets, the mean of the lenght of salty tweets...
'''

def salty_test(tweet):
    '''
    Returns True if the tweet contains an insult and False if not
    '''
    return tweet

def salty_list(tweets):
    '''
    returns the list of the salty tweets and the list of the non-salty tweets
    '''
    salt=[] #insulting tweets
    nosalt=[] #not salty tweets
    for single_tweet in tweets:
        if salty_test(single_tweet):
            salt.append(single_tweet)
        else:
            nosalt.append(single_tweet)
    return salt,nosalt

def rank(list_of_values,indice):
    '''
    returns the rank of list[i] in list
    '''
    pos=0
    for value in list_of_values:
        if value<list_of_values[indice]:
            pos+=1
    return pos


def frequency(tweets):
    '''
    returns the frequency of tweet containing insults
    '''
    tot=len(tweets)
    prop=0 #number of salty tweets
    for single_tweet in tweets:
        if salty_test(single_tweet):
            #the function salty tests if the tweet is salty
            prop+=1
    return prop/tot

def length(tweets):
    '''
    returns the mean of the length of tweets, salty tweets and non-salty tweets
    '''
    salty,nosalty=salty_list(tweets)
    mean_salty=np.mean([len(single_tweet) for single_tweet in salty])
    mean_nosalty=np.mean([len(single_tweet) for single_tweet in nosalty])
    mean_total=np.mean([len(single_tweet) for single_tweet in salty + nosalty])
    return mean_total,mean_salty,mean_nosalty

def ranking(list_of_tweets):
    '''
    ordering a list of lists of tweets from the most insulting to the less insulting
    '''
    freq=[] #frequence of insults in a list of tweets
    for tweets in list_of_tweets:
        freq.append(frequency(tweets))
    ordered=[list_of_tweets[0]]
    for i in range(1,len(list_of_tweets)):
        pos=rank(freq[:i+1],i)
        ordered.insert(pos,list_of_tweets[i])
    return ordered
