import numpy as np

'''
We analyse different datas on the tweets collected,
like the frequency of salty tweets, the mean of the lenght of salty tweets...
'''

###initialisation
def salty(tweet):
    #to define, depends of the format of insult_detection
    return(True or False)

def salty_list(tweets):
    #this function returns the list of the salty tweets and the list of the non-salty tweets
    salty=[] #salty tweets
    non_salty=[]
    for message in tweets:
        if salty(message):
            salty.append(message)
        else:
            non_salty.append(message)
    return salty,non_salty

def rank(list,indice): #returns the rank of list[indice] in list
    pos=0
    for j in range(len(list)):
        if list[j]<list[indice]:
            pos+=1
    return pos

###analyse
def frequency(tweets):
    lenght=len(tweets)
    proprtion=0 #number of salty tweets
    for message in tweets:
        if salty(message): #the function salty tests if the tweet is salty
            proprtion+=1
    return proprtion/lenght

def lenght(tweets): #returns the mean of the lenght of tweets, salty tweets and non-salty tweets
    mean=np.mean([len(message) for message in tweets])
    salty,non_salty=salty_list(tweets)
    mean_salty=np.mean([len(message) for message in salty])
    mean_non_salty=np.mean([len(message) for message in non_salty])
    return mean,mean_salty,mean_non_salty

def ranking(list_of_tweets):
    #orddering a list of lists of tweets from the most insulting to the less insulting
    freq=[]
    for tweets in list_of_tweets:
        freq.append(frequency(tweets))
    ordered=[list_of_tweets[0]]
    for i in range(1,len(list_of_tweets)):
        pos=rank(freq[:i+1],i)
        ordered.insert(pos,list_of_tweets[i])
    return ordered