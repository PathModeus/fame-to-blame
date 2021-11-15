import csv

def convert_database(doc):
    database=[]
    with open(doc, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            database.append(row[0])
    return database

swear_words_database=convert_database('C:/Users/33675/fame-to-blame/Data/swear_words_database.csv')
