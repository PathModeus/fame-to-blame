from textblob import TextBlob
from textblob import Word


from Data.swear_words_database import convert_database

path='Data/swear_words_database.csv'
swear_words_data=convert_database(path)
def detect_insult_tweet(tweet):
    insults=[]
    sentence=TextBlob(tweet['Texte'])
    for word in sentence.words:
        word=word.singularize
        word=Word(word)
        word=word.lemmatize
        if word in swear_words_data:
            insults.append(word)
    return insults

def detect_insults_tweets(data):
    data_insults={}
    for i in range(len(data)):
        data_insults[str(i)]=[detect_insult_tweet(tweet) for tweet in data[i][2]]
    return data_insults

print ('ok')



