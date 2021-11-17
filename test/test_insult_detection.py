from textblob.blob import TextBlob, Word
from src.insult_detection.insult_detection import detect_insult_tweet, detect_insults_tweets
tweet1={"Texte":'shit! you are a hot chick' }
tweet2={"Texte": 'Hot ! blabla chick'}
tweet3={"Texte": 'Shit you SUCK'}
tweet4={"Texte": 'Shits he sucked'}

def test_detect_insult_tweet():
    assert detect_insult_tweet(tweet1)==['hot chick','shit']
    assert detect_insult_tweet(tweet2)==[]
    assert detect_insult_tweet(tweet3)==['shit','suck']
    assert detect_insult_tweet(tweet4)==['shit','suck']

test_detect_insult_tweet()

data=[[1,'@1',[tweet1,tweet2]],[2,'@2',[tweet3]]]

def test_detect_insults_tweets():
    assert detect_insults_tweets(data)=={'1':[['hot chick','shit'],[]],'2':[['shit','suck']]}

test_detect_insults_tweets()
