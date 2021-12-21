import json
from src.services.extractor import extractor
from settings import PATH_TO_DATA

def run_stream():
    with open(PATH_TO_DATA) as f:
        for object_ in f:
            json_lines = json.loads(object_)
            for line in json_lines:
                print(line)

if __name__ == '__main__':
    run_stream()