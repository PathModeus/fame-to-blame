import json
import pandas as pd

def createjson(tweets,file):
    """
    Cette fonction créé un fichier file.json contenant les données tweets.
    """
    data=tweets
    with open(file, "w") as write_file:
        json.dump(data, write_file)

def extractjson(file):
    """
    Renvoie des données à partir d'un fichier .json

    file est de la forme : chemin/vers/le/fichier/fichier.json
    """
    with open(file, "r") as read_file:
        data = json.load(read_file)
  
    return(data)

def storeTweet(tweets):
    """
    Met sous forme .json les tweets collectés en sélectionnant les données à conserver
    """
    T=[]
    for i in range(len(tweets)):
        tweet={}
        tweet['Likes']=tweets[i]['favorite_count']
        tweet['RT']=tweets[i]['retweet_count']
        tweet['Texte']=tweets[i]['text']
        tweet['Date']=tweets[i]['created_at']
        T.append(tweet)
    createjson(T,'t')

