"""
Main file to launch the collection of tweets
"""
import json
import pandas as pd
from collect import twitter_setup,get_candidate_queries,get_tweets_from_candidates_search_queries
from collect import get_replies_to_candidate,get_retweets_of_candidate
from storetweet import store_tweets,extractjson

def collection(celebrities_amount):
    """
    Collects and stores the tweets talking about one of the studied celebrity
    :param celebrity_amount: (int) number of celebrities studied
    :return: (list) list of 3-element-lists corresponding to one celebrity,
    each containing their number, name and a dataframe with the tweets about them
    """
    collect=[]
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    tweets=[]
>>>>>>> main
    for i in range(1,celebrities_amount + 1):
        print('Next celebrity')
        num_celebrity = str(i)
        twitter_api = twitter_setup('C:/Users/gaspa/OneDrive/Documents/CS/Coding Weeks')
        keywords = get_candidate_queries(num_celebrity, 'Data/keywords_celebrity_')
        name=keywords[0]
<<<<<<< HEAD
        result=get_tweets_from_candidates_search_queries(keywords,twitter_api)+get_replies_to_candidate(num_celebrity,twitter_api)+get_retweets_of_candidate(num_celebrity,twitter_api) #Renvoie une liste contenant tous les statuts récoltés
=======
    for i in range(celebrities_amount + 1):
=======
    for i in range(1,celebrities_amount + 1):
>>>>>>> c6d9d35 (Adaptation des fonctions collect + collecte pour plusieurs celebrites)
        num_celebrity = str(i)
        twitter_api = twitter_setup('C:/Users/gaspa/OneDrive/Documents/CS/Coding Weeks') #On se connecte à l'API
        keywords = get_candidate_queries(num_celebrity, 'Data/keywords_celebrity_')  #On récupère les mots-clés à rechercher
        name=keywords[0]
<<<<<<< HEAD
        result=get_tweets_from_candidates_search_queries(keywords,twitter_api)+get_replies_to_candidate(num_celebrity,twitter_api)+get_retweets_of_candidate(num_celebrity,twitter_api)
        result=result+stream(keywords,5) #Renvoie une liste contenant tous les statuts récoltés
>>>>>>> f72ffbd (Adaptation collection)
=======
        result=get_tweets_from_candidates_search_queries(keywords,twitter_api)+get_replies_to_candidate(num_celebrity,twitter_api)+get_retweets_of_candidate(num_celebrity,twitter_api) #Renvoie une liste contenant tous les statuts récoltés
>>>>>>> c6d9d35 (Adaptation des fonctions collect + collecte pour plusieurs celebrites)
        tweets=[]
=======
        result = get_tweets_from_candidates_search_queries(keywords,twitter_api)
        result = result + get_replies_to_candidate(num_celebrity,twitter_api)
        result = result + get_retweets_of_candidate(num_celebrity,twitter_api)
>>>>>>> main
        for status in result:
            try:
                tweets.append(status._json) #pylint: disable=protected-access
            except AttributeError:
                tweets.append(json.loads(status.decode('utf-8')))
        store_tweets(tweets,name)
        dataframe=pd.DataFrame.from_dict(extractjson('Data/' + name + '.json'))
<<<<<<< HEAD
<<<<<<< HEAD
        collect.append([int(num_celebrity),name,dataframe])
    return collect

print(collection(3))
=======
        collect.append([num_celebrity,name,dataframe])
    return collect
>>>>>>> f72ffbd (Adaptation collection)
=======
        collect.append([int(num_celebrity),name,dataframe])
    return collect
<<<<<<< HEAD

print(collection(3))
>>>>>>> c6d9d35 (Adaptation des fonctions collect + collecte pour plusieurs celebrites)
=======
>>>>>>> main
