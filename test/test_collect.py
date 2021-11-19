"""
test module for collect module
"""
import pytest
import sys
sys.path.append('../')
sys.path.insert(1,'./')
from src.datacollection.collect import *


def test_twitter_setup():
    assert twitter_setup('C:/Users/gaspa/OneDrive/Documents/CS/Coding Weeks') is not None

def test_get_tweets_from_candidates_search_queries():
    api = twitter_setup('C:/Users/gaspa/OneDrive/Documents/CS/Coding Weeks')
    assert get_tweets_from_candidates_search_queries([], api) == []
    assert get_tweets_from_candidates_search_queries(['test'], api) != []

def test_get_replies_to_candidate():
    api = twitter_setup('C:/Users/gaspa/OneDrive/Documents/CS/Coding Weeks')
    assert get_replies_to_candidate(999, api) == "This candidate is not in our database"
    replies = get_replies_to_candidate(2, api)
    assert isinstance(replies, list) and replies != []

def test_get_retweets_of_candidate():
    api = twitter_setup('C:/Users/gaspa/OneDrive/Documents/CS/Coding Weeks')
    assert get_retweets_of_candidate(999, api) == "This candidate is not in our database"
    retweets = get_retweets_of_candidate(1, api)
    assert isinstance(retweets, list) and retweets != []

def test_stream():
    assert stream([],0.1,'C:/Users/gaspa/OneDrive/Documents/CS/Coding Weeks') == "Please insert keywords"
    streamed = stream(['test'],1,'C:/Users/gaspa/OneDrive/Documents/CS/Coding Weeks')
    assert isinstance(streamed, list) and streamed != []

def test_get_id():
    api = twitter_setup('C:/Users/gaspa/OneDrive/Documents/CS/Coding Weeks')
    assert get_id('', api) == "Please enter a screen name."
    assert get_id('EmmanuelMacron', api) == '1976143068'

def test_collect():
    api = twitter_setup('C:/Users/gaspa/OneDrive/Documents/CS/Coding Weeks')
    assert collect('', api) == "Please enter a valid keyword (string)."
    assert collect(42, api) == "Please enter a valid keyword (string)."
    test = collect('test', api)
    assert isinstance(test, list) and test != []

def test_collect_by_user():
    api = twitter_setup('C:/Users/gaspa/OneDrive/Documents/CS/Coding Weeks')
    test = collect_by_user(1976143068, api, 1)
    assert isinstance(test, list) and len(test) == 1
