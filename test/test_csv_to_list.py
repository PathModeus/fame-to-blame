from src.insult_detection.csv_to_list import convert_database

def test_convert_database():
    assert convert_database('data\data_test.csv')==['hello','world','hello world']

test_convert_database()
