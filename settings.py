import os
import dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
dotenv.load_dotenv(f'{BASE_DIR}/.env')

PATH_TO_DATA = os.environ.get('PATH_TO_DATA')