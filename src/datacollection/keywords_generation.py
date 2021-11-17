"""
Functions that allow the user to select the keywords he want to search
"""

def converting_keywords(keywords):
    """
    Converts a string containing the keywords separated by commas into a list of keywords
    :param keywords: (str) all the keywords separated by commas, ex : 'Macron,Emmanuel,président'
    :return: (list) list of strings containing each one a keyword
    """
    list_keywords=keywords.split(', ')
    return list_keywords
