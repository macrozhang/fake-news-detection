import os
import sys
import json
import time
import pyspark
from datetime import datetime
from settings import BATCH_SIZE

if __name__ == '__main__':

    print(f"Batch size is = {BATCH_SIZE}")

    with open("data/prepared_shuffled.json") as f:
        for object_ in f:
            json_lines = json.loads(object_)
            batch = 0
            data = []
            for line in json_lines:
                if batch <= BATCH_SIZE:
                    data.append(line)
                    batch += 1
                else:
                    newFileName = f"NAS/batch_{datetime.now().strftime('%Y%m%d_%H%M%S%f')}.json"
                    with open(newFileName, "w") as f:
                        json.dump(data, f)
                    print(f"{newFileName} was created!")
                    batch = 0
                    data = []
