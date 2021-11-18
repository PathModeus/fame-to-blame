"""
Functions that allow the user to select the keywords he want to search
"""
import os

def cleanup(celeb_amount):
    """
    Cleans up the Data folder by removing the files containing the keywords
    """
    for i in range(1,celeb_amount+1):
        os.remove('Data/keywords_celebrity_' + str(i) + '.txt')

def converting_keywords(keywords):
    """
    Converts a string containing the keywords separated by commas into a list of keywords
    :param keywords: (str) all the keywords separated by commas, ex : 'Macron,Emmanuel,président'
    :return: (list) list of strings containing each one a keyword
    """
    list_keywords=keywords.split(', ')
    return list_keywords

def writing_keyword(celeb_number,keywords):
    """
    Writes the keyword in the txt file Data/keywords_celebrity_celeb_number.txt
    :param celeb_number: (int) the number of the celebrity
    :param keywords: (list) list of strings containing the keywords we want to write in the file
    """
    try:
        path = 'Data/keywords_celebrity_' + str(celeb_number) + '.txt'
        with open(path, 'w',encoding='utf-8') as fichier:
            for keyword in keywords:
                fichier.write(keyword + '\n')
        return "The files are created."
    except FileNotFoundError:
        return "The file does not exist."

cleanup()