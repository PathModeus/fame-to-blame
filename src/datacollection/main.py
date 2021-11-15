from collect import twitter_setup,get_candidate_queries,get_tweets_from_candidates_search_queries,get_replies_to_candidate,get_retweets_of_candidate,stream
from storetweet import storeTweet,extractjson
import json
import pandas as pd

num_candidate = str(input('Entrez le numéro de candidat '))
twitter_api = twitter_setup() #On se connecte à l'API
keywords = get_candidate_queries(num_candidate, 'Data\keywords_celebrity_') #On récupère les mots-clés à rechercher
result=get_tweets_from_candidates_search_queries(keywords,twitter_api)
result=result+get_replies_to_candidate(num_candidate,twitter_api)
result=result+get_retweets_of_candidate(num_candidate,twitter_api)
result=result+stream(keywords,5) #Renvoie une liste contenant tous les statuts récoltés
tweets=[]
for status in result:
    try:
        tweets.append(status._json)
    except AttributeError:
        tweets.append(json.loads(status.decode('utf-8')))
storeTweet(tweets)
dataframe=pd.DataFrame.from_dict(extractjson('Data/t.json'))
print(dataframe)