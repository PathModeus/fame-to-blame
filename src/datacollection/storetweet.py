"""
All the functions necessary to store the collected tweets
"""
import json

def createjson(tweets,file):
    """
    Cette fonction créé un fichier file.json contenant les données tweets.
    """
    data=tweets
    with open(file, "w", encoding='utf-8)') as write_file:
        json.dump(data, write_file)

def extractjson(file):
    """
    Renvoie des données à partir d'un fichier .json

    file est de la forme : chemin/vers/le/fichier/fichier.json
    """
    with open(file, "r", encoding='utf-8') as read_file:
        data = json.load(read_file)
    return data

def store_tweets(collected_tweets,name):
    """
    Met sous forme .json les tweets collectés en sélectionnant les données à conserver
    name est une chaîne de caractères contenant le nom à donner au fichier
    """
    returned_tweets=[]
    for collected_tweet in collected_tweets:
        tweet={}
        tweet['Likes']=collected_tweet['favorite_count']
        tweet['RT']=collected_tweet['retweet_count']
        tweet['Texte']=collected_tweet['text']
        tweet['Date']=collected_tweet['created_at']
        returned_tweets.append(tweet)
    createjson(returned_tweets,'Data/' + name + '.json')
