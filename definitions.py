import os
import json

import pandas as pd

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIGS_DIR = os.path.join(ROOT_DIR, 'configs')
FILES_DIR = os.path.join(ROOT_DIR, 'files')

DAILYPROGRAMER_POSTS_DIR = os.path.join(FILES_DIR, 'dailyprogrammerposts.csv')

with open(os.path.join(CONFIGS_DIR, 'praw.json')) as f:
    PRAW_CONFIG = json.load(f)

