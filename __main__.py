"""
This is the main module of our app, execute in your shell to run it!
"""

from carbonai import PowerMeter
import pandas as pd
from src.UI.user_interface import start
from src.datacollection.keywords_generation import converting_keywords, cleanup
from src.datacollection.__main__ import collection
from src.insult_detection.insult_detection import detect_insults_tweets
from src.dataanalysis.analyse import insult_frequency
from src.Layout.app import appli


power_meter = PowerMeter.from_config('docs/config.json')

"""
@power_meter.measure_power(
    
    package="main",
    algorithm="insult detector",
    step="refactoring",
    data_type="tabular",
    comments="first try of power-meter"

)"""
def main():
    """
    Main function of the programm which coordinates the different modules.
    Just run it to start the app.
    """
    start()
    from src.UI.user_interface import PATH,NUM_OF_CEL,PEOPLES,LANGUAGE
    set_of_data=[]
    names = []
    flag=0
    for celeb_number in range(NUM_OF_CEL):
        user_keywords=PEOPLES[celeb_number]
        keywords=converting_keywords(user_keywords)
        names.append(keywords[0])
        tweet_collection=collection(keywords,PATH,lang=LANGUAGE)
        if tweet_collection == 'This twitter user does not exist.':
            set_of_data.append([celeb_number,keywords[0],'This user does not exist.'])
            flag+=1
        else:
            tweet_collection.insert(0,celeb_number)
            set_of_data.append(tweet_collection)
    if flag==0:
        detect_insults=detect_insults_tweets(set_of_data,lang=LANGUAGE)
        list_of_frequencies={'celebrity':[], 'frequency' : []}
           
        for celeb_number in range(NUM_OF_CEL):
            frequency = insult_frequency(detect_insults[str(celeb_number)])
            list_of_frequencies['celebrity'].append(names[celeb_number])
            list_of_frequencies['frequency'].append(frequency)
        cleanup(names)
        appli(pd.DataFrame.from_dict(list_of_frequencies))
        
    else : 
        print(str(flag) + ' celebrities you entered did not have a valid twitter username')
        print(set_of_data)

main()