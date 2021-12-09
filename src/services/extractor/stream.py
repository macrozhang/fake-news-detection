import csv
import json

def run_stream(path_to_data):
    f = open(path_to_data, newline='')
    csv_reader = csv.reader(f)
    print(next(csv_reader))