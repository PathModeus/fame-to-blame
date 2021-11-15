from collect import twitter_setup,get_candidate_queries,get_tweets_from_candidates_search_queries,get_replies_to_candidate,get_retweets_of_candidate,stream
from storetweet import storeTweet,extractjson
import json
import pandas as pd

def collection(celebrities_amount):
    collect=[]
<<<<<<< HEAD
<<<<<<< HEAD
    for i in range(1,celebrities_amount + 1):
        num_celebrity = str(i)
        twitter_api = twitter_setup('C:/Users/gaspa/OneDrive/Documents/CS/Coding Weeks') #On se connecte à l'API
        keywords = get_candidate_queries(num_celebrity, 'Data/keywords_celebrity_')  #On récupère les mots-clés à rechercher
        name=keywords[0]
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
        for status in result:
            try:
                tweets.append(status._json)
            except AttributeError:
                tweets.append(json.loads(status.decode('utf-8')))
        storeTweet(tweets,name)
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

print(collection(3))
>>>>>>> c6d9d35 (Adaptation des fonctions collect + collecte pour plusieurs celebrites)
