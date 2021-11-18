"""
This is the main module of our app, execute in your shell to run it!
"""
from src.UI.user_interface import *
from src.datacollection.keywords_generation import *
from src.datacollection.__main__ import *
from src.insult_detection.insult_detection import *
from src.dataanalysis.analyse import *

start()
from src.UI.user_interface import PATH,NUM_OF_CEL,PEOPLES
set_of_data=[]
for celeb_number in range(1,NUM_OF_CEL+1):
    user_keywords=PEOPLES[celeb_number-1]
    keywords=converting_keywords(user_keywords)
    tweet_collection=collection(keywords,PATH)
    tweet_collection.insert(0,celeb_number)
    set_of_data.append(tweet_collection)
detect_insults=detect_insults_tweets(set_of_data)
list_of_frequencies=[]
for celeb_number in range(1,NUM_OF_CEL+1):
    frequency = insult_frequency(detect_insults[str(celeb_number)])
    list_of_frequencies.append([celeb_number, keywords[0], frequency])
print(list_of_frequencies)
print(detect_insults)
