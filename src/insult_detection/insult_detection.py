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
from csv_to_list import convert_database

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
    sentence=TextBlob(tweet['Texte'])
    str_tweet=""
    for word in sentence.words:
        word=word.singularize
        word=Word(word)
        word=word.lemmatize
        str_tweet+=word
        for insult in swear_words_data:
            if insult in str_tweet:
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
        data_insults[str(i+1)]=[detect_insult_tweet(tweet) for tweet in data[i][2]]
    return data_insults
