import sys
sys.path.append('C:\Users\mneau\Documents\Coding_Weeks\local_project\fame-to-blame\src\datacollection')
from collect import collect
from analyse import ranking

def ranking(list_of_celebrities):
"""
ranks the celebrities of the list from the most insulted to the least insulted
"""
tweets_by_celeb=[]
tweets_by_celeb_bis=[]
for celeb in list_of_celebrities:
    tweets_by_celeb.append([celeb]+collect(celeb,twitter_api))
    tweets_by_celeb_bis.append(collect(celeb,twitter_api))
tweets_by_celebrity=ranking(tweets_by_celeb)
celebs_ranked=[]
for list_of_tweets in tweets_by_celebrity:
