"""
Insult detection module 
    Description: 
        Detects and returns the insults in a tweet or a dataframe
    Contains:
        detect_insult_tweet(tweet) : returns a list of insults(type strings)

        detect_insults_tweets(data) : returns a dictionnary (per celebrity_ID) of list of lists,
        each sub-list containing the insults in one tweet
    """

from textblob import TextBlob
from textblob import Word
from src.insult_detection.csv_to_list import convert_database

PATH='data/swear_words_database.csv'
swear_words_data=convert_database(PATH)
def detect_insult_tweet(tweet):
    """Return a list of the insults contained in a tweet
    Parameters
    ----------
    tweet : a dataframe panda with a key 'Texte'

    Returns
    --------
    insults : a list of strings
    """
    insults=[]
    sentence=TextBlob(tweet)
    str_tweet=""
    for word in sentence.words:
        word=word.singularize
        word=Word(word)
        word=word.lemmatize
        str_tweet+=str(word)
    str_tweet_min=str_tweet.lower()   
    #print(str_tweet)
    for insult in swear_words_data:
        if insult in str_tweet_min:
            insults.append(insult)
    return insults

def detect_insults_tweets(data):
    """Return a  dictionnary of key celebrity_ID and for each key containing a list of lists
        Each list of list contains the insults in one tweet
    Parameters
    ----------
    tweet : a dataframe panda with a key 'Texte'

    Returns
    --------
    insults : a dictionnary of lists of lists
    """
    data_insults={}
    for i in range(len(data)):
        data_insults[str(i+1)]=[detect_insult_tweet(tweet) for tweet in data[i][2]['Texte']]
    return data_insults

def insult_frequencies(data) : 
    """Return a dictionnary of key swear_words and for each key containing the number of occurences 
    of the word in our tweet collection
    Parameters
    ----------
    tweet : a dataframe panda with a key 'Texte'

    Returns 
    -------
    insult_freq : a dictionnary
    """
    insult_freq = {}
    for i in range(len(data)) : 
        insults=[]
        sentence = TextBlob( data[i]['Texte'] )
        str_tweet=""
        for word in sentence.words:
            word=word.singularize
            word=Word(word)
            word=word.lemmatize
            if word in swear_words_data :
                insult_freq[word] += 1
            else : 
                insult_freq[word] = 1

    return insult_freq

def most_frequent_insult(data) : 
    max = 0
    most_frequent_swear_word = str()
    iter = insult_frequencies(data)
    for cle, valeur in iter.items():
        if valeur > max : 
            max = valeur
            most_frequent_swear_word = cle
    return cle