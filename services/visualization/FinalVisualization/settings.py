import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_CONNECTION = str(os.environ.get('DB_CONNECTION'))