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
    with open(doc, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            database.append(row[0])
    return database
path='Data/swear_words_database.csv'

swear_words_data=convert_database(path)
