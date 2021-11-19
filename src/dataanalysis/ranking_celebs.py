import sys
import pandas as pd
<<<<<<< HEAD
from analyse import frequency
=======
sys.path.append('C:\\Users\\mneau\\Documents\\Coding_Weeks\\local_project\\fame-to-blame\\src\\datacollection')
from analyse import insult_frequency
>>>>>>> 1a23d834d19724affcd12dacf21e9a71ed8bed81


def ranking(tweets_by_celebrities):
    """
    ranks the celebrities of the list from the most insulted to the least insulted
    
    returns a dataframe where the keys are the celebs and the values are
    the percentage of offensive tweets about them
    """
    mean_tweet_rate={}
    for celeb in tweets_by_celebrities:
        mean_tweet_rate[celeb]=[insult_frequency(tweets_by_celebrities[celeb])]
    df = pd.DataFrame(mean_tweet_rate) 
    return(df)
