import numpy as np
import dash
'''We analyse different datas on the tweets collected, like the frequency of salty tweets, the mean of the lenght of salty tweets...'''

###initialisation
def salty(tweet):
    #to define

def salty_list(tweets): #this function returns the list of the salty tweets and the list of the non-salty tweets
    S=[] #salty tweets
    NS=[]
    for t in tweets:
        if salty(t):
            S.append(t)
        else:
            NS.append(t)
    return S,NS

def rank(L,i): #returns the rank of L[i] in L
    pos=0
    for j in range(len(L)):
        if L[j]<L[i]:
            pos+=1
    return pos

###analyse
def frequency(tweets):
    n=len(tweets)
    p=0 #number of salty tweets
    for t in tweets:
        if salty(t): #the function salty tests if the tweet is salty
            p+=1
    return p/n

def lenght(tweets): #returns the mean of the lenght of tweets, salty tweets and non-salty tweets
    m=np.mean([len(t) for t in tweets])
    S,NS=salty_list(tweets)
    ms=np.mean([len(t) for t in S])
    mns=np.mean([len(t) for t in NS])
    return m,ms,mns

def ranking(LOT): #orddering a list of tweets from the most insulting to the less insulting
    freq=[]
    for tweets in LOT:
        freq.append(frequency(tweets))
    ordered=[LOT[0]]
    for i in range(1,len(LOT)):
        pos=rank(freq[:i+1],i)
        ordered.insert(pos,LOT[i])
    return ordered

###Graphe
