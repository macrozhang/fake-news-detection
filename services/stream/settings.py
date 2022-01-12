import os
# import dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
# dotenv.load_dotenv(f'{BASE_DIR}/.env')

BATCH_SIZE = int(os.environ.get('BATCH_SIZE'))
DB_CONNECTION = str(os.environ.get('DB_CONNECTION'))