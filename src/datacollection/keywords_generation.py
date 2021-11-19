"""
Functions that allow the user to select the keywords he want to search
"""
import os

def cleanup(names):
    """
    Cleans up the Data folder by removing the json created by executing the main
    :param names: list of str corresponding to the twitter @ of the last celebrities studied
    """
    try:
        for name in names:
            os.remove('Data/' + name + '.json')
        return None
    except FileNotFoundError:
        return None

def converting_keywords(keywords):
    """
    Converts a string containing the keywords separated by commas into a list of keywords
    :param keywords: (str) all the keywords separated by commas, ex : 'Macron, Emmanuel, président'
    :return: (list) list of strings containing each one a keyword
    """
    if keywords[-2:]==', ':
        return [keywords[:-2]]
    list_keywords=keywords.split(', ')
    return list_keywords
