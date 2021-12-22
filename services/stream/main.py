import os
import sys
import json
import time
import pyspark
from datetime import datetime
from settings import BATCH_SIZE

if __name__ == '__main__':
    with open("/opt/application/data/prepared_shuffled.json") as f:
        for object_ in f:
            json_lines = json.loads(object_)
            batch = 0
            data = []
            for line in json_lines:
                if batch <= BATCH_SIZE:
                    data.append(line)
                    batch += 1
                else:
                    with open(f"/opt/application/NAS/batch_{datetime.now().strftime('%Y%m%d_%H%M%S%f')}.json", "w") as f:
                        json.dump(data, f)
                    print("New file was created!")
                    batch = 0
                    data = []
