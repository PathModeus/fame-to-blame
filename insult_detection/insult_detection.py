from Data import swear_words_database
import csv


with open('swear_words_database.csv') as csv_file : 
    csv_reader = csv.reader(csv_file, delimiter = '\n')

