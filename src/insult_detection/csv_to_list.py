"""
csv_to_list module
    Description :
        Converts a csv database into a list of strings (per line of the database)
    Contains:
        convert_database : returns a list of strings
        """

import csv

def convert_database(doc):
    """Return a list of the data stocked in a csv file

    Parameters
    -----------
    doc : csv file

    Returns:
    -----------
    database : list of strings of each line of the csv file
    """
    database=[]
    with open(doc, newline='', encoding="utf-8") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            database.append(row[0])
    return database

PATH_TO_DATABASE='data/swear_words_database.csv'
swear_words_data=convert_database(PATH_TO_DATABASE)
