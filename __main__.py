"""
This is the main module of our app, execute in your shell to run it!
"""
from src.UI.user_interface import *
from src.datacollection.keywords_generation import *
from src.datacollection.__main__ import *
from src.insult_detection.insult_detection import *
from src.dataanalysis.analyse import *
from src.Layout.twitter_wordcloud import * 
from src.Layout.app import * 


start()
from src.UI.user_interface import PATH,NUM_OF_CEL,PEOPLES,LANGUAGE
set_of_data=[]
names = []
for celeb_number in range(1,NUM_OF_CEL+1):
    user_keywords=PEOPLES[celeb_number-1]
    keywords=converting_keywords(user_keywords)
    names.append(keywords[0])
    tweet_collection=collection(keywords,PATH,lang=LANGUAGE)
    tweet_collection.insert(0,celeb_number)
    set_of_data.append(tweet_collection)
detect_insults=detect_insults_tweets(set_of_data)
list_of_frequencies={'celebrity':[], 'frequency' : []}
for celeb_number in range(1,NUM_OF_CEL+1):
    frequency = insult_frequency(detect_insults[str(celeb_number)])
    list_of_frequencies['celebrity'].append(names[celeb_number - 1])
    list_of_frequencies['frequency'].append(frequency)
cleanup(names)
print(list_of_frequencies)
print(detect_insults)
print(pd.DataFrame.from_dict(list_of_frequencies))
appli(pd.DataFrame.from_dict(list_of_frequencies))

