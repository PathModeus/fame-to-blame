import sys
import pandas as pd
sys.path.append('C:\\Users\\mneau\\Documents\\Coding_Weeks\\local_project\\fame-to-blame\\src\\datacollection')
from analyse import frequency


def ranking(tweets_by_celebrities):
    """
    ranks the celebrities of the list from the most insulted to the least insulted
    returns a dataframe where the keys are the celebs and the values are the percentage of offensive tweets about them
    """
    mean_tweet_rate={}  
    for celeb in tweets_by_celebrities:
        mean_tweet_rate[celeb]=[frequency(tweets_by_celebrities[celeb])]
    df = pd.DataFrame(mean_tweet_rate) 
    return(df)
    
print(ranking({'Macron' : 'Macron u ass', 'Zemmour' : 'Zemmour you\'re the best'}))